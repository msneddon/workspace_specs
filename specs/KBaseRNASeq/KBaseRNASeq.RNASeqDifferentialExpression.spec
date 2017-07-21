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
Id for expression sample set
@id ws KBaseRNASeq.RNASeqExpressionSet
*/
typedef string ws_expressionSet_id;

/*
The workspace id for a RNASeqAlignmentSet object
@id ws KBaseRNASeq.RNASeqAlignmentSet
*/
typedef string ws_alignmentSet_id;

/*
Id for KBaseRNASeq.RNASeqSampleSet
@id ws KBaseRNASeq.RNASeqSampleSet KBaseSets.ReadsSet
*/
typedef string ws_Sampleset_id;

/*
Object RNASeqDifferentialExpression file structure
@optional tool_opts tool_version sample_ids comments
*/
typedef structure {
  string tool_used;
  string tool_version;
  list<mapping<string, string>> tool_opts;
  Handle file;
  list<string> sample_ids;
  list<string> condition;
  string genome_id;
  ws_expressionSet_id expressionSet_id;
  ws_alignmentSet_id alignmentSet_id;
  ws_Sampleset_id sampleset_id;
  string comments;
} RNASeqDifferentialExpression;