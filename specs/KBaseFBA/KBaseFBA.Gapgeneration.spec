/*
Gapgen ID
@id kb
*/
typedef string gapgen_id;

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

typedef int bool;

/*
Reference to a model template
@id ws KBaseBiochem.Media
*/
typedef string media_ref;

/*
Gapgeneration solution ID
@id external
*/
typedef string gapgensol_id;

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
GapGenerationSolutionReaction object holds data a reaction proposed to be removed from the model
*/
typedef structure {
  modelreaction_ref modelreaction_ref;
  string direction;
} GapgenerationSolutionReaction;

/*
GapGenerationSolution object holds data on a solution proposed by the gapgeneration command
*/
typedef structure {
  gapgensol_id id;
  float solutionCost;
  list<modelcompound_ref> biomassSuppplement_refs;
  list<modelcompound_ref> mediaRemoval_refs;
  list<modelreaction_ref> additionalKO_refs;
  bool integrated;
  bool suboptimal;
  list<GapgenerationSolutionReaction> gapgenSolutionReactions;
} GapgenerationSolution;

/*
GapGeneration object holds data on formulation and solutions from gapgen analysis

@optional fba_ref totalTimeLimit timePerSolution media_ref referenceMedia_ref gprHypothesis reactionRemovalHypothesis biomassHypothesis mediaHypothesis
@searchable ws_subset id totalTimeLimit timePerSolution referenceMedia_ref fbamodel_ref fba_ref reactionRemovalHypothesis gprHypothesis biomassHypothesis mediaHypothesis
*/
typedef structure {
  gapgen_id id;
  fba_ref fba_ref;
  fbamodel_ref fbamodel_ref;
  bool mediaHypothesis;
  bool biomassHypothesis;
  bool gprHypothesis;
  bool reactionRemovalHypothesis;
  media_ref media_ref;
  media_ref referenceMedia_ref;
  int timePerSolution;
  int totalTimeLimit;
  list<GapgenerationSolution> gapgenSolutions;
} Gapgeneration;