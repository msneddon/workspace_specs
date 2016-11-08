/*
Information about a strain.
genetic_code - the genetic code of the strain.
    See http://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?mode=c
genus - the genus of the strain
species - the species of the strain
strain - the identifier for the strain
source - information about the source of the strain
organelle - the organelle of interest for the related data (e.g.
    mitochondria)
ncbi_taxid - the NCBI taxonomy ID of the strain
location - the location from which the strain was collected

@optional genetic_code source ncbi_taxid organelle location
*/
typedef structure {
  int genetic_code;
  string genus;
  string species;
  string strain;
  string organelle;
  #KBaseCommon.SourceInfo-1.0# source;
  int ncbi_taxid;
  #KBaseCommon.Location-1.0# location;
} StrainInfo;