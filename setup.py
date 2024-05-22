from setuptools import setup, find_packages

setup(
    name='DDoS',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
    ],
    entry_points={
        'console_scripts': [
            'DDoS=DDoS:main',
        ],
    },
    author='joshua Apostol',
    description='A powerful DDoS tool',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
