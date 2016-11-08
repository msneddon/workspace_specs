/*
Reference to a taxon object 
    @id ws KBaseGenomeAnnotations.Taxon
*/
typedef string taxon_ref;

/*
The Taxon object holds the data associated with a taxon.  This taxon could be a leaf or branch in the taxonomic tree.

We lost reference_genome_annotation_id 

@optional aliases genetic_code scientific_lineage parent_taxon_ref kingdom rank embl_code inherited_div_flag inherited_GC_flag mitochondrial_genetic_code inherited_MGC_flag GenBank_hidden_flag hidden_subtree_flag division_id comments
*/
typedef structure {
  int taxonomy_id;
  string scientific_name;
  string scientific_lineage;
  string rank;
  string kingdom;
  string domain;
  list<string> aliases;
  int genetic_code;
  taxon_ref parent_taxon_ref;
  string embl_code;
  int inherited_div_flag;
  int inherited_GC_flag;
  int mitochondrial_genetic_code;
  int inherited_MGC_flag;
  int GenBank_hidden_flag;
  int hidden_subtree_flag;
  int division_id;
  string comments;
} Taxon;