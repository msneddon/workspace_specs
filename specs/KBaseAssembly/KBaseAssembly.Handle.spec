/*
@id handle
*/
typedef string handle_id;

/*
Note: the underlying data will not be shared correctly in the Workspace unless
the hid field is properly set.
@optional hid file_name type url remote_md5 remote_sha1
*/
typedef structure {
  handle_id hid;
  string file_name;
  string id;
  string type;
  string url;
  string remote_md5;
  string remote_sha1;
} Handle;