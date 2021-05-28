from setuptools import setup

setup(
    name="tzc",
    version="1.0.0",
    summary="convert timezone in filename",
    home_page="https://github.com/anaclumos/tools-convert-timezone-in-filename",
    author="anaclumos",
    license="MIT",
    description="convert timezone in filename",
    entry_points={"console_scripts": ["tzc=tzc:run"]},
)
