/*
@id ws KBaseGenomes.Genome
*/
typedef string genome_ref;

typedef string domain_accession;

/*
genome_ref genome_ref - reference to genome
alignments - alignments of domain profile against region in feature sequence stored as 
        mapping from domain model reference to inner mapping from feature id to inner-inner 
        mapping from start position of alignment in feature sequence to aligned sequence of 
        domain occurrence (mapping<domain_accession, mapping<string feature_id,
                mapping<string start_in_feature, string alignment_with_profile>>>).
*/
typedef structure {
  genome_ref genome_ref;
  mapping<domain_accession, mapping<string, mapping<string, string>>> alignments;
} DomainAlignments;