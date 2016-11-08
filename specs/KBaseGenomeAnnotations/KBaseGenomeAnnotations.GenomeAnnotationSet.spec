/*
Reference to a taxon object 
    @id ws KBaseGenomeAnnotations.GenomeAnnotation
*/
typedef string genome_annotation_ref;

/*
The GenomeAnnotationSet object holds references to 1 or more GenomeAnnotations.  It can be used generically to hold multiple GenomeAnnotations.

genome_annotation_ref is a WS object reference.

@optional name description notes
*/
typedef structure {
  string genome_annotation_set_id;
  string name;
  string description;
  string notes;
  mapping<string, genome_annotation_ref> genome_annotations;
} GenomeAnnotationSet;