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

typedef structure {
  string pathwayName;
  string pathwayId;
  int totalModelReactions;
  int totalabsentRxns;
  int totalKEGGRxns;
  int totalRxnFlux;
  int gsrFluxPExpP;
  int gsrFluxPExpN;
  int gsrFluxMExpP;
  int gsrFluxMExpM;
  int gpRxnsFluxP;
} FBAPathwayAnalysisCounts;

typedef structure {
  expression_matrix_ref expression_matrix_ref;
  string expression_condition;
  fbamodel_ref fbamodel_ref;
  fba_ref fba_ref;
  list<FBAPathwayAnalysisCounts> count_list;
} FBAPathwayAnalysisPathwayMultiple;

typedef structure {
  string pathwayType;
  list<FBAPathwayAnalysisPathwayMultiple> fbaexpression;
} FBAPathwayAnalysisMultiple;