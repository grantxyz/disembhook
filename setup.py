from setuptools import setup, find_packages

setup(
    name="disembhook",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests"],
    description="A simple Python library for sending webhooks",
    author="grantxyz",
    url="https://github.com/grantxyz/disembhook",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
