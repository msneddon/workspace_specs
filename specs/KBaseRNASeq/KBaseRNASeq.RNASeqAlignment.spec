/*
Id for KBaseRNASeq.Bowtie2Indexes
@id ws KBaseRNASeq.Bowtie2Indexes
*/
typedef string ws_bowtieIndex_id;

/*
Id for KBaseRNASeq.RNASeqSampleSet
@id ws KBaseRNASeq.RNASeqSampleSet KBaseSets.ReadsSet
*/
typedef string ws_Sampleset_id;

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
Object for the RNASeq Alignment bam file
@optional aligner_opts aligner_version aligned_using replicate_id platform size mapped_sample_id sampleset_id alignment_stats bowtie2_index 
@metadata ws aligned_using
@metadata ws aligner_version
@metadata ws genome_id
@metadata ws size
@metadata ws alignment_stats.total_reads
@metadata ws alignment_stats.mapped_reads
@metadata ws alignment_stats.alignment_rate
@metadata ws read_sample_id
@metadata ws library_type
@metadata ws replicate_id
@metadata ws condition
@metadata ws platform
*/
typedef structure {
  string aligned_using;
  string aligner_version;
  string library_type;
  string read_sample_id;
  string replicate_id;
  string condition;
  string platform;
  string genome_id;
  ws_bowtieIndex_id bowtie2_index;
  mapping<string, string> aligner_opts;
  mapping<string, mapping<string, string>> mapped_sample_id;
  ws_Sampleset_id sampleset_id;
  Handle file;
  int size;
  #KBaseRNASeq.AlignmentStatsResults-2.0# alignment_stats;
} RNASeqAlignment;