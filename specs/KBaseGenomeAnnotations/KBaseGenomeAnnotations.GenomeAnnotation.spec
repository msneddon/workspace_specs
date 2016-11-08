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
Reference to an Annotation quality object 
    @id ws KBaseGenomeAnnotations.AnnotationQuality
*/
typedef string annotation_quality_ref;

/*
Structure for a publication (from ER API)
also want to capture authors, journal name (not in ER)
*/
typedef tuple<int, string, string, string, string, string, string> publication;

/*
Reference to an FeatureContainer object 
    @id ws KBaseGenomeAnnotations.FeatureContainer
*/
typedef string feature_container_ref;

/*
feature_container_ref is a versioned workspace reference
The feature type is a controlled vocabulary perhaps derived from http://www.insdc.org/files/feature_table.html#7.2
*/
typedef mapping<string, feature_container_ref> feature_containers_map;

/*
Reference to an ProteinContainer object 
    @id ws KBaseGenomeAnnotations.ProteinContainer
*/
typedef string protein_container_ref;

/*
Reference to an EvidenceContainer object 
    @id ws KBaseGenomeAnnotations.EvidenceContainer
*/
typedef string evidence_container_ref;

/*
Feature lookup is way to look up a feature within a GenomeAnnotation.
Able to lookup by id or alias
 
note feature key could be id or alias. Allows for fast lookup of any feature by id or alias.  

feature_container_ref is a WS reference
*/
typedef mapping<string, list<tuple<feature_container_ref, string>>> feature_lookup;

/*
The type is either a feature type or "protein". 
This is designed for fast count lookup of all the types instead of having to drill down into the containers
*/
typedef mapping<string, int> counts_map;

/*
Reference to a SeedRoles object
    @id ws KBaseGenomeAnnotations.SeedRoles
*/
typedef string seed_roles_ref;

/*
Reference to a handle to the Genbank file on shock
    @id handle
*/
typedef string genbank_handle_ref;

/*
Reference to a handle to the GFF file on shock 
    @id handle
*/
typedef string gff_handle_ref;

/*
The key is alias source.
This is designed for fast count lookup of all the allias sources instead of having to drill down into the containers
*/
typedef mapping<string, int> alias_source_counts_map;

/*
The key is interfeature relationship.
This is designed for fast count lookup of all the interfeature relationships. instead of having to drill down into the containers
*/
typedef mapping<string, int> interfeature_relationship_counts_map;

/*
The GenomeAnnotation is the core central object. It is the annotation of a given organism and assembly.

location and environment information (perhaps separate fields for latitude, longitude, altitude)(perhaps we need a MixS object)

quality_score could be in genome_annotation_quality_detail instead

methodology - Not sure if needed? example would be rast

type -refers to representative, reference, user, etc

display_sc_name is the scientific_name for display purposes only.  Should go through taxon object for accurate information. as scientific names can change.

taxon_ref is a versioned workspace reference
annotation_quality_ref is a versioned workspace reference
evidence_container_ref would be a versioned workspace reference 
protein_container_ref would be a versioned workspace reference
assembly_ref would be a versioned workspace reference

genbank_handle_ref are handle service references to shock.

@metadata ws display_sc_name as Name
@metadata ws external_source as Source
@metadata ws release as Release
@metadata ws original_source_file_name as Source_File_Name

@optional external_source external_source_id external_source_origination_date notes environmental_comments quality_score 
@optional annotation_quality_ref publications evidence_container_ref methodology seed_roles_ref genbank_handle_ref gff_handle_ref
@optional alias_source_counts_map interfeature_relationship_counts_map release original_source_file_name
*/
typedef structure {
  string genome_annotation_id;
  string display_sc_name;
  string external_source;
  string external_source_id;
  string external_source_origination_date;
  string release;
  string original_source_file_name;
  string notes;
  string environmental_comments;
  taxon_ref taxon_ref;
  assembly_ref assembly_ref;
  int reference_annotation;
  float quality_score;
  annotation_quality_ref annotation_quality_ref;
  list<publication> publications;
  feature_containers_map feature_container_references;
  protein_container_ref protein_container_ref;
  evidence_container_ref evidence_container_ref;
  feature_lookup feature_lookup;
  string methodology;
  counts_map counts_map;
  seed_roles_ref seed_roles_ref;
  string type;
  genbank_handle_ref genbank_handle_ref;
  gff_handle_ref gff_handle_ref;
  alias_source_counts_map alias_source_counts_map;
  interfeature_relationship_counts_map interfeature_relationship_counts_map;
} GenomeAnnotation;