/*
KBase genome ID
@id kb
*/
typedef string Genome_id;

/*
Reference to a Genome object in the workspace
@id ws KBaseGenomes.Genome
*/
typedef string Genome_ref;

/*
Domain - a subobject holding information on a single protein domain
string id - numerical ID assigned by KBase
string source_id - assession ID from CDD database;
string type - type of CDD, possible values are cd, pfam, smart, COG, PRK, CHL
string name - name of CDD
string description - description of CDD
*/
typedef structure {
  string id;
  string source_id;
  string type;
  string name;
  string description;
} Domain;

/*
FeatureDomain - a subobject holding information on how a domain appears in a gene
string id - numerical ID assigned by KBase
string source_id - assession ID from CDD database;
string type - type of CDD, possible values are cd, pfam, smart, COG, PRK, CHL
string name - name of CDD
string description - description of CDD

@optional feature_ref domains
*/
typedef structure {
  string id;
  string feature_id;
  string feature_ref;
  string function;
  int feature_length;
  list<tuple<string, int, int, int, int, float, float, float, float, float, float>> domains;
} FeatureDomainData;

/*
GenomeDomainData object: this object holds all data regarding protein domains in a genome in KBase

    @optional genome_ref
@searchable ws_subset id genome_id scientific_name genome_ref num_domains num_features
*/
typedef structure {
  string id;
  Genome_id genome_id;
  string scientific_name;
  Genome_ref genome_ref;
  int num_domains;
  int num_features;
  list<Domain> domains;
  list<FeatureDomainData> featuredomains;
} GenomeDomainData;