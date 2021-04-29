from PyNWChemEx import *

class Psi4SCF(sde.ModuleBase):
    def __init__(self):
        super(Psi4SCF, self).__init__(self, self)
        canonical_mos = property_types.type.canonical_space_t["double"]
        pt_type = property_types.ReferenceWavefunction["double", canonical_mos]

        self.satisfies_property_type[pt_type]

    def run_(self, inputs, submods):
        canonical_mos = property_types.type.canonical_space_t["double"]
        pt_type = property_types.ReferenceWavefunction["double", canonical_mos]

        mol, aos = pt_type.unwrap_inputs(inputs)
        print(mol)

        egy = 0.0
        rv = self.results()
        return pt_type.wrap_results(rv, egy)


