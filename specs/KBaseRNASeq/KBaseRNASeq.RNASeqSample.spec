/*
Create an analysis id RNASeq analysis object
@id KBaseRNASeq.RNASeqAnalysis
*/
typedef string ws_rnaseq_analysis_id;

/*
reference genome id for mapping the RNA-Seq fastq file
@id ws KBaseGenomes.Genome
*/
typedef string ws_genome_id;

/*
Kbase SampleAnnotation ID
*/
typedef string sample_annotation_id;

/*
Kbase OntologyID
*/
typedef string ontology_id;

/*
Kbase OntologyName
*/
typedef string ontology_name;

/*
Kbase OntologyDefinition
*/
typedef string ontology_definition;

/*
Data structure for top level information for sample annotation and ontology
*/
typedef structure {
  sample_annotation_id sample_annotation_id;
  ontology_id ontology_id;
  ontology_name ontology_name;
  ontology_definition ontology_definition;
} SampleAnnotation;

/*
List of KBaseExpression.SampleAnnotation
*/
typedef list<SampleAnnotation> sample_annotations;

/*
Specification for the RNASeqFastq Metadata

 Object for the RNASeq Metadata
 @optional library_type platform source tissue condition source_id ext_source_date sample_desc title sample_annotations genome_id genome_scientific_name custom
*/
typedef structure {
  string sample_id;
  string library_type;
  string replicate_id;
  string platform;
  string sample_desc;
  string title;
  string source;
  string source_id;
  string ext_source_date;
  string domain;
  ws_genome_id genome_id;
  string genome_scientific_name;
  sample_annotations sample_annotations;
  string tissue;
  string condition;
  string custom;
} RNASeqSampleMetaData;

/*
RNASeq fastq  object
@optional  singleend_sample pairedend_sample metadata analysis_id analysis_desc
@metadata ws analysis_id
@metadata ws analysis_desc
@metadata ws metadata.sample_id
@metadata ws metadata.replicate_id
@metadata ws metadata.library_type
@metadata ws metadata.platform
@metadata ws metadata.title
@metadata ws metadata.source
@metadata ws metadata.source_id
@metadata ws metadata.sample_desc
@metadata ws metadata.tissue
@metadata ws metadata.condition
@metadata ws metadata.genome_id
@metadata ws metadata.ext_source_date
@metadata ws length(metadata.sample_annotations)
*/
typedef structure {
  #KBaseAssembly.SingleEndLibrary-2.1# singleend_sample;
  #KBaseAssembly.PairedEndLibrary-2.1# pairedend_sample;
  ws_rnaseq_analysis_id analysis_id;
  string analysis_desc;
  RNASeqSampleMetaData metadata;
} RNASeqSample;