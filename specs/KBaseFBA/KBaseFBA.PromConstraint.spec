/*
ID for a set of PROM constraints
@id external
*/
typedef string prom_constraints_id;

/*
Reference to a model template
@id ws KBaseGenomes.Genome
*/
typedef string genome_ref;

/*
Object required by the prom_constraints object which defines the computed probabilities for a target gene.  The
TF regulating this target can be deduced based on the tfMap object.

    string target_uuid        - id of the target gene in the annotation object namespace
    float tfOffProbability    - PROB(target=ON|TF=OFF)
                                the probability that the transcriptional target is ON, given that the
                                transcription factor is not expressed, as defined in Candrasekarana &
                                Price, PNAS 2010 and used to predict cumulative effects of multiple
                                regulatory interactions with a single target.  Set to null or empty if
                                this probability has not been calculated yet.
    float probTTonGivenTFon   - PROB(target=ON|TF=ON)
                                the probability that the transcriptional target is ON, given that the
                                transcription factor is expressed.    Set to null or empty if
                                this probability has not been calculated yet.
@deprecated
*/
typedef structure {
  string target_ref;
  float tfOnProbability;
  float tfOffProbability;
} RegulatoryTarget;

/*
Object required by the prom_constraints object, this maps a transcription factor by its uuid (in some
annotation namespace) to a group of regulatory target genes.

    string transcriptionFactor_uuid                       - id of the TF in the annotation object namespace
    list<regulatory_target> transcriptionFactorMapTarget - collection of regulatory target genes for the TF
                                                            along with associated joint probabilities for each
                                                            target to be on given that the TF is on or off.

@deprecated
*/
typedef structure {
  string transcriptionFactor_ref;
  list<RegulatoryTarget> transcriptionFactorMapTargets;
} TFMap;

/*
ID for an expression data collection
@id external
*/
typedef string expression_data_collection_id;

/*
An object that encapsulates the information necessary to apply PROM-based constraints to an FBA model. This
includes a regulatory network consisting of a set of regulatory interactions (implied by the set of TFMap
objects) and interaction probabilities as defined in each regulatory_target object.  A link the the annotation
object is required in order to properly link to an FBA model object.  A reference to the expression_data_collection
used to compute the interaction probabilities is provided for future reference.

    prom_constraints_id id                                         - the id of this prom_constraints object in a
                                                                    workspace
    annotation_uuid annotation_uuid                               - the id of the annotation object in the workspace
                                                                    which specfies how TFs and targets are named
    list<TFMap> transcriptionFactorMaps                          - the list of TFMaps which specifies both the
                                                                    regulatory network and interaction probabilities
                                                                    between TF and target genes
    expression_data_collection_id expression_data_collection_id   - the id of the expresion_data_collection object in
                                                                    the workspace which was used to compute the
                                                                    regulatory interaction probabilities

@deprecated
*/
typedef structure {
  prom_constraints_id id;
  genome_ref genome_ref;
  list<TFMap> transcriptionFactorMaps;
  expression_data_collection_id expression_data_collection_id;
} PromConstraint;