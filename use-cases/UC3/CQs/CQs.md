# Competency Questions (CQs)
We list a number of CQs that can be used to query the information related to the use case 3.

1. Which crystal structure share the same cubic crystal system?
2. Which crystal structure share the same hexagonal crystal system?
3. What are the lattice parameters of length given a crystal structure?
4. What are the lattice parameters of angle given a crystal structure?
5. Given the space group of a crystal structure, what is the bravais lattice centering?
6. Given the crystal structure, what are the corresponding space group and point group?
7. Given the point group of a crystal structure, what is the corresponding crystal system?
8. What are the slip systems of a given crystal structure?
9. What are the slip planes of a given crystal structure?
10. What is the family of slip plane given a slip plane in the crystal?
11. What is the  family of slip direction given a slip direction in the crystal?
12. Given a slip plane of the crystal structure, what is the slip direction?
13. In which slip planes is a dislocation moves on?
14. What is the Burgers vector of the dislocation?
15. What is the Burgers vector magnitude of the dislocation?
16. Given a 3-D vector instance (Burgers vector, vector position, etc), what are the vector components?
17. Given a 3-D vector instance ( Burgers vector, vector position, etc), what is the vector magnitude?
18. Given a Basis of a vector in 3-D space, what are the first axis basis vector?
19. Given a Basis of a vector in 3-D space, what are the second axis basis vector?
20. Given a 3-D vector instance Burgers vector, what is the unit?

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

8. What are the slip systems of a given crystal structure?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/disos/diso#>
PREFIX cso: <https://purls.helmholtz-metadaten.de/disos/cso#> 

SELECT ?crystalstructure ?slip_system ?slip_plane_normal_val ?slip_direction_val WHERE{
	?crystalstructure a cso:CrystalStructure ; 
		diso:hasSlipSystem ?slip_system . 
	?slip_system diso:hasSlipPlaneNormal ?slip_plane_normal ; 
		diso:hasSlipDirection ?slip_direction.
	?slip_plane_normal diso:directionMillerIndice ?slip_plane_normal_val. 
	?slip_direction diso:directionMillerIndice ?slip_direction_val.
}
```

9. What are the slip planes of a given crystal structure?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/disos/diso#>
PREFIX cso: <https://purls.helmholtz-metadaten.de/disos/cso#> 

SELECT  ?crystal_structure ?slip_plane ?slip_plane_miller_indice 
WHERE{
	?crystal_structure a cso:CrystalStructure.
	?crystal_structure diso:hasSlipPlane ?slip_plane.
	?slip_plane diso:planeMillerIndice ?slip_plane_miller_indice .
}
```
10. What is the family of slip plane given a slip plane in the crystal?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/disos/diso#>

SELECT  ?slip_plane ?slip_plane_miller_indice ?family_of_slip_plane_miller_indice
WHERE{
	?slip_plane a diso:SlipPlane ; 
		diso:planeMillerIndice ?slip_plane_miller_indice ; 
		diso:familyPlaneMillerIndice ?family_of_slip_plane_miller_indice .
	
}
```

11. What is the  family of slip direction given a slip direction in the crystal?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/disos/diso#>
 
SELECT  ?slip_direction ?slip_direction_miller_indice ?family_of_slip_direction_miller_indice
WHERE{
	?slip_direction a diso:SlipDirection ; 
		diso:directionMillerIndice ?slip_direction_miller_indice ; 
		diso:familyDirectionMillerIndice ?family_of_slip_direction_miller_indice .
	
}
```

12. Given a slip plane of the crystal structure, what is the slip direction?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/disos/diso#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT  ?slip_plane ?slip_direction_val WHERE{
	?slip_plane a diso:SlipPlane.
	?slip_plane diso:planeMillerIndice "(111)"^^xsd:string;
		diso:hasSlipDirection ?slip_direction. 
	?slip_direction diso:directionMillerIndice ?slip_direction_val.
}
```

13. In which slip planes is a dislocation moves on?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/disos/diso#>

SELECT  ?dislocation ?slip_plane ?slip_plane_miller_indice
WHERE{
	?dislocation a diso:Dislocation ; 
		diso:movesOn ?slip_plane . 
	?slip_plane diso:planeMillerIndice ?slip_plane_miller_indice . 
}
```
14. What is the Burgers vector of the dislocation?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/disos/diso#>
PREFIX cso: <https://purls.helmholtz-metadaten.de/disos/cso#> 

SELECT ?dislocation ?firstAxisComponent ?secondAxisComponent ?thirdAxisComponent  WHERE{
	?dislocation a diso:Dislocation . 
	?dislocation diso:hasBurgersVector ?Burgers_vector.
	?Burgers_vector	cso:hasVectorComponent ?VectorComponentOfBasis .
	?VectorComponentOfBasis cso:firstAxisComponent ?firstAxisComponent;
		cso:secondAxisComponent ?secondAxisComponent;
		cso:thirdAxisComponent ?thirdAxisComponent .
}
```
15. What is the Burgers vector magnitude of the dislocation?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/disos/diso#>
PREFIX cso: <https://purls.helmholtz-metadaten.de/disos/cso#>  

SELECT ?dislocation ?Burgers_vector_magnitude  WHERE{
	?dislocation a diso:Dislocation . 
	?dislocation diso:hasBurgersVector ?Burgers_vector.
	?Burgers_vector cso:vectorMagnitude ?Burgers_vector_magnitude .
}
```

16. Given a 3-D vector instance (Burgers vector, vector position, etc), what are the vector components?

```
PREFIX diso: <https://purls.helmholtz-metadaten.de/disos/diso#>
PREFIX cso: <https://purls.helmholtz-metadaten.de/disos/cso#>   

SELECT ?Burgers_vector ?firstAxisComponent ?secondAxisComponent ?thirdAxisComponent WHERE{
	?Burgers_vector a diso:BurgersVector;
		cso:hasVectorComponent ?VectorComponentOfBasis .
	?VectorComponentOfBasis cso:firstAxisComponent ?firstAxisComponent;
		cso:secondAxisComponent ?secondAxisComponent;
		cso:thirdAxisComponent ?thirdAxisComponent .
}
```

17. Given a 3-D vector instance ( Burgers vector, vector position, etc), what is the vector magnitude?

```
PREFIX diso: <https://purls.helmholtz-metadaten.de/disos/diso#>
PREFIX cso: <https://purls.helmholtz-metadaten.de/disos/cso#> 

SELECT ?Burgers_vector ?vectorMagnitude WHERE{
	?Burgers_vector a diso:BurgersVector;
		cso:vectorMagnitude ?vectorMagnitude .
}
```

18. Given a Basis of a vector in 3-D space, what are the first axis basis vector?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/disos/diso#>
PREFIX cso: <https://purls.helmholtz-metadaten.de/disos/cso#> 
PREFIX mdo: <https://w3id.org/mdo/structure/>    


SELECT ?Burgers_vector ?first_axis_basis_e_x ?first_axis_basis_e_y ?first_axis_basis_e_z WHERE{
	?Burgers_vector a diso:BurgersVector;
		cso:hasVectorComponent ?VectorComponents . 
	?VectorComponents cso:hasBasis ?Basis .
	?Basis cso:hasFirstAxisVector ?CoordinateVector .
	?CoordinateVector mdo:X_axisCoordinate ?first_axis_basis_e_x;
		mdo:Y_axisCoordinate ?first_axis_basis_e_y;
		mdo:Z_axisCoordinate ?first_axis_basis_e_z . 
}
```

19. Given a Basis of a vector in 3-D space, what are the second axis basis vector?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/disos/diso#>
PREFIX cso: <https://purls.helmholtz-metadaten.de/disos/cso#> 
PREFIX mdo: <https://w3id.org/mdo/structure/>    

SELECT ?Burgers_vector ?second_axis_basis_e_x ?second_axis_basis_e_y ?second_axis_basis_e_z WHERE{
	?Burgers_vector a diso:BurgersVector;
		cso:hasVectorComponent ?VectorComponents . 
	?VectorComponents cso:hasBasis ?Basis .
	?Basis cso:hasSecondAxisVector ?CoordinateVector .
	?CoordinateVector mdo:X_axisCoordinate ?second_axis_basis_e_x;
		mdo:Y_axisCoordinate ?second_axis_basis_e_y;
		mdo:Z_axisCoordinate ?second_axis_basis_e_z . 
}
```

20. Given a 3-D vector instance Burgers vector, what is the unit?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/disos/diso#>
PREFIX cso: <https://purls.helmholtz-metadaten.de/disos/cso#>  
PREFIX qudt: <http://qudt.org/schema/qudt/>

SELECT ?Burgers_vector ?unit ?quantity_kind WHERE{
	?Burgers_vector a diso:BurgersVector;
		cso:hasVectorComponent ?VectorComponents .
	?VectorComponents qudt:hasQuantityKind ?quantity_kind ;
		qudt:quantityValue ?qv.
	?qv qudt:unit ?unit.
}
```