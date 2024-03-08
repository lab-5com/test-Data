from setuptools import setup, find_packages

# Read requirements.txt and use it for the install_requires option
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='lab5_data',
    description="LAB5 data assessment tools",
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'data-generate=data_gen.data_generate:main'
        ]
    },
    install_requires=required,
)