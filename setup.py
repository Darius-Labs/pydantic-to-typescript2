from setuptools import find_packages, setup


def readme():
    with open("README.md", "r") as infile:
        return infile.read()


classifiers = [
    "Development Status :: 5 - Production/Stable",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]

install_requires = [
    "pydantic",
]

setup(
    name="pydantic-to-typescript2",
    version="1.0.6",
    description="Convert pydantic v1 and pydantic v2 models to typescript interfaces",
    license="MIT",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="pydantic pydantic2 typescript annotations validation interface",
    author="Phillip Dupuis, Darius Labs",
    author_email="sean@dariuslabs.com",
    url="https://github.com/dariuslabs/pydantic-to-typescript2",
    packages=find_packages(exclude=["tests*"]),
    install_requires=install_requires,
    extras_require={
        "dev": ["pytest", "pytest-cov", "coverage"],
    },
    entry_points={"console_scripts": ["pydantic2ts = pydantic2ts.cli.script:main"]},
    classifiers=classifiers,
)
