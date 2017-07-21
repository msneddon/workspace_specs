/*
The workspace ID for a Genome data object.
@id ws KBaseGenomes.Genome
*/
typedef string ws_genome_id;

/*
@optional label
*/
typedef structure {
  ws_genome_id ref;
  string label;
} GenomeSetItem;

/*
@metadata ws description as description
@metadata ws length(items) as item_count
*/
typedef structure {
  string description;
  list<GenomeSetItem> items;
} GenomeSet;