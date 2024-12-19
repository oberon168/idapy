from setuptools import setup, find_packages

setup(
    name='idapy',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy>=2.0.2', 
        'pandas>=2.2.3',
        'cupy>=13.3.0'
        # List your library's dependencies here
    ],
    author='Oberon Leung',
    author_email='ob_001@hotmail.com',
    description='Interactive Data Analysis in Python',
    url='https://github.com/oberon168/idapy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Apache License 2.0',
        'Operating System :: OS Independent',
    ],
    python_reqyures='>=3.10'
)
