/*
id_to_pos - simple representation of a cluster, which maps features/conditions of the cluster to the
row/col index in the data (0-based index).  The index is useful for fast lookup of data
for a specified feature/condition in the cluster.
@optional meancor msec
*/
typedef structure {
  mapping<string, int> id_to_pos;
  float meancor;
  float msec;
} labeled_cluster;

/*
A workspace ID that references a Float2DMatrix wrapper data object.
@id ws KBaseFeatureValues.ExpressionMatrix KBaseFeatureValues.SingleKnockoutFitnessMatrix
*/
typedef string ws_matrix_id;

/*
A set of clusters, typically generated for a Float2DMatrix wrapper, such as Expression
data or single feature knockout fitness data.

feature_clusters - list of labeled feature clusters
condition_clusters - (optional) list of labeled condition clusters
feature_dendrogram - (optional) maybe output from hierchical clustering approaches
condition_dendogram - (optional) maybe output from hierchical clustering approaches
original_data - pointer to the original data used to make this cluster set
report - information collected during cluster construction.

@metadata ws original_data as source_data_ref
@metadata ws length(feature_clusters) as n_feature_clusters
@metadata ws length(condition_clusters) as n_condition_clusters
@optional condition_clusters 
@optional feature_dendrogram condition_dendrogram
@optional original_data report
*/
typedef structure {
  list<labeled_cluster> feature_clusters;
  list<labeled_cluster> condition_clusters;
  string feature_dendrogram;
  string condition_dendrogram;
  ws_matrix_id original_data;
  #KBaseFeatureValues.AnalysisReport-1.0# report;
} ClusterSet;