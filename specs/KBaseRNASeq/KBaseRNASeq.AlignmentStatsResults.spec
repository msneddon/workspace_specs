/*
Structure Read_mapping_sections
@optional introns exons splice_junctions intergenic_regions
*/
typedef structure {
  int introns;
  int exons;
  int splice_junctions;
  int intergenic_regions;
} Read_mapping_sections;

/*
Object - getAlignmentStats method
@optional singletons multiple_alignments properly_paired alignment_rate unmapped_reads mapped_sections total_reads mapped_reads
*/
typedef structure {
  string alignment_id;
  int properly_paired;
  int multiple_alignments;
  int singletons;
  float alignment_rate;
  Read_mapping_sections mapped_sections;
  int unmapped_reads;
  int mapped_reads;
  int total_reads;
} AlignmentStatsResults;