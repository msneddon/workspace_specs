/*
PhenotypeSimulationSet ID
@id kb
*/
typedef string phenosimset_id;

/*
Reference to a model object
@id ws KBaseFBA.FBAModel
*/
typedef string fbamodel_ref;

/*
Reference to a PhenotypeSet object
@id ws KBasePhenotypes.PhenotypeSet
*/
typedef string phenotypeset_ref;

/*
Phenotype simulation ID
@id external
*/
typedef string phenosim_id;

/*
Reference to a PhenotypeSet object
@id subws KBasePhenotypes.PhenotypeSet.phenotypes.[*].id
*/
typedef string phenotype_ref;

/*
PhenotypeSimulation subobject holds data on a single phenotype simulation

@searchable ws_subset id phenotype_ref simulatedGrowth simulatedGrowthFraction phenoclass
*/
typedef structure {
  phenosim_id id;
  phenotype_ref phenotype_ref;
  float simulatedGrowth;
  float simulatedGrowthFraction;
  int numGapfilledReactions;
  string phenoclass;
} PhenotypeSimulation;

/*
PhenotypeSimulationSet object holds data on simulations of many phenotypes

    @metadata ws length(phenotypeSimulations) as Number phenotypes
*/
typedef structure {
  phenosimset_id id;
  fbamodel_ref fbamodel_ref;
  phenotypeset_ref phenotypeset_ref;
  list<PhenotypeSimulation> phenotypeSimulations;
} PhenotypeSimulationSet;