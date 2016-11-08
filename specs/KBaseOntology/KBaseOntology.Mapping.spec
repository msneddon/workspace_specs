/*
ID of map object
@id kb
*/
typedef string map_id;

/*
ID of role object
@id external
*/
typedef string role_id;

/*
Role object containing data relating to functional role
            
@optional name seedfeature
@searchable ws_subset id seedfeature name
*/
typedef structure {
  role_id id;
  string name;
  string seedfeature;
} Role;

/*
ID of subsystem object
@id external
*/
typedef string subsystem_id;

/*
Reference to a role
@id subws KBaseOntology.Mapping.roles.[*].id
*/
typedef string role_ref;

/*
Subsystem object with data on functionally related groups of roles
            
@optional name
@searchable ws_subset id name class subclass type role_refs
*/
typedef structure {
  subsystem_id id;
  string name;
  string class;
  string subclass;
  string type;
  list<role_ref> role_refs;
} Subsystem;

/*
ID of complex object
@id external
*/
typedef string complex_id;

/*
ComplexRole object containing data relating to role in complex

@searchable ws_subset role_ref optionalRole type triggering
*/
typedef structure {
  role_ref role_ref;
  int optionalRole;
  string type;
  int triggering;
} ComplexRole;

/*
Complex object combines multiple subunit roles in a single biological function
            
@optional name
@searchable ws_subset id name
@searchable ws_subset complexroles.[*].(role_ref,type,optionalRole,triggering)
*/
typedef structure {
  complex_id id;
  string name;
  list<ComplexRole> complexroles;
} Complex;

/*
Mapping object holds data on subsystems and complexes
            
@optional name
@searchable ws_subset id name role_aliases complex_aliases subsystem_aliases
@searchable ws_subset roles.[*].(id,name,seedfeature) 
@searchable ws_subset subsystems.[*].(id,name,class,subclass,type,role_refs) 
@searchable ws_subset complexes.[*].(id,name,complexroles.[*].(role_ref,type,optionalRole,triggering))
*/
typedef structure {
  map_id id;
  string name;
  list<Role> roles;
  list<Subsystem> subsystems;
  list<Complex> complexes;
  mapping<role_id, mapping<string, list<string>>> role_aliases;
  mapping<complex_id, mapping<string, list<string>>> complex_aliases;
  mapping<subsystem_id, mapping<string, list<string>>> subsystem_aliases;
} Mapping;