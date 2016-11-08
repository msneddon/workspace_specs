/*
Reference to metabolic model
@id ws KBaseFBA.FBAModel
*/
typedef string fbamodel_ref;

/*
This type represents an element of a FBAModelSet.
@optional metadata
*/
typedef structure {
  mapping<string, string> metadata;
  fbamodel_ref ref;
} FBAModelSetElement;

/*
A type describing a set of FBAModels, where each element of the set 
is an FBAModel object reference.
*/
typedef structure {
  string description;
  mapping<string, FBAModelSetElement> elements;
} FBAModelSet;