# Dislocation Ontology (DISO)

[![PID](https://img.shields.io/badge/PID-https%3A%2F%2Fpurls.helmholtz--metadaten.de%2Fdisos%2Fdiso-brightgreen)](https://purls.helmholtz-metadaten.de/disos/diso) 
[![doc](https://img.shields.io/badge/doc-https%3A%2F%2Fmaterials--data--science--and--informatics.github.io%2Fdislocation--ontology%2F-blue)](https://materials-data-science-and-informatics.github.io/Dislocation-Ontology-Suite/DISO/index.html) 

![GitHub contributors](https://img.shields.io/github/contributors/Materials-Data-Science-and-Informatics/dislocation-ontology) 

## Table of content
  1. [About DISOS](#about-diso)
  2. [Repository Description](#repository-description)
  3. [Documentation](#documentation)
  4. [Usage](#usage)
  5. [Contact](#contact)
  6. [License](#license)
  7. [Acknowledgements](#acknowledgements)
  8. [Citation](#citation)

## About DISO
The dislocation ontology (DISO) is an ontology defining the concepts and relationships related to linear defects in crystalline materials. We developed DISO using a top-down approach in which we start defining the most general concepts in the dislocation domain and subsequent specialization of them. DISO is published through a persistent URL following W3C best practices for publishing Linked Data.

For the version 1.1, we adapt and extend the DISO so that it can model various concepts and relationships in the discrete dislocation dynamics domain. The adaption includes adding missing concepts, improving classes definitions, exploring additional relationships between concepts, and finally aligning it with other domain-related ontologies, including the Elementary Multi-perspective Material Ontology (EMMO) and the Materials Design Ontology (MDO). This allows for representing the dislocation simulation data efficiently.

![diso-extend](https://github.com/Materials-Data-Science-and-Informatics/Dislocation-Ontology-Suite/assets/71790028/0a7e14be-4ba6-4a93-a184-32c28a25df80)


## Repository Description
* You may find the DISO with various formats: [rdf](./dislocation-ontology.owl), [turtle](./dislocation-ontology.ttl), [json-ld](./dislocation-ontology.jsonld), etc.
* We locate the folder related to data of dislocation microstructure [here](./data/)
    * [Dislocation microstructure of nickel material](./data/modelib-microstructure/modelib-nickel-microstructure.ttl) is the simulation data of dislocation microstructure of nickel (Ni) material generated by [MoDELib](https://github.com/giacomo-po/MoDELib)
* You may find a set of competence questions (CQs) along with SPARQL queries [here](./CQs/CQs_v1_1.md).
* [RDF genererator](/python-script/) is the folder to locate python scripts that are used to generate rdf-data from the [data](./data/).
    * To generate the RDF graph from the given [data](./data/), we use the [RDFLib](https://github.com/RDFLib/rdflib) python library.`
    * To generate the dislocation microstructure of nickel material, the script is in [here](./python-script/modelib/) and execute it with `python map_data.py`

## Documentation
To make it easier to understand and reuse our ontology, human-readable documentation of the ontology is generated and can be found [here](https://materials-data-science-and-informatics.github.io/Dislocation-Ontology-Suite/DISO/docs/index.html).
## Usage
* We recommend to use [Protégé 5.5.0](https://protege.stanford.edu/products.php#desktop-protege) to be able to view and navigate classes and properties in DISO.
* We recommend also to use HermiT as a reasoner for DISO. You can select it through the menu *Reasoner* in Protégé software.

## Contact
You may contact the author of DISO via a.ihsan@fz-juelich.de

## License
The code is licensed under the [MIT license](../LICENSE). Copyright © 2022.

## Acknowledgements
* European Research Council through the ERC Grant Agreement No. 759419 MuDiLingo (”A Multiscale Dislocation Language for Data-Driven Materials Science”)
* Helmholtz Metadata Collaboration (HMC) within the Hub Information at the Forschungszentrum Jülich.

## Citation 
please cite the following paper if you used any part of this work. 

`
Ahmad Zainul Ihsan, Said Fathalla, and Stefan Sandfeld. 2023. DISO: A Domain
Ontology for Modeling Dislocations in Crystalline Materials. In The 38th
ACM/SIGAPP Symposium on Applied Computing (SAC ’23), March 27-March
31, 2023, Tallinn, Estonia. ACM, New York, NY, USA, Article 4, 8 pages.
https://doi.org/10.1145/3555776.3578739
`

`
@inproceedings{ihsan2021steps,
title={Steps towards a Dislocation Ontology for Crystalline Materials},
author={Ahmad Zainul Ihsan and Danilo Dessì and Mehwish Alam and Harald Sack and Stefan Sandfeld},
booktitle={Second International Workshop on Semantic Digital Twins },
year={2021},
url={http://ceur-ws.org/Vol-2887/paper4.pdf}}`
