/*
A gene_id is a string (usually kb.g.NNNN.CCC.NNNN, but can be free-form)
*/
typedef string gene_id;

/*
Structure for OntologyAnnotation object
        @optional p_value
*/
typedef structure {
  string ontology_id;
  string ontology_type;
  string ontology_description;
  string p_value;
} OntologyAnnotation;

typedef list<OntologyAnnotation> ontology_annotation_list;

/*
Structure for GeneAnnotations
*/
typedef structure {
  mapping<gene_id, ontology_annotation_list> gene_enrichment_annotations;
} GeneAnnotations;