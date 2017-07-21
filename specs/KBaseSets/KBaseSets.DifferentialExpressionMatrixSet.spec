/*
The workspace id for a FeatureSet data object.
@id ws KBaseFeatureValues.DifferentialExpressionMatrix
*/
typedef string ws_diffexpmatrix_id;

typedef structure {
  ws_diffexpmatrix_id ref;
  string label;
} DifferentialExpressionMatrixSetItem;

/*
@metadata ws description as description
@metadata ws length(items) as item_count
*/
typedef structure {
  string description;
  list<DifferentialExpressionMatrixSetItem> items;
} DifferentialExpressionMatrixSet;