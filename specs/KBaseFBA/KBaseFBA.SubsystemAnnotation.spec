/*
Reference to a biochemistry object
@id ws KBaseBiochem.Biochemistry
*/
typedef string Biochemistry_ref;

/*
Reference to a mapping object
@id ws KBaseOntology.Mapping
*/
typedef string mapping_ref;

/*
SubsystemReaction object: this object holds information about individual reactions in a subsystems
*/
typedef structure {
  string id;
  string reaction_ref;
  list<string> roles;
  string tooltip;
} SubsystemReaction;

/*
SubsystemAnnotation object: this object holds all reactions in subsystems
*/
typedef structure {
  string id;
  Biochemistry_ref biochemistry_ref;
  mapping_ref mapping_ref;
  mapping<string, list<tuple<string, SubsystemReaction>>> subsystems;
} SubsystemAnnotation;