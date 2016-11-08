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
Genome feature ID
@id external
*/
typedef string Feature_id;

typedef string Feature_type;

/*
Structure for a protein family
        @optional query_begin query_end subject_begin subject_end score evalue subject_description release_version
*/
typedef structure {
  string id;
  string subject_db;
  string release_version;
  string subject_description;
  int query_begin;
  int query_end;
  int subject_begin;
  int subject_end;
  float score;
  float evalue;
} ProteinFamily;

/*
a notation by a curator of the genome object
*/
typedef tuple<string, string, int> annotation;

/*
Structure for subsystem data (from CDMI API)
*/
typedef tuple<string, string, string> subsystem_data;

/*
Structure for regulon data (from CDMI API)
*/
typedef tuple<string, list<Feature_id>, list<Feature_id>> regulon_data;

/*
Structure for an atomic regulon (from CDMI API)
*/
typedef tuple<string, int> atomic_regulon;

/*
Structure for coexpressed fids (from CDMI API)
*/
typedef tuple<Feature_id, float> coexpressed_fid;

/*
Structure for co-occurring fids (from CDMI API)
*/
typedef tuple<Feature_id, float> co_occurring_fid;

/*
@optional weighted_hit_count hit_count existence_priority overlap_rules pyrrolysylprotein truncated_begin truncated_end existence_confidence frameshifted selenoprotein
*/
typedef structure {
  Bool truncated_begin;
  Bool truncated_end;
  float existence_confidence;
  Bool frameshifted;
  Bool selenoprotein;
  Bool pyrrolysylprotein;
  list<string> overlap_rules;
  float existence_priority;
  float hit_count;
  float weighted_hit_count;
} Feature_quality_measure;

typedef string Analysis_event_id;

/*
Structure for a single feature of a genome
    
    Should genome_id contain the genome_id in the Genome object,
    the workspace id of the Genome object, a genomeref,
    something else?
    Should sequence be in separate objects too?
    We may want to add additional fields for other CDM functions
    (e.g., atomic regulons, coexpressed fids, co_occurring fids,...)

    @optional orthologs quality feature_creation_event md5 location function protein_translation protein_families subsystems publications subsystem_data aliases annotations regulon_data atomic_regulons coexpressed_fids co_occurring_fids dna_sequence protein_translation_length dna_sequence_length
*/
typedef structure {
  Feature_id id;
  list<tuple<Contig_id, int, string, int>> location;
  Feature_type type;
  string function;
  string md5;
  string protein_translation;
  string dna_sequence;
  int protein_translation_length;
  int dna_sequence_length;
  list<publication> publications;
  list<string> subsystems;
  list<ProteinFamily> protein_families;
  list<string> aliases;
  list<tuple<string, float>> orthologs;
  list<annotation> annotations;
  list<subsystem_data> subsystem_data;
  list<regulon_data> regulon_data;
  list<atomic_regulon> atomic_regulons;
  list<coexpressed_fid> coexpressed_fids;
  list<co_occurring_fid> co_occurring_fids;
  Feature_quality_measure quality;
  Analysis_event_id feature_creation_event;
} Feature;

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
@searchable ws_subset taxonomy num_contigs source_id source genetic_code id scientific_name domain contigset_ref
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
  list<Feature> features;
  ContigSet_ref contigset_ref;
  Genome_quality_measure quality;
  list<Close_genome> close_genomes;
  list<Analysis_event> analysis_events;
} Genome;