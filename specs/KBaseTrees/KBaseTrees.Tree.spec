/*
A string representation of a phylogenetic tree.  The format/syntax of the string is
specified by using one of the available typedefs declaring a particular format, such as 'newick_tree',
'phylo_xml_tree' or 'json_tree'.  When a format is not explictily specified, it is possible to return
trees in different formats depending on addtional parameters. Regardless of format, all leaf nodes
in trees built from MSAs are indexed to a specific MSA row.  You can use the appropriate functionality
of the API to replace these IDs with other KBase Ids instead. Internal nodes may or may not be named.
Nodes, depending on the format, may also be annotated with structured data such as bootstrap values and
distances.
*/
typedef string tree;

/*
Trees are represented in KBase by default in newick format (http://en.wikipedia.org/wiki/Newick_format)
and are returned to you in this format by default.
*/
typedef tree newick_tree;

typedef string node_id;

typedef string label;

/*
An enumeration of reference types for a node.  Either the one letter abreviation or full
name can be given.  For large trees, it is strongly advised you use the one letter abreviations.
Supported types are:
    g | genome  => genome typed object or CDS data
    p | protein => protein sequence object or CDS data, often given as the MD5 of the sequence
    n | dna     => dna sequence object or CDS data, often given as the MD5 of the sequence
    f | feature => feature object or CDS data
*/
typedef string ref_type;

/*
@id ws
*/
typedef string ws_obj_id;

/*
A KBase ID is a string starting with the characters "kb|".  KBase IDs are typed. The types are
designated using a short string. For instance," g" denotes a genome, "tree" denotes a Tree, and
"aln" denotes a sequence alignment. KBase IDs may be hierarchical.  For example, if a KBase genome
identifier is "kb|g.1234", a protein encoding gene within that genome may be represented as
"kb|g.1234.peg.771".
@id kb
*/
typedef string kbase_id;

/*
Data type for phylogenetic trees.

    @optional name description type tree_attributes
    @optional default_node_labels ws_refs kb_refs leaf_list
*/
typedef structure {
  string name;
  string description;
  string type;
  newick_tree tree;
  mapping<string, string> tree_attributes;
  mapping<node_id, label> default_node_labels;
  mapping<node_id, mapping<ref_type, list<ws_obj_id>>> ws_refs;
  mapping<node_id, mapping<ref_type, list<kbase_id>>> kb_refs;
  list<node_id> leaf_list;
} Tree;