/*
@optional is_anonymous name namespace alt_id def comment subset synonym xref instance_of property_value relationship created_by creation_date is_obsolete replaced_by consider
*/
typedef structure {
  string id;
  string is_anonymous;
  string name;
  string namespace;
  list<string> alt_id;
  list<string> def;
  list<string> comment;
  list<string> subset;
  list<string> synonym;
  list<string> xref;
  list<string> instance_of;
  list<string> property_value;
  list<string> relationship;
  string created_by;
  string creation_date;
  string is_obsolete;
  list<string> replaced_by;
  list<string> consider;
} OntologyInstance;