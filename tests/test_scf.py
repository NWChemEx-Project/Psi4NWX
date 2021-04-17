import sys
import os
from PyNWChemEx import *

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)
from psi4nwx import *

mm = sde.ModuleManager()
nwx.load_modules(mm)
psi4nwx.load_modules(mm)
molecule = libchemist.MoleculeManager().at("water")
basis = libchemist.apply_basis("sto-3g", molecule)
canonical_mos = property_types.type.canonical_space_t["double"]
pt_type = property_types.ReferenceWavefunction["double", canonical_mos]

C = mm.run_as[pt_type]("Psi4 SCF", molecule, basis)
