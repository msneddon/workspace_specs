/*
Reference to a model template
@id ws KBaseGenomes.Genome
*/
typedef string genome_ref;

typedef tuple<genome_ref, string, list<string>> WorkspaceGenomeClassData;

typedef tuple<string, string, string, list<string>> ExternalGenomeClassData;

typedef tuple<string, string> ClassData;

/*
@optional attribute_type source description
*/
typedef structure {
  string id;
  string description;
  string source;
  string attribute_type;
  list<WorkspaceGenomeClassData> workspace_training_set;
  list<ExternalGenomeClassData> external_training_set;
  list<ClassData> class_data;
} ClassifierTrainingSet;