/*
note: this needs review from Marcin
*/
typedef structure {
  int best_k;
  list<tuple<int, float>> estimate_cluster_sizes;
} EstimateKResult;