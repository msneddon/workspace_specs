/*
###  KBaseTrees.ConcatMSA KBaseTrees.MS
        @id ws KBaseTrees.MSA
*/
typedef string ws_alignment_id;

/*
Type for MSA collection element. There could be mutual exclusively 
defined either ref or data field.
@optional metadata
@optional ref
@optional data
*/
typedef structure {
  mapping<string, string> metadata;
  ws_alignment_id ref;
  #KBaseTrees.MSA-1.0# data;
} MSASetElement;

/*
Type for collection of MSA objects.
*/
typedef structure {
  string description;
  list<MSASetElement> elements;
} MSASet;