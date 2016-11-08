typedef string domain_library_id;

/*
enum: CDD, SMART, Pfam, etc
*/
typedef string domain_source;

/*
date in ISO 8601 format; e.g., 2014-11-26
*/
typedef string date;

/*
enum: hmmscan-3.1b1, rpsblast-2.2.30
*/
typedef string program_version;

typedef structure {
  string file_name;
  string shock_id;
} Handle;

typedef string domain_accession;

/*
enum: PSSM, HMM-Family, HMM-Domain, HMM-Repeat, HMM-Motif
*/
typedef string model_type;

/*
accession - accession of domain model (e.g., PF00244.1, or COG0001)
cdd_id - (optional) in case of CDD it's inner id which is reported by rps-blast program
name - name of domain model
description - description of domain model
length - length of profile
model_type - domain model type
trusted_cutoff - (optional) trusted cutoff of domain model for HMM libraries
@optional cdd_id trusted_cutoff
*/
typedef structure {
  domain_accession accession;
  string cdd_id;
  string name;
  string description;
  int length;
  model_type model_type;
  float trusted_cutoff;
} DomainModel;

/*
id - id of library
source - source of library (e.g., Cog, Pfam, ...)
source_url - ftp/http url where library can be downloaded 
version - version of library release
release_date - release date of library
program - program for running domain search
domain_prefix - prefix of domain accession defining library
dbxref_prefix - url prefix for db-external referencing
library_files - library files stored in Shock storage
domains - domain information
*/
typedef structure {
  domain_library_id id;
  domain_source source;
  string source_url;
  string version;
  date release_date;
  program_version program;
  string domain_prefix;
  string dbxref_prefix;
  list<Handle> library_files;
  mapping<domain_accession, DomainModel> domains;
} DomainLibrary;