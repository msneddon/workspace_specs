/*
Reference to a model template
@id ws KBaseGenomes.Genome
*/
typedef string genome_ref;

/*
@optional attribute_type source description
*/
typedef structure {
  string id;
  string description;
  string source;
  string attribute_type;
  list<tuple<genome_ref, string, list<string>>> workspace_training_set;
  list<tuple<string, string, string, list<string>>> external_training_set;
  list<tuple<string, string>> class_data;
} ClassifierTrainingSet;