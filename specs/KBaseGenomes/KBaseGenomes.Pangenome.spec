/*
Reference to a Genome object in the workspace
@id ws KBaseGenomes.Genome
*/
typedef string Genome_ref;

/*
OrthologFamily object: this object holds all data for a single ortholog family in a metagenome

@searchable ws_subset id type function md5 protein_translation
*/
typedef structure {
  string id;
  string type;
  string function;
  string md5;
  string protein_translation;
  list<tuple<string, float>> orthologs;
} OrthologFamily;

/*
Pangenome object: this object holds all data regarding a pangenome

@searchable ws_subset id name
*/
typedef structure {
  string id;
  string name;
  string type;
  list<Genome_ref> genome_refs;
  list<OrthologFamily> orthologs;
} Pangenome;