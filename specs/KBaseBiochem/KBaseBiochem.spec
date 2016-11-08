/*
@author chenry
*/
module KBaseBiochem {
	typedef int bool;
	/*
		Reference to a reaction object in a biochemistry
		@id subws KBCHEM.BiochemistryStructures.structures.[*].id
	*/
    typedef string structure_ref;
	/*
		Reference to a reaction object in a biochemistry
		@id subws KBCHEM.Biochemistry.reactions.[*].id
	*/
    typedef string reaction_ref;
	/*
		Reference to a cue object in a biochemistry
		@id subws KBCHEM.Biochemistry.cues.[*].id
	*/
    typedef string cue_ref;
	/*
		Reference to a compartment object in a biochemistry
		@id subws KBCHEM.Biochemistry.compartments.[*].id
	*/
    typedef string compartment_ref;
	/*
		Reference to a compound object in a biochemistry
		@id subws KBCHEM.Biochemistry.compounds.[*].id
	*/
    typedef string compound_ref;
	/*
		KBase genome ID
		@id kb
	*/
    typedef string genome_id;
    /*
		Reaction set ID
		@id external
	*/
    typedef string reactionset_id;
    /*
		Compound set ID
		@id external
	*/
    typedef string compoundset_id;
    /*
		Genome ID
		@id external
	*/
    typedef string biomass_id;
    /*
		Compound ID
		@id external
	*/
    typedef string compound_id;
    /*
		Reaction ID
		@id external
	*/
    typedef string reaction_id;
    /*
		Reaction ID
		@id external
	*/
    typedef string compartment_id;
    /*
		Reaction ID
		@id external
	*/
    typedef string cue_id;
    /*
		Model compartment ID
		@id external
	*/
    typedef string modelcompartment_id;
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
		Source ID
		@id external
	*/
    typedef string source_id;
    /*
		Biochemistry ID
		@id kb
	*/
    typedef string biochem_id;
    /*
		Gapgen ID
		@id kb
	*/
    typedef string gapgen_id;
	/*
		Gapfill ID
		@id kb
	*/
    typedef string gapfill_id;
    /*
		FBAModel ID
		@id kb
	*/
    typedef string fbamodel_id;
    /*
		Media ID
		@id kb
	*/
    typedef string media_id;
    /*
		Biochemistry structure ID
		@id kb
	*/
    typedef string biochemstruct_id;
	/*
		Compound structure ID
		@id external
	*/
    typedef string structure_id;
    
    /* 
    	Compound object
    	 
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
    	mapping<cue_ref,float> cues;
    	mapping<int,float> pkas;
    	mapping<int,float> pkbs;
    } Compound;
    
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
    	mapping<cue_ref,float> cues;
    	list<Reagent> reagents; 
    } Reaction;
    
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
    	Cue object
    	 
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
    	MediaCompound object
    	
    	@searchable ws_subset compound_ref concentration maxFlux minFlux
    */
	typedef structure {
		compound_ref compound_ref;
		float concentration;
		float maxFlux;
		float minFlux;
	} MediaCompound;
	
	/* 
    	Media object
    	
    	@searchable ws_subset id isDefined isMinimal name type
    	@searchable ws_subset mediacompounds.[*].(compound_ref,concentration,maxFlux,minFlux)
    */
	typedef structure {
		media_id id;
		source_id source_id;
		bool isDefined;
		bool isMinimal;
		string name;
		string type;
		list<MediaCompound> mediacompounds;
	} Media;
	
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
    	Biochemistry object
    	
    	@optional description name
    	@searchable ws_subset compartments.[*].(id,name,hierarchy)
    	@searchable ws_subset compounds.[*].(id,isCofactor,name,abbreviation,md5,formula,unchargedFormula,mass,defaultCharge,deltaG,abstractCompound_ref,comprisedOfCompound_refs,structure_ref,cues)
    	@searchable ws_subset reactions.[*].(name,abbreviation,md5,direction,thermoReversibility,status,defaultProtons,deltaG,abstractReaction_ref,cues,reagents.[*].(compound_ref,compartment_ref,coefficient,isCofactor))
    	@searchable ws_subset cues.[*].(id,name,abbreviation,formula,unchargedFormula,mass,defaultCharge,deltaG,smallMolecule,priority,structure_key,structure_type)
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
		
		mapping<compound_id,mapping<string,list<string>>> compound_aliases;
		mapping<reaction_id,mapping<string,list<string>>> reaction_aliases;
	} Biochemistry;
	
	/* 
    	ReactionSet object
    	
    	@searchable ws_subset id type
    */
	typedef structure {
		structure_id id;
		string type;
		string data;
	} CompoundStructure;
	
	/* 
    	BiochemistryStructures object
    	
    	@optional description name
    	@searchable ws_subset id name structures
    */
	typedef structure {
		biochemstruct_id id;
		string name;
		string description;
		list<CompoundStructure> structures;
	} BiochemistryStructures;
};
