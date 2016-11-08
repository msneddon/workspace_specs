/*
A gene_id is a string (usually kb.g.NNNN.CCC.NNNN, but can be free-form)
*/
typedef string gene_id;

/*
A ontology id is a string (usually GO:NNNN)
*/
typedef string ontology_id;

/*
A code for evidence
*/
typedef string evidence_code;

/*
Structure for OntologyAnnotation object
*/
typedef structure {
  string ontology_type;
  string ontology_description;
  list<evidence_code> evidence_codes;
} OntologyAnnotation;

typedef mapping<ontology_id, OntologyAnnotation> ontology_annotation_map;

/*
Structure for GeneAnnotations
*/
typedef mapping<gene_id, ontology_annotation_map> gene_enrichment_annotations;