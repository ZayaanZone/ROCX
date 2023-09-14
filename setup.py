from setuptools import setup, find_packages

setup(
    name="rocx",
    version="2.0.0",
    url="https://github.com/SanaurAsif/ROCX",
    license="Apache License 2.0",
    author="Sanaur Asif",
    author_email="sanaurasif2@gmail.com",
    description="A python module to run tools",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "rocx=roc.helper:run_cli"
        ]
    }
)
