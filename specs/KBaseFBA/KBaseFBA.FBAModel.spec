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
@id ws KBaseGenomes.Genome
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
@id ws KBaseFBA.ModelTemplate
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

typedef int bool;

/*
Reference to a model template
@id ws KBaseBiochem.Media
*/
typedef string media_ref;

/*
ModelGapfill object
 
@optional integrated_solution
    @searchable ws_subset id gapfill_id gapfill_ref integrated_solution integrated media_ref
*/
typedef structure {
  gapfill_id id;
  gapfill_id gapfill_id;
  gapfill_ref gapfill_ref;
  bool integrated;
  string integrated_solution;
  media_ref media_ref;
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
    @searchable ws_subset id gapgen_id gapgen_ref integrated media_ref integrated_solution
*/
typedef structure {
  gapgen_id id;
  gapgen_id gapgen_id;
  gapgen_ref gapgen_ref;
  bool integrated;
  string integrated_solution;
  media_ref media_ref;
} ModelGapgen;

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
*/
typedef structure {
  modelcompound_ref modelcompound_ref;
  float coefficient;
} BiomassCompound;

/*
Biomass object

    @searchable ws_subset id name other dna rna protein cellwall lipid cofactor energy
    @searchable ws_subset biomasscompounds.[*].(modelcompound_ref,coefficient)
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

    @searchable ws_subset id compartment_ref compartmentIndex label pH potential
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

    @searchable ws_subset id compound_ref name charge formula modelcompartment_ref
*/
typedef structure {
  modelcompound_id id;
  compound_ref compound_ref;
  list<string> aliases;
  string name;
  float charge;
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
 
    @searchable ws_subset complex_ref modelReactionProteinSubunits.[*].(role,triggering,optionalSubunit,feature_refs)
*/
typedef structure {
  complex_ref complex_ref;
  string note;
  list<ModelReactionProteinSubunit> modelReactionProteinSubunits;
} ModelReactionProtein;

/*
ModelReaction object

@optional name pathway reference
    @searchable ws_subset id reaction_ref direction protons modelcompartment_ref probability
    @searchable ws_subset modelReactionReagents.[*].(modelcompound_ref,coefficient)
    @searchable ws_subset modelReactionProteins.[*].(complex_ref,modelReactionProteinSubunits.[*].(role,triggering,optionalSubunit,feature_refs))
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
  modelcompartment_ref modelcompartment_ref;
  float probability;
  list<ModelReactionReagent> modelReactionReagents;
  list<ModelReactionProtein> modelReactionProteins;
} ModelReaction;

/*
FBAModel object

@optional metagenome_otu_ref metagenome_ref genome_ref
@searchable ws_subset id source_id source name type genome_ref metagenome_ref metagenome_otu_ref template_ref
@searchable ws_subset gapfillings.[*].(gapfill_id,gapfill_ref,integrated,media_ref,integrated_solution) 
@searchable ws_subset gapgens.[*].(gapgen_id,gapgen_ref,integrated,media_ref,integrated_solution) 
@searchable ws_subset biomasses.[*].(id,name,other,dna,rna,protein,cellwall,lipid,cofactor,energy,biomasscompounds.[*].(modelcompound_ref,coefficient)) 
@searchable ws_subset modelcompartments.[*].(id,compartment_ref,compartmentIndex,label,pH,potential) 
@searchable ws_subset modelcompounds.[*].(id,name)
@searchable ws_subset modelreactions.[*].(id,modelReactionReagents.[*].(modelcompound_ref,coefficient),modelReactionProteins.[*].(modelReactionProteinSubunits.[*].(feature_refs)))
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
  list<ModelGapfill> gapfillings;
  list<ModelGapgen> gapgens;
  list<Biomass> biomasses;
  list<ModelCompartment> modelcompartments;
  list<ModelCompound> modelcompounds;
  list<ModelReaction> modelreactions;
} FBAModel;