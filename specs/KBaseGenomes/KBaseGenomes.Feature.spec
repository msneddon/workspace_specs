/*
KBase Feature ID
@id external
*/
typedef string Feature_id;

/*
ContigSet contig ID
@id external
*/
typedef string Contig_id;

/*
@optional translation_provenance alignment_evidence
*/
typedef structure {
  string method;
  string method_version;
  string timestamp;
  tuple<string, string, string> translation_provenance;
  list<tuple<int, int, int, float>> alignment_evidence;
} OntologyEvidence;

typedef structure {
  string id;
  string ontology_ref;
  list<string> term_lineage;
  string term_name;
  list<OntologyEvidence> evidence;
} OntologyData;

/*
KBase CDS ID
@id external
*/
typedef string cds_id;

/*
KBase mRNA ID
@id external
*/
typedef string mrna_id;

/*
Structure for a publication (from ER API)
also want to capture authors, journal name (not in ER)
*/
typedef tuple<int, string, string, string, string, string, string> publication;

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
typedef tuple<string, string, float> annotation;

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

typedef int Bool;

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
Structure for a single feature of a genome
    
    Should genome_id contain the genome_id in the Genome object,
    the workspace id of the Genome object, a genomeref,
    something else?
    Should sequence be in separate objects too?
    We may want to add additional fields for other CDM functions
    (e.g., atomic regulons, coexpressed fids, co_occurring fids,...)

    @optional cdss mrnas orthologs quality feature_creation_event md5 location function ontology_terms protein_translation protein_families subsystems publications subsystem_data aliases annotations regulon_data atomic_regulons coexpressed_fids co_occurring_fids dna_sequence protein_translation_length dna_sequence_length
*/
typedef structure {
  Feature_id id;
  list<tuple<Contig_id, int, string, int>> location;
  string type;
  string function;
  mapping<string, mapping<string, OntologyData>> ontology_terms;
  string md5;
  string protein_translation;
  list<cds_id> cdss;
  list<mrna_id> mrnas;
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
  Analysis_event feature_creation_event;
} Feature;