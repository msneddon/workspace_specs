/*
KBase contig set ID
@id kb
*/
typedef string ContigSet_id;

/*
Reference to a source_id
@id external
*/
typedef string source_id;

/*
Reference to a reads file in shock
@id shock
*/
typedef string Reads_ref;

/*
Reference to a fasta file in shock
@id shock
*/
typedef string Fasta_ref;

/*
ContigSet contig ID
@id external
*/
typedef string Contig_id;

/*
Type spec for a "Contig" subobject in the "ContigSet" object

                Contig_id id - ID of contig in contigset
                string md5 - unique hash of contig sequence
                string sequence - sequence of the contig
                string description - Description of the contig (e.g. everything after the ID in a FASTA file)

                @optional length name description
                @searchable ws_subset id md5
*/
typedef structure {
  Contig_id id;
  int length;
  string md5;
  string sequence;
  string name;
  string description;
} Contig;

/*
Type spec for the "ContigSet" object

                contigset_id id - unique kbase ID of the contig set
                string name - name of the contig set
                string type - type of the contig set (values are: Genome,Transcripts,Environment,Collection)
                source_id source_id - source ID of the contig set
                string source - source of the contig set
                list<Contig> contigs - list of contigs in the contig set
                reads_ref reads_ref - reference to the shocknode with the rawreads from which contigs were assembled
                fasta_ref fasta_ref - reference to fasta file from which contig set were read

                @optional name type reads_ref fasta_ref
            @searchable ws_subset contigs.[*].(id,md5) md5 id name source_id source type
*/
typedef structure {
  ContigSet_id id;
  string name;
  string md5;
  source_id source_id;
  string source;
  string type;
  Reads_ref reads_ref;
  Fasta_ref fasta_ref;
  list<Contig> contigs;
} ContigSet;