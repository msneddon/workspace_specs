/*
Reference to metabolic model
@id ws KBaseFBA.FBAModel
*/
typedef string fbamodel_ref;

typedef int bool;

/*
Reference to a reaction object in a model
@id subws KBaseFBA.FBAModel.modelreactions.[*].id
*/
typedef string modelreaction_ref;

/*
Model compound ID
@id external
*/
typedef string modelcompound_id;

/*
Model reaction ID
@id external
*/
typedef string modelreaction_id;

/*
Genome feature ID
@id external
*/
typedef string feature_id;

/*
Object for holding reaction knockout sensitivity reaction data

kb_sub_id kbid - KBase ID for reaction knockout sensitivity reaction
ws_sub_id model_reaction_wsid - ID of model reaction
bool delete - indicates if reaction is to be deleted
bool deleted - indicates if the reaction has been deleted
float growth_fraction - Fraction of wild-type growth after knockout
float normalized_activated_reaction_count - Normalized number of activated reactions
list<ws_sub_id> biomass_compounds  - List of biomass compounds that depend on the reaction
list<ws_sub_id> new_inactive_rxns - List of new reactions dependant upon reaction KO
list<ws_sub_id> new_essentials - List of new essential genes with reaction knockout
        
@optional direction
*/
typedef structure {
  string id;
  modelreaction_ref modelreaction_ref;
  float growth_fraction;
  bool delete;
  bool deleted;
  string direction;
  float normalized_activated_reaction_count;
  list<modelcompound_id> biomass_compounds;
  list<modelreaction_id> new_inactive_rxns;
  list<feature_id> new_essentials;
} ReactionSensitivityAnalysisReaction;

/*
ReactionSensitivityAnalysisCorrectedReaction object

kb_sub_id kbid - KBase ID for reaction knockout corrected reaction
ws_sub_id model_reaction_wsid - ID of model reaction
float normalized_required_reaction_count - Normalized count of reactions required for this reaction to function
list<ws_sub_id> required_reactions - list of reactions required for this reaction to function

@optional
*/
typedef structure {
  modelreaction_ref modelreaction_ref;
  float normalized_required_reaction_count;
  list<modelreaction_id> required_reactions;
} ReactionSensitivityAnalysisCorrectedReaction;

/*
Object for holding reaction knockout sensitivity results

        kb_id kbid - KBase ID of reaction sensitivity object
        ws_id model_wsid - Workspace reference to associated model
        string type - type of reaction KO sensitivity object
        bool deleted_noncontributing_reactions - boolean indicating if noncontributing reactions were deleted
        bool integrated_deletions_in_model - boolean indicating if deleted reactions were implemented in the model
        list<ReactionSensitivityAnalysisReaction> reactions - list of sensitivity data for tested reactions
        list<ReactionSensitivityAnalysisCorrectedReaction> corrected_reactions - list of reactions dependant upon tested reactions
        
        @searchable ws_subset id fbamodel_ref type deleted_noncontributing_reactions integrated_deletions_in_model
        @optional
*/
typedef structure {
  string id;
  fbamodel_ref fbamodel_ref;
  string type;
  bool deleted_noncontributing_reactions;
  bool integrated_deletions_in_model;
  list<ReactionSensitivityAnalysisReaction> reactions;
  list<ReactionSensitivityAnalysisCorrectedReaction> corrected_reactions;
} ReactionSensitivityAnalysis;