/*
A handle id from the Handle Service for a shock node.
@id handle
*/
typedef string handle_id;

/*
A handle for a file stored in Shock.
hid - the id of the handle in the Handle Service that references this
   shock node
id - the id for the shock node
url - the url of the shock server
type - the type of the handle. This should always be ‘shock’.
file_name - the name of the file
remote_md5 - the md5 digest of the file.
remote_sha1 - the sha1 digest of the file.
    
@optional file_name remote_md5 remote_sha1
*/
typedef structure {
  handle_id hid;
  string file_name;
  string id;
  string url;
  string type;
  string remote_md5;
  string remote_sha1;
} Handle;

/*
A reference to a file stored in Shock.
file - the location of and information about a file stored in Shock
encoding - the encoding of the file (e.g. UTF8)
type - the file type (e.g. XML, FASTA, GFF)
size - the file size in bytes.
description - a description of the file

@optional description
@meta ws encoding
@meta ws name
@meta ws description
@meta ws size
@meta ws type
*/
typedef structure {
  Handle file;
  string encoding;
  string type;
  int size;
  string description;
} FileRef;