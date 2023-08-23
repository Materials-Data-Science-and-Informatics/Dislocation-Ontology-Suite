import h5py
import json
from rdf_serializer import rdf_serializer
from pathlib import Path

# Load data 
def main():
    path_microstructure = Path("../data/modelib-microstructure/modelib-nickel-microstructure.h5")
    path_nickel_cif = Path("../data/MaterialProject/mp_Nickel/json/Ni_cif.json")
    path_nickel_space_group = Path("../data/MaterialProject/mp_Nickel/spacegroup/Ni_spacegroup.json")
    mic_name = path_microstructure.stem +'.ttl'
    path_save = Path('../turtle/')/mic_name
    data = h5py.File(path_microstructure, "r")
    node_data_50 = data['00000050']['node data']
    linker_data_50 = data['00000050']['linker data']
    loop_data_50 = data['00000050']['loop data']
    IRI = 'http://example.org/dislocation-microstructure/'

    with open(path_nickel_cif) as data1, open(path_nickel_space_group) as data2: 
        json_nickel_data = json.load(data1)
        json_nickel_sg = json.load(data2)

    G = rdf_serializer(json_nickel_data, json_nickel_sg, node_data_50, linker_data_50, loop_data_50, IRI)
    G.serialize(destination=path_save, format='turtle')

if __name__ == "__main__":
    main()