/*
Reference to a generic workspace object.  Used in evidence. 
    @id ws
*/
typedef string generic_ws_reference;

/*
Evidence is information that supports some other bit of information or assertion

Generic WS reference, not to a specific typed object.  A workspace reference.

Evidence type - structural or functional?

@optional description supporting_objects
*/
typedef structure {
  string evidence_id;
  string description;
  string evidence_type;
  list<generic_ws_reference> supporting_objects;
} evidence;

/*
EvidenceContainer is a set of evidences.  Technically it could be any list of evidences, but typically it would be set of evidences to support the annotation of a genome.

May want publications in here?

@optional name description notes
*/
typedef structure {
  string evidence_container_id;
  string name;
  string description;
  string notes;
  mapping<string, evidence> evidences;
} EvidenceContainer;