import argparse
import configparser
from datetime import datetime
import grp, pwd
from fnmatch import fnmatch
import hashlib
from math import ceil
import os
import re
import sys
import zlib

'''
The libraries we have are for the following

* Parsing command line arguments
* Simple datetime to keep track of commits
* fnmatch to match file extensions, this will be used in gitignore
* haslib creates unique id for commits
* zlib compression algorith. Make file size smaller when commiting/pushing I bet

'''


argpaser = argparse.ArgumentParser(description="A content parser")

argsubparsers = argpaser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True