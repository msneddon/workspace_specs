/*
Structure for the "MetagenomeAnnotationOTUFunction" object

list<string> reference_genes - list of genes associated with hit
string functional_role - annotated function
string kbid - kbase ID of OTU function in metagenome
int abundance - number of hits with associated role and OTU
float confidence - confidence of functional role hit
string confidence_type - type of functional role hit

            @searchable ws_subset id abundance confidence functional_role
*/
typedef structure {
  string id;
  list<string> reference_genes;
  string functional_role;
  int abundance;
  float confidence;
} MetagenomeAnnotationOTUFunction;

/*
Structure for the "MetagenomeAnnotationOTU" object

        string name - name of metagenome OTU
        string kbid - KBase ID of OTU of metagenome object
        string source_id - ID used for OTU in metagenome source
        string source - source OTU ID
        list<MetagenomeAnnotationOTUFunction> functions - list of functions in OTU

    @searchable ws_subset id name source_id source functions.[*].(id,abundance,confidence,functional_role)
*/
typedef structure {
  float ave_confidence;
  float ave_coverage;
  string id;
  string name;
  string source_id;
  string source;
  list<MetagenomeAnnotationOTUFunction> functions;
} MetagenomeAnnotationOTU;

/*
Structure for the "MetagenomeAnnotation" object

        string type - type of metagenome object
        string name - name of metagenome object
        string kbid - KBase ID of metagenome object
        string source_id - ID used in metagenome source
        string source - source of metagenome data
        string confidence_type - type of confidence score
        list<MetagenomeAnnotationOTU> otus - list of otus in metagenome
        
    @searchable ws_subset type name id source_id source confidence_type otus.[*].(id,name,source_id,source,functions.[*].(id,abundance,confidence,functional_role))
        @metadata ws type as Type
        @metadata ws name as Name
        @metadata ws source_id as Source ID
        @metadata ws source as Source
        @metadata ws length(otus) as Number OTUs
*/
typedef structure {
  string type;
  string name;
  string id;
  string source_id;
  string source;
  string confidence_type;
  list<MetagenomeAnnotationOTU> otus;
} MetagenomeAnnotation;