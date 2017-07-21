/*
Protein

Included function, but technically a protein may have different functions in different organisms or environments 
Note the following:
mapping<string domain, <list<list<tuple<int coordinate_start, int coordinate_stop>>>>>; 
The outer list is for multiple of the same domain in the same protein.
The inner list is to accommodate domains that are non-continuous sequence.

What about the following?
INTERACTIONS? ACTIVE SITE? ALLOSTERIC SITE? Folding pattern?

@optional function domain_locations aliases
*/
typedef structure {
  string protein_id;
  mapping<string, list<list<tuple<int, int>>>> domain_locations;
  string amino_acid_sequence;
  string function;
  mapping<string, list<string>> aliases;
  string md5;
  int translation_derived;
} protein;

/*
The protein container has multiple proteins in it 

@optional name description notes
*/
typedef structure {
  string protein_container_id;
  string name;
  string description;
  string notes;
  mapping<string, protein> proteins;
} ProteinContainer;