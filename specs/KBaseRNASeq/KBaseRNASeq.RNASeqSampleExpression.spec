/*
reference genome annotation id for mapping the RNA-Seq fastq file
@id ws KBaseGenomeAnnotations.GenomeAnnotation
*/
typedef string ws_genome_annotation_id;

/*
Id for KBaseRNASeq.GFFAnnotation
@id ws KBaseRNASeq.GFFAnnotation
*/
typedef string ws_referenceAnnotation_id;

/*
The workspace id for a RNASeqSampleAlignment object
@id ws KBaseRNASeq.RNASeqSampleAlignment
*/
typedef string ws_samplealignment_id;

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
The workspace object for a RNASeqSampleExpression
@optional description data_quality_level original_median external_source_date source file processing_comments
@metadata ws type
@metadata ws numerical_interpretation
@metadata ws description
@metadata ws genome_id
@metadata ws platform
*/
typedef structure {
  string id;
  string type;
  string numerical_interpretation;
  string description;
  int data_quality_level;
  float original_median;
  string external_source_date;
  list<mapping<string, float>> expression_levels;
  ws_genome_annotation_id genome_id;
  ws_referenceAnnotation_id annotation_id;
  string condition;
  mapping<string, ws_samplealignment_id> mapped_rnaseq_alignment;
  mapping<string, mapping<string, string>> mapped_sample_id;
  string platform;
  string source;
  Handle file;
  string processing_comments;
  string tool_used;
  string tool_version;
  list<mapping<string, string>> tool_opts;
} RNASeqSampleExpression;