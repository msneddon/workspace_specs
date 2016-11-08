/*
@id ws KBaseGenomes.Genome
*/
typedef string genome_ref;

/*
@id ws KBaseGeneFamilies.DomainModelSet
*/
typedef string dms_ref;

typedef string contig_id;

typedef string domain_accession;

/*
@id ws KBaseGeneFamilies.DomainCluster
        typedef string domain_cluster_ref;
*/
typedef tuple<int, int, float, float, float> domain_place;

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
        typedef structure {
domain_accession model;
domain_cluster_ref parent_ref;
mapping<genome_ref,list<domain_cluster_element>> data;
ws_alignment_id msa_ref;
        } DomainCluster;
*/
typedef tuple<string, int, int, int, mapping<domain_accession, list<domain_place>>> annotation_element;

/*
genome_ref genome_ref - reference to genome
dms_ref used_dms_ref - domain models used for search
mapping<contig_id, list<annotation_element>> data - 
        list of entrances of different domains into proteins of annotated genome
        (annotation_element -> typedef tuple<string feature_id,int feature_start,int feature_stop,
                int feature_dir,mapping<domain_accession,list<domain_place>>>;
        domain_place -> tuple<int start_in_feature,int stop_in_feature,float evalue,
                float bitscore,float domain_coverage>).
mapping<contig_id, tuple<int size,int features>> contig_to_size_and_feature_count - 
        feature count and nucleotide size of every contig
mapping<string feature_id, tuple<contig_id,int feature_index> feature_to_contig_and_index - 
        index of every feature in feature list in every contig
*/
typedef structure {
  genome_ref genome_ref;
  dms_ref used_dms_ref;
  mapping<contig_id, list<annotation_element>> data;
  mapping<contig_id, tuple<int, int>> contig_to_size_and_feature_count;
  mapping<string, tuple<contig_id, int>> feature_to_contig_and_index;
} DomainAnnotation;