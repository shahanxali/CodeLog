from setuptools import setup

setup (name = 'codelog',
    version = '1.0',
    packages = ['codelog'],
    entry_points = {
        'console_scripts' : [
            'codelog = codelog.cli:main'
        ]
    })
