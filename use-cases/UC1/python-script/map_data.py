import json
from rdf_serializer import rdf_serializer
from pathlib import Path

# Load data 
path_data = Path('../data/MaterialProject/mp_Aluminium') #mp_Aluminium, mp_Copper, mp_Nickel, mp_Tungsten, mp_Zirconium

def main():
    path_cif_json = path_data/'json'/'Al_cif.json' #Al_cif.json, Cu_cif.json, Ni_cif.json, W_cif.json, Zr_cif.json
    path_sg = path_data/'spacegroup'/'Al_spacegroup.json' #Al_spacegroup.json, Cu_spacegroup.json, Ni_spacegroup.json, W_spacegroup.json, Zr_spacegroup.json
    with open(path_cif_json) as data1, open(path_sg) as data2: 
        cif_data = json.load(data1)
        sg_data = json.load(data2)
        mat_id = path_cif_json.stem 
        save_file = path_cif_json.stem +'.ttl'
        path_save = Path('../turtle/')/save_file
        example_uri = "http://www.example.org/{}/".format(mat_id)
        g = rdf_serializer(cif_data, sg_data, example_uri, mat_id)
        g.serialize(destination=path_save, format='turtle')

if __name__ == "__main__":
    main()