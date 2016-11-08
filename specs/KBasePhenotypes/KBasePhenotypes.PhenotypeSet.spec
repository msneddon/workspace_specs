/*
PhenotypeSet ID
@id kb
*/
typedef string phenotypeset_id;

/*
Source ID
@id external
*/
typedef string source_id;

/*
Reference to a feature of a genome object
@id subws KBaseGenomes.Genome
*/
typedef string genome_ref;

/*
Phenotype ID
@id external
*/
typedef string phenotype_id;

/*
Reference to a mapping object
@id ws KBaseBiochem.Media
*/
typedef string media_ref;

/*
Reference to a feature of a genome object
@id subws KBaseGenomes.Genome.features.[*].id
*/
typedef string feature_ref;

/*
Reference to a compound object
@id subws KBaseBiochem.Biochemistry.compounds.[*].id
*/
typedef string compound_ref;

/*
Phenotype subobject holds data on a single phenotype
            
@optional name
@searchable ws_subset id media_ref geneko_refs additionalcompound_refs normalizedGrowth name
*/
typedef structure {
  phenotype_id id;
  media_ref media_ref;
  list<feature_ref> geneko_refs;
  list<compound_ref> additionalcompound_refs;
  float normalizedGrowth;
  string name;
} Phenotype;

/*
PhenotypeSet object contains a set of phenotype objects
            
@optional name
@searchable ws_subset id source_id source name genome_ref
@searchable ws_subset phenotypes.[*].(media_ref,geneko_refs,normalizedGrowth)
*/
typedef structure {
  phenotypeset_id id;
  source_id source_id;
  string source;
  string name;
  genome_ref genome_ref;
  list<Phenotype> phenotypes;
  string importErrors;
  string type;
} PhenotypeSet;