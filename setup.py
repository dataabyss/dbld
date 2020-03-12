# setup.py file

from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dbld",
    version="1.0",
    author="db",
    #author_email="email@email.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/dataabyss/dbld",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)