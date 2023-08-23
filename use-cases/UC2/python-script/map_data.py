import json
from rdf_serializer import rdf_serializer
from pathlib import Path

# Load data 
path_data = Path('../data/MaterialProject/mp_Nickel')

# slip system configuration 
# slip plane and slip direction data for Nickel (face-centered cubic)
slip_plane_configs={'(11-1)':['[101]', '[1-10]', '[011]'], 
                  '(111)':['[1-10]', '[10-1]', '[0-11]'],
                  '(1-11)':['[10-1]', '[110]', '[011]'],
                  '(1-1-1)':['[110]', '[101]', '[0-11]'],
                 }
# slip plane normals for Nickel (face-centered cubic)
slip_plane_normals = {'(11-1)': ['[11-1]',] ,
                           '(111)': ['[111]']  ,
                           '(1-11)':['[1-11]']  ,
                          '(1-1-1)':['[1-1-1]'], 
                         }
def main():
    path_cif_json = path_data/'json'/'Ni_cif.json' 
    path_sg = path_data/'spacegroup'/'Ni_spacegroup.json' 
    with open(path_cif_json) as data1, open(path_sg) as data2: 
        cif_data = json.load(data1)
        sg_data = json.load(data2)
        mat_id = path_cif_json.stem 
        save_file = path_cif_json.stem +'.ttl'
        path_save = Path('../turtle/')/save_file
        example_uri = "http://www.example.org/{}/".format(mat_id)
        g = rdf_serializer(cif_data, sg_data, slip_plane_configs, slip_plane_normals, example_uri, mat_id)
        g.serialize(destination=path_save, format='turtle')

if __name__ == "__main__":
    main()