/*
The workspace id for a FeatureSet data object.
@id ws KBaseCollections.FeatureSet
*/
typedef string ws_featureset_id;

typedef structure {
  ws_featureset_id ref;
  string label;
} FeatureSetSetItem;

/*
@metadata ws description as description
@metadata ws length(items) as item_count
*/
typedef structure {
  string description;
  list<FeatureSetSetItem> items;
} FeatureSetSet;