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
Reference to a compound object in a biochemistry
@id subws KBaseBiochem.Media.mediacompounds.[*].id
*/
typedef string mediacompound_ref;

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
  mapping<mediacompound_ref, int> associated_compounds;
} MediaReagent;

/*
Reference to a compound object in a biochemistry
@id subws KBaseBiochem.Biochemistry.compounds.[*].id
*/
typedef string compound_ref;

/*
MediaCompound object
*/
typedef structure {
  compound_ref compound_ref;
  float concentration;
  float maxFlux;
  float minFlux;
} MediaCompound;

/*
Media object

@optional reagents atmosphere_addition atmosphere temperature pH_data isAerobic protocol_link source source_id
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