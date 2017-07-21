/*


*/
module KBaseSets {

    /*
        The workspace ID for a any data object.
        @id ws
    */
    typedef string ws_obj_id;

    /*
        A representation for any Workspace object that should be associated with a Set item.
    */
    typedef structure {
        string name;
        ws_obj_id ref;
    } DataAttachment;


    /****************************** */
    /* DIFFERENTIALEXPRESSIONMATRIX SET */

    /*
        The workspace id for a FeatureSet data object.
        @id ws KBaseFeatureValues.DifferentialExpressionMatrix
    */
    typedef string ws_diffexpmatrix_id;

    typedef structure {
        ws_diffexpmatrix_id ref;
        string label;
    } DifferentialExpressionMatrixSetItem;

    /*
        @metadata ws description as description
        @metadata ws length(items) as item_count
    */
    typedef structure {
        string description;
        list<DifferentialExpressionMatrixSetItem> items;
    } DifferentialExpressionMatrixSet;


    /****************************** */
    /* FEATURESET SET */

    /*
        The workspace id for a FeatureSet data object.
        @id ws KBaseCollections.FeatureSet
    */
    typedef string ws_featureset_id;

    typedef structure {
        ws_featureset_id ref;
        string label;
    } FeatureSetSetItem;

    /*
        @metadata ws description as description
        @metadata ws length(items) as item_count
    */
    typedef structure {
        string description;
        list<FeatureSetSetItem> items;
    } FeatureSetSet;


    /****************************** */
    /* EXPRESSION SET */
    /*
        The workspace id for a RNASeqExpression data object.
        @id ws KBaseRNASeq.RNASeqExpression
    */
    typedef string ws_expression_id;

    /*
        @optional label data_attachments
    */
    typedef structure {
        ws_expression_id ref;
        string label;
        list <DataAttachment> data_attachments;
    } ExpressionSetItem;

    /*
        @metadata ws description as description
        @metadata ws length(items) as item_count
    */
    typedef structure {
        string description;
        list<ExpressionSetItem> items;
    } ExpressionSet;


    /****************************** */
    /* READS ALIGNMENTS SET */

    /*
        The workspace id for a ReadsAlignment data object.
        @id ws KBaseRNASeq.RNASeqAlignment
    */
    typedef string ws_reads_align_id;

    /*
        @optional label data_attachments
    */
    typedef structure {
        ws_reads_align_id ref;
        string label;
        list <DataAttachment> data_attachments;
    } ReadsAlignmentSetItem;

    /*
        @metadata ws description as description
        @metadata ws length(items) as item_count
    */
    typedef structure {
        string description;
        list<ReadsAlignmentSetItem> items;
    } ReadsAlignmentSet;


    /****************************** */
    /* READS SET */

    /*
        The workspace ID for a Reads data object.
        @id ws KBaseFile.PairedEndLibrary KBaseFile.SingleEndLibrary
    */
    typedef string ws_reads_id;

    /*
        @optional label data_attachments
    */
    typedef structure {
        ws_reads_id ref;
        string label;
        list <DataAttachment> data_attachments;
    } ReadsSetItem;

    /*
        @metadata ws description as description
        @metadata ws length(items) as item_count
    */
    typedef structure {
        string description;
        list<ReadsSetItem> items;
    } ReadsSet;


    /****************************** */
    /* ASSEMBLY SET */

    /*
        The workspace ID for an Assembly data object.
        @id ws KBaseGenomeAnnotations.Assembly
    */
    typedef string ws_assembly_id;

    /* @optional label */
    typedef structure {
        ws_assembly_id ref;
        string label;
    } AssemblySetItem;

    /*
        @metadata ws description as description
        @metadata ws length(items) as item_count
    */
    typedef structure {
        string description;
        list<AssemblySetItem> items;
    } AssemblySet;



    /*************************************************************** */
    /* GENOME SET */

    /*
        The workspace ID for a Genome data object.
        @id ws KBaseGenomes.Genome
    */
    typedef string ws_genome_id;

    /* @optional label */
    typedef structure {
        ws_genome_id ref;
        string label;
    } GenomeSetItem;

    /*
        @metadata ws description as description
        @metadata ws length(items) as item_count
    */
    typedef structure {
        string description;
        list<GenomeSetItem> items;
    } GenomeSet;

};
