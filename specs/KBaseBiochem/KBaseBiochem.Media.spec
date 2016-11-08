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
@id subws KBCHEM.Biochemistry.compounds.[*].id
*/
typedef string compound_ref;

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