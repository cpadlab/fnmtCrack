[Leer en Español](./ES.md)

# FNMT Crack

FNMT Crack is a **tool designed to recover the password of a natural person's FNMT** (Fábrica Nacional de Moneda y Timbre) digital certificate by means of a brute force attack. *This software is intended for legal purposes only and should be used only by the owner of the digital certificate.*

**Author**: Carlos Padilla (cpadlab)

## Description

This tool allows you to try to recover the password of a PKCS#12 (.p12) file using a password list (wordlist). The execution of the process can be parallelized by using threads to increase efficiency.

## Requirements

Python Modules: `argparse`, `cryptography`

```
pip install -r requirements.txt
```

## Instalación

```
git clone https://github.com/cpadlab/fnmtCrack.git
cd fnmtCrack && pip installRead in English -r requirements.txt
```

## Usage

To run the tool, you need to provide the path to the PKCS#12 file and a list of passwords. Optionally, you can specify the number of threads to use. Example of execution:

```
python fnmtcrack.py -f path/to/certificate.p12 -w path/to/wordlist.txt -t 4
```

### Parameters

- -f o --file: Path to PKCS#12 file.
- -w o --wordlist: Path to the password list file.
- -t o --threads: Number of threads to be used (optional, default is 3).

## Legal Notice

This software should be used only for lawful purposes. The author is not responsible for any misuse of this tool.

## Example of output

```
========================================
fnmtCrack       Carlos Padilla (cpadlab)
========================================
Certificate Path: path/to/certificate.p12
Wordlist Path: path/to/wordlist.txt
Threads: 5
========================================
Wordlist Size: 10000
Block Size: 2500
========================================
[Info] Testing password: password1
[Info] Testing password: password2
...
========================================
[Successful] [3ºt] Password found: your_password
```

If the password is not found in the list of passwords provided, the tool will display:

```
[Err] Password not found
```

## Licencia

This project is licensed under the MIT License. See the LICENSE file for more details.