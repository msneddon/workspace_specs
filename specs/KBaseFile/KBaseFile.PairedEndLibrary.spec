typedef int bool;

/*
A library of paired end reads. If data is interleaved lib2 will be null
or absent.
      lib1 - the left reads
      lib2 - the right reads
      strain - information about the genetic source
      source - information about the source of this data
      insert_size_mean - the mean size of the genetic fragments
      insert_size_std_dev - the standard deviation of the size of the genetic
  fragments
      interleaved - whether the left and right reads are interleaved in a
  single file
      read_orientation_outward - the orientation of the reads. If false or
  absent, the read directions face each other. Otherwise, the
  sequencing occurs in in an outward direction from the primer pairs.
      sequencing_tech - the technology used to sequence the genetic information
      read_count - the number of reads in the this dataset
      read_size - the total size of the reads, in bases
      gc_content - the GC content of the reads.

      @optional lib2
      @optional insert_size_mean insert_size_std_dev interleaved
      @optional read_orientation_outward gc_content source
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
  #KBaseFile.FileRef-1.1# lib1;
  #KBaseFile.FileRef-1.1# lib2;
  #KBaseCommon.StrainInfo-1.0# strain;
  #KBaseCommon.SourceInfo-1.0# source;
  float insert_size_mean;
  float insert_size_std_dev;
  bool interleaved;
  bool read_orientation_outward;
  string sequencing_tech;
  int read_count;
  int read_size;
  float gc_content;
} PairedEndLibrary;