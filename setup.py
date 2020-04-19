"""The setup script."""

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as fh:
    requirements = fh.read().splitlines()

with open("test-requirements.txt") as fh:
    test_requirements = fh.read().splitlines()

setup_requirements = ["pytest-runner"]

setup(
    author="Joris den Uijl",
    author_email="jorisdenuijl@gmail.com",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    description="Basic web app to get CircleCI build artifacts.",
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=["CircleCI", "Flask", "API"],
    name="Artifact Getter",
    packages=find_packages(include=["artifact_getter"]),
    test_suite="tests",
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    url="https://github.com/uijl/get-circleci-artifact",
    version="0.0.1",
    zip_safe=False,
)
