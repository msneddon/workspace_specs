typedef structure {
  string function;
  string gene;
  string locus;
  float log2fc;
  float log2fc_f;
  float log2fc_fa;
  float p_value;
  float p_value_f;
  string significant;
  float value_1;
  float value_2;
} gene_expression_stat;

typedef list<gene_expression_stat> voldata;

typedef structure {
  string condition_1;
  string condition_2;
  voldata voldata;
} condition_pair_unit;

typedef structure {
  list<condition_pair_unit> condition_pairs;
  list<string> unique_conditions;
} DifferentialExpressionStat;