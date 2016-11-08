/*
A ontology id is a string (usually GO:NNNN)
*/
typedef string ontology_acc;

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

@optional evidence_codes gene_list
*/
typedef structure {
  ontology_acc acc;
  string type;
  string name;
  list<evidence_code> evidence_codes;
  mapping<genome_id, gene_list> gene_list;
} Ontology;