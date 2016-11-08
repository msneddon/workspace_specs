/*
Biochemistry structure ID
@id kb
*/
typedef string biochemstruct_id;

/*
Compound structure ID
@id external
*/
typedef string structure_id;

/*
ReactionSet object

@searchable ws_subset id type
*/
typedef structure {
  structure_id id;
  string type;
  string data;
} CompoundStructure;

/*
BiochemistryStructures object

@optional description name
@searchable ws_subset id name structures
*/
typedef structure {
  biochemstruct_id id;
  string name;
  string description;
  list<CompoundStructure> structures;
} BiochemistryStructures;