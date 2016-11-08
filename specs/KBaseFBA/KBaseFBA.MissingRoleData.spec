/*
A string representing a ContigSet id.
*/
typedef string contigset_id;

/*
description of a role missing in the contigs
*/
typedef structure {
  string reaction_id;
  string reaction_name;
} ReactionItem;

typedef structure {
  string role_id;
  string role_description;
  string genome_hits;
  string blast_score;
  float perc_identity;
  string hit_location;
  string protein_sequence;
  list<ReactionItem> reactions;
} MissingRoleItem;

/*
KBase genome ID
@id kb
*/
typedef string genome_id;

typedef string genome_name;

/*
description of a close genome
*/
typedef structure {
  genome_id id;
  int hit_count;
  genome_name name;
} CloseGenomeItem;

/*
description of a role found in the contigs
*/
typedef structure {
  string role_id;
  string role_description;
} FoundRoleItem;

typedef structure {
  contigset_id contigset_id;
  list<MissingRoleItem> missing_roles;
  list<CloseGenomeItem> close_genomes;
  list<FoundRoleItem> found_roles;
} MissingRoleData;