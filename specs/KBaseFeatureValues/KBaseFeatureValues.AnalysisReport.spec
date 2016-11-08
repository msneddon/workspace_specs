/*
Indicates true or false values, false = 0, true = 1
@range [0,1]
*/
typedef int boolean;

/*
A basic report object used for a variety of cases to mark informational
messages, warnings, and errors related to processing or quality control
checks of raw data.
*/
typedef structure {
  string checkTypeDetected;
  string checkUsed;
  list<string> checkDescriptions;
  list<boolean> checkResults;
  list<string> messages;
  list<string> warnings;
  list<string> errors;
} AnalysisReport;