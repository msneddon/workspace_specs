/*
A ontology id is a string (usually GO:NNNN)
*/
typedef string ontology_id;

/*
A code for evidence
*/
typedef string evidence_code;

/*
A genome_id is a string (usually kb|g.NNNN, but can be free-form)
*/
typedef string genome_id;

/*
A gene_id is a string (usually kb.g.NNNN.CCC.NNNN, but can be free-form)
*/
typedef string gene_id;

/*
A gene list is a list of gene_ids
*/
typedef list<gene_id> gene_list;

/*
Structure for Ontology object

@optional evidence_codes
*/
typedef structure {
  ontology_id id;
  string ontology_type;
  string ontology_domain;
  string ontology_description;
  list<evidence_code> evidence_codes;
  mapping<genome_id, gene_list> gene_list;
} Ontology;