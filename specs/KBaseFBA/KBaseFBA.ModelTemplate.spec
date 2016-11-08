/*
ModelTemplate ID
@id kb
*/
typedef string modeltemplate_id;

/*
Reference to a mapping object
@id ws KBaseOntology.Mapping
*/
typedef string mapping_ref;

/*
Reference to a biochemistry object
@id ws KBaseBiochem.Biochemistry
*/
typedef string Biochemistry_ref;

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
Reference to a compartment object
@id subws KBaseBiochem.Biochemistry.compartments.[*].id
*/
typedef string compartment_ref;

/*
Reference to a complex object
@id subws KBaseOntology.Mapping.complexes.[*].id
*/
typedef string complex_ref;

/*
TemplateReaction object holds data on reaction in template

@optional base_cost forward_penalty reverse_penalty
@searchable ws_subset id direction type reaction_ref compartment_ref complex_refs
*/
typedef structure {
  templatereaction_id id;
  reaction_ref reaction_ref;
  compartment_ref compartment_ref;
  list<complex_ref> complex_refs;
  string direction;
  string type;
  float base_cost;
  float forward_penalty;
  float reverse_penalty;
} TemplateReaction;

/*
Template biomass ID
@id external
*/
typedef string templatebiomass_id;

/*
Template biomass compound ID
@id external
*/
typedef string templatebiomasscomponent_id;

/*
Reference to a compound object
@id subws KBaseBiochem.Biochemistry.compounds.[*].id
*/
typedef string compound_ref;

/*
TemplateBiomassComponent object holds data on a compound of biomass in template

@searchable ws_subset id coefficientType class compound_ref compartment_ref
*/
typedef structure {
  templatebiomasscomponent_id id;
  string class;
  compound_ref compound_ref;
  compartment_ref compartment_ref;
  string coefficientType;
  float coefficient;
  list<compound_ref> linked_compound_refs;
  list<float> link_coefficients;
} TemplateBiomassComponent;

/*
TemplateBiomass object holds data on biomass in template

@searchable ws_subset id name type other dna rna protein lipid cellwall cofactor energy
@searchable ws_subset templateBiomassComponents.[*].(id,coefficientType,class,compound_ref,compartment_ref)
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
  list<TemplateBiomassComponent> templateBiomassComponents;
} TemplateBiomass;

/*
ModelTemplate object holds data on how a model is constructed from an annotation
            
@optional name
@searchable ws_subset id name modelType domain mapping_ref
@searchable ws_subset templateReactions.[*].(id,reaction_ref,compartment_ref,complex_refs,direction,type) 
@searchable ws_subset templateBiomasses.[*].(id,name,type,other,dna,rna,protein,lipid,cellwall,cofactor,energy,templateBiomassComponents.[*].(id,coefficientType,class,compound_ref,compartment_ref))
*/
typedef structure {
  modeltemplate_id id;
  string name;
  string modelType;
  string domain;
  mapping_ref mapping_ref;
  Biochemistry_ref biochemistry_ref;
  list<TemplateReaction> templateReactions;
  list<TemplateBiomass> templateBiomasses;
} ModelTemplate;