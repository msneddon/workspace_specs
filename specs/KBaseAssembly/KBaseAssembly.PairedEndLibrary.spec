typedef int bool;

/*
@optional handle_2 insert_size_mean insert_size_std_dev interleaved read_orientation_outward
@metadata ws handle_1.file_name
@metadata ws handle_1.type
@metadata ws handle_2.file_name
@metadata ws handle_2.type
@metadata ws insert_size_mean
@metadata ws insert_size_std_dev
@metadata ws interleaved
@metadata ws read_orientation_outward
*/
typedef structure {
  #KBaseAssembly.Handle-2.0# handle_1;
  #KBaseAssembly.Handle-2.0# handle_2;
  float insert_size_mean;
  float insert_size_std_dev;
  bool interleaved;
  bool read_orientation_outward;
} PairedEndLibrary;