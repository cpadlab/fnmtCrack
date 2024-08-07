
# ┏┓┳┓┳┳┓┏┳┓  ┏┓┳┓┏┓┏┓┓┏┓
# ┣ ┃┃┃┃┃ ┃   ┃ ┣┫┣┫┃ ┃┫ 
# ┻ ┛┗┛ ┗ ┻   ┗┛┛┗┛┗┗┛┛┗┛                    
                                                      
# FNMT CRACK
# Author: Carlos Padilla (cpadlab)

# Description -----
# FNMT Crack is a tool designed to recover the password of a natural person's FNMT
# (Fábrica Nacional de Moneda y Timbre) digital certificate by means of a brute force 
# attack. This software is intended for legal purposes only and should be used only by 
# the owner of the digital certificate.

# MIT License -----
# Copyright (c) 2024 Carlos Padilla

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os, threading
from argparse import ArgumentParser
from cryptography.hazmat.primitives.serialization.pkcs12 import load_pkcs12
from cryptography.hazmat.primitives.serialization import pkcs12

class Config:
    def __init__(self) -> None:
        
        self.file = ""
        self.wordlist = ""
        self.threads = 3

class Arguments:
    def __init__(self) -> None:
        
        self.parser = ArgumentParser(
            description = str("FNMT Crack is a tool designed to recover the password of a natural person's FNMT"),
        )

    def _add(self):

        self.parser.add_argument("-f", "--file", type=str, help="Path to PKCS#12 file.", required=True)
        self.parser.add_argument("-w", "--wordlist", type=str, help="Path to the password list file.", required=True)
        self.parser.add_argument("-t", "--threads", type=int, help="Number of threads to be used.", default=3)

    def _get(self):

        return self.parser.parse_args()
    
class Utils:

    @staticmethod
    def _fileExists(filepath) -> bool:

        return bool(os.path.isfile(filepath))

class Crack:
    
    def __init__(self, conf) -> None:

        self.config = conf

        with open(self.config.file, "rb") as certfile:
            self.certp12 = certfile.read()

        self._bruteForce(
            wordlist_path=self.config.wordlist,
            num_threads=self.config.threads
        )

    def _load(self, password):

        print(f"[Info] Testing password: {password}")
        try:return pkcs12.load_key_and_certificates(self.certp12, password.encode())
        except Exception:return None

    def _worker(self, passwords, found_event, thread_id):
        
        for password in passwords:
            
            if found_event.is_set():return
            if self._load(password):
                print("="*40 + f'\n[Sucessful] [{thread_id}ºt] Password found: {password}')
                found_event.set();return

    def _bruteForce(self, wordlist_path, num_threads):

        threads = []

        with open(wordlist_path, 'r', encoding='UTF-8', errors='ignore') as f:
            passwords = [line.strip() for line in f]
            
        found_event = threading.Event();block_size = len(passwords) // num_threads + 1
        print(f"Wordlist Size: {len(passwords)}" + f"\nBlock Size: {block_size}\n" + "="*40)

        for i in range(num_threads):
            
            start_index = i * block_size
            end_index = min((i + 1) * block_size, len(passwords))
            thread_passwords = passwords[start_index:end_index]

            thread = threading.Thread(
                target=self._worker, 
                args=(thread_passwords, found_event, i)
            )

            threads.append(thread);thread.start()

        for thread in threads:thread.join()
        if not found_event.is_set():
            print('[Err] Password not found')

class Boot:
    def __init__(self, conf) -> None:

        self.config = conf

    def run(self):

        self._arguments = Arguments()
        self._arguments._add()

        self.args = self._arguments._get()

        if not Utils._fileExists(self.args.file):
            raise FileExistsError(f"The file {self.args.file} does not exist or was not found.")
        
        if not Utils._fileExists(self.args.wordlist):
            raise FileExistsError(f"The file {self.args.wordlist} does not exist or was not found.")

        self.config.wordlist = self.args.wordlist
        self.config.file = self.args.file

        if self.args.threads:
            self.config.threads = self.args.threads

        print("="*40 + "\nfnmtCrack\tCarlos Padilla (cpadlab)\n" + "="*40 + 
            f"\nCertificate Path: {self.config.file}" + 
            f"\nWordlist Path: {self.config.wordlist}" + 
            f"\nThreads: {self.config.threads}\n" + "="*40)

        with open(self.config.file, "rb") as certfile:
            p12tmp = certfile.read()

        try:
            load_pkcs12(p12tmp, None).cert
            raise ValueError(f"The {self.config.file} certificate does not require a password.")
        except Exception:pass
        finally:certfile.close()

        Crack(conf=self.config)
        
if __name__ == '__main__':

    print("""┏┓┳┓┳┳┓┏┳┓  ┏┓┳┓┏┓┏┓┓┏┓
┣ ┃┃┃┃┃ ┃   ┃ ┣┫┣┫┃ ┃┫   by cpadlab
┻ ┛┗┛ ┗ ┻   ┗┛┛┗┛┗┗┛┛┗┛""")

    Boot(conf=Config()).run()