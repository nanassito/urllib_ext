from datetime import date

import requests
from setuptools import find_packages, setup
from urllib_ext.parse import urlparse


def get_next_version(project: str):
    project_url = urlparse("https://pypi.org/project") / project
    today = date.today()
    version = f"{today:%Y}.{today:%m}.{today:%d}"
    minor = 0
    while requests.get(str(project_url / version)).status_code == 200:
        minor += 1
        version = f"{today:%Y}.{today:%m}.{today:%d}.{minor}"
    return version


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="urllib_ext",
    version=get_next_version("urllib-ext"),
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
