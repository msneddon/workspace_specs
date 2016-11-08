typedef string boolean_gene_expression_data_id;

/*
Genome feature ID
@id external
*/
typedef string feature_id;

/*
Indicates on/off state of a gene, 1=on, -1=off, 0=unknown
*/
typedef int on_off_state;

typedef string source;

/*
A simplified representation of gene expression data under a SINGLE condition. Note that the condition
information is not explicitly tracked here. also NOTE: this data object should be migrated to the Expression
Data service, and simply imported here.

    mapping<feature_id,on_off_state> on_off_call - a mapping of genome features to on/off calls under the given
                                           condition (true=on, false=off).  It is therefore assumed that
                                           the features are protein coding genes.
    source expression_data_source        - the source of this collection of expression data
    source_id expression_data_source_id  - the id of this data object in the workspace
*/
typedef structure {
  boolean_gene_expression_data_id id;
  mapping<feature_id, on_off_state> on_off_call;
  source expression_data_source;
  source expression_data_source_id;
} BooleanGeneExpressionData;