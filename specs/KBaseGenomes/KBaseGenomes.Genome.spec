/*
KBase genome ID
@id kb
*/
typedef string Genome_id;

/*
ContigSet contig ID
@id external
*/
typedef string Contig_id;

typedef int Bool;

/*
Type spec for a "Contig" subobject in the "ContigSet" object

                Contig_id id - ID of contig in contigset
                string md5 - unique hash of contig sequence
                string sequence - sequence of the contig
                string description - Description of the contig (e.g. everything after the ID in a FASTA file)

                @optional length md5 genetic_code cell_compartment replicon_geometry replicon_type name description complete
*/
typedef structure {
  Contig_id id;
  int length;
  string md5;
  string sequence;
  int genetic_code;
  string cell_compartment;
  string replicon_type;
  string replicon_geometry;
  string name;
  string description;
  Bool complete;
} Contig;

/*
Reference to a source_id
@id external
*/
typedef string source_id;

/*
Structure for a publication (from ER API)
also want to capture authors, journal name (not in ER)
*/
typedef tuple<int, string, string, string, string, string, string> publication;

/*
Reference to a ContigSet object containing the contigs for this genome in the workspace
    @id ws KBaseGenomes.ContigSet
*/
typedef string ContigSet_ref;

/*
@optional frameshift_error_rate sequence_error_rate
*/
typedef structure {
  float frameshift_error_rate;
  float sequence_error_rate;
} Genome_quality_measure;

/*
@optional genome closeness_measure
*/
typedef structure {
  Genome_id genome;
  float closeness_measure;
} Close_genome;

typedef string Analysis_event_id;

/*
@optional tool_name execution_time parameters hostname
*/
typedef structure {
  Analysis_event_id id;
  string tool_name;
  float execution_time;
  list<string> parameters;
  string hostname;
} Analysis_event;

/*
Genome object holds much of the data relevant for a genome in KBase
        Genome publications should be papers about the genome, not
        papers about certain features of the genome (which go into the
        Feature object)
        Should the Genome object have a list of feature ids? (in
        addition to having a list of feature_refs)
        Should the Genome object contain a list of contig_ids too?

@optional quality close_genomes analysis_events features source_id source contigs contig_ids publications md5 taxonomy gc_content complete dna_size num_contigs contig_lengths contigset_ref
@metadata ws gc_content as GC content
@metadata ws taxonomy as Taxonomy
@metadata ws md5 as MD5
@metadata ws dna_size as Size
@metadata ws genetic_code as Genetic code
@metadata ws domain as Domain
    @metadata ws source_id as Source ID
    @metadata ws source as Source
    @metadata ws scientific_name as Name
    @metadata ws length(close_genomes) as Close genomes
    @metadata ws length(features) as Number features
    @metadata ws num_contigs as Number contigs
*/
typedef structure {
  Genome_id id;
  string scientific_name;
  string domain;
  int genetic_code;
  int dna_size;
  int num_contigs;
  list<Contig> contigs;
  list<int> contig_lengths;
  list<Contig_id> contig_ids;
  string source;
  source_id source_id;
  string md5;
  string taxonomy;
  float gc_content;
  int complete;
  list<publication> publications;
  list<#KBaseGenomes.Feature-2.1#> features;
  ContigSet_ref contigset_ref;
  Genome_quality_measure quality;
  list<Close_genome> close_genomes;
  list<Analysis_event> analysis_events;
} Genome;