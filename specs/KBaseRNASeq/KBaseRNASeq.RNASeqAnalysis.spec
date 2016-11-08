/*
reference genome id for mapping the RNA-Seq fastq file
@id ws KBaseGenomes.Genome
*/
typedef string ws_genome_id;

/*
The workspace id of a RNASeqSample
@id ws KBaseRNASeq.RNASeqSample
*/
typedef string ws_rnaseqSample_id;

/*
Object type to define replicate group
/*

typedef structure{
      ws_rnaseq_analysis_id analysis_id;
      string sample_name;
      ws_rnaseqSample_ids sample_replicate_group;
  }RNASeqSampleReplicateGroup;

/*
Object type to define id to RNASeqSampleReplicateGroup
@id ws KBaseRNASeq.RNASeqSampleReplicateGroup
*/
typedef string ws_RNASeqSampleReplicateGroup_id;

/*
The workspace id for a RNASeqSampleAlignment object
@id ws KBaseRNASeq.RNASeqSampleAlignment
*/
typedef string ws_samplealignment_id;

/*
The mapping object for the ws_rnaseqSample_id with the ws_samplealignment_id
*/
typedef mapping<ws_rnaseqSample_id, ws_samplealignment_id> mapped_sample_alignment;

/*
Id for expression sample
@id ws KBaseExpression.ExpressionSample
*/
typedef string ws_expression_sample_id;

/*
The mapping object for the ws_rnaseqSample_id with the ws_expression_sample_id
*/
typedef mapping<ws_rnaseqSample_id, ws_expression_sample_id> mapped_sample_expression;

/*
Id for KBaseRNASeq.RNASeqCuffmergetranscriptome
@id ws KBaseRNASeq.RNASeqCuffmergetranscriptome
*/
typedef string ws_transcriptome_id;

/*
Id for KBaseRNASeq.RNASeqCuffdiffdifferentialExpression
@id ws KBaseRNASeq.RNASeqCuffdiffdifferentialExpression
*/
typedef string ws_cuffdiff_diff_exp_id;

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
Id for KBaseRNASeq.ReferenceAnnotation
@id ws KBaseRNASeq.ReferenceAnnotation
*/
typedef string ws_referenceAnnotation_id;

/*
Object to Describe the RNASeq analysis
@optional experiment_desc num_replicates title platform genome_id source tissue condition annotation_id publication_id source_ids external_source_date sample_ids alignments expression_values sample_annotations_map genome_scientific_name sample_rep_groups alignments expression_values transcriptome_id cuffdiff_diff_exp_id experiment_design
@metadata ws experiment_id
@metadata ws title
@metadata ws experiment_desc
@metadata ws experiment_design
@metadata ws platform
@metadata ws genome_id
@metadata ws genome_scientific_name
@metadata ws num_samples
@metadata ws num_replicates 
@metadata ws annotation_id
*/
typedef structure {
  string experiment_id;
  string title;
  string experiment_desc;
  string experiment_design;
  string domain;
  string platform;
  ws_genome_id genome_id;
  string genome_scientific_name;
  int num_samples;
  int num_replicates;
  list<ws_rnaseqSample_id> sample_ids;
  list<ws_RNASeqSampleReplicateGroup_id> sample_rep_groups;
  mapped_sample_alignment alignments;
  mapped_sample_expression expression_values;
  ws_transcriptome_id transcriptome_id;
  ws_cuffdiff_diff_exp_id cuffdiff_diff_exp_id;
  list<string> tissue;
  list<string> condition;
  mapping<string, sample_annotations> sample_annotations_map;
  ws_referenceAnnotation_id annotation_id;
  string source;
  string Library_type;
  string publication_id;
  list<string> source_ids;
  string external_source_date;
} RNASeqAnalysis;