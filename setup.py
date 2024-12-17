from setuptools import setup, find_packages

setup(
    name="python-cli-docker",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "cli_app = cli_app.main:cli",
        ],
    },
)
