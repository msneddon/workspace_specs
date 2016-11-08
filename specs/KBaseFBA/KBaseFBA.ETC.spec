/*
ETCCompound object
*/
typedef structure {
  list<string> compound_refs;
  string name;
} ETCCompound;

/*
ETCStep object
*/
typedef structure {
  list<string> reactions;
  ETCCompound substrates;
  ETCCompound products;
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