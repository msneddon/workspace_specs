/*
Reference to an assembly object 
    @id ws KBaseGenomeAnnotations.Assembly
*/
typedef string assembly_ref;

/*
Structure for a publication (from ER API)
also want to capture authors, journal name (not in ER)
*/
typedef tuple<int, string, string, string, string, string, string> publication;

/*
Reference to an EvidenceContainer object 
    @id ws KBaseGenomeAnnotations.EvidenceContainer
*/
typedef string evidence_container_ref;

/*
Reference to an ProteinContainer object 
    @id ws KBaseGenomeAnnotations.ProteinContainer
*/
typedef string protein_container_ref;

/*
@optional EC_Number associated_mRNA parent_gene codes_for_protein_ref

NOTE THAT associated_mRNA feature type is there so you go up to the GenomeAnnotation object and pull its mRNA info from the feature_containers_map
Same thing for the parent gene.
This design choice was made because of the chicken and egg scenario between CDS, mRNA and Gene
*/
typedef structure {
  tuple<protein_container_ref, string> codes_for_protein_ref;
  string EC_Number;
  tuple<string, string> associated_mRNA;
  tuple<string, string> parent_gene;
} CDS_properties;

/*
@optional associated_CDS parent_gene

NOTE THAT associated_CDS feature type is there so you go up to the GenomeAnnotation object and pull its CDS info from the feature_containers_map
Same thing for the parent gene.
This design choice was made because of the chicken and egg scenario between CDS, mRNA and Gene
*/
typedef structure {
  tuple<string, string> associated_CDS;
  tuple<string, string> parent_gene;
} mRNA_properties;

/*
@optional children_CDS children_mRNA

NOTE THAT Children * feature type is there so you go up to the GenomeAnnotation object and pull its mRNA info from the feature_containers_map
Same thing for the parent gene.
This design choice was made because of the chicken and egg scenario between CDS, mRNA and Gene
*/
typedef structure {
  list<tuple<string, string>> children_CDS;
  list<tuple<string, string>> children_mRNA;
} gene_properties;

/*
Key is the key from the file
Value is the value of the file.  
This is a catch all for keys that do not directly map to an object field.  
Downside, no API methods will know the keys and how tooperate on them.
*/
typedef mapping<string, string> additional_properties_map;

/*
Feature is a individual feature of the Genome annotation (Ex: a CDS, a promoter, etc)
It has specific subobjects for particular feature types. (ex: CDS, mRNA, gene, operon, pathway) 
This is expandable in the future to include more specific properties for more types.
 
For quality_warnings do we want severity (warnings, errors)?

Do all features have coordinates? Shuffleons do and do not Genbank has a mobile_element_type feature type.
Do we want to try and capture motifs. Orthologs? Orthologs get a little tricky in terms of multiple annotations for the same genome and taxonomy.

evidence_container_ref is a workspace reference.  The list of strings is ids into EvidenceContainer mapping.
 
@optional function aliases publications notes inference feature_quality evidences 
@optional CDS_properties mRNA_properties gene_properties additional_properties trans_splicing
*/
typedef structure {
  string feature_id;
  list<tuple<string, int, string, int>> locations;
  string type;
  string function;
  string md5;
  string dna_sequence;
  int dna_sequence_length;
  list<publication> publications;
  mapping<string, list<string>> aliases;
  string notes;
  string inference;
  float feature_quality;
  list<string> quality_warnings;
  tuple<evidence_container_ref, list<string>> evidences;
  CDS_properties CDS_properties;
  mRNA_properties mRNA_properties;
  gene_properties gene_properties;
  additional_properties_map additional_properties;
  int trans_splicing;
} feature;

/*
A feature_conatainer is a set a features.  Typically this would be used to group annotations of the same type that are associated with the same genome annotation.
Technically it can support a bunch of features of different types from different genome_annotations.

The feature type is a controlled vocabulary perhaps derived from http://www.insdc.org/files/feature_table.html#7.2
type would be controlled vocabulary - Ex: CDS, etc.

Note this structure allows for flexible sets.  
So type may not be required or a "mixed" type may need to be introduced into the controlled vocabulary.(assuming mixed for now)
However it is a requirement that all the features within the container must be referencing the same assembly.

@optional name description notes
*/
typedef structure {
  string feature_container_id;
  string type;
  string name;
  string description;
  string notes;
  assembly_ref assembly_ref;
  mapping<string, feature> features;
} FeatureContainer;