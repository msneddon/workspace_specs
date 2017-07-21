/*
Structure Read_mapping_sections
@optional five_UTR three_UTR exons TSS TES introns intergenic_regions
*/
typedef structure {
  float five_UTR;
  float three_UTR;
  float TSS;
  float TES;
  float exons;
  float introns;
  float intergenic_regions;
} Read_mapping_sections;

/*
Object - getAlignmentStats method
@optional singletons multiple_alignments properly_paired alignment_rate unmapped_reads mapped_sections total_reads mapped_reads
*/
typedef structure {
  int properly_paired;
  int multiple_alignments;
  int singletons;
  float alignment_rate;
  Read_mapping_sections mapped_sections;
  int unmapped_reads;
  int mapped_reads;
  int total_reads;
} AlignmentStatsResults;