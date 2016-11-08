/*
Reference to a classifier object
@id ws KBaseFBA.Classifier
*/
typedef string Classifier_ref;

/*
Reference to a model template
@id ws KBaseGenomes.Genome KBaseGenomeAnnotations.GenomeAnnotation
*/
typedef string genome_ref;

typedef tuple<genome_ref, string, float> WorkspaceGenomeClassPrediction;

typedef tuple<string, string, string, float> ExternalGenomeClassPrediction;

typedef structure {
  string id;
  Classifier_ref classifier_ref;
  list<WorkspaceGenomeClassPrediction> workspace_genomes;
  list<ExternalGenomeClassPrediction> external_genomes;
} ClassifierResult;