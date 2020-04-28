from datetime import date

from setuptools import find_packages, setup

today = date.today()

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="urllib_ext",
    version=f"{today:%Y}.{today:%m}.{today:%d}",
    author="Dorian Jaminais",
    author_email="urllib_ext@jaminais.fr",
    description="Overload urllib.parse.ParseResult to be able to use operators "
    "like / and & on it.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nanassito/urllib.parse.ParseResult",
    packages=find_packages(),
    # test_suite="test_all",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
