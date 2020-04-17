from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="urllib_parse_ParseResult_overloaded",
    version="0.1.0",
    author="Dorian Jaminais",
    author_email="argparse_logging@jaminais.fr",
    description="Overload urllib.parse.ParseResult to be able to use operators like / and & on it.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nanassito/urllib.parse.ParseResult",
    py_modules=["urllib_parse_ParseResult_overloaded"],
    # test_suite="test_all",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)