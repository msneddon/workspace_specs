/*
@id ws KBaseGeneFamilies.DomainClusterSearchResult
*/
typedef string dcsr_ref;

/*
@id ws KBaseGeneFamilies.DomainModelSet
*/
typedef string dms_ref;

/*
@id ws KBaseGenomes.Genome
*/
typedef string genome_ref;

/*
@id ws KBaseGeneFamilies.DomainAnnotation
*/
typedef string domain_annotation_ref;

/*
Aggreagated data for every genome.
*/
typedef structure {
  genome_ref genome_ref;
  string kbase_id;
  string scientific_name;
  int features;
  int features_with_domains;
  int domain_models;
  int domains;
} GenomeStat;

typedef string domain_accession;

/*
@id ws KBaseGeneFamilies.DomainCluster
*/
typedef string domain_cluster_ref;

/*
@id ws KBaseTrees.MSA
*/
typedef string ws_alignment_id;

/*
Aggregated data for every domain cluster.
*/
typedef structure {
  domain_accession domain_accession;
  string name;
  int genomes;
  int features;
  int domains;
} DomainClusterStat;

/*
@id ws KBaseTrees.Tree
*/
typedef string ws_tree_id;

/*
dcsr_ref parent_ref - optional reference to parent domain clusters search results
dms_ref used_dms_ref - domain models used for search
mapping<genome_ref, DomainAnnotation> annotations - found domains in genomes that user 
        defined as input data for domain search
mapping<genome_ref, DomainAlignment> alignments - alignments for found domains in genomes 
        that user defined as input data for domain search
mapping<genome_ref, domain_annotation_ref> annotation_refs - domain annotation references 
        in case we don't want to store annotations and alignments inside result object
mapping<domain_accession, DomainCluster> domain_clusters - clusters constructed based on 
        query_genomes plus genomes from parent object
mapping<domain_accession, domain_cluster_ref> domain_cluster_refs - references to clusters 
        in case we don't want to store these clusters inside search result object
mapping<domain_accession, KBaseTrees.MSA> msas - multiple alignment objects where all domain sequences 
        are collected (keys in these MSA objects are constructed according to such pattern: 
        <genome_ref>_<feature_id>_<start_in_feature>), in case this field is not set or has
        empty mapping msa_refs field should be used
mapping<domain_accession, ws_alignment_id> msa_refs - references to multiple alignment objects 
        where all domain sequences are collected (keys in these MSA objects are constructed 
        according to such pattern: <genome_ref>_<feature_id>_<start_in_feature>)
mapping<domain_accession, KBaseTrees.Tree> trees - trees built for MSAs stored in msas field
mapping<domain_accession, ws_tree_id> tree_refs - trees built for MSAs stored in msa_refs field
@optional parent_ref
@optional used_dms_ref
@optional annotations
@optional alignments
@optional annotation_refs
@optional domain_clusters
@optional domain_cluster_refs
@optional msas
@optional msa_refs
@optional trees
@optional tree_refs
*/
typedef structure {
  dcsr_ref parent_ref;
  dms_ref used_dms_ref;
  mapping<genome_ref, #KBaseGeneFamilies.DomainAnnotation-1.0#> annotations;
  mapping<genome_ref, #KBaseGeneFamilies.DomainAlignments-1.0#> alignments;
  mapping<genome_ref, domain_annotation_ref> annotation_refs;
  mapping<genome_ref, GenomeStat> genome_statistics;
  mapping<domain_accession, #KBaseGeneFamilies.DomainCluster-1.0#> domain_clusters;
  mapping<domain_accession, domain_cluster_ref> domain_cluster_refs;
  mapping<domain_accession, #KBaseTrees.MSA-1.0#> msas;
  mapping<domain_accession, ws_alignment_id> msa_refs;
  mapping<domain_accession, DomainClusterStat> domain_cluster_statistics;
  mapping<domain_accession, #KBaseTrees.Tree-1.0#> trees;
  mapping<domain_accession, ws_tree_id> tree_refs;
} DomainClusterSearchResult;