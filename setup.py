import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="ia870",
    version="0.8",
    author="Roberto A Lotufo and collaborators",
    author_email="robertoalotufo@gmail.com",
    description="Python Morphology Toolbox for Teaching Image Processing",
    license="BSD 3 clauses",
    keywords=["image processing", "morphological image processing", "mathematical morphology"],
    url="https://github.com/robertoalotufo/ia870",
    packages=['ia870'],
    long_description=read('README.txt'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "License :: OSI Approved :: BSD License",
    ],
)
