/*
A type for a DNA feature.

      CDS - A coding sequence of DNA, e.g. a protein encoding gene
      locus - a gene with potentially many mRNAs and CDSs
      mRNA - messenger RNA
      tRNA - transfer RNA
      sRNA - small RNA
      siRNA - small interfering RNA
      promoter - a promoter for a gene
      operon - an operon
      bind - a binding site
      pbind - a binding site for a protein
      operator - an operator site for a promoter
      atten - an attenuator
      term - a terminator
      CRISPR - a CRISPR
      pseudo - a pseudogene
      proph - a prophage
      ribosw - a riboswitch
      transp - a transposon
      pathis - a pathogenicity island
*/
typedef string dna_feature_type;

/*
A workspace id for an assembly file.
@id ws KBaseFile.AssemblyFile
*/
typedef string assembly_id;

/*
A file containing annotation data.
Note it is *strongly* recommended to include the assembly id, but the
field is optional since for some data sources the mapping is not
maintained.

annotation_file - the annotation file
strain - information about the genetic source
source - information about the source of this data
features_by_type - the count of features by the type of the feature
assembly_id - a reference to the assembly used to construct this
    annotation.

@optional source
@optional assembly
@optional features_by_type
@meta ws strain.genus
@meta ws strain.species
@meta ws strain.strain
@meta ws strain.ncbi_taxid
@meta ws source.source
@meta ws source.source_id
@meta ws source.project_id
*/
typedef structure {
  #KBaseFile.FileRef-1.0# annotation_file;
  #KBaseCommon.StrainInfo-1.0# strain;
  #KBaseCommon.SourceInfo-1.0# source;
  mapping<dna_feature_type, int> features_by_type;
  assembly_id assembly;
} AnnotationFile;