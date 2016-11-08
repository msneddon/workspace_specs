/*
@id ws KBaseGeneFamilies.DomainLibrary
*/
typedef string ws_lib_id;

typedef string domain_accession;

/*
string set_name - name of model set
*/
typedef structure {
  string set_name;
  mapping<string, ws_lib_id> domain_libs;
  mapping<string, string> domain_prefix_to_dbxref_url;
  mapping<domain_accession, string> domain_accession_to_description;
} DomainModelSet;