/*
@optional is_anonymous name namespace alt_id def comment subset synonym xref property_value domain range builtin holds_over_chain is_anti_symmetric is_cyclic is_reflexive is_symmetric is_transitive is_functional is_inverse_functional is_a intersection_of union_of equivalent_to disjoint_from inverse_of transitive_over equivalent_to_chain disjoint_over relationship is_obsolete created_by creation_date replaced_by consider expand_assertion_to expand_expression_to is_metadata_tag is_class_level
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
  list<string> property_value;
  list<string> domain;
  list<string> range;
  list<string> builtin;
  list<string> holds_over_chain;
  string is_anti_symmetric;
  string is_cyclic;
  string is_reflexive;
  string is_symmetric;
  string is_transitive;
  string is_functional;
  string is_inverse_functional;
  list<string> is_a;
  list<string> intersection_of;
  list<string> union_of;
  list<string> equivalent_to;
  list<string> disjoint_from;
  list<string> inverse_of;
  list<string> transitive_over;
  list<string> equivalent_to_chain;
  list<string> disjoint_over;
  list<string> relationship;
  string is_obsolete;
  string created_by;
  string creation_date;
  list<string> replaced_by;
  list<string> consider;
  list<string> expand_assertion_to;
  list<string> expand_expression_to;
  string is_metadata_tag;
  string is_class_level;
} OntologyTypedef;