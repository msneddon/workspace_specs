/*
Biochemistry ID
@id kb
*/
typedef string biochem_id;

/*
Reaction ID
@id external
*/
typedef string compartment_id;

/*
Compartment object

    @searchable ws_subset id name hierarchy
*/
typedef structure {
  compartment_id id;
  string name;
  int hierarchy;
} Compartment;

/*
Compound ID
@id external
*/
typedef string compound_id;

typedef int bool;

/*
Reference to a compound object in a biochemistry
@id subws KBCHEM.Biochemistry.compounds.[*].id
*/
typedef string compound_ref;

/*
Reference to a reaction object in a biochemistry
@id subws KBCHEM.BiochemistryStructures.structures.[*].id
*/
typedef string structure_ref;

/*
Reference to a cue object in a biochemistry
@id subws KBCHEM.Biochemistry.cues.[*].id
*/
typedef string cue_ref;

/*
Compound object

@optional md5 formula unchargedFormula mass deltaG deltaGErr abstractCompound_ref comprisedOfCompound_refs structure_ref cues pkas pkbs
    @searchable ws_subset id isCofactor name abbreviation md5 formula unchargedFormula mass defaultCharge deltaG abstractCompound_ref comprisedOfCompound_refs structure_ref cues
*/
typedef structure {
  compound_id id;
  bool isCofactor;
  string name;
  string abbreviation;
  string md5;
  string formula;
  string unchargedFormula;
  int mass;
  float defaultCharge;
  float deltaG;
  float deltaGErr;
  compound_ref abstractCompound_ref;
  list<compound_ref> comprisedOfCompound_refs;
  structure_ref structure_ref;
  mapping<cue_ref, float> cues;
  mapping<int, list<float>> pkas;
  mapping<int, list<float>> pkbs;
} Compound;

/*
Reaction ID
@id external
*/
typedef string reaction_id;

/*
Reference to a reaction object in a biochemistry
@id subws KBCHEM.Biochemistry.reactions.[*].id
*/
typedef string reaction_ref;

/*
Reference to a compartment object in a biochemistry
@id subws KBCHEM.Biochemistry.compartments.[*].id
*/
typedef string compartment_ref;

/*
Reactant object

    @searchable ws_subset compound_ref compartment_ref coefficient isCofactor
*/
typedef structure {
  compound_ref compound_ref;
  compartment_ref compartment_ref;
  float coefficient;
  bool isCofactor;
} Reagent;

/*
Reaction object

@optional md5 deltaG deltaGErr abstractReaction_ref cues
    @searchable ws_subset id name abbreviation md5 direction thermoReversibility status defaultProtons deltaG abstractReaction_ref cues
    @searchable ws_subset reagents.[*].(compound_ref,compartment_ref,coefficient,isCofactor)
*/
typedef structure {
  reaction_id id;
  string name;
  string abbreviation;
  string md5;
  string direction;
  string thermoReversibility;
  string status;
  float defaultProtons;
  float deltaG;
  float deltaGErr;
  reaction_ref abstractReaction_ref;
  mapping<cue_ref, float> cues;
  list<Reagent> reagents;
} Reaction;

/*
Reaction set ID
@id external
*/
typedef string reactionset_id;

/*
ReactionSet object

@searchable ws_subset id name class reaction_refs type
*/
typedef structure {
  reactionset_id id;
  string name;
  string class;
  string type;
  list<reaction_ref> reaction_refs;
} ReactionSet;

/*
Compound set ID
@id external
*/
typedef string compoundset_id;

/*
CompoundSet object

@searchable ws_subset id name class compound_refs type
*/
typedef structure {
  compoundset_id id;
  string name;
  string class;
  string type;
  list<compound_ref> compound_refs;
} CompoundSet;

/*
Reaction ID
@id external
*/
typedef string cue_id;

/*
Cue object

@optional mass deltaGErr deltaG defaultCharge structure_key structure_data structure_type
    @searchable ws_subset structure_key id name abbreviation formula unchargedFormula mass defaultCharge deltaG smallMolecule priority structure_key structure_data
*/
typedef structure {
  cue_id id;
  string name;
  string abbreviation;
  string formula;
  string unchargedFormula;
  int mass;
  float defaultCharge;
  float deltaG;
  float deltaGErr;
  bool smallMolecule;
  int priority;
  string structure_key;
  string structure_data;
  string structure_type;
} Cue;

/*
Biochemistry object

@optional description name
@searchable ws_subset compartments.[*].(id,name,hierarchy)
@searchable ws_subset compounds.[*].(id,isCofactor,name,abbreviation,formula,unchargedFormula,abstractCompound_ref,comprisedOfCompound_refs)
@searchable ws_subset reactions.[*].(id,name,abbreviation,defaultProtons,abstractReaction_ref,reagents.[*].(compound_ref))
@searchable ws_subset cues.[*].(id,name,abbreviation,formula,unchargedFormula,smallMolecule,priority)
@searchable ws_subset reactionSets.[*].(id,name,class,reaction_refs,type)
@searchable ws_subset compoundSets.[*].(id,name,class,compound_refs,type)
*/
typedef structure {
  biochem_id id;
  string name;
  string description;
  list<Compartment> compartments;
  list<Compound> compounds;
  list<Reaction> reactions;
  list<ReactionSet> reactionSets;
  list<CompoundSet> compoundSets;
  list<Cue> cues;
  mapping<compound_id, mapping<string, list<string>>> compound_aliases;
  mapping<reaction_id, mapping<string, list<string>>> reaction_aliases;
} Biochemistry;