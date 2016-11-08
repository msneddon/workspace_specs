/*
Reference to a classifier object
@id ws KBaseFBA.Classifier
*/
typedef string Classifier_ref;

/*
Reference to a model template
@id ws KBaseGenomes.Genome
*/
typedef string genome_ref;

typedef structure {
  string id;
  Classifier_ref classifier_ref;
  list<tuple<genome_ref, string, float>> workspace_genomes;
  list<tuple<string, string, string, float>> external_genomes;
} ClassifierResult;