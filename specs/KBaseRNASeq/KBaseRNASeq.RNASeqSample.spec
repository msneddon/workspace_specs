/*
Create an analysis id RNASeq analysis object
@id KBaseRNASeq.RNASeqSampleSet
*/
typedef string ws_rnaseq_sampleset_id;

/*
Specification for the RNASeqFastq Metadata

 Object for the RNASeq Metadata
 @optional library_type replicate_id platform custom
*/
typedef structure {
  string sample_id;
  string library_type;
  string replicate_id;
  string platform;
  string condition;
  string custom;
} RNASeqSampleMetaData;

/*
RNASeq fastq  object
@optional  singleend_sample pairedend_sample metadata 
@metadata ws singleend_sample.handle.file_name
@metadata ws pairedend_sample.handle_1.file_name
@metadata ws pairedend_sample.handle_2.file_name
@metadata ws metadata.replicate_id
@metadata ws metadata.library_type
@metadata ws metadata.platform
@metadata ws metadata.condition
*/
typedef structure {
  #KBaseAssembly.SingleEndLibrary-2.0# singleend_sample;
  #KBaseAssembly.PairedEndLibrary-2.0# pairedend_sample;
  ws_rnaseq_sampleset_id sampleset_id;
  RNASeqSampleMetaData metadata;
} RNASeqSample;