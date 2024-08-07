[Leer en Español](./docs/ES.md)

<div style="text-align: center;">

# FNMT Crack

![GitHub top language](https://img.shields.io/github/languages/top/cpadlab/fnmtCrack)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cpadlab/fnmtCrack)
![GitHub License](https://img.shields.io/github/license/cpadlab/fnmtCrack)
![GitHub Repo stars](https://img.shields.io/github/stars/cpadlab/fnmtCrack)

</div>

FNMT Crack is a **tool designed to recover the password of a natural person's FNMT** (Fábrica Nacional de Moneda y Timbre) digital certificate by means of a brute force attack. *This software is intended for legal purposes only and should be used only by the owner of the digital certificate.*

**Author**: Carlos Padilla (cpadlab)

## Table of Contents

- [Requirements](#requirements)
- [Install](#install)
- [Usage](#usage)
- [Examples](#examples)
- [Legal Notice](#legal-notice)
- [License](#license)

## Description

This tool allows you to try to recover the password of a PKCS#12 (.p12) file using a password list (wordlist). The execution of the process can be parallelized by using threads to increase efficiency.

## Requirements

Python Modules: `argparse`, `cryptography`

```
pip install -r requirements.txt
```

## Install

```
git clone https://github.com/cpadlab/fnmtCrack.git
cd fnmtCrack && pip installRead in English -r requirements.txt
```

## Usage

To run the tool, you need to provide the path to the PKCS#12 file and a list of passwords. Optionally, you can specify the number of threads to use. Example of execution with python:

```
python fnmtcrack.py -f path/to/certificate.p12 -w path/to/wordlist.txt -t 4
```

You can download the binary from [Release 1.0](https://github.com/cpadlab/fnmtCrack/releases/tag/1.0) or you can run it directly from the repository. Example of execution with executable:

```
./dist/fnmtcrack -f path/to/certificate.p12 -w path/to/wordlist.txt -t 4
```

### Parameters

- `-f` o `--file`: Path to PKCS#12 file.
- `-w` o `--wordlist`: Path to the password list file.
- `-t` o `--threads`: Number of threads to be used (optional, default is 3).


## Legal Notice

This software should be used only for lawful purposes. The author is not responsible for any misuse of this tool.

## Example of output

```
┏┓┳┓┳┳┓┏┳┓  ┏┓┳┓┏┓┏┓┓┏┓
┣ ┃┃┃┃┃ ┃   ┃ ┣┫┣┫┃ ┃┫   by cpadlab
┻ ┛┗┛ ┗ ┻   ┗┛┛┗┛┗┗┛┛┗┛
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