/*
Reference to expression data
@id ws KBaseFeatureValues.ExpressionMatrix
*/
typedef string expression_matrix_ref;

/*
Reference to metabolic model
@id ws KBaseFBA.FBAModel
*/
typedef string fbamodel_ref;

/*
Reference to a FBA object
@id ws KBaseFBA.FBA
*/
typedef string fba_ref;

/*
FBAPathwayAnalysis object: this object holds the analysis of FBA, expression and gapfilling data
*/
typedef structure {
  string pegId;
  float expression;
} FBAPathwayAnalysisFeature;

typedef structure {
  string id;
  string name;
  float flux;
  int gapfill;
  int expressed;
  list<FBAPathwayAnalysisFeature> pegs;
} FBAPathwayAnalysisReaction;

typedef structure {
  string pathwayName;
  string pathwayId;
  int totalModelReactions;
  int totalKEGGRxns;
  int totalRxnFlux;
  int gsrFluxPExpP;
  int gsrFluxPExpN;
  int gsrFluxMExpP;
  int gsrFluxMExpM;
  int gpRxnsFluxP;
  list<FBAPathwayAnalysisReaction> reaction_list;
} FBAPathwayAnalysisPathway;

typedef structure {
  string pathwayType;
  expression_matrix_ref expression_matrix_ref;
  string expression_condition;
  fbamodel_ref fbamodel_ref;
  fba_ref fba_ref;
  list<FBAPathwayAnalysisPathway> pathways;
} FBAPathwayAnalysis;