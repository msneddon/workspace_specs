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
Reference to a taxon object 
    @id ws KBaseGenomeAnnotations.Taxon
*/
typedef string taxon_ref;

/*
Reference to an assembly object 
    @id ws KBaseGenomeAnnotations.Assembly
*/
typedef string assembly_ref;

/*
The GenomeAnnotationSummary is a hidden object that's purpose is to optimize landing page performance. 
This object needs to be generated every time a new version of the genome annotation is generated.
All fields are required.
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
  list<string> alias_sources;
  taxon_ref taxon_ref;
  assembly_ref assembly_ref;
  int cds_coding_for_proteins_count;
} GenomeAnnotationSummary;