/*
Reference to a media object
@id ws KBaseBiochem.Media
*/
typedef string media_ref;

typedef structure {
  mapping<string, string> string_metadata;
  mapping<string, float> numerial_metadata;
  media_ref ref;
} MediaSetElement;

/*
Media set object
*/
typedef structure {
  string description;
  list<MediaSetElement> elements;
} MediaSet;