/*
Reference to a model template
@id ws KBaseGenomes.Genome KBaseGenomeAnnotations.GenomeAnnotation
*/
typedef string genome_ref;

/*
Object required by the prom_constraints object which defines the computed probabilities for a target gene.  The
TF regulating this target can be deduced based on the TFtoTGmap object.

    string target_gene_ref           - reference to the target gene
    float probTGonGivenTFoff    - PROB(target=ON|TF=OFF)
                                the probability that the target gene is ON, given that the
                                transcription factor is not expressed.  Set to null or empty if
                                this probability has not been calculated yet.
    float probTGonGivenTFon   - PROB(target=ON|TF=ON)
                                the probability that the transcriptional target is ON, given that the
                                transcription factor is expressed.    Set to null or empty if
                                this probability has not been calculated yet.
*/
typedef structure {
  string target_gene_ref;
  float probTGonGivenTFoff;
  float probTGonGivenTFon;
} TargetGeneProbabilities;

/*
Object required by the prom_constraints object, this maps a transcription factor 
 to a group of regulatory target genes.

    string transcriptionFactor_ref                       - reference to the transcription factor
    list<TargetGeneProbabilities> targetGeneProbs        - collection of target genes for the TF
                                                            along with associated joint probabilities for each
                                                            target to be on given that the TF is on or off.
*/
typedef structure {
  string transcriptionFactor_ref;
  list<TargetGeneProbabilities> targetGeneProbs;
} TFtoTGmap;

/*
Reference to expression data
@id ws KBaseExpression.ExpressionSeries
*/
typedef string expression_series_ref;

/*
Reference to regulome
@id ws KBaseRegulation.Regulome
*/
typedef string regulome_ref;

/*
An object that encapsulates the information necessary to apply PROM-based constraints to an FBA model. This
includes a regulatory network consisting of a set of regulatory interactions (implied by the set of TFtoTGmap
objects) and interaction probabilities as defined in each TargetGeneProbabilities object.  A link the the annotation
object is required in order to properly link to an FBA model object.  A reference to the expression_data_collection
used to compute the interaction probabilities is provided for future reference.

    string id                                         - the id of this prom_constraints object in a
                                                                    workspace
    genome_ref                                                                        
                                                                    which specfies how TFs and targets are named
    list<TFtoTGmap> transcriptionFactorMaps                                     - the list of TFMaps which specifies both the
                                                                    regulatory network and interaction probabilities
                                                                    between TF and target genes
    expression_series_ref expression_series_ref   - the id of the expresion_data_collection object in
                                                                    the workspace which was used to compute the
                                                                    regulatory interaction probabilities
*/
typedef structure {
  string id;
  genome_ref genome_ref;
  list<TFtoTGmap> transcriptionFactorMaps;
  expression_series_ref expression_series_ref;
  regulome_ref regulome_ref;
} PromConstraint;