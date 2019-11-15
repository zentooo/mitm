from distutils.core import setup

requirements = [
    'aiohttp==3.6.2',
    'async-timeout==3.0.1',
    'attrs==19.3.0',
    'cffi==1.13.2',
    'chardet==3.0.4',
    'cryptography==2.8',
    'http-parser==0.8.3',
    'idna==2.8',
    'mitm==1.0',
    'multidict==4.5.2',
    'pycparser==2.19',
    'pyOpenSSL==19.0.0',
    'six==1.13.0',
    'termcolor==1.1.0',
    'yarl==1.3.0',
]

setup(
    name="mitm",
    version="1.0",
    packages=["mitm"],
    long_description=open("README.md").read(),
    install_requires=requirements,
)
