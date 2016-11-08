typedef int bool;

/*
A library of single end reads.
lib - the reads
strain - information about the genetic source
source - information about the source of this data
sequencing_tech - the technology used to sequence the genetic information
read_count - the number of reads in the this dataset
read_size - the total size of the reads, in bases
gc_content - the GC content of the reads.
single_genome - true or missing if the reads are from a single genome.
    False if the reads are from a metagenome.

@optional gc_content source strain read_count read_size single_genome
@metadata ws strain.genus
@metadata ws strain.species
@metadata ws strain.strain
@metadata ws strain.ncbi_taxid
@metadata ws source.source
@metadata ws source.source_id
@metadata ws source.project_id
@metadata ws read_count
@metadata ws read_size
@metadata ws gc_content
@metadata ws sequencing_tech
@metadata ws single_genome
*/
typedef structure {
  #KBaseFile.FileRef-1.1# lib;
  #KBaseCommon.StrainInfo-1.0# strain;
  #KBaseCommon.SourceInfo-1.0# source;
  bool single_genome;
  string sequencing_tech;
  int read_count;
  int read_size;
  float gc_content;
} SingleEndLibrary;