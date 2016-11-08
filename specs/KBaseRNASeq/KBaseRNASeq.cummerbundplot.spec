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
Object for the cummerbund plot
@optional png_json_handle plot_title plot_description
*/
typedef structure {
  Handle png_handle;
  Handle png_json_handle;
  string plot_title;
  string plot_description;
} cummerbundplot;