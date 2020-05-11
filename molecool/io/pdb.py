"""
Functions to manipulate pdb files
"""

import numpy as np

def open_pdb(file_location):
    """Open a PDB file and read atom symbols and coordinates.

    The pdb file must specify the atom elements in the last column, and follow
    the conventions outlined in the PDB format specification.

    Parameters
    -----
    file_location : str
        The path to the PDB file to open

    Returns
    -----
    symbols : np.ndarray
        The atom symbols for each atom in the file
    coordinates : np.ndarray
        The atom x/y/z coordinates for each atom in the file

    
    """


    # This function reads in a pdb file and returns the atom names and coordinates.
    with open(file_location) as f:
        data = f.readlines()

    coordinates = []
    symbols = []
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            atom_coords = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coords)

    coords = np.array(coordinates)
    symbols = np.array(symbols)
    return symbols, coords


