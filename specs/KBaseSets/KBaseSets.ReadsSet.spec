/*
The workspace ID for a Reads data object.
@id ws KBaseFile.PairedEndLibrary KBaseFile.SingleEndLibrary
*/
typedef string ws_reads_id;

/*
The workspace ID for a any data object.
@id ws
*/
typedef string ws_obj_id;

typedef structure {
  string name;
  ws_obj_id ref;
} DataAttachment;

/*
@optional label data_attachments
*/
typedef structure {
  ws_reads_id ref;
  string label;
  list<DataAttachment> data_attachments;
} ReadsSetItem;

/*
@metadata ws description as description
@metadata ws length(items) as item_count
*/
typedef structure {
  string description;
  list<ReadsSetItem> items;
} ReadsSet;