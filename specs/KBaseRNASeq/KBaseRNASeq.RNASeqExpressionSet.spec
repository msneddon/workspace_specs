/*
The workspace id for a RNASeqAlignmentSet object
@id ws KBaseRNASeq.RNASeqAlignmentSet
*/
typedef string ws_alignmentSet_id;

/*
Id for KBaseRNASeq.RNASeqSampleSet
@id ws KBaseRNASeq.RNASeqSampleSet
*/
typedef string ws_Sampleset_id;

/*
Id for expression sample
@id ws KBaseRNASeq.RNASeqExpression
*/
typedef string ws_expression_sample_id;

/*
Set object for RNASeqExpression objects
@optional sample_ids condition tool_used tool_version tool_opts
@metadata ws tool_used
@metadata ws tool_version
@metadata ws alignmentSet_id
*/
typedef structure {
  string tool_used;
  string tool_version;
  mapping<string, string> tool_opts;
  ws_alignmentSet_id alignmentSet_id;
  ws_Sampleset_id sampleset_id;
  string genome_id;
  list<string> sample_ids;
  list<string> condition;
  list<ws_expression_sample_id> sample_expression_ids;
  list<mapping<string, string>> mapped_expression_objects;
  list<mapping<string, ws_expression_sample_id>> mapped_expression_ids;
} RNASeqExpressionSet;