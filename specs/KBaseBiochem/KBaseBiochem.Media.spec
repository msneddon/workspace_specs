/*
Media ID
@id kb
*/
typedef string media_id;

/*
Source ID
@id external
*/
typedef string source_id;

typedef int bool;

/*
MediaReagent object

@optional molecular_weight concentration_units concentration associated_compounds
*/
typedef structure {
  string id;
  string name;
  float concentration;
  string concentration_units;
  float molecular_weight;
  mapping<string, float> associated_compounds;
} MediaReagent;

/*
Reference to a compound object in a biochemistry
@id subws KBaseBiochem.Biochemistry.compounds.[*].id
*/
typedef string compound_ref;

/*
MediaCompound object

@optional id name smiles inchikey
*/
typedef structure {
  compound_ref compound_ref;
  string id;
  string name;
  string smiles;
  string inchikey;
  float concentration;
  float maxFlux;
  float minFlux;
} MediaCompound;

/*
Media object

@optional reagents atmosphere_addition atmosphere temperature pH_data isAerobic protocol_link source source_id         
    @metadata ws source_id as Source ID
    @metadata ws source as Source
    @metadata ws name as Name
    @metadata ws temperature as Temperature
    @metadata ws isAerobic as Is Aerobic
    @metadata ws isMinimal as Is Minimal
    @metadata ws isDefined as Is Defined
    @metadata ws length(mediacompounds) as Number compounds
*/
typedef structure {
  media_id id;
  string name;
  source_id source_id;
  string source;
  string protocol_link;
  bool isDefined;
  bool isMinimal;
  bool isAerobic;
  string type;
  string pH_data;
  float temperature;
  string atmosphere;
  string atmosphere_addition;
  list<MediaReagent> reagents;
  list<MediaCompound> mediacompounds;
} Media;