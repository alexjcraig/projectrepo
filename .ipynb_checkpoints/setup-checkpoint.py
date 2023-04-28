""" Here is my docstring so pylint is happy"""

from setuptools import setup

setup(
    name="ajcpkg",
    version="1.1.",
    description="s23 final project",
    maintainer="Alex Craig",
    maintainer_email="acraig2@andrew.cmu.edu",
    license="MIT",
    packages=["ajcpkg"],
    entry_points={"console_scripts": ["printterm = ajcpkg.main:main"]},
    long_description="""This is my final project for the s23 mini 2""",
)
