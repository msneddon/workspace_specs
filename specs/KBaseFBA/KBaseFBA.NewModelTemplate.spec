/*
ModelTemplate ID
@id kb
*/
typedef string modeltemplate_id;

/*
Reference to a biochemistry object
@id ws KBaseBiochem.Biochemistry
*/
typedef string Biochemistry_ref;

/*
Template role ID
@id external
*/
typedef string templaterole_id;

/*
Genome feature ID
@id external
*/
typedef string feature_id;

/*
TemplateRole object representing link to annotations or genes
*/
typedef structure {
  templaterole_id id;
  string name;
  string source;
  list<string> aliases;
  list<feature_id> features;
} TemplateRole;

/*
Template complex ID
@id external
*/
typedef string templatecomplex_id;

/*
Reference to role in Template Model
@id subws KBaseFBA.TemplateModel.roles.[*].id
*/
typedef string templaterole_ref;

/*
TemplateComplexRole object containing data relating to role in complex
*/
typedef structure {
  templaterole_ref templaterole_ref;
  int optional_role;
  int triggering;
} TemplateComplexRole;

/*
TemplateComplex object
*/
typedef structure {
  templatecomplex_id id;
  string name;
  string reference;
  string source;
  float confidence;
  list<TemplateComplexRole> complexroles;
} TemplateComplex;

/*
Template compound ID
@id external
*/
typedef string templatecompound_id;

/*
Reference to a compound object
@id subws KBaseBiochem.Biochemistry.compounds.[*].id
*/
typedef string compound_ref;

typedef int bool;

/*
TemplateCompound parallel to compound object in biochemistry compound_ref

@optional compound_ref md5
Z25 4437
*/
typedef structure {
  templatecompound_id id;
  compound_ref compound_ref;
  string name;
  string abbreviation;
  string md5;
  bool isCofactor;
  list<string> aliases;
  float defaultCharge;
  float mass;
  float deltaG;
  float deltaGErr;
  string formula;
} TemplateCompound;

/*
Template compartment compound ID
@id external
*/
typedef string templatecompcompound_id;

/*
Reference to compound in Template Model
@id subws KBaseFBA.TemplateModel.compounds.[*].id
*/
typedef string templatecompound_ref;

/*
Reference to compartment in Template Model
@id subws KBaseFBA.TemplateModel.compartments.[*].id
*/
typedef string templatecompartment_ref;

/*
TemplateCompCompound object parallel to compound in model

@optional formula
*/
typedef structure {
  templatecompcompound_id id;
  templatecompound_ref templatecompound_ref;
  float charge;
  float maxuptake;
  string formula;
  templatecompartment_ref templatecompartment_ref;
} TemplateCompCompound;

/*
Template compartment ID
@id external
*/
typedef string templatecompartment_id;

/*
TemplateCompartment parallel to compartment object in biochemistry
*/
typedef structure {
  templatecompartment_id id;
  string name;
  list<string> aliases;
  int hierarchy;
  float pH;
} TemplateCompartment;

/*
Template reaction ID
@id external
*/
typedef string templatereaction_id;

/*
Reference to a reaction object in a biochemistry
@id subws KBaseBiochem.Biochemistry.reactions.[*].id
*/
typedef string reaction_ref;

/*
Reference to compartment compound in Template Model
@id subws KBaseFBA.TemplateModel.compcompounds.[*].id
*/
typedef string templatecompcompound_ref;

/*
TemplateReactionReagent object
*/
typedef structure {
  templatecompcompound_ref templatecompcompound_ref;
  float coefficient;
} TemplateReactionReagent;

/*
Reference to complex in Template Model
@id subws KBaseFBA.TemplateModel.complexes.[*].id
*/
typedef string templatecomplex_ref;

/*
TemplateReaction object holds data on reaction in template

@optional reference base_cost forward_penalty reverse_penalty GapfillDirection reaction_ref
*/
typedef structure {
  templatereaction_id id;
  reaction_ref reaction_ref;
  string name;
  string type;
  string reference;
  string direction;
  string GapfillDirection;
  float maxforflux;
  float maxrevflux;
  templatecompartment_ref templatecompartment_ref;
  float base_cost;
  float forward_penalty;
  float reverse_penalty;
  list<TemplateReactionReagent> templateReactionReagents;
  list<templatecomplex_ref> templatecomplex_refs;
} NewTemplateReaction;

/*
Template biomass ID
@id external
*/
typedef string templatebiomass_id;

/*
TemplateBiomassComponent object holds data on a compound of biomass in template
*/
typedef structure {
  string class;
  templatecompcompound_ref templatecompcompound_ref;
  string coefficient_type;
  float coefficient;
  list<templatecompcompound_ref> linked_compound_refs;
  list<float> link_coefficients;
} NewTemplateBiomassComponent;

/*
TemplateBiomass object holds data on biomass in template
*/
typedef structure {
  templatebiomass_id id;
  string name;
  string type;
  float other;
  float dna;
  float rna;
  float protein;
  float lipid;
  float cellwall;
  float cofactor;
  float energy;
  list<NewTemplateBiomassComponent> templateBiomassComponents;
} NewTemplateBiomass;

/*
Template pathway ID
@id external
*/
typedef string templatepathway_id;

/*
Reference to reaction in Template Model
@id subws KBaseFBA.TemplateModel.reactions.[*].id
*/
typedef string templatereaction_ref;

/*
TemplatePathway object
*/
typedef structure {
  templatepathway_id id;
  string name;
  string source;
  string source_id;
  string broadClassification;
  string midClassification;
  list<templatereaction_ref> templatereaction_refs;
} TemplatePathway;

/*
ModelTemplate object holds data on how a model is constructed from an annotation
            
@optional name
*/
typedef structure {
  modeltemplate_id id;
  string name;
  string type;
  string domain;
  Biochemistry_ref biochemistry_ref;
  list<TemplateRole> roles;
  list<TemplateComplex> complexes;
  list<TemplateCompound> compounds;
  list<TemplateCompCompound> compcompounds;
  list<TemplateCompartment> compartments;
  list<NewTemplateReaction> reactions;
  list<NewTemplateBiomass> biomasses;
  list<TemplatePathway> pathways;
} NewModelTemplate;