import h5py
from rdflib import Graph, Literal
import json
from rdf_serializer_modelib import crystal_rdf_serializer, dislocation_structure_serializer, cube_edge_length
import uuid
from rdflib import Graph
from rdflib.namespace import  Namespace, RDF, PROV, XSD, FOAF
from pathlib import Path


SIM = Namespace("https://purls.helmholtz-metadaten.de/disos/sim#")
MDO_prov = Namespace("https://w3id.org/mdo/provenance/")
MWO = Namespace("http://purls.helmholtz-metadaten.de/mwo/")

def main():
    
    path_microstructure = Path('../data/modelib-microstructure/Copper/Cu_50_1e16_4_relaxed.h5')
    path_cif = Path('../data/MaterialProject/mp_Copper/json/Cu_cif.json')
    path_sg = Path('../data/MaterialProject/mp_Copper/spacegroup/Cu_spacegroup.json')
    path_mesh = Path('../data/modelib-microstructure/Copper/mesh_folder/')
  
    # for path_micro in tqdm(Path(path_microstructure/'h5'/'density_5e16').iterdir()):
    name = path_microstructure.stem
    ttl_name = name + '.ttl'
    mic_name = path_microstructure.stem +'.ttl'
    path_save = Path('../turtle/')/mic_name
    data = h5py.File(path_microstructure, "r")
    mat_info = data['mat_info']
    sim_info = data['dd_config']
    load_ex_info = data['uniformExternalLoadController']
    init_micro = data['init_micro']
    poly_info = data['polycrystal']


    # Graph/Ontology population
    G = Graph()
    IRI = 'http://dislockg.com/{}/'.format(uuid.uuid4())
    person_IRI = 'http://dislockg.com/person/'
    modelib_IRI = 'http://dislockg.com/'
    ns = Namespace(IRI)
    person_ns = Namespace(person_IRI)
    modelib_ns = Namespace(modelib_IRI)
    ddd_sim = ns['ddd_sim']
    data_creator = person_ns['P1']
    soft_model = modelib_ns['modelib']
    cross_slip_param = ns['cross_slip_param']
    junction_param = ns['junction_param']
    external_load_param = ns['external_load_param']
    cross_slip_param_val = sim_info.attrs['crossSlipModel']
    junction_param_val = sim_info.attrs['maxJunctionIterations']
    external_load_param_val = load_ex_info.attrs['enable']
    mesh_file = path_mesh/poly_info.attrs['meshFile'].split('/')[-1]
    edge_length = cube_edge_length(mesh_file, mat_info.attrs['b_SI'])*1e9 # in nm
    G.bind('sim', SIM)
    G.bind("mdoPROV", MDO_prov)
    G.bind("mwo", MWO)
    G.add((ddd_sim, RDF.type, SIM.DDDSimulation))
    G.add((data_creator, RDF.type, PROV.Person))
    G.add((ddd_sim, PROV.wasAssociatedWith, data_creator))
    G.add((data_creator, FOAF.firstName, Literal('Ahmad Zainul', datatype=XSD.string)))
    G.add((data_creator, FOAF.family_name, Literal("Ihsan", datatype=XSD.string)))
    G.add((data_creator, MWO.hasORCID, Literal("0000-0002-1008-4530", datatype=XSD.string)))
    G.add((soft_model, RDF.type, PROV.SoftwareAgent))
    G.add((cross_slip_param, RDF.type, SIM.CrossSlip))
    G.add((junction_param, RDF.type, SIM.JunctionFormation))
    G.add((external_load_param, RDF.type, SIM.ExternalLoadParameter))
    G.add((ddd_sim, PROV.wasAssociatedWith, soft_model))
    G.add((ddd_sim, SIM.simulationDescription, Literal("relaxation calculation", datatype=XSD.string)))
    G.add((ddd_sim, SIM.hasSimulationParameter, cross_slip_param))
    G.add((cross_slip_param, SIM.parameterActivation, Literal(bool(cross_slip_param_val), datatype=XSD.boolean)))
    G.add((ddd_sim, SIM.hasSimulationParameter, junction_param))
    G.add((junction_param, SIM.parameterActivation, Literal(bool(junction_param_val), datatype=XSD.boolean)))
    G.add((ddd_sim, SIM.hasSimulationParameter, external_load_param))
    G.add((external_load_param, SIM.parameterActivation, Literal(bool(external_load_param_val), datatype=XSD.boolean)))
    G.add((soft_model, MDO_prov.SoftwareName, Literal('MODELIB', datatype=XSD.string)))
    G.add((soft_model, SIM.softwareVersion, Literal('1.1.beta1', datatype=XSD.string)))

    with open(path_cif) as data1, open(path_sg) as data2: 
        json_cif_data = json.load(data1)
        json_sg = json.load(data2)

    g_crys=crystal_rdf_serializer(json_cif_data, json_sg, mat_info, ns)
    G += g_crys

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
            is_relaxed = False
            node_data = data[dismic]['node data']
            linker_data = data[dismic]['linker data']
            loop_data = data[dismic]['loop data']

            # adding dislocation microstructures of a simulation. 
        
            g_dis_struc = dislocation_structure_serializer(mat_info, json_cif_data, init_micro, node_data, linker_data, loop_data, ns, key, edge_length, is_relaxed)
            G+=g_dis_struc
        else: 
            key = 'output'
            is_relaxed = data[dismic]['is_relaxed'][()]
            node_data = data[dismic]['node data']
            linker_data = data[dismic]['linker data']
            loop_data = data[dismic]['loop data']

            # adding dislocation microstructures of a simulation. 
            g_dis_struc = dislocation_structure_serializer(mat_info, json_cif_data, init_micro, node_data, linker_data, loop_data, ns, key, edge_length, is_relaxed)
            G+=g_dis_struc
        
    G.serialize(destination=path_save, format='turtle')
        
if __name__ == "__main__":
    main()