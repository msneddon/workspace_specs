/*
List of cummerbundplot
*/
typedef list<#KBaseRNASeq.cummerbundplot-2.0#> cummerbundplotSet;

/*
Object type for the cummerbund_output
*/
typedef structure {
  cummerbundplotSet cummerbundplotSet;
  string rnaseq_experiment_id;
  string cuffdiff_input_id;
} cummerbund_output;