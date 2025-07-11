import argparse
from datetime import datetime
import grp, pwd
from fnmatch import fnmatch
import hashlib
from math import ceil
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


argparser = argparse.ArgumentParser(description="A content parser")

argsubparsers = argparser.add_subparsers(title="Commands", dest="command") # grabs second, thirs and so on command line argumemnts
argsubparsers.required = True

def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    match args.command:
        case "add"          : cmd_add(args)
        case "cat-file"     : cmd_cat_file(args)
        case "check-ignore" : cmd_check_ignore(args)
        case "checkout"     : cmd_checkout(args)
        case "commit"       : cmd_commit(args)
        case "hash-object"  : cmd_hash_object(args)
        case "init"         : cmd_init(args)
        case "log"          : cmd_log(args)
        case "ls-files"     : cmd_ls_files(args)
        case "ls-tree"      : cmd_ls_tree(args)
        case "rev-parse"    : cmd_rev_parse(args)
        case "rm"           : cmd_rm(args)
        case "show-ref"     : cmd_show_ref(args)
        case "status"       : cmd_status(args)
        case "tag"          : cmd_tag(args)
        case _              : print("Bad command.")
