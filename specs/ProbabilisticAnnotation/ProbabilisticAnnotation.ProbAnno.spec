/*
A string identifier for a probabilistic annotation object.
*/
typedef string probanno_id;

/*
A string identifier for a genome.
*/
typedef string genome_id;

/*
A string identifier for a workspace. Any string consisting of alphanumeric characters and "-" is acceptable.
*/
typedef string workspace_id;

/*
A string identifier for a feature.
*/
typedef string feature_id;

/*
A function_probability is a (annotation, probability) pair associated with a gene
An annotation is a "///"-delimited list of roles that could be associated with that gene.
*/
typedef tuple<string, float> function_probability;

/*
Object to carry alternative functions and probabilities for genes in a genome    

        probanno_id id - ID of the probabilistic annotation object    
        genome_id genome - ID of the genome the probabilistic annotation was built for
        workspace_id genome_workspace - ID of the workspace containing genome
        mapping<feature_id, list<function_probability>> roleset_probabilities - mapping of features to list of alternative function_probability objects
        list<feature_id> skipped_features - list of features in genome with no probability
*/
typedef structure {
  probanno_id id;
  genome_id genome;
  workspace_id genome_workspace;
  mapping<feature_id, list<function_probability>> roleset_probabilities;
  list<feature_id> skipped_features;
} ProbAnno;