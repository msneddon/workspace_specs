/*
A workspace id for a paired end library.
@id ws KBaseFile.PairedEndLibrary
*/
typedef string pairedlib_id;

/*
A workspace id for a single end library.
@id ws KBaseFile.SingleEndLibrary
*/
typedef string singlelib_id;

/*
An assembly of reads.
Note it is *strongly* encouraged that the read libraries are included,
but the fields are optional because for some data sources there is
currently no way to map the assembly to the source reads.
    
assembly_file - the assembly
strain - information about the genetic source
source - information about the source of this data
size - the total estimated size of the genome, in bases
gc_content - the overall GC content of the assembly
contigs - the number of contigs in the assembly
pairedlibs - references to the paired end libraries used to construct
    this assembly
singlelibs - references to the single end libraries used to construct
    this assembly
assembler - the assembler program used to create the assembly file
assembler_version - the version of the assembler
assembler_parameters - the parameters provided to the assembler
scaffold_gap_pct - the percentage of bases in scaffolds that are gap
    characters
scaffold_N50 - the N50 value for the scaffolds
scaffold_L50 - the L50 value for the scaffolds
contig_N50 - the N50 value for the contigs
contig_L50 - the L50 value for the contigs

@optional gc_content source
@optional pairedlibs singlelibs
@optional assembler assembler_version assembler_parameters
@optional scaffold_gap_pct
@optional scaffold_N50 scaffold_L50 contig_N50 contig_L50

@meta ws strain.genus
@meta ws strain.species
@meta ws strain.strain
@meta ws strain.ncbi_taxid
@meta ws source.source
@meta ws source.source_id
@meta ws source.project_id
@meta ws size
@meta ws contigs
@meta ws gc_content
*/
typedef structure {
  #KBaseFile.FileRef-1.0# assembly_file;
  #KBaseCommon.StrainInfo-1.0# strain;
  #KBaseCommon.SourceInfo-1.0# source;
  int size;
  int gc_content;
  int contigs;
  string assembler;
  string assembler_version;
  string assembler_parameters;
  float scaffold_gap_pct;
  int scaffold_N50;
  int scaffold_L50;
  int contig_N50;
  int contig_L50;
  list<pairedlib_id> pairedlibs;
  list<singlelib_id> singlelibs;
} AssemblyFile;