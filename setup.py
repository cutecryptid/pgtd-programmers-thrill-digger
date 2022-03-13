import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pgtd",
    version="1.0.0",
    author="trigork",
    author_email="r.martin1@udc.es",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Trigork/pgtd-programmers-thrill-digger",
    project_urls={
        "Bug Tracker": "https://github.com/Trigork/pgtd-programmers-thrill-digger/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "pgtd"},
    packages=setuptools.find_packages(where="pgtd"),
    python_requires=">=3.6",
)