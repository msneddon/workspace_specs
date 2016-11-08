/*
A string identifier for a reaction probabilities object.
*/
typedef string rxnprobs_id;

/*
A string identifier for a template model object.
*/
typedef string template_id;

/*
A string identifier for a workspace. Any string consisting of alphanumeric characters and "-" is acceptable.
*/
typedef string workspace_id;

/*
A string identifier for a genome.
*/
typedef string genome_id;

/*
A string identifier for a probabilistic annotation object.
*/
typedef string probanno_id;

/*
A string identifier for a reaction object.
*/
typedef string reaction_id;

/*
Data structure to hold probability of a reaction

        reaction_id reaction - ID of the reaction
        float probability - Probability of the reaction
        string type - Type of complexes ("HASCOMPLEXES" or "NOCOMPLEXES")
        string complex_info - Detailed information on complexes
        string gene_list - List of genes most likely to be attached to reaction
*/
typedef tuple<reaction_id, float, string, string, string> reaction_probability;

/*
Object to hold reaction probabilities for a genome.

        genome_id genome - ID of the genome the reaction probabilities was built for
        list<reaction_probability> reaction_probabilities - list of reaction probabilities
*/
typedef structure {
  rxnprobs_id id;
  template_id template_model;
  workspace_id template_workspace;
  genome_id genome;
  workspace_id genome_workspace;
  probanno_id probanno;
  workspace_id probanno_workspace;
  list<reaction_probability> reaction_probabilities;
} RxnProbs;