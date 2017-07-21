/*
The workspace id for a ReadsAlignment data object.
@id ws KBaseRNASeq.RNASeqExpression
*/
typedef string ws_expression_id;

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
  ws_expression_id ref;
  string label;
  list<DataAttachment> data_attachments;
} ExpressionSetItem;

/*
@metadata ws description as description
@metadata ws length(items) as item_count
*/
typedef structure {
  string description;
  list<ExpressionSetItem> items;
} ExpressionSet;