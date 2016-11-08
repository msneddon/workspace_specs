/*
Annotation pipeline specific : Seed_role_element

@optional variant_code role
*/
typedef structure {
  string role;
  string subsystem;
  string variant_code;
} seed_role;

/*
Annotation pipeline specific : Seed_roles
*/
typedef structure {
  mapping<string, list<seed_role>> feature_roles;
} SeedRoles;