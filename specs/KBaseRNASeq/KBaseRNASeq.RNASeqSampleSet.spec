/*
Object to Describe the RNASeq SampleSet
@optional platform num_replicates source publication_Id external_source_date sample_ids
@metadata ws sampleset_id
@metadata ws platform
@metadata ws num_samples
@metadata ws num_replicates
@metadata ws length(condition)
*/
typedef structure {
  string sampleset_id;
  string sampleset_desc;
  string domain;
  string platform;
  int num_samples;
  int num_replicates;
  list<string> sample_ids;
  list<string> condition;
  string source;
  string Library_type;
  string publication_Id;
  string external_source_date;
} RNASeqSampleSet;