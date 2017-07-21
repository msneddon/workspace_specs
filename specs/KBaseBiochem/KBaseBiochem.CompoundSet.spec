/*
Reference to a compound object in a biochemistry
@id subws KBaseBiochem.Biochemistry.compounds.[*].id
*/
typedef string compound_ref;

/*
Reference to a compound in a fbamodel  object
*/
typedef string modelcompound_ref;

/*
ImportedCompound object

@optional deltag deltagerr mass exactmass compound_ref modelcompound_ref charge name
*/
typedef structure {
  string id;
  string name;
  string smiles;
  string inchikey;
  float charge;
  string formula;
  float mass;
  float exactmass;
  compound_ref compound_ref;
  modelcompound_ref modelcompound_ref;
  mapping<string, list<string>> dblinks;
  mapping<string, mapping<string, float>> fingerprints;
  float deltag;
  float deltagerr;
} ImportedCompound;

/*
Reference to a fbamodel object
*/
typedef string fbamodel_ref;

/*
Reference to a Biochemistry object
@id ws KBaseBiochem.Biochemistry
*/
typedef string biochemistry_ref;

/*
CompoundSet object

@optional description name fbamodel_ref biochemistry_ref
*/
typedef structure {
  list<ImportedCompound> compounds;
  string id;
  string name;
  string description;
  fbamodel_ref fbamodel_ref;
  biochemistry_ref biochemistry_ref;
} CompoundSet;