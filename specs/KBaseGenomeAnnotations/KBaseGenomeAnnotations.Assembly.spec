/*
Reference to a handle to the Reads file on shock
    @id handle
*/
typedef string reads_handle_ref;

/*
Reference to a handle to the Assembly Fasta file on shock
    @id handle
*/
typedef string fasta_handle_ref;

/*
The Contig is an individual contiguous sequence.
This is the result of an assembly, it can be complete (ex: full chromosome or circular DNA), it can also be partial
due to the limitations of the assembly itself.

is_complete - is an indication of complete chromosome, plasmid, etc.

is_circular - True, False and Unknown are viable values, could make an int(bool). If field not present viewed as unknown.

@optional name description is_complete
*/
typedef structure {
  string contig_id;
  int length;
  string md5;
  string name;
  string description;
  int is_complete;
  string is_circular;
  int start_position;
  int num_bytes;
  float gc_content;
  int Ncount;
} contig;

/*
Reference to a taxon object 
    @id ws KBaseGenomeAnnotations.Taxon
*/
typedef string taxon_ref;

/*
The Assembly object contains the information about an Assembly of Reads. The sequence data for this would be stored within a shock node.
The assembly itself is a collection of Contig subobjects.

Type is a controlled vocabulary.  Example Finished, Draft.

reads_handle_ref and fasta_handle_ref are handle service references to shock.

assembly_stats assembly_stats; - should be in there, but needs to be flushed out by Fang Fang

@metadata ws gc_content as GC content
@metadata ws md5 as MD5
@metadata ws name as Name
@metadata ws dna_size as Size

@optional name external_source external_source_id external_source_origination_date reads_handle_ref notes taxon_ref
*/
typedef structure {
  string assembly_id;
  string name;
  string md5;
  string external_source;
  string external_source_id;
  string external_source_origination_date;
  float gc_content;
  string type;
  reads_handle_ref reads_handle_ref;
  fasta_handle_ref fasta_handle_ref;
  mapping<string, contig> contigs;
  int dna_size;
  int num_contigs;
  string notes;
  taxon_ref taxon_ref;
  mapping<string, int> base_counts;
} Assembly;