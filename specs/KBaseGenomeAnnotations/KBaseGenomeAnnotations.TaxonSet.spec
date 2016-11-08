/*
Reference to a taxon object 
    @id ws KBaseGenomeAnnotations.Taxon
*/
typedef string taxon_ref;

/*
The TaxonSet object holds references to 1 or more taxons.  It can be used generically to hold multiple taxons.
However the main usage will be to hold a list of children taxons.

taxon_ref is a WS object reference.

@optional name description notes
*/
typedef structure {
  string taxon_set_id;
  string name;
  string description;
  string notes;
  mapping<string, taxon_ref> taxons;
} TaxonSet;