/*
Reference to a Genome object in the workspace
@id ws KBaseGenomes.Genome
*/
typedef string Genome_ref;

/*
OrthologFamily object: this object holds all data for a single ortholog family in a metagenome

@optional type function md5 protein_translation
*/
typedef structure {
  string id;
  string type;
  string function;
  string md5;
  string protein_translation;
  list<tuple<string, float, string>> orthologs;
} OrthologFamily;

/*
Pangenome object: this object holds all data regarding a pangenome

@searchable ws_subset id name
    @metadata ws type as Type
    @metadata ws name as Name
    @metadata ws length(orthologs) as Number orthologs
    @metadata ws length(genome_refs) as Number genomes
*/
typedef structure {
  string id;
  string name;
  string type;
  list<Genome_ref> genome_refs;
  list<OrthologFamily> orthologs;
} Pangenome;