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
@metadata ws assembly_ref
@metadata ws handle.hid
@metadata ws handle.id
@metadata ws handle.remote_md5
@metadata ws handle.remote_sha1
*/
typedef structure {
  Handle handle;
  assembly_ref assembly_ref;
} Bowtie2IndexV2;