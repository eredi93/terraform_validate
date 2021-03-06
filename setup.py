from setuptools import setup, find_packages

setup(
    name="terraform_validate",
    version="2.1.6",
    author="Edmund Dipple",
    author_email="elmundio1987@gmail.com",
    description="A library that provides asserts for testing Terraform configuration",
    url="https://github.com/elmundio87/terraform_validator",
    download_url = 'https://github.com/elmundio87/terraform_validate/tarball/2.1.6',
    keywords = ['terraform', 'assert', 'testing'],
    packages = find_packages(),
    install_requires=[
        "pyhcl"
    ],
)
