"""
Unit and regression test for the molecule module.
"""

# Import package, test suite, and other packages as needed
import molecool
import pytest
import sys
import numpy as np


def test_molecular_mass(methane_molecule):
    symbols, coordinates = methane_molecule
    
    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = molecool.atom_data.atomic_weights['C'] + molecool.atom_data.atomic_weights['H'] +\
         molecool.atom_data.atomic_weights['H'] + molecool.atom_data.atomic_weights['H']+ molecool.atom_data.atomic_weights['H']
    
    assert actual_mass == calculated_mass

def test_build_bond_list(methane_molecule):

    symbols, coordinates = methane_molecule

    bonds = molecool.build_bond_list(coordinates)

    assert len(bonds) == 4

    for atoms, bonds in bonds.items():
        assert bonds == 1.4
