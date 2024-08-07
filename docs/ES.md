[Read in English](../README.md)

<div style="text-align: center;">

# FNMT Crack

![GitHub top language](https://img.shields.io/github/languages/top/cpadlab/fnmtCrack)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cpadlab/fnmtCrack)
![GitHub License](https://img.shields.io/github/license/cpadlab/fnmtCrack)
![GitHub Repo stars](https://img.shields.io/github/stars/cpadlab/fnmtCrack)

</div>

FNMT Crack es una **herramienta diseñada para recuperar la contraseña de un certificado digital de la FNMT** (Fábrica Nacional de Moneda y Timbre) de persona física mediante un ataque de fuerza bruta. *Este software está destinado exclusivamente para fines legales y debe ser utilizado únicamente por el propietario del certificado digital*.

**Autor**: Carlos Padilla (cpadlab)

## Descripción

Esta herramienta permite intentar recuperar la contraseña de un archivo PKCS#12 (.p12) utilizando una lista de contraseñas (wordlist). La ejecución del proceso se puede paralelizar mediante el uso de hilos para aumentar la eficiencia.

## Requisitos

Módulos de Python: `argparse`, `cryptography`

```
pip install -r requirements.txt
```

## Instalación

```
git clone https://github.com/cpadlab/fnmtCrack.git
cd fnmtCrack && pip install -r requirements.txt
```

## Uso

Para ejecutar la herramienta, necesitas proporcionar la ruta al archivo PKCS#12 y una lista de contraseñas. Opcionalmente, puedes especificar el número de hilos a utilizar. Ejemplo de ejecución en python:

```
python fnmtcrack.py -f ruta/al/certificado.p12 -w ruta/a/la/wordlist.txt -t 4
```

Puede descargar el binario de la versión 1.0 o ejecutarlo directamente desde el repositorio. Ejemplo de ejecución con binario:

```
./dist/fnmtcrack -f path/to/certificate.p12 -w path/to/wordlist.txt -t 4
```


### Parámetros

- `-f` o `--file`: Ruta al archivo PKCS#12.
- `-w` o `--wordlist`: Ruta al archivo de lista de contraseñas.
- `-t` o `--threads`: Número de hilos a utilizar (opcional, por defecto es 3).

## Nota Legal

Este software debe ser utilizado únicamente con fines legales. El autor no se hace responsable del uso indebido de esta herramienta.

## Ejemplo de salida

```
┏┓┳┓┳┳┓┏┳┓  ┏┓┳┓┏┓┏┓┓┏┓
┣ ┃┃┃┃┃ ┃   ┃ ┣┫┣┫┃ ┃┫   by cpadlab
┻ ┛┗┛ ┗ ┻   ┗┛┛┗┛┗┗┛┛┗┛
========================================
fnmtCrack       Carlos Padilla (cpadlab)
========================================
Certificate Path: ruta/al/certificado.p12
Wordlist Path: ruta/a/la/wordlist.txt
Threads: 4
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

Si la contraseña no se encuentra en la lista de contraseñas proporcionada, la herramienta mostrará:

```
[Err] Password not found
```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.