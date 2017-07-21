/*
The workspace ID for a Genome data object.
@id ws KBaseGenomes.Genome
*/
typedef string ws_genome_id;

/*
The workspace ID for a ConditionSet data object (Note: ConditionSet objects
do not yet exist - this is for now used as a placeholder).
@id ws KBaseExperiments.ConditionSet
*/
typedef string ws_conditionset_id;

/*
A wrapper around a FloatMatrix2D designed for simple matricies of Fitness data
for single gene/feature knockouts.  Generally fitness is measured as growth rate
for the knockout strain relative to wildtype.  This data type only supports
single feature knockouts.

description - short optional description of the dataset
type - ? level, ratio, log-ratio
scale - ? probably: raw, ln, log2, log10
col_normalization - mean_center, median_center, mode_center, zscore
row_normalization - mean_center, median_center, mode_center, zscore
feature_mapping - map from row_id to feature id in the genome
data - contains values for (feature,condition) pairs, where 
    features correspond to rows and conditions are columns
    (ie data.values[feature][condition])

@optional description row_normalization col_normalization
@optional genome_ref feature_ko_mapping conditionset_ref condition_mapping report

@metadata ws type
@metadata ws scale
@metadata ws row_normalization
@metadata ws col_normalization
@metadata ws genome_ref as Genome
@metadata ws length(data.row_ids) as feature_count
@metadata ws length(data.col_ids) as condition_count
*/
typedef structure {
  string description;
  string type;
  string scale;
  string row_normalization;
  string col_normalization;
  ws_genome_id genome_ref;
  mapping<string, string> feature_ko_mapping;
  ws_conditionset_id conditionset_ref;
  mapping<string, string> condition_mapping;
  #KBaseFeatureValues.FloatMatrix2D-1.0# data;
  #KBaseFeatureValues.AnalysisReport-1.0# report;
} SingleKnockoutFitnessMatrix;