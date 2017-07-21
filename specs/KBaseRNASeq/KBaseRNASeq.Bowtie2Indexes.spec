/*
Id for the handle object
@id handle
*/
typedef string HandleId;

/*
@optional hid file_name type url remote_md5 remote_sha1
*/
typedef structure {
  HandleId hid;
  string file_name;
  string id;
  string type;
  string url;
  string remote_md5;
  string remote_sha1;
} Handle;

/*
Id for an assembly or contigset
@id ws KBaseGenomes.ContigSet KBaseGenomeAnnotations.Assembly
*/
typedef string assembly_ref;

/*
@optional genome_scientific_name handle ftp_url assembly_ref
@metadata ws handle.file_name
@metadata ws handle.type
@metadata ws genome_id
@metadata ws genome_scientific_name
@metadata ws assembly_ref
*/
typedef structure {
  Handle handle;
  int size;
  string genome_id;
  string ftp_url;
  string genome_scientific_name;
  assembly_ref assembly_ref;
} Bowtie2Indexes;