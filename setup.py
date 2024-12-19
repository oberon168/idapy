from setuptools import setup, find_packages

setup(
    name='idapy',
    version='0.1.5',
    packages=find_packages(where='src'), 
    package_dir={'':'src'},
    install_requires=[
        'numpy', 
        'pandas',
        'cupy'
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
    python_requires='>=3.10',
    include_package_data=True,
)
