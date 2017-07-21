typedef structure {
  int rel_type_id;
  int id;
} ParentTerm;

/*
Structure for SimpleOntologyTerm
type is ontology type and it can be a domain_name for GO or it could be a relation type 
name is short description of a term
id is an internal unique id for efficient processing
To compress more, it might be changed to list later
@optional parent_list
*/
typedef structure {
  string type;
  string name;
  int id;
  list<ParentTerm> parent_list;
} SimpleOntologyTerm;