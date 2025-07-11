import os
import configparser


# Going to replace git references with got to avoid file confusion with my actual git version control folder 
class GotRepository(object):
    """ A got repository """

    worktree = None
    gotdir = None
    conf = None

    def __init__(self, path, force =False):
        self.worktree = path
        self.gotdir = os.path.join(path, ".got") # whatever directory we are inside plus the obvious .git folder 

        if not (force or os.path.isdir(self.gotdir)):
            raise Exception(f"Not a Git repository {path}")
        
        # read configuration file in .got/config
        self.conf = configparser.ConfigParser()
        cf = repo_file(self, "config")

        if cf and os.path.exists(cf):
            self.conf.read([cf])
        elif not force:
            raise Exception("Configuration file missing")
        
        # version format?
        if not force:
            vers = int(self.conf.get("core", "repositoryformatversion")) # transform string received into int
            if vers != 0:
                raise Exception("Unsupported repositoryformatversion: {vers}")


""" Note on the use of * --
    This basically means that any extra paramters will be accepted and collected as a tuple inside path
"""

def repo_path(repo, *path):
        """ Compute path under repo's gitdir."""
        """ returns the full path as a file path """
        return os.path.join(repo.gotdir, *path)
    
def repo_file(repo, *path, mkdir=False):

    # similar to repo path but creates dirname(*path) if absent
    # If mkdir is true it will return the new path of the new directory
    if repo_dir(path, *path[:-1], mkdir=mkdir):
        return repo_path(repo, *path)
    
def repo_dir(repo, *path, mkdir=False):
    """Samme as repo_path, but mkdir *path if absent if mkdir"""
    """ Creates directory if mkdir is true"""

    path = repo_path(repo, *path)
