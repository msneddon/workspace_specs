/*
Note: will probably need a 'next' DataPalette object, otherwise
max size of palette is 40k refs or something like that.
@metadata ws length(data) as n
*/
typedef structure {
  list<#DataPalette.DataReference-1.0#> data;
} DataPalette;