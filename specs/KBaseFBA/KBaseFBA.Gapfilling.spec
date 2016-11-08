/*
Gapfill ID
@id kb
*/
typedef string gapfill_id;

/*
Reference to a FBA object
@id ws KBaseFBA.FBA
*/
typedef string fba_ref;

/*
Reference to metabolic model
@id ws KBaseFBA.FBAModel
*/
typedef string fbamodel_ref;

/*
Reference to probabilistic annotation
@id ws KBaseProbabilisticAnnotation.ProbAnno
*/
typedef string probanno_ref;

typedef int bool;

/*
Reference to a reaction object in a biochemistry
@id subws KBaseBiochem.Biochemistry.reactions.[*].id
*/
typedef string reaction_ref;

/*
Reference to a compartment object
@id subws KBaseBiochem.Biochemistry.compartments.[*].id
*/
typedef string compartment_ref;

/*
Gapfill solution ID
@id external
*/
typedef string gapfillsol_id;

/*
Reference to a compound object in a model
@id subws KBaseFBA.FBAModel.modelcompounds.[*].id
*/
typedef string modelcompound_ref;

/*
Reference to a reaction object in a model
@id subws KBaseFBA.FBAModel.modelreactions.[*].id
*/
typedef string modelreaction_ref;

/*
Reference to a feature of a genome object
@id subws KBaseGenomes.Genome.features.[*].id
*/
typedef string feature_ref;

/*
GapFillingReaction object holds data on a reaction added by gapfilling analysis

@searchable ws_subset reaction_ref compartment_ref direction candidateFeature_refs
*/
typedef structure {
  reaction_ref reaction_ref;
  compartment_ref compartment_ref;
  string direction;
  list<feature_ref> candidateFeature_refs;
} GapfillingReaction;

/*
GapFillingSolution object holds data on a solution generated by gapfilling analysis

@searchable ws_subset id suboptimal integrated solutionCost koRestore_refs biomassRemoval_refs mediaSupplement_refs
@searchable ws_subset gapfillingSolutionReactions.[*].(reaction_ref,compartment_ref,direction,candidateFeature_refs)
*/
typedef structure {
  gapfillsol_id id;
  float solutionCost;
  list<modelcompound_ref> biomassRemoval_refs;
  list<modelcompound_ref> mediaSupplement_refs;
  list<modelreaction_ref> koRestore_refs;
  bool integrated;
  bool suboptimal;
  list<GapfillingReaction> gapfillingSolutionReactions;
} GapfillingSolution;

/*
GapFilling object holds data on the formulations and solutions of a gapfilling analysis

@searchable ws_subset id totalTimeLimit timePerSolution transporterMultiplier singleTransporterMultiplier biomassTransporterMultiplier noDeltaGMultiplier noStructureMultiplier deltaGMultiplier directionalityMultiplier drainFluxMultiplier reactionActivationBonus allowableCompartment_refs blacklistedReaction_refs targetedreaction_refs guaranteedReaction_refs completeGapfill balancedReactionsOnly reactionAdditionHypothesis gprHypothesis biomassHypothesis fba_ref fbamodel_ref probanno_ref mediaHypothesis
@searchable ws_subset gapfillingSolutions.[*].(id,suboptimal,integrated,solutionCost,koRestore_refs,biomassRemoval_refs,mediaSupplement_refs,gapfillingSolutionReactions.[*].(reaction_ref,compartment_ref,direction,candidateFeature_refs))
*/
typedef structure {
  gapfill_id id;
  fba_ref fba_ref;
  fbamodel_ref fbamodel_ref;
  probanno_ref probanno_ref;
  bool mediaHypothesis;
  bool biomassHypothesis;
  bool gprHypothesis;
  bool reactionAdditionHypothesis;
  bool balancedReactionsOnly;
  bool completeGapfill;
  list<reaction_ref> guaranteedReaction_refs;
  list<reaction_ref> targetedreaction_refs;
  list<reaction_ref> blacklistedReaction_refs;
  list<compartment_ref> allowableCompartment_refs;
  float reactionActivationBonus;
  float drainFluxMultiplier;
  float directionalityMultiplier;
  float deltaGMultiplier;
  float noStructureMultiplier;
  float noDeltaGMultiplier;
  float biomassTransporterMultiplier;
  float singleTransporterMultiplier;
  float transporterMultiplier;
  int timePerSolution;
  int totalTimeLimit;
  mapping<reaction_ref, float> reactionMultipliers;
  list<GapfillingSolution> gapfillingSolutions;
} Gapfilling;