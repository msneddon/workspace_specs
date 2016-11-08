typedef int bool;

/*
@optional handle_2 insert_size_mean insert_size_std_dev interleaved read_orientation_outward
*/
typedef structure {
  #KBaseAssembly.Handle-1.0# handle_1;
  #KBaseAssembly.Handle-1.0# handle_2;
  float insert_size_mean;
  float insert_size_std_dev;
  bool interleaved;
  bool read_orientation_outward;
} PairedEndLibrary;