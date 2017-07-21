/*
object DifferentialExpressionStat structure
This holds the output of differential expression statistics
gene_function - gene description
gene - gene id
locus - chromosomal location
log2fc_text - text version of log2 fold change to hold inf and -inf
log2fc_f - floating point version of log2 fold change (for inf and -inf this has the max fold change in the given comparison
p_value and p_value_f are
significant - to capture significance from cummerbund output. Value has to be âyesâ or ânoâ
value_1 - log2fpkm value of condition 1
value_2 - log2fpkm value of condition 2
*/
typedef structure {
  string gene_function;
  string gene;
  string locus;
  string log2fc_text;
  float log2fc_f;
  float p_value;
  float p_value_f;
  string significant;
  float value_1;
  float value_2;
} gene_expression_stat;

typedef list<gene_expression_stat> voldata;

/*
condition_pair_unit holds value for each pair
*/
typedef structure {
  string condition_1;
  string condition_2;
  voldata voldata;
} condition_pair_unit;

typedef structure {
  list<condition_pair_unit> condition_pairs;
  list<string> unique_conditions;
} DifferentialExpressionStat;