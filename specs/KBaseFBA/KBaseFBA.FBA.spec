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
Reference to regulatory model
@id ws KBaseRegulation.RegModel
*/
typedef string regmodel_ref;

/*
Reference to metabolic model
@id ws KBaseFBA.FBAModel
*/
typedef string fbamodel_ref;

/*
Reference to PROM model
@id ws KBaseRegulation.PROMModel
*/
typedef string prommodel_ref;

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

@searchable ws_subset name rhs sign compound_terms reaction_terms
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

@searchable ws_subset modelreaction_ref variableType upperBound lowerBound
*/
typedef structure {
  modelreaction_ref modelreaction_ref;
  string variableType;
  float upperBound;
  float lowerBound;
} FBAReactionBound;

/*
FBACompoundBound object

@searchable ws_subset modelcompound_ref variableType upperBound lowerBound
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

@searchable ws_subset modelcompound_ref variableType upperBound lowerBound class min max value
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

@searchable ws_subset modelreaction_ref variableType upperBound lowerBound class min max value
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

@searchable ws_subset biomass_ref variableType upperBound lowerBound class min max value
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

@searchable ws_subset objectFraction alpha beta
*/
typedef structure {
  float objectFraction;
  float alpha;
  float beta;
} FBAPromResult;

/*
FBADeletionResult object

@searchable ws_subset feature_refs growthFraction
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

@searchable ws_subset essentialNutrient_refs optionalNutrient_refs
*/
typedef structure {
  list<compound_ref> essentialNutrient_refs;
  list<compound_ref> optionalNutrient_refs;
} FBAMinimalMediaResult;

/*
FBAMetaboliteProductionResult object

@searchable ws_subset modelcompound_ref maximumProduction
*/
typedef structure {
  modelcompound_ref modelcompound_ref;
  float maximumProduction;
} FBAMetaboliteProductionResult;

/*
FBAMinimalReactionsResult object

@searchable ws_subset reaction_refs id
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

@optional minimize_reactions minimize_reaction_costs FBAMinimalReactionsResults PROMKappa phenotypesimulationset_ref objectiveValue phenotypeset_ref prommodel_ref regmodel_ref
@searchable ws_subset comboDeletions id fva fluxMinimization findMinimalMedia allReversible simpleThermoConstraints thermodynamicConstraints noErrorThermodynamicConstraints minimizeErrorThermodynamicConstraints
@searchable ws_subset regmodel_ref fbamodel_ref prommodel_ref media_ref phenotypeset_ref geneKO_refs reactionKO_refs additionalCpd_refs objectiveValue phenotypesimulationset_ref
@searchable ws_subset FBAConstraints.[*].(name,rhs,sign,compound_terms,reaction_terms) 
@searchable ws_subset FBAReactionBounds.[*].(modelreaction_ref,variableType,upperBound,lowerBound)
@searchable ws_subset FBACompoundBounds.[*].(modelcompound_ref,variableType,upperBound,lowerBound)
@searchable ws_subset FBACompoundVariables.[*].(modelcompound_ref,variableType,upperBound,lowerBound,class,min,max,value)
    @searchable ws_subset FBAReactionVariables.[*].(modelreaction_ref,variableType,upperBound,lowerBound,class,min,max,value)
    @searchable ws_subset FBABiomassVariables.[*].(biomass_ref,variableType,upperBound,lowerBound,class,min,max,value)
    @searchable ws_subset FBAPromResults.[*].(objectFraction,alpha,beta)
    @searchable ws_subset FBADeletionResults.[*].(feature_refs,growthFraction)
    @searchable ws_subset FBAMinimalMediaResults.[*].(essentialNutrient_refs,optionalNutrient_refs)
    @searchable ws_subset FBAMetaboliteProductionResults.[*].(modelcompound_ref,maximumProduction)
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
  bool decomposeReversibleFlux;
  bool decomposeReversibleDrainFlux;
  bool fluxUseVariables;
  bool drainfluxUseVariables;
  bool minimize_reactions;
  regmodel_ref regmodel_ref;
  fbamodel_ref fbamodel_ref;
  prommodel_ref prommodel_ref;
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
  list<FBADeletionResult> FBADeletionResults;
  list<FBAMinimalMediaResult> FBAMinimalMediaResults;
  list<FBAMetaboliteProductionResult> FBAMetaboliteProductionResults;
  list<FBAMinimalReactionsResult> FBAMinimalReactionsResults;
} FBA;