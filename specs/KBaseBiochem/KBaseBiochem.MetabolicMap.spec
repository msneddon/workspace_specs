/*
Metabolic map ID
@id external
*/
typedef string map_id;

typedef int bool;

/*
Reference to a compound object in a metabolic map
@id subws KBaseBiochem.MetabolicMap.compounds.[*].id
*/
typedef string mapcompound_ref;

/*
MapReaction object

@optional link
*/
typedef structure {
  string id;
  bool reversible;
  string name;
  string ec;
  string shape;
  string link;
  int h;
  int w;
  int y;
  int x;
  list<string> rxns;
  list<mapcompound_ref> substrate_refs;
  list<mapcompound_ref> product_refs;
} MapReaction;

/*
Reference to a compound object in a metabolic map
@id subws KBaseBiochem.MetabolicMap.linkedmaps.[*].id
*/
typedef string maplink_ref;

/*
MapCompound object

@optional link
*/
typedef structure {
  string id;
  string name;
  string ec;
  string shape;
  string link;
  int h;
  int w;
  int y;
  int x;
  list<string> cpds;
  list<maplink_ref> link_refs;
} MapCompound;

/*
Reference to a metabolic map
@id ws KBaseBiochem.MetabolicMap
*/
typedef string map_ref;

/*
MapLink object

@optional link
*/
typedef structure {
  string id;
  map_ref map_ref;
  string name;
  string shape;
  string link;
  int h;
  int w;
  int y;
  int x;
  map_id map_id;
} MapLink;

/*
MetabolicMap object

@optional description link
@searchable ws_subset id id name source_id source reaction_ids compound_ids
*/
typedef structure {
  map_id id;
  string name;
  string source_id;
  string source;
  string link;
  string description;
  list<string> reaction_ids;
  list<string> compound_ids;
  list<MapReaction> reactions;
  list<MapCompound> compounds;
  list<MapLink> linkedmaps;
} MetabolicMap;