typedef string expression_data_collection_id;

/*
A collection of gene expression data for a single genome under a range of conditions.  This data is returned
as a list of IDs for boolean gene expression data objects in the workspace.  This is a simple object for creating
a PROM Model. NOTE: this data object should be migrated to the Expression Data service, and simply imported here.
*/
typedef structure {
  expression_data_collection_id id;
  list<#KBaseFBA.BooleanGeneExpressionData-1.0#> expression_data_ids;
} BooleanGeneExpressionDataCollection;