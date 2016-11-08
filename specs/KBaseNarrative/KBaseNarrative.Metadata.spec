/*
Reference to any Workspace object that the Narrative is dependent on. 
These can be of any type.
@id ws
*/
typedef string dependency;

/*
A set of (mostly optional) metadata that needs to be included as part of the 
Narrative object. The data_dependencies list is required, but can be empty.
@optional creator
@optional format
@optional name
@optional type
@optional ws_name
*/
typedef structure {
  string description;
  list<dependency> data_dependencies;
  string creator;
  string format;
  string name;
  string type;
  string ws_name;
} Metadata;