/*
ETCStep object
*/
typedef structure {
  list<string> reactions;
} ETCStep;

/*
ETCPathwayObj object
*/
typedef structure {
  string electron_acceptor;
  list<ETCStep> steps;
} ETCPathwayObj;

/*
ElectronTransportChains (ETC) object
*/
typedef structure {
  list<ETCPathwayObj> pathways;
} ETC;