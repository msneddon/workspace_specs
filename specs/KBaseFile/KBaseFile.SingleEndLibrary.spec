typedef int bool;

/*
A library of single end reads.
lib - the reads
strain - information about the genetic source
source - information about the source of this data
sequencing_tech - the technology used to sequence the genetic information
read_count - the number of reads in the this dataset
read_size - sequencing parameter defining the expected read length.
total_bases - the total number of bases for all the the reads in this library.
gc_content - the GC content of the reads.
single_genome - true or missing if the reads are from a single genome.
    False if the reads are from a metagenome.
read_length_mean - The average read length size
read_length_stdev - The standard deviation read lengths
phred_type - The scale of phred scores
number_of_duplicates - The number of reads that are duplicates
qual_min - min quality scores
qual_max - max quality scores
qual_mean - mean quality scores
qual_stdev - stdev of quality scores
base_percentages - The per base percentage breakdown

@optional gc_content source strain read_count read_size single_genome total_bases
@optional read_length_mean read_length_stdev phred_type
@optional number_of_duplicates qual_min qual_max
@optional qual_mean qual_stdev base_percentages
@metadata ws strain.genus
@metadata ws strain.species
@metadata ws strain.strain
@metadata ws strain.ncbi_taxid
@metadata ws source.source
@metadata ws source.source_id
@metadata ws source.project_id
@metadata ws read_count
@metadata ws read_size
@metadata ws total_bases
@metadata ws gc_content
@metadata ws sequencing_tech
@metadata ws single_genome
@metadata ws read_length_mean
@metadata ws read_length_stdev
@metadata ws phred_type
@metadata ws number_of_duplicates
@metadata ws qual_min
@metadata ws qual_max
@metadata ws qual_mean
@metadata ws qual_stdev
*/
typedef structure {
  #KBaseFile.FileRef-1.1# lib;
  #KBaseCommon.StrainInfo-1.0# strain;
  #KBaseCommon.SourceInfo-1.0# source;
  bool single_genome;
  string sequencing_tech;
  int read_count;
  int read_size;
  int total_bases;
  float gc_content;
  float read_length_mean;
  float read_length_stdev;
  string phred_type;
  int number_of_duplicates;
  float qual_min;
  float qual_max;
  float qual_mean;
  float qual_stdev;
  mapping<string, float> base_percentages;
} SingleEndLibrary;