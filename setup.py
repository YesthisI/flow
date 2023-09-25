import os
from distutils.command.register import register as register_orig
from distutils.command.upload import upload as upload_orig
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
class register(register_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')

class upload(upload_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')
    
setuptools.setup(
    name = "flowgo",
    version = "0.0.1",
    author = "YesthisI",
    author_email="teiwaz-h@mail.ru", 
    description = "This module for creating and working with individual threads in the local memory of each.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YesthisI/flow",
    packages=setuptools.find_packages(),
    
    classifiers = ["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    python_requires='>=3.6',
    cmdclass={
        'register': register,
        'upload': upload,
    })
