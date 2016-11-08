/*
A simple 2D matrix of floating point numbers with labels/ids for rows and
columns.  The matrix is stored as a list of lists, with the outer list
containing rows, and the inner lists containing values for each column of
that row.  Row/Col ids should be unique.

row_ids - unique ids for rows.
col_ids - unique ids for columns.
values - two dimensional array indexed as: values[row][col]
@metadata ws length(row_ids) as n_rows
@metadata ws length(col_ids) as n_cols
*/
typedef structure {
  list<string> row_ids;
  list<string> col_ids;
  list<list<float>> values;
} FloatMatrix2D;