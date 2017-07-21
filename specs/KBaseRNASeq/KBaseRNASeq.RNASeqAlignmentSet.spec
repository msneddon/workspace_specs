/*
Id for KBaseRNASeq.RNASeqSampleSet
@id ws KBaseRNASeq.RNASeqSampleSet KBaseSets.ReadsSet
*/
typedef string ws_Sampleset_id;

/*
Id for KBaseRNASeq.Bowtie2Indexes
@id ws KBaseRNASeq.Bowtie2Indexes
*/
typedef string ws_bowtieIndex_id;

/*
The workspace id for a RNASeqAlignment object
@id ws KBaseRNASeq.RNASeqAlignment
*/
typedef string ws_samplealignment_id;

/*
Set object for RNASeqAlignment objects
@optional condition sample_alignments bowtie2_index aligned_using aligner_version aligner_opts
@metadata ws aligned_using
@metadata ws aligner_version
@metadata ws sampleset_id
*/
typedef structure {
  string aligned_using;
  string aligner_version;
  mapping<string, string> aligner_opts;
  ws_Sampleset_id sampleset_id;
  string genome_id;
  ws_bowtieIndex_id bowtie2_index;
  list<string> read_sample_ids;
  list<string> condition;
  list<ws_samplealignment_id> sample_alignments;
  list<mapping<string, string>> mapped_rnaseq_alignments;
  list<mapping<string, ws_samplealignment_id>> mapped_alignments_ids;
} RNASeqAlignmentSet;