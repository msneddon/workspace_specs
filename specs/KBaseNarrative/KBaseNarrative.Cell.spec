/*
A Notebook Cell is specified by a string declaring its type, and an unspecified
metadata field. That metadata object contains state and runtime information that
might not always have the same format, but is required.
*/
typedef structure {
  UnspecifiedObject metadata;
  string cell_type;
} Cell;