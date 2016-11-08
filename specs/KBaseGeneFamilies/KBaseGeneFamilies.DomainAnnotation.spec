/*
@id ws KBaseGenomes.Genome
*/
typedef string genome_ref;

typedef string contig_id;

typedef string domain_accession;

typedef tuple<int, int, float, float, float> domain_place;

typedef tuple<string, int, int, int, mapping<domain_accession, list<domain_place>>> annotation_element;

/*
@id ws KBaseGeneFamilies.DomainAlignments
*/
typedef string domain_alignments_ref;

/*
genome_ref genome_ref - reference to genome
mapping<contig_id, list<annotation_element>> data - 
        list of entrances of different domains into proteins of annotated genome
        (annotation_element -> typedef tuple<string feature_id,int feature_start,int feature_stop,
                int feature_dir,mapping<domain_accession,list<domain_place>>>;
        domain_place -> tuple<int start_in_feature,int stop_in_feature,float evalue,
                float bitscore,float domain_coverage>).
mapping<contig_id, tuple<int size,int features>> contig_to_size_and_feature_count - 
        feature count and nucleotide size of every contig
mapping<string feature_id, tuple<contig_id,int feature_index> feature_to_contig_and_index - 
        index of every feature in feature list in every contig
domain_alignments_ref alignments_ref - reference to alignments of protein sequences against 
        domain profiles
@optional alignments_ref
*/
typedef structure {
  genome_ref genome_ref;
  mapping<contig_id, list<annotation_element>> data;
  mapping<contig_id, tuple<int, int>> contig_to_size_and_feature_count;
  mapping<string, tuple<contig_id, int>> feature_to_contig_and_index;
  domain_alignments_ref alignments_ref;
} DomainAnnotation;