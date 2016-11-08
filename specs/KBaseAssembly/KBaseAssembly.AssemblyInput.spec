/*
@optional paired_end_libs single_end_libs references expected_coverage expected_coverage estimated_genome_size dataset_prefix dataset_description
*/
typedef structure {
  list<#KBaseAssembly.PairedEndLibrary-1.0#> paired_end_libs;
  list<#KBaseAssembly.SingleEndLibrary-1.0#> single_end_libs;
  list<#KBaseAssembly.ReferenceAssembly-1.0#> references;
  float expected_coverage;
  int estimated_genome_size;
  string dataset_prefix;
  string dataset_description;
} AssemblyInput;