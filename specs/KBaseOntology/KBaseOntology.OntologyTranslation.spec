/*
The workspace reference for an ontology dictionary object
@id ws KBaseOntology.OntologyDictionary
*/
typedef string OntologyDictionary_ref;

/*
@optional equiv_name
*/
typedef structure {
  string equiv_term;
  string equiv_name;
} EquivalentTerm;

/*
@optional name
*/
typedef structure {
  string name;
  list<EquivalentTerm> equiv_terms;
} TranslationRecord;

/*
@optional comment
*/
typedef structure {
  string comment;
  OntologyDictionary_ref ontology1;
  OntologyDictionary_ref ontology2;
  mapping<string, TranslationRecord> translation;
} OntologyTranslation;