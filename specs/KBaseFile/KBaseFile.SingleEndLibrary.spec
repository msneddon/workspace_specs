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
@meta ws strain.genus
@meta ws strain.species
@meta ws strain.strain
@meta ws strain.ncbi_taxid
@meta ws source.source
@meta ws source.source_id
@meta ws source.project_id
@meta ws read_count
@meta ws read_size
@meta ws gc_content
@meta ws sequencing_tech
*/
typedef structure {
  #KBaseFile.FileRef-1.0# lib;
  #KBaseCommon.StrainInfo-1.0# strain;
  #KBaseCommon.SourceInfo-1.0# source;
  string sequencing_tech;
  int read_count;
  int read_size;
  float gc_content;
} SingleEndLibrary;