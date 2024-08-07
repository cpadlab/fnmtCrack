from setuptools import setup, find_packages

setup(
    name='fnmtcrack',
    version='1.0.0',
    author='Carlos Padilla',
    author_email='cpadlab@proton.me',
    description='A tool designed to recover the password of a natural person\'s FNMT digital certificate by means of a brute force attack.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cpadlab/fnmtCrack',
    packages=find_packages(),
    install_requires=[
        'cryptography',
    ],
    entry_points={
        'console_scripts': [
            'fnmtcrack=fnmtcrack.main',
        ],
    },
    scripts=['scripts/fnmtcrack'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
