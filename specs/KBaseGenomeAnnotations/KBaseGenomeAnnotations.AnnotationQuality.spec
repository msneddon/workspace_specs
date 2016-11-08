/*
The AnnotationQuality is an object that has details about the quality of and completeness of the annotation

@optional data_quality_warnings metadata_completeness_warnings
*/
typedef structure {
  float metadata_completeness;
  list<string> metadata_completeness_warnings;
  float data_quality;
  list<string> data_quality_warnings;
  int feature_types_present;
  int evidence_supported;
} AnnotationQuality;