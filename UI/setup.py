from setuptools import setup, find_packages

setup(
    name='NeuralScan',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'tensorflow',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            'neuralscan=NeuralScan.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
