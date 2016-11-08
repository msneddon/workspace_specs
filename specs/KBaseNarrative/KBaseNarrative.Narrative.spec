/*
This represents the IPython Notebook translated into a KBase Narrative typed object.
For the IPython-savvy, all of the KBase-specific additions are included as 
modifications to the metadata fields of the Narrative (was Notebook), Worksheet,
or Cell objects.
*/
typedef structure {
  int nbformat;
  int nbformat_minor;
  list<#KBaseNarrative.Cell-3.1#> cells;
  #KBaseNarrative.Metadata-3.0# metadata;
} Narrative;