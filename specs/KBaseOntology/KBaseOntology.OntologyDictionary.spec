/*
@optional data_version date saved_by auto_generated_by import subsetdef synonymtypedef default_namespace namespace_id_rule idspace treat_xrefs_as_equivalent treat_xrefs_as_genus_differentia treat_xrefs_as_relationship treat_xrefs_as_is_a remark ontology typedef_hash instance_hash
*/
typedef structure {
  string format_version;
  string data_version;
  string date;
  string saved_by;
  string auto_generated_by;
  list<string> import;
  list<string> subsetdef;
  list<string> synonymtypedef;
  string default_namespace;
  list<string> namespace_id_rule;
  list<string> idspace;
  list<string> treat_xrefs_as_equivalent;
  list<string> treat_xrefs_as_genus_differentia;
  list<string> treat_xrefs_as_relationship;
  list<string> treat_xrefs_as_is_a;
  list<string> remark;
  string ontology;
  mapping<string, #KBaseOntology.OntologyTerm-1.1#> term_hash;
  mapping<string, #KBaseOntology.OntologyTypedef-1.0#> typedef_hash;
  mapping<string, #KBaseOntology.OntologyInstance-1.0#> instance_hash;
} OntologyDictionary;