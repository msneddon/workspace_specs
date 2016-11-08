typedef string row_id;

typedef string sequence;

typedef int start_pos_in_parent;

typedef int end_pos_in_parent;

typedef int parent_len;

typedef string parent_md5;

typedef tuple<start_pos_in_parent, end_pos_in_parent, parent_len, parent_md5> trim_info;

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
###  KBaseTrees.ConcatMSA KBaseTrees.MS
        @id ws KBaseTrees.MSA
*/
typedef string ws_alignment_id;

/*
Type for multiple sequence alignment.
sequence_type - 'protein' in case sequences are amino acids, 'dna' in case of 
        nucleotides.
int alignment_length - number of columns in alignment.
mapping<row_id, sequence> alignment - mapping from sequence id to aligned sequence.
list<row_id> row_order - list of sequence ids defining alignment order (optional). 
ws_alignment_id parent_msa_ref - reference to parental alignment object to which 
        this object adds some new aligned sequences (it could be useful in case of
        profile alignments where you don't need to insert new gaps in original msa).
@optional name description sequence_type
@optional trim_info alignment_attributes row_order 
@optional default_row_labels ws_refs kb_refs
@optional parent_msa_ref
*/
typedef structure {
  string name;
  string description;
  string sequence_type;
  int alignment_length;
  mapping<row_id, sequence> alignment;
  mapping<row_id, trim_info> trim_info;
  mapping<string, string> alignment_attributes;
  list<row_id> row_order;
  mapping<node_id, label> default_row_labels;
  mapping<node_id, mapping<ref_type, list<ws_obj_id>>> ws_refs;
  mapping<node_id, mapping<ref_type, list<kbase_id>>> kb_refs;
  ws_alignment_id parent_msa_ref;
} MSA;