/*
An ID used for a piece of data at its source.
@id external
*/
typedef string source_id;

/*
An ID used for a project encompassing a piece of data at its source.
@id external
*/
typedef string project_id;

/*
Information about the source of a piece of data.
source - the name of the source (e.g. NCBI, JGI, Swiss-Prot)
source_id - the ID of the data at the source
project_id - the ID of a project encompassing the data at the source

@optional source source_id project_id
*/
typedef structure {
  string source;
  source_id source_id;
  project_id project_id;
} SourceInfo;