typedef string expression_data_collection_id;

typedef string boolean_gene_expression_data_id;

/*
A collection of gene expression data for a single genome under a range of conditions.  This data is returned
as a list of IDs for boolean gene expression data objects in the workspace.  This is a simple object for creating
a PROM Model. NOTE: this data object should be migrated to the Expression Data service, and simply imported here.
*/
typedef structure {
  expression_data_collection_id id;
  list<boolean_gene_expression_data_id> expression_data_ids;
} BooleanGeneExpressionDataCollection;