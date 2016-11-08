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
  string ontology1;
  string ontology2;
  mapping<string, TranslationRecord> translation;
} OntologyTranslation;