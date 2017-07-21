/*
Id for the handle object
@id handle
*/
typedef string HandleId;

/*
@optional hid file_name type url remote_md5 remote_sha1
*/
typedef structure {
  HandleId hid;
  string file_name;
  string id;
  string type;
  string url;
  string remote_md5;
  string remote_sha1;
} Handle;

/*
Object RNASeqDifferentialExpression file structure
     @metadata ws analysis.experiment_id
     @metadata ws analysis.title
     @metadata ws analysis.Library_type
     @metadata ws analysis.platform
     @metadata ws analysis.num_samples
     @metadata ws analysis.num_replicates
     @metadata ws length(analysis.sample_ids)
     @metadata ws length(analysis.tissue)
     @metadata ws length(analysis.condition)
*/
typedef structure {
  Handle file;
  #KBaseRNASeq.RNASeqAnalysis-12.0# analysis;
} RNASeqCuffdiffdifferentialExpression;