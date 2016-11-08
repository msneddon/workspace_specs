/*
KBase FBA ID
@id kb
*/
typedef string fba_id;

typedef int bool;

/*
Model compound ID
@id external
*/
typedef string modelcompound_id;

/*
Model reaction ID
@id external
*/
typedef string modelreaction_id;

/*
Biomass reaction ID
@id external
*/
typedef string biomass_id;

/*
Reference to regulome
@id ws KBaseRegulation.Regulome
*/
typedef string regulome_ref;

/*
Reference to metabolic model
@id ws KBaseFBA.FBAModel
*/
typedef string fbamodel_ref;

/*
Reference to PROM constraints
@id ws KBaseFBA.PromConstraint
*/
typedef string promconstraint_ref;

/*
Reference to expression data
@id ws KBaseExpression.ExpressionSample
*/
typedef string expression_sample_ref;

/*
Reference to a model template
@id ws KBaseBiochem.Media
*/
typedef string media_ref;

/*
Reference to a phenotype set object
@id ws KBasePhenotypes.PhenotypeSet
*/
typedef string phenotypeset_ref;

/*
Reference to a feature of a genome object
@id subws KBaseGenomes.Genome.features.[*].id
*/
typedef string feature_ref;

/*
Reference to a reaction object in a model
@id subws KBaseFBA.FBAModel.modelreactions.[*].id
*/
typedef string modelreaction_ref;

/*
Reference to a compound object in a model
@id subws KBaseFBA.FBAModel.modelcompounds.[*].id
*/
typedef string modelcompound_ref;

/*
FBAConstraint object
*/
typedef structure {
  string name;
  float rhs;
  string sign;
  mapping<modelcompound_id, float> compound_terms;
  mapping<modelreaction_id, float> reaction_terms;
  mapping<biomass_id, float> biomass_terms;
} FBAConstraint;

/*
FBAReactionBound object
*/
typedef structure {
  modelreaction_ref modelreaction_ref;
  string variableType;
  float upperBound;
  float lowerBound;
} FBAReactionBound;

/*
FBACompoundBound object
*/
typedef structure {
  modelcompound_ref modelcompound_ref;
  string variableType;
  float upperBound;
  float lowerBound;
} FBACompoundBound;

/*
Reference to a phenotype simulation set object
@id ws KBasePhenotypes.PhenotypeSimulationSet
*/
typedef string phenotypesimulationset_ref;

/*
FBACompoundVariable object
*/
typedef structure {
  modelcompound_ref modelcompound_ref;
  string variableType;
  float upperBound;
  float lowerBound;
  string class;
  float min;
  float max;
  float value;
} FBACompoundVariable;

/*
FBAReactionVariable object
*/
typedef structure {
  modelreaction_ref modelreaction_ref;
  string variableType;
  float upperBound;
  float lowerBound;
  string class;
  float min;
  float max;
  float value;
} FBAReactionVariable;

/*
Reference to a biomass object in a model
@id subws KBaseFBA.FBAModel.biomasses.[*].id
*/
typedef string biomass_ref;

/*
FBABiomassVariable object
*/
typedef structure {
  biomass_ref biomass_ref;
  string variableType;
  float upperBound;
  float lowerBound;
  string class;
  float min;
  float max;
  float value;
} FBABiomassVariable;

/*
FBAPromResult object
*/
typedef structure {
  float objectFraction;
  float alpha;
  float beta;
} FBAPromResult;

/*
Either of two values: 
 - InactiveOn: specified as on, but turns out as inactive
 - ActiveOff: specified as off, but turns out as active
*/
typedef string conflict_state;

/*
Genome feature ID
@id external
*/
typedef string feature_id;

/*
FBATintleResult object
*/
typedef structure {
  float originalGrowth;
  float growth;
  float originalObjective;
  float objective;
  mapping<conflict_state, feature_id> conflicts;
} FBATintleResult;

/*
FBADeletionResult object
*/
typedef structure {
  list<feature_ref> feature_refs;
  float growthFraction;
} FBADeletionResult;

/*
Reference to a compound object
@id subws KBaseBiochem.Biochemistry.compounds.[*].id
*/
typedef string compound_ref;

/*
FBAMinimalMediaResult object
*/
typedef structure {
  list<compound_ref> essentialNutrient_refs;
  list<compound_ref> optionalNutrient_refs;
} FBAMinimalMediaResult;

/*
FBAMetaboliteProductionResult object
*/
typedef structure {
  modelcompound_ref modelcompound_ref;
  float maximumProduction;
} FBAMetaboliteProductionResult;

/*
FBAMinimalReactionsResult object
*/
typedef structure {
  string id;
  bool suboptimal;
  float totalcost;
  list<modelreaction_ref> reaction_refs;
  list<string> reaction_directions;
} FBAMinimalReactionsResult;

/*
FBA object holds the formulation and results of a flux balance analysis study

@optional minimize_reactions minimize_reaction_costs FBATintleResults FBAMinimalReactionsResults PROMKappa phenotypesimulationset_ref objectiveValue phenotypeset_ref promconstraint_ref regulome_ref tintlesample_ref tintleW tintleKappa
@searchable ws_subset comboDeletions id fva fluxMinimization findMinimalMedia allReversible simpleThermoConstraints thermodynamicConstraints noErrorThermodynamicConstraints minimizeErrorThermodynamicConstraints
@searchable ws_subset regulome_ref fbamodel_ref promconstraint_ref media_ref phenotypeset_ref geneKO_refs reactionKO_refs additionalCpd_refs objectiveValue phenotypesimulationset_ref
*/
typedef structure {
  fba_id id;
  bool fva;
  bool fluxMinimization;
  bool findMinimalMedia;
  bool allReversible;
  bool simpleThermoConstraints;
  bool thermodynamicConstraints;
  bool noErrorThermodynamicConstraints;
  bool minimizeErrorThermodynamicConstraints;
  bool maximizeObjective;
  mapping<modelcompound_id, float> compoundflux_objterms;
  mapping<modelreaction_id, float> reactionflux_objterms;
  mapping<biomass_id, float> biomassflux_objterms;
  int comboDeletions;
  int numberOfSolutions;
  float objectiveConstraintFraction;
  float defaultMaxFlux;
  float defaultMaxDrainFlux;
  float defaultMinDrainFlux;
  float PROMKappa;
  float tintleW;
  float tintleKappa;
  bool decomposeReversibleFlux;
  bool decomposeReversibleDrainFlux;
  bool fluxUseVariables;
  bool drainfluxUseVariables;
  bool minimize_reactions;
  regulome_ref regulome_ref;
  fbamodel_ref fbamodel_ref;
  promconstraint_ref promconstraint_ref;
  expression_sample_ref tintlesample_ref;
  media_ref media_ref;
  phenotypeset_ref phenotypeset_ref;
  list<feature_ref> geneKO_refs;
  list<modelreaction_ref> reactionKO_refs;
  list<modelcompound_ref> additionalCpd_refs;
  mapping<string, float> uptakeLimits;
  mapping<modelreaction_id, float> minimize_reaction_costs;
  mapping<string, string> parameters;
  mapping<string, list<string>> inputfiles;
  list<FBAConstraint> FBAConstraints;
  list<FBAReactionBound> FBAReactionBounds;
  list<FBACompoundBound> FBACompoundBounds;
  float objectiveValue;
  mapping<string, list<string>> outputfiles;
  phenotypesimulationset_ref phenotypesimulationset_ref;
  list<FBACompoundVariable> FBACompoundVariables;
  list<FBAReactionVariable> FBAReactionVariables;
  list<FBABiomassVariable> FBABiomassVariables;
  list<FBAPromResult> FBAPromResults;
  list<FBATintleResult> FBATintleResults;
  list<FBADeletionResult> FBADeletionResults;
  list<FBAMinimalMediaResult> FBAMinimalMediaResults;
  list<FBAMetaboliteProductionResult> FBAMetaboliteProductionResults;
  list<FBAMinimalReactionsResult> FBAMinimalReactionsResults;
} FBA;