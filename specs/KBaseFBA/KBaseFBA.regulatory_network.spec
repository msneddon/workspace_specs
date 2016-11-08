/*
Genome feature ID
@id external
*/
typedef string feature_id;

/*
A simplified representation of a regulatory interaction that also stores the probability of the interaction
(specificially, as the probability the target is on given that the regulator is off), which is necessary for PROM
to construct FBA constraints.  NOTE: this data object should be migrated to the Regulation service, and simply
imported here. NOTE 2: feature_id may actually be a more general ID, as models can potentially be loaded that
are not in the kbase namespace. In this case everything, including expression data and the fba model must be in
the same namespace.

    feature_id TF            - the genome feature that is the regulator
    feature_id target        - the genome feature that is the target of regulation

@deprecated
*/
typedef structure {
  feature_id TF;
  feature_id target;
} RegulatoryInteraction;

/*
A collection of regulatory interactions that together form a regulatory network. This is an extremely
simplified data object for use in constructing a PROM model.  NOTE: this data object should be migrated to
the Regulation service, and simply imported here.
*/
typedef structure {
  list<RegulatoryInteraction> regulatory_network;
} regulatory_network;