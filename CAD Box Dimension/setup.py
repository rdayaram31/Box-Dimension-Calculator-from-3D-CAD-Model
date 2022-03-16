from turtle import clear
from setuptools import setup, find_packages
import codecs
import os



VERSION = '0.0.1'
DESCRIPTION = 'Extracting box dimension From CAd Model Package'
# LONG_DESCRIPTION = 'Extracting the vertex from the step file AP-214. reading the step file using python and extracting the unit and the box dimension .'

# Setting up
setup(
    name="CAD_Box_dimension",
    version=VERSION,
    author="NeuralNine (Ravichandra Gupta)",
    author_email="<rdayaram31@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    # long_description=long_description,
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)