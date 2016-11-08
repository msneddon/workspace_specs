/*
The TaxonLookup holds first three letters of the scientific names as top level key.  Value is a mapping of scientific name or taxon aliases as the key, and the value is the taxonomy id.  This is populated by the names.dmp file from NCBI.
*/
typedef structure {
  mapping<string, mapping<string, string>> taxon_lookup;
} TaxonLookup;