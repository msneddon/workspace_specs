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
Reference to a model template
@id ws KBaseBiochem.Media
*/
typedef string media_ref;

/*
FBAComparisonFBA object: this object holds information about an FBA in a FBA comparison
*/
typedef structure {
  string id;
  fba_ref fba_ref;
  fbamodel_ref model_ref;
  mapping<string, tuple<int, int, int, int, int, int>> fba_similarity;
  float objective;
  media_ref media;
  int reactions;
  int compounds;
  int active_reactions;
  int uptake_compounds;
  int excretion_compounds;
} FBAComparisonFBA;

/*
Conserved state - indicates a possible state of reaction/compound in FBA with values:
        <NOT_IN_MODEL,INACTIVE,FORWARD,REVERSE,UPTAKE,EXCRETION>
*/
typedef string Conserved_state;

/*
FBAComparisonReaction object: this object holds information about a reaction across all compared models
*/
typedef structure {
  string id;
  string name;
  list<tuple<float, string, string, string>> stoichiometry;
  string direction;
  mapping<Conserved_state, tuple<int, float, float, float>> state_conservation;
  Conserved_state most_common_state;
  mapping<string, tuple<Conserved_state, float, float, float, float, float, float, string, string>> reaction_fluxes;
} FBAComparisonReaction;

/*
FBAComparisonCompound object: this object holds information about a compound across a set of FBA simulations
*/
typedef structure {
  string id;
  string name;
  float charge;
  string formula;
  mapping<Conserved_state, tuple<int, float, float>> state_conservation;
  Conserved_state most_common_state;
  mapping<string, tuple<Conserved_state, float, float, float, float, float, string>> exchanges;
} FBAComparisonCompound;

/*
FBAComparison object: this object holds information about a comparison of multiple FBA simulations

@metadata ws id as ID
@metadata ws common_reactions as Common reactions
@metadata ws common_reactions as Common compounds
@metadata ws length(fbas) as Number FBAs
@metadata ws length(reactions) as Number reactions
@metadata ws length(compounds) as Number compounds
*/
typedef structure {
  string id;
  int common_reactions;
  int common_compounds;
  list<FBAComparisonFBA> fbas;
  list<FBAComparisonReaction> reactions;
  list<FBAComparisonCompound> compounds;
} FBAComparison;