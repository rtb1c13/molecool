"""
molecool
A Python package for analysing and visualising xyz files. For MolSSI workshop Python Package Development.
"""

# Add imports here
from .measure import *
from .molecule import *
from .visualise import *
from .atom_data import * 

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
