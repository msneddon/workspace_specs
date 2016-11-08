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
reference genome id for mapping the RNA-Seq fastq file
@id ws KBaseGenomes.Genome
*/
typedef string ws_genome_id;

/*
@optional genome_id genome_scientific_name handle ftp_url
@metadata ws handle.file_name
@metadata ws handle.type
@metadata ws genome_id
@metadata ws genome_scientific_name
*/
typedef structure {
  Handle handle;
  int size;
  ws_genome_id genome_id;
  string ftp_url;
  string genome_scientific_name;
} Bowtie2Indexes;