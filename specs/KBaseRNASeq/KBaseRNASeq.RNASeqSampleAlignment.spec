/*
Id for the handle object
@id handle
*/
typedef string HandleId;

/*
@optional hid file_name type url remote_md5 remote_sha1
*/
typedef structure {
  HandleId hid;
  string file_name;
  string id;
  string type;
  string url;
  string remote_md5;
  string remote_sha1;
} Handle;

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
Object for the RNASeq Alignment bam file
@optional aligner_opts aligner_version aligned_using metadata
@metadata ws metadata.sample_id
@metadata ws metadata.replicate_id
@metadata ws metadata.platform
@metadata ws metadata.title
@metadata ws metadata.source
@metadata ws metadata.source_id
@metadata ws metadata.ext_source_date
@metadata ws metadata.sample_desc
@metadata ws metadata.genome_id
@metadata ws metadata.tissue
@metadata ws metadata.condition
@metadata ws aligned_using
@metadata ws aligner_version
*/
typedef structure {
  string aligned_using;
  string aligner_version;
  list<mapping<string, string>> aligner_opts;
  Handle file;
  int size;
  RNASeqSampleMetaData metadata;
} RNASeqSampleAlignment;