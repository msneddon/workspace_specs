typedef tuple<string, int> AncestralTerm;

typedef mapping<string, list<AncestralTerm>> RelatinoshipClosure;

/*
@optional is_anonymous name namespace alt_id def comment subset synonym xref builtin property_value is_a intersection_of union_of equivalent_to disjoint_from relationship created_by creation_date is_obsolete replaced_by consider relationship_closure
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
  list<string> builtin;
  list<string> property_value;
  list<string> is_a;
  list<string> intersection_of;
  list<string> union_of;
  list<string> equivalent_to;
  list<string> disjoint_from;
  list<string> relationship;
  string created_by;
  string creation_date;
  string is_obsolete;
  list<string> replaced_by;
  list<string> consider;
  RelatinoshipClosure relationship_closure;
} OntologyTerm;