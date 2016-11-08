/*
A workspace ID that references a Genome data object.
@id ws KBaseGenomes.Genome
*/
typedef string ws_genome_id;

/*
int inner_pos - position of gene name in inner genome (see dataN field in ProteomeComparison
int score - bit score of blast alignment multiplied by 100
int percent_of_best_score - best bit score of all hits connected to either of two genes from this hit
*/
typedef tuple<int, int, int> hit;

/*
string genome1ws - workspace of genome1 (depricated, use genome1ref instead)
string genome1id - id of genome1 (depricated, use genome1ref instead)
ws_genome_id genome1ref - reference to genome1
string genome2ws - workspace of genome2 (depricated, use genome2ref instead)
string genome2id - id of genome2 (depricated, use genome2ref instead)
ws_genome_id genome2ref - reference to genome2
float sub_bbh_percent - optional parameter, minimum percent of bit score compared to best bit score, default is 90
string max_evalue -  optional parameter, maximum evalue, default is 1e-10
list<string> proteome1names - names of genes of genome1
mapping<string, int> proteome1map - map from genes of genome1 to their positions
list<string> proteome2names - names of genes of genome2
mapping<string, int> proteome2map - map from genes of genome2 to their positions
list<list<hit>> data1 - outer list iterates over positions of genome1 gene names, inner list iterates over hits from given gene1 to genome2
list<list<hit>> data2 - outer list iterates over positions of genome2 gene names, inner list iterates over hits from given gene2 to genome1
@optional genome1ws
@optional genome1id
@optional genome1ref
@optional genome2ws
@optional genome2id
@optional genome2ref
*/
typedef structure {
  string genome1ws;
  string genome1id;
  ws_genome_id genome1ref;
  string genome2ws;
  string genome2id;
  ws_genome_id genome2ref;
  float sub_bbh_percent;
  string max_evalue;
  list<string> proteome1names;
  mapping<string, int> proteome1map;
  list<string> proteome2names;
  mapping<string, int> proteome2map;
  list<list<hit>> data1;
  list<list<hit>> data2;
} ProteomeComparison;