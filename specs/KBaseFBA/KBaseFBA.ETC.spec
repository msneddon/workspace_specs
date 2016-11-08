/*
ETCCompound object
*/
typedef structure {
  string compound_ref;
  string name;
} ETCCompound;

/*
ETCStep object
*/
typedef structure {
  list<string> reactions;
  list<ETCCompound> substrates;
  list<ETCCompound> products;
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