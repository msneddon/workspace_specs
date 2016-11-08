/*
FBAModel ID
@id kb
*/
typedef string fbamodel_id;

/*
Source ID
@id external
*/
typedef string source_id;

/*
Reference to a model template
@id ws KBaseGenomes.Genome KBaseGenomeAnnotations.GenomeAnnotation
*/
typedef string genome_ref;

/*
Reference to a metagenome object
@id ws KBaseGenomes.MetagenomeAnnotation
*/
typedef string metagenome_ref;

/*
Reference to an OTU in a metagenome
@id subws KBaseGenomes.MetagenomeAnnotation.otus.[*].id
*/
typedef string metagenome_otu_ref;

/*
Reference to a model template
*/
typedef string template_ref;

/*
Gapfill ID
@id kb
*/
typedef string gapfill_id;

/*
Reference to a gapfilling object
@id ws KBaseFBA.Gapfilling
*/
typedef string gapfill_ref;

/*
Reference to a FBA object
@id ws KBaseFBA.FBA
*/
typedef string fba_ref;

typedef int bool;

/*
Reference to a model template
@id ws KBaseBiochem.Media
*/
typedef string media_ref;

/*
ModelGapfill object
 
@optional integrated_solution
@optional fba_ref
@optional gapfill_ref jobnode
*/
typedef structure {
  gapfill_id id;
  gapfill_id gapfill_id;
  gapfill_ref gapfill_ref;
  fba_ref fba_ref;
  bool integrated;
  string integrated_solution;
  media_ref media_ref;
  string jobnode;
} ModelGapfill;

/*
Gapgen ID
@id kb
*/
typedef string gapgen_id;

/*
Reference to a gapgen object
@id ws KBaseFBA.Gapgeneration
*/
typedef string gapgen_ref;

/*
ModelGapgen object

@optional integrated_solution
@optional fba_ref
@optional gapgen_ref jobnode
*/
typedef structure {
  gapgen_id id;
  gapgen_id gapgen_id;
  gapgen_ref gapgen_ref;
  fba_ref fba_ref;
  bool integrated;
  string integrated_solution;
  media_ref media_ref;
  string jobnode;
} ModelGapgen;

typedef structure {
  bool integrated;
  list<tuple<string, float, bool>> ReactionMaxBounds;
  list<tuple<string, float>> UptakeMaxBounds;
  list<tuple<string, string, float>> BiomassChanges;
  float ATPSynthase;
  float ATPMaintenance;
} QuantOptSolution;

/*
ModelQuantOpt object
*/
typedef structure {
  string id;
  fba_ref fba_ref;
  media_ref media_ref;
  bool integrated;
  int integrated_solution;
  list<QuantOptSolution> solutions;
} ModelQuantOpt;

/*
Biomass reaction ID
@id external
*/
typedef string biomass_id;

/*
Reference to a compound object in a model
@id subws KBaseFBA.FBAModel.modelcompounds.[*].id
*/
typedef string modelcompound_ref;

/*
BiomassCompound object

    @searchable ws_subset modelcompound_ref coefficient
    @optional gapfill_data
*/
typedef structure {
  modelcompound_ref modelcompound_ref;
  float coefficient;
  mapping<gapfill_id, bool> gapfill_data;
} BiomassCompound;

/*
Biomass object

@optional removedcompounds
*/
typedef structure {
  biomass_id id;
  string name;
  float other;
  float dna;
  float rna;
  float protein;
  float cellwall;
  float lipid;
  float cofactor;
  float energy;
  list<BiomassCompound> biomasscompounds;
  list<BiomassCompound> removedcompounds;
} Biomass;

/*
Model compartment ID
@id external
*/
typedef string modelcompartment_id;

/*
Reference to a compartment object
@id subws KBaseBiochem.Biochemistry.compartments.[*].id
*/
typedef string compartment_ref;

/*
ModelCompartment object
*/
typedef structure {
  modelcompartment_id id;
  compartment_ref compartment_ref;
  int compartmentIndex;
  string label;
  float pH;
  float potential;
} ModelCompartment;

/*
Model compound ID
@id external
*/
typedef string modelcompound_id;

/*
Reference to a compound object
@id subws KBaseBiochem.Biochemistry.compounds.[*].id
*/
typedef string compound_ref;

/*
Reference to a compartment object in a model
@id subws KBaseFBA.FBAModel.modelcompartments.[*].id
*/
typedef string modelcompartment_ref;

/*
ModelCompound object

@optional aliases maxuptake
*/
typedef structure {
  modelcompound_id id;
  compound_ref compound_ref;
  list<string> aliases;
  string name;
  float charge;
  float maxuptake;
  string formula;
  modelcompartment_ref modelcompartment_ref;
} ModelCompound;

/*
Model reaction ID
@id external
*/
typedef string modelreaction_id;

/*
Reference to a reaction object in a biochemistry
@id subws KBaseBiochem.Biochemistry.reactions.[*].id
*/
typedef string reaction_ref;

/*
ModelReactionReagent object

    @searchable ws_subset modelcompound_ref coefficient
*/
typedef structure {
  modelcompound_ref modelcompound_ref;
  float coefficient;
} ModelReactionReagent;

/*
Reference to a complex object
@id subws KBaseOntology.Mapping.complexes.[*].id
*/
typedef string complex_ref;

/*
Reference to a feature of a genome object
@id subws KBaseGenomes.Genome.features.[*].id
*/
typedef string feature_ref;

/*
ModelReactionProteinSubunit object

    @searchable ws_subset role triggering optionalSubunit feature_refs
*/
typedef structure {
  string role;
  bool triggering;
  bool optionalSubunit;
  string note;
  list<feature_ref> feature_refs;
} ModelReactionProteinSubunit;

/*
ModelReactionProtein object

@optional source complex_ref
*/
typedef structure {
  complex_ref complex_ref;
  string note;
  list<ModelReactionProteinSubunit> modelReactionProteinSubunits;
  string source;
} ModelReactionProtein;

/*
ModelReaction object

@optional gapfill_data name pathway reference aliases maxforflux maxrevflux
*/
typedef structure {
  modelreaction_id id;
  reaction_ref reaction_ref;
  string name;
  list<string> aliases;
  string pathway;
  string reference;
  string direction;
  float protons;
  float maxforflux;
  float maxrevflux;
  modelcompartment_ref modelcompartment_ref;
  float probability;
  list<ModelReactionReagent> modelReactionReagents;
  list<ModelReactionProtein> modelReactionProteins;
  mapping<string, mapping<int, tuple<string, bool, list<ModelReactionProtein>>>> gapfill_data;
} ModelReaction;

/*
FBAModel object

@optional gapfilledcandidates metagenome_otu_ref metagenome_ref genome_ref template_refs ATPSynthaseStoichiometry ATPMaintenance quantopts
    @metadata ws source_id as Source ID
    @metadata ws source as Source
    @metadata ws name as Name
    @metadata ws type as Type
    @metadata ws genome_ref as Genome
    @metadata ws length(biomasses) as Number biomasses
    @metadata ws length(modelcompartments) as Number compartments
    @metadata ws length(modelcompounds) as Number compounds
    @metadata ws length(modelreactions) as Number reactions
    @metadata ws length(gapgens) as Number gapgens
    @metadata ws length(gapfillings) as Number gapfills
*/
typedef structure {
  fbamodel_id id;
  string source;
  source_id source_id;
  string name;
  string type;
  genome_ref genome_ref;
  metagenome_ref metagenome_ref;
  metagenome_otu_ref metagenome_otu_ref;
  template_ref template_ref;
  float ATPSynthaseStoichiometry;
  float ATPMaintenance;
  list<template_ref> template_refs;
  list<ModelGapfill> gapfillings;
  list<ModelGapgen> gapgens;
  list<ModelQuantOpt> quantopts;
  list<Biomass> biomasses;
  list<ModelCompartment> modelcompartments;
  list<ModelCompound> modelcompounds;
  list<ModelReaction> modelreactions;
  list<ModelReaction> gapfilledcandidates;
} FBAModel;