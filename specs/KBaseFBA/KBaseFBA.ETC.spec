/*
ETCSubstrates object
*/
typedef structure {
  string name;
  list<string> compound_refs;
} ETCSubstrates;

/*
ETCProducts object
*/
typedef structure {
  string name;
  list<string> compound_refs;
} ETCProducts;

/*
ETCSteps object
*/
typedef structure {
  list<string> reactions;
  ETCSubstrates substrates;
  ETCProducts products;
} ETCSteps;

/*
ETCPathwayObj object
*/
typedef structure {
  string type;
  string name;
  list<ETCSteps> steps;
} ETCPathwayObj;

/*
ElectronTransportChains (ETC) object
*/
typedef structure {
  list<ETCPathwayObj> pathways;
} ETC;