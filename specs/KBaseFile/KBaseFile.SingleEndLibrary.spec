/*
A library of single end reads.
lib - the reads
strain - information about the genetic source
source - information about the source of this data
sequencing_tech - the technology used to sequence the genetic information
read_count - the number of reads in the this dataset
read_size - the total size of the reads, in bases
gc_content - the GC content of the reads.

@optional gc_content source
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
*/
typedef structure {
  #KBaseFile.FileRef-1.1# lib;
  #KBaseCommon.StrainInfo-1.0# strain;
  #KBaseCommon.SourceInfo-1.0# source;
  string sequencing_tech;
  int read_count;
  int read_size;
  float gc_content;
} SingleEndLibrary;