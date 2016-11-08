/*
A gene_id is a string (usually kb.g.NNNN.CCC.NNNN, but can be free-form)
*/
typedef string gene_id;

/*
A ontology id is a string (usually GO:NNNN)
*/
typedef string ontology_acc;

/*
A code for evidence
*/
typedef string evidence_code;

/*
Structure for OntologyTermAnnotation object
@optional ontology_type ontology_description
*/
typedef structure {
  string ontology_type;
  string ontology_description;
  list<evidence_code> evidence_codes;
} OntologyTermAnnotation;

typedef mapping<ontology_acc, OntologyTermAnnotation> ontology_term_annotation_map;

typedef mapping<gene_id, ontology_term_annotation_map> gene_annotation_map;

/*
Structure for GeneOntologyAnnotations
@optional source
*/
typedef structure {
  gene_annotation_map ga;
  string source;
} GeneOntologyAnnotation;