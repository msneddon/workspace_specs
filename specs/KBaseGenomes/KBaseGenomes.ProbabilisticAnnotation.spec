/*
ProbabilisticAnnotation ID
@id kb
*/
typedef string ProbabilisticAnnotation_id;

/*
Reference to a Genome object in the workspace
@id ws KBaseGenomes.Genome
*/
typedef string Genome_ref;

/*
KBase Feature ID
@id external
*/
typedef string Feature_id;

/*
A function_probability is a (annotation, probability) pair associated with a gene
An annotation is a "///"-delimited list of roles that could be associated with that gene.
*/
typedef tuple<string, float> function_probability;

/*
Object to carry alternative functions and probabilities for genes in a genome    

        probanno_id id - ID of the probabilistic annotation object    
        Genome_ref genome_ref - reference to genome probabilistic annotation was built for
        mapping<Feature_id, list<function_probability>> roleset_probabilities - mapping of features to list of alternative function_probability objects
        list<Feature_id> skipped_features - list of features in genome with no probability
        
            @searchable ws_subset id genome_ref skipped_features
*/
typedef structure {
  ProbabilisticAnnotation_id id;
  Genome_ref genome_ref;
  mapping<Feature_id, list<function_probability>> roleset_probabilities;
  list<Feature_id> skipped_features;
} ProbabilisticAnnotation;