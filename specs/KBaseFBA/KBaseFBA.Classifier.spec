/*
Reference to a training set object
@id ws KBaseFBA.ClassifierTrainingSet
*/
typedef string Trainingset_ref;

typedef structure {
  string id;
  string description;
  float tp_rate;
  float fb_rate;
  float precision;
  float recall;
  float f_measure;
  float ROC_area;
  mapping<string, int> missclassifications;
} ClassifierClasses;

typedef structure {
  string id;
  string attribute_type;
  string classifier_type;
  Trainingset_ref trainingset_ref;
  string data;
  string readable;
  int correctly_classified_instances;
  int incorrectly_classified_instances;
  int total_instances;
  float kappa;
  float mean_absolute_error;
  float root_mean_squared_error;
  float relative_absolute_error;
  float relative_squared_error;
  list<ClassifierClasses> classes;
} Classifier;