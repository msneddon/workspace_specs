/*
Reference to an GenomeAnnotation object 
    @id ws KBaseGenomeAnnotations.GenomeAnnotation
*/
typedef string genome_annotation_ref;

/*
The type is either a feature type or "protein". 
This is designed for fast count lookup of all the types instead of having to drill down into the containers
*/
typedef mapping<string, int> counts_map;

/*
The GenomeAnnotationSummary is a hidden object that's purpose is to optimize landing page performance. 
This object needs to be generated every time a new version of the genome annotation is generated.
dropped alias_source_counts_map for now

@optional organism_aliases genetic_code scientific_lineage assembly_source assembly_source_id assembly_source_origination_date
@optional external_source external_source_origination_date original_source_file_name
*/
typedef structure {
  genome_annotation_ref genome_annotation_ref;
  string scientific_name;
  int taxonomy_id;
  string kingdom;
  string scientific_lineage;
  int genetic_code;
  list<string> organism_aliases;
  string assembly_source;
  string assembly_source_id;
  string assembly_source_origination_date;
  float gc_content;
  int dna_size;
  int num_contigs;
  list<string> contig_ids;
  string external_source;
  string external_source_origination_date;
  string release;
  string original_source_file_name;
  counts_map feature_counts_map;
} GenomeAnnotationSummary;