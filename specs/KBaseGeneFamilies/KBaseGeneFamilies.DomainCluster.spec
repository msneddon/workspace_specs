typedef string domain_accession;

/*
@id ws KBaseGeneFamilies.DomainCluster
*/
typedef string domain_cluster_ref;

/*
@id ws KBaseGenomes.Genome
*/
typedef string genome_ref;

typedef tuple<int, int, float, float, float> domain_place;

typedef tuple<string, string, int, list<domain_place>> domain_cluster_element;

/*
@id ws KBaseTrees.MSA
*/
typedef string ws_alignment_id;

/*
domain_accession model - reference to domain model
domain_cluster_ref parent_ref - optional reference to parent cluster (containing data 
        describing some common set of genomes)
mapping<genome_ref,list<domain_cluster_element>> data - list of entrances of this domain 
        into different genomes (domain_cluster_element -> ;
        domain_place -> tuple<int start_in_feature,int stop_in_feature,float evalue,
                float bitscore,float domain_coverage>).
ws_alignment_id msa_ref - reference to multiple alignment object where all domain 
        sequences are collected (keys in this MSA object are constructed according to this 
        pattern: <genome_ref>_<feature_id>_<start_in_feature>), field is not set in case
        clusters are stored inside DomainClusterSearchResult object, use 'msas' field of
        DomainClusterSearchResult object instead.
@optional parent_ref
@optional msa_ref
*/
typedef structure {
  domain_accession model;
  domain_cluster_ref parent_ref;
  mapping<genome_ref, list<domain_cluster_element>> data;
  ws_alignment_id msa_ref;
} DomainCluster;