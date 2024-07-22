from setuptools import setup, find_packages


with open("version", "r") as f:
    version = f.read().strip()

with open("requirements.txt", "r") as f:
    requirements = list(filter(lambda x: not x.startswith('#') and not x.startswith('--') and x, f.read().split('\n')))

with open("LICENSE.txt", "r") as f:
    license = f.read()

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="setup-package",
    description="some description",
    long_description=readme,
    long_description_content_type="text/markdown",
    version=version,
    license=license,
    package_dir={"":"."},
    packages=find_packages(include=["setuptools_package", "setuptools_package.*"], where="."),
    install_requires=requirements,
    python_requires=">=3.11",
    setup_requires=["setuptools","wheel"]
)