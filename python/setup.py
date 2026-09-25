from setuptools import setup, find_packages

setup(
    name="quantoken",
    version="0.1.0",
    description="Python SDK for QuantumToken (奇物匣) open API",
    author="QuantumToken",
    url="https://github.com/boy-389/quantoken-sdk",
    packages=find_packages(),
    install_requires=["requests>=2.25.0"],
    python_requires=">=3.8",
    license="MIT",
)
