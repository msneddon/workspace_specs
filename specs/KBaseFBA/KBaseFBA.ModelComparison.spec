/*
Reference to a Proteome Comparison object in the workspace
@id ws GenomeComparison.ProteomeComparison
*/
typedef string protcomp_ref;

/*
Reference to a Pangenome object in the workspace
@id ws KBaseGenomes.Pangenome
*/
typedef string pangenome_ref;

/*
Reference to metabolic model
@id ws KBaseFBA.FBAModel
*/
typedef string fbamodel_ref;

/*
Reference to a model template
@id ws KBaseGenomes.Genome
*/
typedef string genome_ref;

/*
ModelComparisonModel object: this object holds information about a model in a model comparison
*/
typedef structure {
  string id;
  fbamodel_ref model_ref;
  genome_ref genome_ref;
  mapping<string, tuple<int, int, int, int, int>> model_similarity;
  string name;
  string taxonomy;
  int reactions;
  int families;
  int compounds;
  int biomasscpds;
  int biomasses;
} ModelComparisonModel;

/*
Reference to a reaction object in a biochemistry
@id subws KBaseBiochem.Biochemistry.reactions.[*].id
*/
typedef string reaction_ref;

typedef int bool;

/*
Genome feature ID
@id external
*/
typedef string feature_id;

/*
Feature family ID
@id external
*/
typedef string family_id;

/*
ModelComparisonReaction object: this object holds information about a reaction across all compared models
*/
typedef structure {
  string id;
  reaction_ref reaction_ref;
  string name;
  string equation;
  int number_models;
  float fraction_models;
  bool core;
  mapping<string, tuple<bool, string, list<tuple<feature_id, family_id, float, bool>>, string>> reaction_model_data;
} ModelComparisonReaction;

/*
Reference to a compound object
@id subws KBaseBiochem.Biochemistry.compounds.[*].id
*/
typedef string compound_ref;

/*
Reference to a compartment object
@id subws KBaseBiochem.Biochemistry.compartments.[*].id
*/
typedef string compartment_ref;

/*
ModelComparisonCompound object: this object holds information about a compound across a set of models
*/
typedef structure {
  string id;
  compound_ref compound_ref;
  string name;
  int number_models;
  float fraction_models;
  bool core;
  mapping<string, list<tuple<compartment_ref, float>>> model_compound_compartments;
} ModelComparisonCompound;

/*
Reaction ID
@id external
*/
typedef string reaction_id;

/*
ModelComparisonFamily object: this object holds information about a protein family across a set of models
*/
typedef structure {
  string id;
  family_id family_id;
  string function;
  int number_models;
  float fraction_models;
  bool core;
  mapping<string, tuple<bool, list<reaction_id>>> family_model_data;
} ModelComparisonFamily;

/*
ModelComparisonBiomassCompound object: this object holds information about a biomass compound across a set of models
*/
typedef structure {
  string id;
  compound_ref compound_ref;
  string name;
  int number_models;
  float fraction_models;
  bool core;
  mapping<string, list<tuple<compartment_ref, float>>> model_biomass_compounds;
} ModelComparisonBiomassCompound;

/*
ModelComparisonResult object: this object holds information about a comparison of multiple models

@optional protcomp_ref pangenome_ref
@metadata ws core_reactions as Core reactions
@metadata ws core_compounds as Core compounds
@metadata ws core_families as Core families
@metadata ws core_biomass_compounds as Core biomass compounds
@metadata ws name as Name
@metadata ws id as ID
@metadata ws length(models) as Number models
@metadata ws length(reactions) as Number reactions
@metadata ws length(compounds) as Number compounds
@metadata ws length(families) as Number families
@metadata ws length(biomasscpds) as Number biomass compounds
*/
typedef structure {
  string id;
  string name;
  int core_reactions;
  int core_compounds;
  int core_families;
  int core_biomass_compounds;
  protcomp_ref protcomp_ref;
  pangenome_ref pangenome_ref;
  list<ModelComparisonModel> models;
  list<ModelComparisonReaction> reactions;
  list<ModelComparisonCompound> compounds;
  list<ModelComparisonFamily> families;
  list<ModelComparisonBiomassCompound> biomasscpds;
} ModelComparison;