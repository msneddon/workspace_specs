/*
The workspace ID for an Assembly data object.
@id ws KBaseGenomeAnnotations.Assembly
*/
typedef string ws_assembly_id;

/*
@optional label
*/
typedef structure {
  ws_assembly_id ref;
  string label;
} AssemblySetItem;

/*
@metadata ws description as description
@metadata ws length(items) as item_count
*/
typedef structure {
  string description;
  list<AssemblySetItem> items;
} AssemblySet;