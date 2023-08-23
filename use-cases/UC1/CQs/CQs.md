# Competency Questions (CQs)
We list a number of CQs that can be used to query the information related to the use case 1.

1. Which crystal structure share the same cubic crystal system?
2. Which crystal structure share the same hexagonal crystal system?
3. What are the lattice parameters of length given a crystal structure?
4. What are the lattice parameters of angle given a crystal structure?
5. Given the space group of a crystal structure, what is the bravais lattice centering?
6. Given the crystal structure, what are the corresponding space group and point group?
7. Given the point group of a crystal structure, what is the corresponding crystal system?

# Answer to CQs via SPARQL

1. Which crystal structure share the same cubic crystal system?
```
PREFIX cso: <https://purls.helmholtz-metadaten.de/disos/cso#> 
PREFIX chebi: <http://purl.obolibrary.org/obo/> 

SELECT ?crystalstructure ?crystal_system WHERE{
	?crystalstructure a cso:CrystalStructure ; cso:hasLattice ?lattice .
	?lattice cso:hasCrystalSystem ?crystal_system.
	?crystal_system a cso:Cubic .
}
```

2. Which crystal structure share the same hexagonal crystal system?
```
PREFIX cso: <https://purls.helmholtz-metadaten.de/disos/cso#> 

SELECT ?crystalstructure ?crystal_system WHERE{
	?crystalstructure a cso:CrystalStructure ; cso:hasLattice ?lattice .
	?lattice cso:hasCrystalSystem ?crystal_system.
	?crystal_system a cso:Hexagonal .
}
```

3. What are the lattice parameters of length given a crystal structure? 
```
PREFIX cso: <https://purls.helmholtz-metadaten.de/disos/cso#> 

SELECT ?crystalstructure ?length_a ?length_b ?length_c WHERE{
	?crystalstructure a cso:CrystalStructure ; cso:hasLattice ?lattice .
	?lattice cso:hasUnitCell ?unitcell .
	?unitcell cso:hasLatticeParameterLength ?latticeParameterLength.  
	?latticeParameterLength cso:latticeParameterLengthA ?length_a;
		cso:latticeParameterLengthB ?length_b;
		cso:latticeParameterLengthC ?length_c.
}
```

4. What are the lattice parameters of angle given a crystal structure?
```
PREFIX cso: <https://purls.helmholtz-metadaten.de/disos/cso#> 

SELECT ?crystalstructure ?angle_alpha ?angle_beta ?angle_gamma WHERE{
	?crystalstructure a cso:CrystalStructure ; cso:hasLattice ?lattice .
	?lattice cso:hasUnitCell ?unitcell .
	?unitcell cso:hasLatticeParameterAngle ?latticeParameterAngle.
	?latticeParameterAngle cso:latticeParameterAngleAlpha ?angle_alpha;  
		cso:latticeParameterAngleBeta ?angle_beta;
		cso:latticeParameterAngleGamma ?angle_gamma.
}
```

5. Given the space group of a crystal structure, what is the bravais lattice centering?
```
PREFIX cso: <https://purls.helmholtz-metadaten.de/disos/cso#> 

SELECT  ?crystal_structure ?centering WHERE{
	?crystal_structure a cso:CrystalStructure;
		cso:hasLattice ?bravais_lattice . 
	?bravais_lattice cso:centering ?centering . 
}
```

6. Given the crystal structure, what are the corresponding space group and point group?
```
PREFIX cso: <https://purls.helmholtz-metadaten.de/disos/cso#> 
PREFIX mdo: <https://w3id.org/mdo/structure/> 

SELECT  ?crystal_structure ?space_group ?point_group WHERE{
	?crystal_structure a cso:CrystalStructure;
		mdo:hasSpaceGroup ?sg.
	?sg mdo:hasPointGroup ?pg ;
	 	mdo:SpaceGroupSymbol ?space_group . 
	?pg mdo:PointGroupHMName ?point_group .
}
```

7. Given the point group of a crystal structure, what is the corresponding crystal system?
```
PREFIX cso: <https://purls.helmholtz-metadaten.de/disos/cso#> 
PREFIX mdo: <https://w3id.org/mdo/structure/> 

SELECT  ?point_group ?crystal_system WHERE{
	?point_group a mdo:PointGroup;
		cso:isPointGroupOf ?cs.
	?cs rdf:type cso:CrystalSystem.
	?cs rdf:type ?crystal_system
}
```