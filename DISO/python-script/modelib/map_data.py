import h5py
from rdflib import Graph, Literal
import json
from rdf_serializer_modelib import crystal_rdf_serializer, dislocation_structure_serializer
import uuid
from rdflib import Graph
from rdflib.namespace import  Namespace, RDF, PROV, XSD
from pathlib import Path
import os
from tqdm import tqdm

#dislocation ontology
DISO = Namespace("https://purls.helmholtz-metadaten.de/disos/diso#")
MDO_prov = Namespace("https://w3id.org/mdo/provenance/")

def main():
    
    path_microstructure = Path('../../data/modelib-microstructure/Copper/')
    path_cifs = Path('../../../CSO/data/MaterialProject/mp_Copper/')
    
  
    for path_micro in tqdm(Path(path_microstructure/'h5'/'density_5e16').iterdir()):
        name = path_micro.stem
        path_cif_json = path_cifs/'json'/'Cu_cif.json'
        path_sg = path_cifs/'json'/'Cu_mp-30_spacegroup.json'
        ttl_name = name + '.ttl'
        save_turtle = path_micro.parent.parent.parent/'ttl'/ttl_name
        data = h5py.File(path_micro, "r")
        mat_info = data['mat_info']

        # Graph/Ontology population
        G = Graph()
        IRI = 'http://diso-kg.com/{}/'.format(uuid.uuid4())
        ns = Namespace(IRI)
        ddd_sim = ns['ddd_sim']
        soft_model = ns['modelib']
        G.bind("diso", DISO)
        G.bind("mdoPROV", MDO_prov)
        G.add((ddd_sim, RDF.type, DISO.DDDSimulation))
        G.add((soft_model, RDF.type, PROV.SoftwareAgent))
        G.add((ddd_sim, PROV.wasAssociatedWith, soft_model))
        G.add((soft_model, MDO_prov.SoftwareName, Literal('MoDELib', datatype=XSD.string)))
        G.add((soft_model, DISO.softwareVersion, Literal('1.1.beta1', datatype=XSD.string)))
        with open(path_cif_json) as data1, open(path_sg) as data2: 
            json_cif_data = json.load(data1)
            json_sg = json.load(data2)

        crystal_rdf_serializer(G, json_cif_data, json_sg, mat_info, ns)

        # A loop that iterate through dislocation microstructure virtual specimen
        # and connect with the crystal structure information
        keys = list(data.keys())
        int_keys = [int(x) for x in keys if x.isdigit()]
        start_time_step = min(int_keys)
        end_time_step = max(int_keys)
        padded_list = [str(num).zfill(8) for num in [start_time_step, end_time_step]]
        for i, dismic in enumerate(padded_list):
            if i == 0:
                key = 'input'
            else: 
                key = 'output'
            node_data = data[dismic]['node data']
            linker_data = data[dismic]['linker data']
            loop_data = data[dismic]['loop data']

            # adding dislocation microstructures of a simulation. 
            # so far only the input and the output of dislocation microstructure
            dislocation_structure_serializer(G, mat_info, node_data, linker_data, loop_data, ns, key)

        G.serialize(destination=save_turtle, format='turtle')
        
if __name__ == "__main__":
    main()