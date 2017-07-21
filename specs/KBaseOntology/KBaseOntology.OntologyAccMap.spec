/*
A ontology id is a string (usually GO:NNNN)
*/
typedef string ontology_acc;

typedef structure {
  mapping<ontology_acc, #KBaseOntology.SimpleOntologyTerm-1.0#> ontology_acc_term_map;
} OntologyAccMap;