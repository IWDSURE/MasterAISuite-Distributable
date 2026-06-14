# 11_Global_Payroll — Tables Index

**Total Tables:** 440

| Name                                               | Description |
|----------------------------------------------------|-------------|
| [HCM_BULK_SEED_HIER_LEVELS_GT](Tables/HCM_BULK_SEED_HIER_LEVELS_GT.md) | Global Temporary Table used during bulk seed SQL processing. Oracle internal use only. |
| [PAY_ACTION_CLASSES](Tables/PAY_ACTION_CLASSES.md) | This table contains the mapping information between action classifications and action types. |
| [PAY_ACTION_CONTEXTS](Tables/PAY_ACTION_CONTEXTS.md) | This table contains the payroll relationship action contexts used and processed for an employee. |
| [PAY_ACTION_CONTEXTS_VAR](Tables/PAY_ACTION_CONTEXTS_VAR.md) | This child table of PAY_ACTION_CONTEXTS contains context values of non-global and user defined contexts that were proces… |
| [PAY_ACTION_DETAILS](Tables/PAY_ACTION_DETAILS.md) | This stores the overall processing details of an Action performed by the Processes. |
| [PAY_ACTION_INFORMATION](Tables/PAY_ACTION_INFORMATION.md) | Table for Payroll Action Information |
| [PAY_ACTION_INTERLOCKS](Tables/PAY_ACTION_INTERLOCKS.md) | This table contains the assignment action locking rules to control rollback processing. |
| [PAY_ACTION_LOGS](Tables/PAY_ACTION_LOGS.md) | This table holds the Log File details of the ADF/in-memory processes. |
| [PAY_ACTION_LOG_LINES](Tables/PAY_ACTION_LOG_LINES.md) | This table stores the log file line text for ADF processing. |
| [PAY_ACTION_MATRIX](Tables/PAY_ACTION_MATRIX.md) | Action Matrix controls what action is available in which context |
| [PAY_ACTION_PARAM_GROUPS](Tables/PAY_ACTION_PARAM_GROUPS.md) | This table contains user-defined action parameter groups. |
| [PAY_ACTION_PARAM_VALUES](Tables/PAY_ACTION_PARAM_VALUES.md) | This table contains parameter values that control certain processes, such as payroll runs. |
| [PAY_ACTION_TYPES](Tables/PAY_ACTION_TYPES.md) | This table contains types of payroll action, such as payroll run and prepayments. |
| [PAY_ADJUSTED_COSTING_DETAILS](Tables/PAY_ADJUSTED_COSTING_DETAILS.md) | This table contains adjusted costing details. |
| [PAY_ALLOW_OVERRIDES_F](Tables/PAY_ALLOW_OVERRIDES_F.md) | This table contains the values that can be overridden for a value definition, such as rate, additional amount, and total… |
| [PAY_ALLOW_OVERRIDES_TL](Tables/PAY_ALLOW_OVERRIDES_TL.md) | This table contains translation information for PAY_ALLOW_OVERRIDES_F. |
| [PAY_ALL_PAYROLLS_F](Tables/PAY_ALL_PAYROLLS_F.md) | This table contains definitions of groups of workers who share the same frequency of processing and payment. It defines … |
| [PAY_AMER_GEOGRAPHIES](Tables/PAY_AMER_GEOGRAPHIES.md) | This table contains North America specific payroll geographies (townships and school districts). |
| [PAY_AMER_GEOGRAPHY_RANGES](Tables/PAY_AMER_GEOGRAPHY_RANGES.md) | This table contains zip codes for North America specific payroll geographies (townships). |
| [PAY_AMER_INTERFACE_PARAMETERS](Tables/PAY_AMER_INTERFACE_PARAMETERS.md) | This table contains the file version and parameter details of various North America processes. |
| [PAY_ANA_BAL_RESULTS](Tables/PAY_ANA_BAL_RESULTS.md) | This table contains payroll balance results analytics transactional data. |
| [PAY_ANA_CHILD_ACTIONS](Tables/PAY_ANA_CHILD_ACTIONS.md) | This table contains payroll child actions analytics transactional data. |
| [PAY_ANA_COST_RESULTS](Tables/PAY_ANA_COST_RESULTS.md) | This table contains payroll cost results analytics transactional data. |
| [PAY_ANA_PAYROLL_ACTIONS](Tables/PAY_ANA_PAYROLL_ACTIONS.md) | This table contains payroll actions analytics transactional data. |
| [PAY_ARCHIVE_ITEMS](Tables/PAY_ARCHIVE_ITEMS.md) | Archive table which holds individual items of data to allow archive retrieval via database items |
| [PAY_ARCHIVE_SORT_VALUES](Tables/PAY_ARCHIVE_SORT_VALUES.md) | Table for Archive action sort values |
| [PAY_ASSIGNED_PAYROLLS_DN](Tables/PAY_ASSIGNED_PAYROLLS_DN.md) | Stores details of which payrolls an employee is assigned to at a point in time. This allows an employee to transition pa… |
| [PAY_ASSIGNED_PAYROLLS_DN_](Tables/PAY_ASSIGNED_PAYROLLS_DN_.md) | Stores details of which payrolls an employee is assigned to at a point in time. This allows an employee to transition pa… |
| [PAY_ASSIGNED_PAYROLLS_F](Tables/PAY_ASSIGNED_PAYROLLS_F.md) | Stores details of which payrolls an employee is assigned to at a point in time. This allows an employee to transition pa… |
| [PAY_ASSIGNED_PAYROLLS_F_](Tables/PAY_ASSIGNED_PAYROLLS_F_.md) | Stores details of which payrolls an employee is assigned to at a point in time. This allows an employee to transition pa… |
| [PAY_AUTO_INDIRECTS_F](Tables/PAY_AUTO_INDIRECTS_F.md) | This table contains elements for automatic indirect generation. If a fast formula is supplied, then multiple indirects o… |
| [PAY_BALANCE_ATTRIBUTES](Tables/PAY_BALANCE_ATTRIBUTES.md) | This table contains mappings between attributes and defined balances. |
| [PAY_BALANCE_CATEGORIES_F](Tables/PAY_BALANCE_CATEGORIES_F.md) | This table contains balance category definitions, which are independent subsets of balance types. |
| [PAY_BALANCE_CATEGORIES_TL](Tables/PAY_BALANCE_CATEGORIES_TL.md) | This table contains translated information for PAY_BALANCE_CATEGORIES_F. |
| [PAY_BALANCE_DIMENSIONS](Tables/PAY_BALANCE_DIMENSIONS.md) | This table contains information allowing the summation of a balance. |
| [PAY_BALANCE_FEEDS_F](Tables/PAY_BALANCE_FEEDS_F.md) | This table contains the details of how a given element input value contributes to a specific balance. The existence of a… |
| [PAY_BALANCE_GROUPS](Tables/PAY_BALANCE_GROUPS.md) | This table contains balance group definitions, which are sets of defined balances. |
| [PAY_BALANCE_GROUPS_TL](Tables/PAY_BALANCE_GROUPS_TL.md) | This table contains translated information for PAY_BALANCE_GROUPS. |
| [PAY_BALANCE_LOGS](Tables/PAY_BALANCE_LOGS.md) | This table contains data returned by the mechanism for monitoring how a balance value was retrieved, such as from the la… |
| [PAY_BALANCE_TYPES](Tables/PAY_BALANCE_TYPES.md) | This table contains the definitions of balances used in calculations and reporting. |
| [PAY_BALANCE_TYPES_TL](Tables/PAY_BALANCE_TYPES_TL.md) | This table contains translated information for PAY_BALANCE_TYPES. |
| [PAY_BALANCE_VALIDATION](Tables/PAY_BALANCE_VALIDATION.md) | This table contains validity information of each run level balance for the legislative data group. |
| [PAY_BAL_ADJ_GROUPS](Tables/PAY_BAL_ADJ_GROUPS.md) | This table contains definitions that correspond to balance adjustment payroll actions. It is a child table of PAY_BAL_AD… |
| [PAY_BAL_ADJ_HEADERS](Tables/PAY_BAL_ADJ_HEADERS.md) | This table contains balance adjustment batch headers |
| [PAY_BAL_ADJ_LINES](Tables/PAY_BAL_ADJ_LINES.md) | This table contains details of individual balance adjustment entries. It is a child table of PAY_BAL_ADJ_GROUPS. |
| [PAY_BAL_ADJ_LINE_ACTIONS](Tables/PAY_BAL_ADJ_LINE_ACTIONS.md) | This table contains the actions for a balance adjustment. |
| [PAY_BAL_ADJ_VALUES](Tables/PAY_BAL_ADJ_VALUES.md) | This table contains adjustment value information. It is a child table of PAY_BAL_ADJ_LINES. |
| [PAY_BAL_ATT_DEFAULTS](Tables/PAY_BAL_ATT_DEFAULTS.md) | This table contains definitions to populate balance attributes automatically. A balance attribute default record tells w… |
| [PAY_BAL_ATT_DEFINITIONS](Tables/PAY_BAL_ATT_DEFINITIONS.md) | This table contains definitions of balance attributes, with which defined balances can be associated. A balance attribut… |
| [PAY_BAL_ATT_DEFINITIONS_TL](Tables/PAY_BAL_ATT_DEFINITIONS_TL.md) | This table contains translated information for PAY_BAL_ATT_DEFINITIONS. |
| [PAY_BAL_BATCH_HEADERS](Tables/PAY_BAL_BATCH_HEADERS.md) | This table contains header information that defines the contents of a batch of balance initialisations to be  transferre… |
| [PAY_BAL_BATCH_LINES](Tables/PAY_BAL_BATCH_LINES.md) | This table contains the batch lines of a batch of balance initialisations to be  transferred into the live schema. |
| [PAY_BAL_CLASSIFICATIONS](Tables/PAY_BAL_CLASSIFICATIONS.md) | This table contains the details that show which element classifications feed balances, either by adding or subtracting. … |
| [PAY_BAL_EXCEPTIONS_B](Tables/PAY_BAL_EXCEPTIONS_B.md) | This table contains balance exception information. |
| [PAY_BAL_EXCEPTIONS_TL](Tables/PAY_BAL_EXCEPTIONS_TL.md) | This table contains translated information for PAY_BAL_EXCEPTIONS_B. |
| [PAY_BAL_EXCEPTION_REPORTS_B](Tables/PAY_BAL_EXCEPTION_REPORTS_B.md) | This table contains balance exception report information. |
| [PAY_BAL_EXCEPTION_REPORTS_TL](Tables/PAY_BAL_EXCEPTION_REPORTS_TL.md) | This table contains translated information for PAY_BAL_EXCEPTION_REPORTS_B |
| [PAY_BAL_EXCEP_REPORT_ENTRIES](Tables/PAY_BAL_EXCEP_REPORT_ENTRIES.md) | This table contains information of balance exception report entries. |
| [PAY_BAL_GRP_INCLUSIONS](Tables/PAY_BAL_GRP_INCLUSIONS.md) | This table contains information about which balance attribute definitions are included in the balance group. It is an in… |
| [PAY_BAL_GRP_USAGES](Tables/PAY_BAL_GRP_USAGES.md) | This table contains balance group usage definitions, which are instances of a balance group and hold detailed informatio… |
| [PAY_BAL_GRP_USAGES_TL](Tables/PAY_BAL_GRP_USAGES_TL.md) | This table contains translated information for PAY_BAL_GRP_USAGES. |
| [PAY_BAL_GRP_USAGE_ITEMS](Tables/PAY_BAL_GRP_USAGE_ITEMS.md) | This table contains the item level information of the balance group usages. For example, if the balance group usage is a… |
| [PAY_BANK_ACCOUNT_PRENOTES](Tables/PAY_BANK_ACCOUNT_PRENOTES.md) | This is a bank account prenote table, this will be replaced when the prenote functionality is finalised. |
| [PAY_BATCH_HEADERS](Tables/PAY_BATCH_HEADERS.md) | This table contains header information that defines the contents of a batch to be transferred into the live schema. |
| [PAY_BATCH_LINES](Tables/PAY_BATCH_LINES.md) | This table contains batch lines to be transferred into the live schema via the batch loader. |
| [PAY_BATCH_LINE_VALUES](Tables/PAY_BATCH_LINE_VALUES.md) | This table contains individual values of a parameter in a batch line used in the generic batch loader. |
| [PAY_CALCULATION_UNITS_F](Tables/PAY_CALCULATION_UNITS_F.md) | This table contains the value definitions, or ranges, to be used for the calculation of an element attached to a deducti… |
| [PAY_CALC_METHODS_F](Tables/PAY_CALC_METHODS_F.md) | This table contains methods of calculation supported by fast formulas, such as a cumulative or annualized calculation. |
| [PAY_CALC_METHODS_TL](Tables/PAY_CALC_METHODS_TL.md) | This table contains translated information for PAY_CALC_METHODS_F. |
| [PAY_CALC_PARTS_F](Tables/PAY_CALC_PARTS_F.md) | This table contains a part of a calculation in a fast formula, such as, result amount = base_amount multiplied by rate +… |
| [PAY_CALC_PARTS_TL](Tables/PAY_CALC_PARTS_TL.md) | This table contains translated information for PAY_CALC_PARTS_F. |
| [PAY_CALC_TYPES](Tables/PAY_CALC_TYPES.md) | This table contains the types of calculation supported by value definitions through a core function or by a custom fast … |
| [PAY_CALC_TYPES_TL](Tables/PAY_CALC_TYPES_TL.md) | This table contains translated information for PAY_CALC_TYPES. |
| [PAY_CE_TRANSACTIONS](Tables/PAY_CE_TRANSACTIONS.md) | Populated as a result of running the payment processes to keep track of how employees were paid. |
| [PAY_CHECKLISTS](Tables/PAY_CHECKLISTS.md) | Table stores checklist template utilized while checklist is created at runrtime |
| [PAY_CHECKLISTS_TL](Tables/PAY_CHECKLISTS_TL.md) | Holds translated information for PAY_CHECKLISTS. |
| [PAY_CHECKLIST_INSTANCES](Tables/PAY_CHECKLIST_INSTANCES.md) | Table captures the checklist instances created for the flow instance |
| [PAY_CHKLST_ANNOTATIONS](Tables/PAY_CHKLST_ANNOTATIONS.md) | Annotations describing the checklist |
| [PAY_CHKLST_ANNOTATIONS_TL](Tables/PAY_CHKLST_ANNOTATIONS_TL.md) | Holds translated information for PAY_CHKLST_ANNOTATIONS. |
| [PAY_CHUNK_STATUS](Tables/PAY_CHUNK_STATUS.md) | This table contains the status of processing on specific units of work to be processed by a payroll action or process. |
| [PAY_CIR_DATA_BACKUP_GLB_TRX](Tables/PAY_CIR_DATA_BACKUP_GLB_TRX.md) | This table backup cir data whose effective start date is after global transfer date for later processing. |
| [PAY_COIN_BREAKDOWNS](Tables/PAY_COIN_BREAKDOWNS.md) | The table holds the details of any Cash Payments with the breakdown on the currency amounts needed. |
| [PAY_CONNECTED_FLOWS](Tables/PAY_CONNECTED_FLOWS.md) | A record will be inserted into this table when a user creates a connection rule for a flow using connector tag. |
| [PAY_CONSOLIDATION_SETS](Tables/PAY_CONSOLIDATION_SETS.md) | This table contains details of groups used to consolidate the results of multiple payroll processes. The consolidation g… |
| [PAY_CONTEXT_USAGES](Tables/PAY_CONTEXT_USAGES.md) | This table contains the context details used by each localization. |
| [PAY_CONTEXT_USAGES_TL](Tables/PAY_CONTEXT_USAGES_TL.md) | This table contains translated information for PAY_CONTEXT_USAGES. |
| [PAY_CONTRIB_PAYMENTS](Tables/PAY_CONTRIB_PAYMENTS.md) | Stores details of payments made to third party from multiple sources. For example, if a number of employees all contribu… |
| [PAY_COSTS](Tables/PAY_COSTS.md) | This table contains cost details and values for payroll run results. |
| [PAY_COST_ADJUSTMENTS](Tables/PAY_COST_ADJUSTMENTS.md) | This table contains a name and description for costing adjustments. |
| [PAY_COST_ADJUST_LINES](Tables/PAY_COST_ADJUST_LINES.md) | This table contains details of what was changed as a result of a costing adjustment. |
| [PAY_COST_ALLOCATIONS_F](Tables/PAY_COST_ALLOCATIONS_F.md) | This table contains the definition of the cost allocation to various objects such as job, payroll, and payroll relations… |
| [PAY_COST_ALLOC_ACCOUNTS](Tables/PAY_COST_ALLOC_ACCOUNTS.md) | This table contains details of how payroll costs are apportioned across various accounts, for example, to allocate costs… |
| [PAY_COST_ALLOC_KEYFLEX](Tables/PAY_COST_ALLOC_KEYFLEX.md) | This table contains the combinations for the cost allocation key flexfield for each of the typical accounts maintained b… |
| [PAY_COST_CLASSIFICATIONS](Tables/PAY_COST_CLASSIFICATIONS.md) | This table contains classifications that group elements based on common costing requirements. |
| [PAY_COST_CLASSIFICATIONS_TL](Tables/PAY_COST_CLASSIFICATIONS_TL.md) | This table contains translated information for PAY_COST_CLASSIFICATIONS. |
| [PAY_COST_INFO_F](Tables/PAY_COST_INFO_F.md) | This table contains costing attrinutes for each classification. |
| [PAY_CUST_OBJECTS](Tables/PAY_CUST_OBJECTS.md) | this will be utilized in ui customization |
| [PAY_CUST_RULES](Tables/PAY_CUST_RULES.md) | Table capturing rules for UI Custimization |
| [PAY_DAEMON_ACTIONS](Tables/PAY_DAEMON_ACTIONS.md) | Implements the queue of actions to be processed by the Daemon process. |
| [PAY_DATES](Tables/PAY_DATES.md) | This entity stores Payroll information about when an employee was eligible for Payroll processing. |
| [PAY_DATETRACKED_EVENTS](Tables/PAY_DATETRACKED_EVENTS.md) | This table contains information about what the event captures and stores, such as a change to a grade, an element entry |
| [PAY_DEDN_REPORT_USE](Tables/PAY_DEDN_REPORT_USE.md) | This table contains details of which deductions are reported by each tax reporting unit. |
| [PAY_DEDUCTION_GROUPS](Tables/PAY_DEDUCTION_GROUPS.md) | This table contains logical groupings of deductions, such as an income tax group that includes the value definitions for… |
| [PAY_DEDUCTION_GROUPS_TL](Tables/PAY_DEDUCTION_GROUPS_TL.md) | This table contains translated information for PAY_DEDUCTION_GROUPS. |
| [PAY_DEDUCTION_TYPES](Tables/PAY_DEDUCTION_TYPES.md) | This table contains deduction definitions, such as income tax and social security. |
| [PAY_DEDUCTION_TYPES_TL](Tables/PAY_DEDUCTION_TYPES_TL.md) | This table contains translated information for PAY_DEDUCTION_TYPE. |
| [PAY_DED_CONTEXT_USAGES](Tables/PAY_DED_CONTEXT_USAGES.md) | This table contains context usages for deduction types or deduction card components. |
| [PAY_DEFINED_BALANCES](Tables/PAY_DEFINED_BALANCES.md) | This table contains a complete description of a balance. It is the intersection between balance types and balance dimens… |
| [PAY_DIAGNOSTIC_LOGS](Tables/PAY_DIAGNOSTIC_LOGS.md) | This table will be used to capture details of diagnostics |
| [PAY_DIMENSION_ROUTES](Tables/PAY_DIMENSION_ROUTES.md) | This table contains additional route information for balance dimensions. |
| [PAY_DIMENSION_USAGES](Tables/PAY_DIMENSION_USAGES.md) | This table contains details of how dimensions are used and named within a legislation. |
| [PAY_DIMENSION_USAGES_TL](Tables/PAY_DIMENSION_USAGES_TL.md) | This table contains translated information for PAY_DIMENSION_USAGES. |
| [PAY_DIM_CONTEXT_USAGES](Tables/PAY_DIM_CONTEXT_USAGES.md) | This table contains details of which formula contexts are available to be used in a legislation for balance dimensions. |
| [PAY_DIR_CARDS_F](Tables/PAY_DIR_CARDS_F.md) | This table contains the header of a person's deduction card. |
| [PAY_DIR_CARDS_F_](Tables/PAY_DIR_CARDS_F_.md) | This table contains the header of a person's deduction card. |
| [PAY_DIR_CARD_COMPONENTS_F](Tables/PAY_DIR_CARD_COMPONENTS_F.md) | This table contains the details of a person's deduction card. |
| [PAY_DIR_CARD_COMPONENTS_F_](Tables/PAY_DIR_CARD_COMPONENTS_F_.md) | This table contains the details of a person's deduction card. |
| [PAY_DIR_CARD_COMP_DEFS_F](Tables/PAY_DIR_CARD_COMP_DEFS_F.md) | This table contains deduction component definitions. |
| [PAY_DIR_CARD_COMP_DEFS_TL](Tables/PAY_DIR_CARD_COMP_DEFS_TL.md) | This table contains translated information for PAY_DIR_CARD_COMP_DEFS_F. |
| [PAY_DIR_CARD_DEFINITIONS](Tables/PAY_DIR_CARD_DEFINITIONS.md) | This table contains details of a deduction or set of related deductions, such as a government tax card. |
| [PAY_DIR_CARD_DEFINITIONS_TL](Tables/PAY_DIR_CARD_DEFINITIONS_TL.md) | This table contains translated information for PAY_DIR_CARD_DEFINITIONS. |
| [PAY_DIR_CARD_LEVELS_F](Tables/PAY_DIR_CARD_LEVELS_F.md) | This table contains the level at which a deduction card is valid, such as person or tax reporting unit level. |
| [PAY_DIR_COMP_DETAILS_F](Tables/PAY_DIR_COMP_DETAILS_F.md) | This table contains any flexfield data defined for components of the deduction card. |
| [PAY_DIR_COMP_DETAILS_F_](Tables/PAY_DIR_COMP_DETAILS_F_.md) | This table contains any flexfield data defined for components of the deduction card. |
| [PAY_DIR_COMP_FLEXS_F](Tables/PAY_DIR_COMP_FLEXS_F.md) | This table contains details of which flexfield contexts are available to a card component. |
| [PAY_DIR_COMP_FLEX_RSHIPS_F](Tables/PAY_DIR_COMP_FLEX_RSHIPS_F.md) | This table contains the hierarchy of structures (parent/child) and the sequence in which they can be displayed. |
| [PAY_DIR_FLEX_SEGMENTS_F](Tables/PAY_DIR_FLEX_SEGMENTS_F.md) | This table contains details of which segments of a flexfield are hidden or shown for a given combination of contexts. It… |
| [PAY_DIR_FLEX_USAGES_F](Tables/PAY_DIR_FLEX_USAGES_F.md) | This table contains details of how flexfield contexts are used for a given component. |
| [PAY_DIR_OVERRIDE_USAGES_F](Tables/PAY_DIR_OVERRIDE_USAGES_F.md) | This table contains the overrides for a particular card component, with the values that can be set for that override. |
| [PAY_DIR_REP_CARDS_F](Tables/PAY_DIR_REP_CARDS_F.md) | This table contains the association between a card, or a section of a card, and a tax reporting unit, thus forming a rep… |
| [PAY_DIR_REP_CARDS_F_](Tables/PAY_DIR_REP_CARDS_F_.md) | This table contains the association between a card, or a section of a card, and a tax reporting unit, thus forming a rep… |
| [PAY_DIR_REP_CARD_USAGES_F](Tables/PAY_DIR_REP_CARD_USAGES_F.md) | This table contains mappings of deduction components to employment terms or assignments within a reporting card. |
| [PAY_DIR_REP_CARD_USAGES_F_](Tables/PAY_DIR_REP_CARD_USAGES_F_.md) | This table contains mappings of deduction components to employment terms or assignments within a reporting card. |
| [PAY_ELEMENT_CRITERIA](Tables/PAY_ELEMENT_CRITERIA.md) | This table contains combinations of eligibility criteria that are referenced by element eligibilty (PAY_ELEMENT_LINKS_F)… |
| [PAY_ELEMENT_ENTRIES_F](Tables/PAY_ELEMENT_ENTRIES_F.md) | This table contains element entries for each assignment. The actual values for each entry are held in PAY_ELEMENT_ENTRY_… |
| [PAY_ELEMENT_ENTRIES_F_](Tables/PAY_ELEMENT_ENTRIES_F_.md) | This table contains element entries for each assignment. The actual values for each entry are held in PAY_ELEMENT_ENTRY_… |
| [PAY_ELEMENT_ENTRY_VALUES_F](Tables/PAY_ELEMENT_ENTRY_VALUES_F.md) | This table contains the actual values entered for a specific element entry. For example, the overtime element may have a… |
| [PAY_ELEMENT_ENTRY_VALUES_F_](Tables/PAY_ELEMENT_ENTRY_VALUES_F_.md) | This table contains the actual values entered for a specific element entry. For example, the overtime element may have a… |
| [PAY_ELEMENT_LINKS_F](Tables/PAY_ELEMENT_LINKS_F.md) | This table contains the eligibility rules that link elements to groups of employees. An assignment must match the eligib… |
| [PAY_ELEMENT_SPAN_USAGES](Tables/PAY_ELEMENT_SPAN_USAGES.md) | This table contains information to determine which retropay element to use depending on the age of the retrospective cha… |
| [PAY_ELEMENT_TYPES_F](Tables/PAY_ELEMENT_TYPES_F.md) | This table contains the definitions of elements, which are the units used to build all earnings and benefits. NOTE: User… |
| [PAY_ELEMENT_TYPES_TL](Tables/PAY_ELEMENT_TYPES_TL.md) | This table contains translation information for PAY_ELEMENT_TYPES_F. |
| [PAY_ELEMENT_TYPE_USAGES_F](Tables/PAY_ELEMENT_TYPE_USAGES_F.md) | Used to identify how  the Element is used with the Run Type |
| [PAY_ELE_CLASSIFICATIONS](Tables/PAY_ELE_CLASSIFICATIONS.md) | This table contains element classifications that define groups of elements for legislative and informational needs. Prim… |
| [PAY_ELE_CLASSIFICATIONS_TL](Tables/PAY_ELE_CLASSIFICATIONS_TL.md) | This table contains translation information for PAY_ELE_CLASSIFICATIONS. |
| [PAY_ELE_CLASS_USAGES_F](Tables/PAY_ELE_CLASS_USAGES_F.md) | Table For Element Class Usages PAY_ELE_CLASS_USAGES_F |
| [PAY_ELE_PAY_FREQ_RULES](Tables/PAY_ELE_PAY_FREQ_RULES.md) | This table contains the periods in which an element should be processed. For example, if a deduction should process in p… |
| [PAY_ELE_SECURITY_DETAILS](Tables/PAY_ELE_SECURITY_DETAILS.md) | This table holds information of payroll element security details. |
| [PAY_ELE_SECURITY_DETAILS_](Tables/PAY_ELE_SECURITY_DETAILS_.md) | This table holds information of payroll element security details. |
| [PAY_ELE_SECURITY_PROFILES](Tables/PAY_ELE_SECURITY_PROFILES.md) | This table holds information of payroll element security profiles. |
| [PAY_ELE_SECURITY_PROFILES_](Tables/PAY_ELE_SECURITY_PROFILES_.md) | This table holds information of payroll element security profiles. |
| [PAY_ELE_TMPLT_CLASS_USAGES](Tables/PAY_ELE_TMPLT_CLASS_USAGES.md) | This table contains information about which element templates are applicable for each element classification. For exampl… |
| [PAY_ELE_TMPLT_CLASS_USAGES_TL](Tables/PAY_ELE_TMPLT_CLASS_USAGES_TL.md) | This table contains translation information for PAY_ELE_TMPLT_CLASS_USAGES. |
| [PAY_ELE_TYPE_EXTRA_INFO](Tables/PAY_ELE_TYPE_EXTRA_INFO.md) | This table contains the additional information details defined for an element flexfield. |
| [PAY_ELE_TYPE_INFO_TYPES](Tables/PAY_ELE_TYPE_INFO_TYPES.md) | This table contains additional flexfield structures to provide extra configuration for an element. |
| [PAY_ENTRY_PCT_DIST](Tables/PAY_ENTRY_PCT_DIST.md) | This table contains a percentage break down of an entry value across one or more payroll terms or assignments. These per… |
| [PAY_ENTRY_PROC_DETAILS](Tables/PAY_ENTRY_PROC_DETAILS.md) | This table contains internal processing details for certain types of element entries. |
| [PAY_ENTRY_USAGES](Tables/PAY_ENTRY_USAGES.md) | This table contains the periods of time that an element entry is active and therefore may be processed. It also specifie… |
| [PAY_EVENT_ACTIONS_F](Tables/PAY_EVENT_ACTIONS_F.md) | This table contains the Action Definitions to be used by Events. |
| [PAY_EVENT_ACTIONS_TL](Tables/PAY_EVENT_ACTIONS_TL.md) | This is the translation table for Pay Event Actions. |
| [PAY_EVENT_ACTION_CRITERIA_F](Tables/PAY_EVENT_ACTION_CRITERIA_F.md) | This associates an Event Group Action to the objects that will use the Action. |
| [PAY_EVENT_ACTION_TYPES](Tables/PAY_EVENT_ACTION_TYPES.md) | This is a seeded table of the Event Action Types that can be used by clients. |
| [PAY_EVENT_ACTION_TYPES_TL](Tables/PAY_EVENT_ACTION_TYPES_TL.md) | This is the translation table for the Event Action Types. |
| [PAY_EVENT_GROUPS](Tables/PAY_EVENT_GROUPS.md) | This table contains payroll event groups, such as retro events. |
| [PAY_EVENT_GROUPS_TL](Tables/PAY_EVENT_GROUPS_TL.md) | This table contains translation data for PAY_EVENT_GROUPS. |
| [PAY_EVENT_GROUP_ACTIONS_F](Tables/PAY_EVENT_GROUP_ACTIONS_F.md) | This table links the Actions to the Event Groups to identify the Actions that will be performed when an Event is detecte… |
| [PAY_EVENT_GROUP_USAGES](Tables/PAY_EVENT_GROUP_USAGES.md) | This associates the Event Group to the Products that use the Event Group |
| [PAY_EVENT_PEOPLE](Tables/PAY_EVENT_PEOPLE.md) | This table is used to identify the people affected by an Event. |
| [PAY_EVENT_QUALIFIERS_F](Tables/PAY_EVENT_QUALIFIERS_F.md) | This table contains event qualifiers, which define which changes are relevant to track, such as changes to a specific se… |
| [PAY_EVENT_RELATIONSHIPS](Tables/PAY_EVENT_RELATIONSHIPS.md) | This table contains details of event notifications raised in the system and their current status. |
| [PAY_EVENT_TEMP_PROC_ACTIONS](Tables/PAY_EVENT_TEMP_PROC_ACTIONS.md) | This table is a denomalisation of the Actions and Events that are to be considered in the Event process. |
| [PAY_EVENT_USAGES](Tables/PAY_EVENT_USAGES.md) | This table contains the intersection between PAY_PROCESS_EVENTS and PAY_EVENT_RELATIONSHIPS. Thus it identifies the even… |
| [PAY_EVENT_VALUE_CHANGES_F](Tables/PAY_EVENT_VALUE_CHANGES_F.md) | This table contains specific value changes that qualify a change and cause an event to be raised, or disqualify a change… |
| [PAY_EVENT_VALUE_QUAL_F](Tables/PAY_EVENT_VALUE_QUAL_F.md) | This table holds teh Qualifiers for an Event Value Change. |
| [PAY_FILE_DETAILS](Tables/PAY_FILE_DETAILS.md) | Report file details that have been saved in the system |
| [PAY_FLOWS](Tables/PAY_FLOWS.md) | this will be utilized in Payrollflow s |
| [PAY_FLOWS_TL](Tables/PAY_FLOWS_TL.md) | Holds translated information for PAY_FLOWS. |
| [PAY_FLOW_INSTANCES](Tables/PAY_FLOW_INSTANCES.md) | Its an Instance table to capture Flow Instances |
| [PAY_FLOW_INST_INTERACTNS](Tables/PAY_FLOW_INST_INTERACTNS.md) | When the user selects and submits a Payroll Flow Pattern a Payroll Flow instance will be created. |
| [PAY_FLOW_METRICS](Tables/PAY_FLOW_METRICS.md) | This table is used to store the metrics for a flow. |
| [PAY_FLOW_OUTBOUND_CONFIG](Tables/PAY_FLOW_OUTBOUND_CONFIG.md) | This table is used for storing configurations to notify external systems. |
| [PAY_FLOW_PARAMETERS](Tables/PAY_FLOW_PARAMETERS.md) | Table capturing the flow parameters |
| [PAY_FLOW_PARAMETERS_TL](Tables/PAY_FLOW_PARAMETERS_TL.md) | Holds translated information for PAY_FLOW_PARAMETERS. |
| [PAY_FLOW_PARAMETER_PROPERTIES](Tables/PAY_FLOW_PARAMETER_PROPERTIES.md) | this will be utilized to store flow parameter properties |
| [PAY_FLOW_PARAM_VALUES](Tables/PAY_FLOW_PARAM_VALUES.md) | Table captures the flow parameter values |
| [PAY_FLOW_TASKS](Tables/PAY_FLOW_TASKS.md) | PAY_FLOW_TASKS captures the flow task details |
| [PAY_FLOW_TASKS_TL](Tables/PAY_FLOW_TASKS_TL.md) | Holds translated information for PAY_FLOW_TASKS. |
| [PAY_FLOW_TASK_INSTANCES](Tables/PAY_FLOW_TASK_INSTANCES.md) | Table capturing the flow task instance details |
| [PAY_FLOW_TASK_INTERACTNS](Tables/PAY_FLOW_TASK_INTERACTNS.md) | Table captures the branching and sequencing of flow tasks |
| [PAY_FLOW_TASK_NOTIFICATIONS](Tables/PAY_FLOW_TASK_NOTIFICATIONS.md) | Table captures tasks associated with the flow module |
| [PAY_FLOW_TASK_PARAMETERS](Tables/PAY_FLOW_TASK_PARAMETERS.md) | This Table captures the parameters to execute the flow task parameters |
| [PAY_FLOW_TASK_PARAMETERS_TL](Tables/PAY_FLOW_TASK_PARAMETERS_TL.md) | Holds translated information for PAY_FLOW_TASK_PARAMETERS. |
| [PAY_FLOW_TASK_PARAM_VALS](Tables/PAY_FLOW_TASK_PARAM_VALS.md) | Table captures the Flow Task Parameter values. |
| [PAY_FLW_SECURITY_PROFILES](Tables/PAY_FLW_SECURITY_PROFILES.md) | This table holds information of flow security profiles. |
| [PAY_FLW_SECURITY_PROFILES_](Tables/PAY_FLW_SECURITY_PROFILES_.md) | This table holds information of flow security profiles. |
| [PAY_FLW_SECURITY_PROFILE_PAYS](Tables/PAY_FLW_SECURITY_PROFILE_PAYS.md) | This table holds information of payroll flow security profiles. |
| [PAY_FLW_SECURITY_PROFILE_PAYS_](Tables/PAY_FLW_SECURITY_PROFILE_PAYS_.md) | This table holds information of payroll flow security profiles. |
| [PAY_FORMULA_RESULT_RULES_F](Tables/PAY_FORMULA_RESULT_RULES_F.md) | This table contains the rules that control what happens to the results produced by a specific formula calculation. When … |
| [PAY_FREQ_RULE_PERIODS](Tables/PAY_FREQ_RULE_PERIODS.md) | This table, which is a child table of PAY_ELE_PAY_FREQ_RULES, contains the actual frequency rule for an element. If the … |
| [PAY_GENERIC_ANA_ATT_DEFS](Tables/PAY_GENERIC_ANA_ATT_DEFS.md) | This table contains attribute definitions which used by pay generic analysis type. |
| [PAY_GENERIC_ANA_ATT_DEFS_TL](Tables/PAY_GENERIC_ANA_ATT_DEFS_TL.md) | This table contains translated information for PAY_GENERIC_ANALYTICS_ATT_DEFS. |
| [PAY_GENERIC_ANA_DATA](Tables/PAY_GENERIC_ANA_DATA.md) | This table contains pay generic analytics transaction data. |
| [PAY_GENERIC_ANA_TYPES](Tables/PAY_GENERIC_ANA_TYPES.md) | This table contains pay generic ANALYTICS type. |
| [PAY_GENERIC_ANA_TYPES_TL](Tables/PAY_GENERIC_ANA_TYPES_TL.md) | This table contains translated information for PAY_GENERIC_ANALYTICS_TYPES. |
| [PAY_GENERIC_MAPPINGS_F](Tables/PAY_GENERIC_MAPPINGS_F.md) | Generic table to store value mappings for use with LOVs |
| [PAY_GEOGRAPHIES](Tables/PAY_GEOGRAPHIES.md) | This table contains payroll geographies (state, county, city, school district, township and political subdivision) |
| [PAY_GEOGRAPHY_BOUNDARIES](Tables/PAY_GEOGRAPHY_BOUNDARIES.md) | This table stores the boundareis for the geographies. |
| [PAY_GEOGRAPHY_INTERFACE](Tables/PAY_GEOGRAPHY_INTERFACE.md) | This interface table contains geography information from ORAMAST.txt file. |
| [PAY_GEOGRAPHY_SPANS](Tables/PAY_GEOGRAPHY_SPANS.md) | This table contains muliple country/city mappings within a geography. |
| [PAY_GI_INTERFACE_TYPES](Tables/PAY_GI_INTERFACE_TYPES.md) | This table contains the general interface type information. |
| [PAY_GI_MAPPINGS](Tables/PAY_GI_MAPPINGS.md) | This table contains the general interface mapping information. |
| [PAY_GI_MAPPING_USAGES](Tables/PAY_GI_MAPPING_USAGES.md) | This table contains the general interface mapping usage information. |
| [PAY_GROSSUP_BAL_EXCLS](Tables/PAY_GROSSUP_BAL_EXCLS.md) | This table contains details of explicit balances that have been marked for exclusion from the net-to-gross processing. |
| [PAY_INPUT_VALUES_F](Tables/PAY_INPUT_VALUES_F.md) | This table contains the input values for an element. Each input value has a unit of measure and can have validations and… |
| [PAY_INPUT_VALUES_TL](Tables/PAY_INPUT_VALUES_TL.md) | This table contains translation information for PAY_INPUT_VALUES_F. |
| [PAY_INSTALLED_LEGISLATIONS](Tables/PAY_INSTALLED_LEGISLATIONS.md) | This table contains details of legislations, both predefined and those created using the Configure Payroll Legislations … |
| [PAY_ITERATIVE_RULES_F](Tables/PAY_ITERATIVE_RULES_F.md) | This table contains the processing rules of iterative elements. |
| [PAY_JOB_SUBMISSIONS](Tables/PAY_JOB_SUBMISSIONS.md) | This table stores the details of the last job submission from the Event System for certain Actions. |
| [PAY_LATEST_BALANCES](Tables/PAY_LATEST_BALANCES.md) | This table contains calculated balance values of the latest payroll relationship actions, which enable the quick balance… |
| [PAY_LEGISLATION_RULES](Tables/PAY_LEGISLATION_RULES.md) | This table contains legislation-specific rules and structure identifiers. |
| [PAY_LEG_UPDATES](Tables/PAY_LEG_UPDATES.md) | PAY_LEG_UPDATES - contains seed row for planned updates by Country and Update Type |
| [PAY_LEG_UPDATES_PROCESS](Tables/PAY_LEG_UPDATES_PROCESS.md) | PAY_LEG_UPDATES_PROCESS - stores transaction of legislative data update process. |
| [PAY_LEG_UPDATES_TL](Tables/PAY_LEG_UPDATES_TL.md) | PAY_LEG_UPDATES_TL - translation table for the translated name |
| [PAY_LEG_UPDATE_FILES](Tables/PAY_LEG_UPDATE_FILES.md) | PAY_LEG_UPDATE_FILES - contains delivered monthly updates. |
| [PAY_LEG_UPDATE_MERGE_ERRORS](Tables/PAY_LEG_UPDATE_MERGE_ERRORS.md) | PAY_LEG_UPDATE_MERGE_ERRORS - contains errors occurred during execution of pay_legislative_updates procedure. |
| [PAY_LINK_INPUT_VALUES_F](Tables/PAY_LINK_INPUT_VALUES_F.md) | This table contains input value settings for a specific link rule to override the definitions for the element. For examp… |
| [PAY_MARKED_OBJECTS](Tables/PAY_MARKED_OBJECTS.md) | This Table is used to capture the unprocessed business objects. |
| [PAY_MASS_GLB_TRANSFER_CONFIG](Tables/PAY_MASS_GLB_TRANSFER_CONFIG.md) | Table is to store the payroll config options in Mass Global Transfer |
| [PAY_MESSAGE_LINES](Tables/PAY_MESSAGE_LINES.md) | This table contains error messages from running a process. |
| [PAY_MIG_STAGING_ELEMENTS](Tables/PAY_MIG_STAGING_ELEMENTS.md) | This table contains information that is useful for element migration itself and related areas. It contains a mapping bet… |
| [PAY_MIG_STD_TEMPL_QUES](Tables/PAY_MIG_STD_TEMPL_QUES.md) | This table contains the superset of questions used across the relevant element templates, including both core and legisl… |
| [PAY_MONETARY_UNITS](Tables/PAY_MONETARY_UNITS.md) | PAY_MONETARY_UNITS holds the valid denominations for currencies.  Used for coinage analysis. |
| [PAY_MONETARY_UNITS_TL](Tables/PAY_MONETARY_UNITS_TL.md) | Translated data for the table PAY_MONETARY_UNITS_TL |
| [PAY_OBJECT_ACTIONS](Tables/PAY_OBJECT_ACTIONS.md) | This table contains detailed information for what was processed in some types of payroll actions. |
| [PAY_OBJECT_GROUPS](Tables/PAY_OBJECT_GROUPS.md) | This table contains groups of elements, people, or deduction card data, used for reporting, processing, data entry, and … |
| [PAY_OBJECT_GROUPS_TL](Tables/PAY_OBJECT_GROUPS_TL.md) | This table contains translated information for PAY_OBJECT_GROUPS. |
| [PAY_OBJECT_GROUP_AMENDS](Tables/PAY_OBJECT_GROUP_AMENDS.md) | This table contains the revised definition of what to include or exclude from the default definition group based on the … |
| [PAY_OBJECT_GROUP_LEVELS](Tables/PAY_OBJECT_GROUP_LEVELS.md) | This table contains the level of the employment hierarchy that the rule applies to. |
| [PAY_OBJECT_GROUP_PARAMS](Tables/PAY_OBJECT_GROUP_PARAMS.md) | This table contains the parameters that define an object group, such as the payroll name for an assignment group. |
| [PAY_OBJECT_GROUP_RULES](Tables/PAY_OBJECT_GROUP_RULES.md) | This table contains the rules that define a dynamic group whose members are evaluated by runniing a fast formula, such a… |
| [PAY_OBJECT_GROUP_STORE](Tables/PAY_OBJECT_GROUP_STORE.md) | Table used for Object Group flex support |
| [PAY_OBJECT_GROUP_TYPES](Tables/PAY_OBJECT_GROUP_TYPES.md) | This table contains the type of rule for an object group. |
| [PAY_OBJECT_GROUP_TYPE_PARAS](Tables/PAY_OBJECT_GROUP_TYPE_PARAS.md) | This table contains the parameters that define object group rules. |
| [PAY_OBSOLETE](Tables/PAY_OBSOLETE.md) | Table to hold index of obsoleted seed data. |
| [PAY_OLD_RANGE_ITEMS_F](Tables/PAY_OLD_RANGE_ITEMS_F.md) | This table contains the values or sets of values used in the calculation of a value definition. For example, for a value… |
| [PAY_OLD_RANGE_ITEMS_F_](Tables/PAY_OLD_RANGE_ITEMS_F_.md) | This table contains the values or sets of values used in the calculation of a value definition. For example, for a value… |
| [PAY_OLD_VALUE_DEFNS_F](Tables/PAY_OLD_VALUE_DEFNS_F.md) | This table contains details of how a value is calculated in payroll processing using range items, calculation types, and… |
| [PAY_OLD_VALUE_DEFNS_F_](Tables/PAY_OLD_VALUE_DEFNS_F_.md) | This table contains details of how a value is calculated in payroll processing using range items, calculation types, and… |
| [PAY_OLD_VALUE_DEFNS_TL](Tables/PAY_OLD_VALUE_DEFNS_TL.md) | This table contains translation information for PAY_VALUE_DEFINITIONS_F. |
| [PAY_ORG_PAYER_MAPPINGS_F](Tables/PAY_ORG_PAYER_MAPPINGS_F.md) | Rules used within an Organization Payment Method to determine the appropriate source bank account. |
| [PAY_ORG_PAY_METHODS_F](Tables/PAY_ORG_PAY_METHODS_F.md) | table to define payment methods for org |
| [PAY_ORG_PAY_METHODS_TL](Tables/PAY_ORG_PAY_METHODS_TL.md) | Holds translated information for PAY_ORG_PAY_METHODS_F. |
| [PAY_ORG_PAY_METHOD_USAGES_F](Tables/PAY_ORG_PAY_METHOD_USAGES_F.md) | Org Pay Method Usages is the Date Tracked table that stores details of the different payment methods that are used as pe… |
| [PAY_PARAM_CONTEXTS_B](Tables/PAY_PARAM_CONTEXTS_B.md) | this we will be utilizing in storing context name of parameter for security |
| [PAY_PARAM_CONTEXTS_TL](Tables/PAY_PARAM_CONTEXTS_TL.md) | Holds translated information for PAY_PARAM_CONTEXTS. |
| [PAY_PARAM_CONTEXT_DETAILS](Tables/PAY_PARAM_CONTEXT_DETAILS.md) | this we will be utilizing in storing context value for a parameter |
| [PAY_PAYMENT_COSTS](Tables/PAY_PAYMENT_COSTS.md) | This table contains the results from the Costing of Payments process to enable reconciliation with the Financials Cash A… |
| [PAY_PAYMENT_TYPES](Tables/PAY_PAYMENT_TYPES.md) | PAY_PAYMENT_TYPES holds the definitions of payment type. |
| [PAY_PAYMENT_TYPES_TL](Tables/PAY_PAYMENT_TYPES_TL.md) | Translated payment type details |
| [PAY_PAYROLL_ACTIONS](Tables/PAY_PAYROLL_ACTIONS.md) | This table contains general details of the execution of payroll processes, including their type and all parameters suppl… |
| [PAY_PAYROLL_REL_ACTIONS](Tables/PAY_PAYROLL_REL_ACTIONS.md) | This table contains details of the individuals processed in a payroll process. |
| [PAY_PAY_RELATIONSHIPS_DN](Tables/PAY_PAY_RELATIONSHIPS_DN.md) | Payroll relationships non datetrack table |
| [PAY_PAY_RELATIONSHIPS_F](Tables/PAY_PAY_RELATIONSHIPS_F.md) | PAY_PAYROLL_RELATIONSHIPS_F is used to store date effective information for Payroll Relationship. The Payroll Relationsh… |
| [PAY_PAY_SECURITY_PROFILES](Tables/PAY_PAY_SECURITY_PROFILES.md) | Table file for PAY_PAY_SECURITY_PROFILES |
| [PAY_PAY_SECURITY_PROFILES_](Tables/PAY_PAY_SECURITY_PROFILES_.md) | Table file for PAY_PAY_SECURITY_PROFILES |
| [PAY_PAY_SECURITY_PROFILE_PAYS](Tables/PAY_PAY_SECURITY_PROFILE_PAYS.md) | This table holds information of payroll security profiles. |
| [PAY_PAY_SECURITY_PROFILE_PAYS_](Tables/PAY_PAY_SECURITY_PROFILE_PAYS_.md) | This table holds information of payroll security profiles. |
| [PAY_PEOPLE_GROUPS](Tables/PAY_PEOPLE_GROUPS.md) | People group flexfield information. |
| [PAY_PERSON_PAY_METHODS_F](Tables/PAY_PERSON_PAY_METHODS_F.md) | personal payment methods definition |
| [PAY_PERSON_PAY_METHODS_F_](Tables/PAY_PERSON_PAY_METHODS_F_.md) | personal payment methods definition |
| [PAY_POPULATION_RANGES](Tables/PAY_POPULATION_RANGES.md) | This table contains ranges of people to be inserted as assignment actions, used to manage parallel running of payroll pr… |
| [PAY_PRE_PAYMENTS](Tables/PAY_PRE_PAYMENTS.md) | Pre-Payment details for an assignment, including the currency, the amount and the specific payment method. |
| [PAY_PROCESSES](Tables/PAY_PROCESSES.md) | This table contains payroll process information. |
| [PAY_PROCESS_CHANGES](Tables/PAY_PROCESS_CHANGES.md) | This table contains a functional audit of the processing of CIR Components. |
| [PAY_PROCESS_EVENTS](Tables/PAY_PROCESS_EVENTS.md) | This table contains general details of the execution of payroll processes, including their type and all parameters suppl… |
| [PAY_PROCESS_TIMINGS](Tables/PAY_PROCESS_TIMINGS.md) | This table contains the timings for processing areas. |
| [PAY_PURGE_OBJECTS](Tables/PAY_PURGE_OBJECTS.md) | This table is used to identify the objects that are to be purged from the syste, |
| [PAY_QUALIFIER_CRITERIA](Tables/PAY_QUALIFIER_CRITERIA.md) | This table contains details of whether a combination of element eligibility criteria is potentially matched by a combina… |
| [PAY_QUICKPAY_CIR_EXCLUSIONS](Tables/PAY_QUICKPAY_CIR_EXCLUSIONS.md) | This table contains a list of element entries that are to be excluded from a QuickPay run. |
| [PAY_QUICKPAY_EXCLUSIONS](Tables/PAY_QUICKPAY_EXCLUSIONS.md) | This table contains a list of element entries that are to be excluded from a QuickPay run. |
| [PAY_RANGE_DEFS_F](Tables/PAY_RANGE_DEFS_F.md) | This table contains the values or sets of values used in the calculation of a value definition. For example, for a value… |
| [PAY_RANGE_INSTS_F](Tables/PAY_RANGE_INSTS_F.md) | This table contains the values or sets of values used in the calculation of a value definition. For example, for a value… |
| [PAY_RATE_CONTRIBUTORS_F](Tables/PAY_RATE_CONTRIBUTORS_F.md) | This table contains the rate contributor information. A rate contributor is a value that contributes to a rate definitio… |
| [PAY_RATE_DEFINITIONS_F](Tables/PAY_RATE_DEFINITIONS_F.md) | This table contains the definition of a rate to be used by the rate engine. |
| [PAY_RATE_DEFINITIONS_F_TL](Tables/PAY_RATE_DEFINITIONS_F_TL.md) | This table contains translated information for PAY_RATE_DEFINITIONS_F. |
| [PAY_RATE_ELEMENT_INDIRECTS](Tables/PAY_RATE_ELEMENT_INDIRECTS.md) | This table is used by the Rates process to identify the indirect Element Types of an Element Type. |
| [PAY_RATE_VALUES](Tables/PAY_RATE_VALUES.md) | This table contains the calculated rate values for the Payroll Relationship. |
| [PAY_RECORDED_REQUESTS](Tables/PAY_RECORDED_REQUESTS.md) | This table contains dated process information. |
| [PAY_RELATIONSHIP_TYPES](Tables/PAY_RELATIONSHIP_TYPES.md) | This table holds a set of types that distguishes the Payroll Relationships |
| [PAY_RELATIONSHIP_TYPES_TL](Tables/PAY_RELATIONSHIP_TYPES_TL.md) | Holds translated information for PAY_RELATIONSHIP_TYPES. |
| [PAY_REL_GROUPS_DN](Tables/PAY_REL_GROUPS_DN.md) | Defines setup information for how payroll relationships behave within a legislation. |
| [PAY_REL_GROUPS_F](Tables/PAY_REL_GROUPS_F.md) | Defines setup information for how payroll relationships behave within a legislation. |
| [PAY_REL_GROUPS_USED](Tables/PAY_REL_GROUPS_USED.md) | This table contains details of the components of a person's configuration that were processed in a payroll run. |
| [PAY_REL_TYPE_MAPS](Tables/PAY_REL_TYPE_MAPS.md) | This allows the localisations to map the different types of Terms to a Relationship Type. |
| [PAY_REPORT_BLOCKS](Tables/PAY_REPORT_BLOCKS.md) | BLock description of extract blocks. |
| [PAY_REPORT_BLOCKS_TL](Tables/PAY_REPORT_BLOCKS_TL.md) | PAY_REPORT_BLOCKS_TL hold translated information for PAY_REPORT_BLOCKS. |
| [PAY_REPORT_CATEGORIES](Tables/PAY_REPORT_CATEGORIES.md) | Holds Report Category Definitions |
| [PAY_REPORT_CATEGORIES_TL](Tables/PAY_REPORT_CATEGORIES_TL.md) | translation table for pay_report_categories |
| [PAY_REPORT_DEFINITIONS](Tables/PAY_REPORT_DEFINITIONS.md) | report definition, containing information about mreporting block to be processed |
| [PAY_REPORT_FORMAT_MAPS_F](Tables/PAY_REPORT_FORMAT_MAPS_F.md) | Table for Report Format Mappings |
| [PAY_REPORT_FORMAT_MAPS_TL](Tables/PAY_REPORT_FORMAT_MAPS_TL.md) | Holds translated information for PAY_REPORT_FORMAT_MAPS_F. |
| [PAY_REPORT_FORMAT_PARAMS](Tables/PAY_REPORT_FORMAT_PARAMS.md) | Table for defining paramters for specfic reports |
| [PAY_REPORT_GROUPS](Tables/PAY_REPORT_GROUPS.md) | Used to identify a Group of report definitions and categories that are related. |
| [PAY_REPORT_RECORDS_F](Tables/PAY_REPORT_RECORDS_F.md) | Record for the extracts definition, used by reporting processing code |
| [PAY_REPORT_RECORDS_TL](Tables/PAY_REPORT_RECORDS_TL.md) | Holds translated information for PAY_REPORT_RECORDS_F. |
| [PAY_REPORT_REGISTER_GT](Tables/PAY_REPORT_REGISTER_GT.md) | This is a temporary table which is used internally by Oracle. |
| [PAY_REPORT_SORT_ITEMS](Tables/PAY_REPORT_SORT_ITEMS.md) | Defines the items that can be sorted in a balance group |
| [PAY_REPORT_SORT_ORDERS](Tables/PAY_REPORT_SORT_ORDERS.md) | Table for Order or Sorting in Reports |
| [PAY_REPORT_SORT_TYPES](Tables/PAY_REPORT_SORT_TYPES.md) | Holds the sort method information for a payroll report |
| [PAY_REPORT_SORT_TYPES_TL](Tables/PAY_REPORT_SORT_TYPES_TL.md) | Holds translated information for PAY_REPORT_SORT_TYPES. |
| [PAY_REPORT_VARIABLES](Tables/PAY_REPORT_VARIABLES.md) | This holds the information to generate the report via the Archiver processes, such as report template, source data, etc. |
| [PAY_REP_ARCHIVE_ITEMS](Tables/PAY_REP_ARCHIVE_ITEMS.md) | Archive table which holds parameter value information for a relationship action |
| [PAY_REP_CAT_COMPONENTS](Tables/PAY_REP_CAT_COMPONENTS.md) | Report Category Components table |
| [PAY_REP_CONTEXT_USAGES](Tables/PAY_REP_CONTEXT_USAGES.md) | Internal table to be used by archive process if context usages are required to be stored. |
| [PAY_REP_CRITERIA_F](Tables/PAY_REP_CRITERIA_F.md) | Table for Report Criteria information |
| [PAY_REP_FORMAT_HIERARCHY_F](Tables/PAY_REP_FORMAT_HIERARCHY_F.md) | PAY_REP_FORMAT_HIERARCHY_F is a date effective table that hold information about the hierarchy of payroll reports. |
| [PAY_REP_FORMAT_ITEMS_F](Tables/PAY_REP_FORMAT_ITEMS_F.md) | PAY_REP_FORMAT_ITEMS_F contains information about items within a report definition. |
| [PAY_REP_RECORD_RULES_F](Tables/PAY_REP_RECORD_RULES_F.md) | table to exclude report records from processing or to override them |
| [PAY_REP_SELECT_F](Tables/PAY_REP_SELECT_F.md) | Report Selection Information Table |
| [PAY_REQUESTS](Tables/PAY_REQUESTS.md) | PAY_REQUESTS_TABLE captures all the requests details for the flow |
| [PAY_REQUEST_ACTIONS](Tables/PAY_REQUEST_ACTIONS.md) | This table contains details of the requests made to process batch payroll processes. |
| [PAY_REST_SECURITY](Tables/PAY_REST_SECURITY.md) | This table contains pay rest security name and class definition. |
| [PAY_REST_SECURITY_USAGES](Tables/PAY_REST_SECURITY_USAGES.md) | This table contains usage of pay rest. |
| [PAY_REST_VOS](Tables/PAY_REST_VOS.md) | This table contains register VO names which can be accessed by generic rest webservice. |
| [PAY_RETRO_COMPONENTS](Tables/PAY_RETRO_COMPONENTS.md) | This table contains legislative details of how retropay should process. |
| [PAY_RETRO_COMP_USAGES](Tables/PAY_RETRO_COMP_USAGES.md) | This table contains legislative details of how a new element should behave for retropay processing. |
| [PAY_RETRO_DEFINITIONS](Tables/PAY_RETRO_DEFINITIONS.md) | This table contains the definition for the recalculation of a payroll run for a person because of backdated changes. |
| [PAY_RETRO_DEFN_COMPS](Tables/PAY_RETRO_DEFN_COMPS.md) | This table contains legislative details of how retropay should process, such as whether to use corrective, backdated or … |
| [PAY_RETRO_ENTRIES](Tables/PAY_RETRO_ENTRIES.md) | This table contains entries that have retrospective changes and thus require reprocessing |
| [PAY_RULES_F](Tables/PAY_RULES_F.md) | This table contains business rule definitions, which generate fast formulas to extend basic validation for costing overr… |
| [PAY_RULE_QUALIFIERS_F](Tables/PAY_RULE_QUALIFIERS_F.md) | This table contains the qualifiers being applied to defined costing rules. |
| [PAY_RULE_QUAL_LINES_F](Tables/PAY_RULE_QUAL_LINES_F.md) | This table contains the qualifier conditions for selecting a defined costing rule. |
| [PAY_RULE_RESULTS_F](Tables/PAY_RULE_RESULTS_F.md) | This table contains the sequence in which costing override rules are applied for a specific business rule. |
| [PAY_RULE_RESULT_LINES_F](Tables/PAY_RULE_RESULT_LINES_F.md) | This table contains costing accounts assigned to a costing rule. |
| [PAY_RULE_SEGMENTS_F](Tables/PAY_RULE_SEGMENTS_F.md) | This table contains the cost allocation segment for which a costing rule is defined. |
| [PAY_RUN_BALANCES](Tables/PAY_RUN_BALANCES.md) | This table contains calculated run-level balance values, which are used for performant balance calculations. |
| [PAY_RUN_RESULTS](Tables/PAY_RUN_RESULTS.md) | This table contains the result of processing a single element entry. |
| [PAY_RUN_RESULT_VALUES](Tables/PAY_RUN_RESULT_VALUES.md) | This table contains result values from processing a single element entry. |
| [PAY_RUN_TYPES_F](Tables/PAY_RUN_TYPES_F.md) | The different types of Payroll Run processing |
| [PAY_RUN_TYPES_TL](Tables/PAY_RUN_TYPES_TL.md) | Holds translated information for PAY_RUN_TYPES_F. |
| [PAY_RUN_TYPE_ORG_METHODS_F](Tables/PAY_RUN_TYPE_ORG_METHODS_F.md) | Organisation level payment methods associated with a particular run type. |
| [PAY_RUN_TYPE_USAGES_F](Tables/PAY_RUN_TYPE_USAGES_F.md) | Holds child run types where the run type parent is of type Cumulative. |
| [PAY_SHDW_DIR_CARD_COMPONENTS_F](Tables/PAY_SHDW_DIR_CARD_COMPONENTS_F.md) | This table contains the details of a person's deduction card. |
| [PAY_SHDW_DIR_COMP_DETAILS_F](Tables/PAY_SHDW_DIR_COMP_DETAILS_F.md) | This table contains any flexfield data defined for components of the deduction card. |
| [PAY_SHDW_DIR_REP_CARDS_F](Tables/PAY_SHDW_DIR_REP_CARDS_F.md) | This table contains the association between a card, or a section of a card, and a tax reporting unit, thus forming a rep… |
| [PAY_SHDW_DIR_REP_CARD_USAGES_F](Tables/PAY_SHDW_DIR_REP_CARD_USAGES_F.md) | This table contains mappings of deduction components to employment terms or assignments within a reporting card. |
| [PAY_SHDW_OLD_RANGE_ITEMS_F](Tables/PAY_SHDW_OLD_RANGE_ITEMS_F.md) | This table contains the values or sets of values used in the calculation of a value definition. For example, for a value… |
| [PAY_SHDW_OLD_VALUE_DEFNS_F](Tables/PAY_SHDW_OLD_VALUE_DEFNS_F.md) | This table contains details of how a value is calculated in payroll processing using range items, calculation types, and… |
| [PAY_STATISTICS](Tables/PAY_STATISTICS.md) | Stores the statistics for payroll. based on the types available in statistics types. |
| [PAY_STATISTIC_CONTEXTS](Tables/PAY_STATISTIC_CONTEXTS.md) | It stores the all possible context, against which statistics can be stored. |
| [PAY_STATISTIC_CONTEXTS_TL](Tables/PAY_STATISTIC_CONTEXTS_TL.md) | Holds translated information for PAY_STATISTIC_CONTEXTS. |
| [PAY_STATISTIC_CONTEXT_VALUES](Tables/PAY_STATISTIC_CONTEXT_VALUES.md) | Stores context values, against contexts available in pay_statistic_contexts. |
| [PAY_STATISTIC_CONTEXT_VALUE_TL](Tables/PAY_STATISTIC_CONTEXT_VALUE_TL.md) | Holds translated information for PAY_STATISTIC_CONTEXT_VALUES |
| [PAY_STATISTIC_TYPES](Tables/PAY_STATISTIC_TYPES.md) | Stroes types of statistics , that are available in payroll. |
| [PAY_STATISTIC_TYPES_TL](Tables/PAY_STATISTIC_TYPES_TL.md) | Holds translated information for PAY_STATISTIC_TYPES. |
| [PAY_STATS_FLOW_ACTIONS](Tables/PAY_STATS_FLOW_ACTIONS.md) | PAY_STATS_FLOW_ACTIONS table created for payroll flows subject area |
| [PAY_STATUS_PROC_RULES_F](Tables/PAY_STATUS_PROC_RULES_F.md) | This table contains the processing rules or formula for each element for a specific assignment statuses. For example, sa… |
| [PAY_SUBMIT_RELATED_FLOWS](Tables/PAY_SUBMIT_RELATED_FLOWS.md) | this will be utilized in Payrollflow s |
| [PAY_SUB_CLASSN_RULES_F](Tables/PAY_SUB_CLASSN_RULES_F.md) | This table contains the rules that define which elements are included in a sub or secondary classification. For payrolls… |
| [PAY_TASKS](Tables/PAY_TASKS.md) | PAY_TASK describes the tasks that can take part in process flows |
| [PAY_TASKS_TL](Tables/PAY_TASKS_TL.md) | Translation table for pay_tasks |
| [PAY_TASK_ACTIONS](Tables/PAY_TASK_ACTIONS.md) | PAY _TASK_ACTIONS TABLE TO STORE PAYROLLFLOWS ACTIONS |
| [PAY_TASK_ACTIONS_TL](Tables/PAY_TASK_ACTIONS_TL.md) | Translate table for PAY_TASK_ACTIONS |
| [PAY_TASK_PARAMETERS](Tables/PAY_TASK_PARAMETERS.md) | pay_task_parameters captures the parameters  required to execute a task |
| [PAY_TASK_PARAMETERS_TL](Tables/PAY_TASK_PARAMETERS_TL.md) | Holds translated information for PAY_TASK_PARAMETERS. |
| [PAY_TASK_PROPERTIES](Tables/PAY_TASK_PROPERTIES.md) | Properties table captures properties as name value pairs to support the execution of tasks |
| [PAY_TASK_PROPERTIES_TL](Tables/PAY_TASK_PROPERTIES_TL.md) | Holds translated information for PAY_TASK_PROPERTIES. |
| [PAY_TASK_USAGE](Tables/PAY_TASK_USAGE.md) | It will be utilized by Payroll Flow |
| [PAY_TAXABILITY_RULES_F](Tables/PAY_TAXABILITY_RULES_F.md) | This table contains the taxability rules for tax types and element classifications for localizations. For example, an ea… |
| [PAY_TEMPLATES](Tables/PAY_TEMPLATES.md) | This Table Stores the Template Information Like its name etc |
| [PAY_TEMPLATE_CORE_OBJECTS](Tables/PAY_TEMPLATE_CORE_OBJECTS.md) | Template Core Object keeps track of the core schema objects generated from element templates. e.g. Elements, Input Value… |
| [PAY_TEMPORAL_VALUES](Tables/PAY_TEMPORAL_VALUES.md) | This table contains values that can change over time. |
| [PAY_TEMP_ACTION_INFORMATION](Tables/PAY_TEMP_ACTION_INFORMATION.md) | Table for Payroll Action Information |
| [PAY_TEMP_BAL_ADJUSTMENTS](Tables/PAY_TEMP_BAL_ADJUSTMENTS.md) | This table contains temporary balance adjustment records, created by the Balance Initialization process, to calculate co… |
| [PAY_TEMP_OBJECT_ACTIONS](Tables/PAY_TEMP_OBJECT_ACTIONS.md) | This table contains temporary actions that are only required while a process is in progress. |
| [PAY_TEMP_PAYROLL_ACTIONS](Tables/PAY_TEMP_PAYROLL_ACTIONS.md) | This table contains general details of the execution of payroll processes, including their type and all parameters suppl… |
| [PAY_TIME_DEFINITIONS](Tables/PAY_TIME_DEFINITIONS.md) | This table contains details of period of time. |
| [PAY_TIME_DEF_USAGES](Tables/PAY_TIME_DEF_USAGES.md) | This table contains the usage type for each time definition, such as balance retrieval or proration. |
| [PAY_TIME_DEPEND_VALUES](Tables/PAY_TIME_DEPEND_VALUES.md) | This table hold the definition of a value that can change over time. |
| [PAY_TIME_PERIODS](Tables/PAY_TIME_PERIODS.md) | This table contains the payroll calendar used as the basis for regular payroll processing. |
| [PAY_TIME_PERIOD_RULES](Tables/PAY_TIME_PERIOD_RULES.md) | This table contains the internal rules used to define specific time periods. |
| [PAY_TIME_PERIOD_TYPES](Tables/PAY_TIME_PERIOD_TYPES.md) | This table contains the predefined list of valid period types used to define calendars for payroll processing. |
| [PAY_TIME_SPANS](Tables/PAY_TIME_SPANS.md) | This table contains details of time spans used to create time definitions. |
| [PAY_TMPLT_CLMN_INST](Tables/PAY_TMPLT_CLMN_INST.md) | This Table Holds the clmn instances for template data |
| [PAY_TMPLT_CLMN_INST_F](Tables/PAY_TMPLT_CLMN_INST_F.md) | This Date Effctive Table Holds the clmn instances for template data |
| [PAY_TMPLT_CLMN_INST_GT](Tables/PAY_TMPLT_CLMN_INST_GT.md) | This Table Holds the clmn instances for template data |
| [PAY_TMPLT_CLMN_INST_TRANS_B](Tables/PAY_TMPLT_CLMN_INST_TRANS_B.md) | This Table Holds the clmn instances for template data |
| [PAY_TMPLT_CLMN_INST_TRANS_F](Tables/PAY_TMPLT_CLMN_INST_TRANS_F.md) | This Table Holds the clmn instances for template data |
| [PAY_TMPLT_CLMN_INST_TRANS_F_TL](Tables/PAY_TMPLT_CLMN_INST_TRANS_F_TL.md) | This Table Holds the clmn instances for template data |
| [PAY_TMPLT_CLMN_INST_TRANS_TL](Tables/PAY_TMPLT_CLMN_INST_TRANS_TL.md) | This Table Holds the clmn instances for template data |
| [PAY_TMPLT_COL_INFO](Tables/PAY_TMPLT_COL_INFO.md) | This holds the attribute definition for a given entity. E.g. For the Person entity the Row Instance should hold the info… |
| [PAY_TMPLT_DSGN_PTRN](Tables/PAY_TMPLT_DSGN_PTRN.md) | This holds various design patterns available for a given functional area. E.g. An Element Template might have various pa… |
| [PAY_TMPLT_ENT_RULE_USGS](Tables/PAY_TMPLT_ENT_RULE_USGS.md) | This entity indicated how a rule (i.e. a question) can be used to exclude a record or another rule. |
| [PAY_TMPLT_ENT_RULE_USGS_F](Tables/PAY_TMPLT_ENT_RULE_USGS_F.md) | This entity indicated how a rule (i.e. a question) can be used to exclude a record or another rule. |
| [PAY_TMPLT_EXCLUDE_LIST_GT](Tables/PAY_TMPLT_EXCLUDE_LIST_GT.md) | This table holds row instances eligible for exclusion. |
| [PAY_TMPLT_FUN_AREAS](Tables/PAY_TMPLT_FUN_AREAS.md) | Functional are contains various patterns for a given feature. A template can have various functional areas to segregate … |
| [PAY_TMPLT_PTRN_ENT_USGS](Tables/PAY_TMPLT_PTRN_ENT_USGS.md) | This entity indicates which records are applicable for a given design pattern. |
| [PAY_TMPLT_PTRN_RULE_USGS](Tables/PAY_TMPLT_PTRN_RULE_USGS.md) | This entity indicates which rules/questions are applicable for a given design pattern. For example the question "Process… |
| [PAY_TMPLT_PTRN_SELECT](Tables/PAY_TMPLT_PTRN_SELECT.md) | This holds the pattern selection based on the available list of patterns for a given Functional Area. E.g. For back date… |
| [PAY_TMPLT_ROW_INST](Tables/PAY_TMPLT_ROW_INST.md) | This table would store the Seeded Row Instance and transactional row instances |
| [PAY_TMPLT_ROW_INST_F](Tables/PAY_TMPLT_ROW_INST_F.md) | This table would store the Seeded Row Instance and transactional row instances |
| [PAY_TMPLT_ROW_INST_GT](Tables/PAY_TMPLT_ROW_INST_GT.md) | This table would store the Seeded Row Instance and transactional row instances |
| [PAY_TMPLT_RULES](Tables/PAY_TMPLT_RULES.md) | This Table holds the Rule Information for The element Template Wizard |
| [PAY_TMPLT_RULES_F](Tables/PAY_TMPLT_RULES_F.md) | This Table holds the Rule Information for The element Template Wizard |
| [PAY_TMPLT_RULES_F_TL](Tables/PAY_TMPLT_RULES_F_TL.md) | Holds translated information for PAY_TMPLT_RULES. |
| [PAY_TMPLT_RULES_TL](Tables/PAY_TMPLT_RULES_TL.md) | Holds translated information for PAY_TMPLT_RULES. |
| [PAY_TMPLT_RULE_DEPENDENCIES](Tables/PAY_TMPLT_RULE_DEPENDENCIES.md) | This Table holds meta data for dependency storage |
| [PAY_TMPLT_RULE_DEPENDENCIES_F](Tables/PAY_TMPLT_RULE_DEPENDENCIES_F.md) | This Table holds meta data for dependency storage |
| [PAY_TMPLT_RULE_GROUPS](Tables/PAY_TMPLT_RULE_GROUPS.md) | Holds details of the grouping of the template rules which are used in the display of the template |
| [PAY_TMPLT_RULE_GROUPS_F](Tables/PAY_TMPLT_RULE_GROUPS_F.md) | Holds details of the grouping of the template rules which are used in the display of the template |
| [PAY_TMPLT_RULE_GROUPS_F_TL](Tables/PAY_TMPLT_RULE_GROUPS_F_TL.md) | Holds translated information for PAY_TMPLT_RULE_GROUPS. |
| [PAY_TMPLT_RULE_GROUPS_TL](Tables/PAY_TMPLT_RULE_GROUPS_TL.md) | Holds translated information for PAY_TMPLT_RULE_GROUPS. |
| [PAY_TMPLT_RULE_GR_USAGES](Tables/PAY_TMPLT_RULE_GR_USAGES.md) | This Table will hold the relatoinship between the rules and the template |
| [PAY_TMPLT_RULE_GR_USAGES_F](Tables/PAY_TMPLT_RULE_GR_USAGES_F.md) | This Table will hold the relatoinship between the rules and the template |
| [PAY_TMPLT_RULE_VALUES](Tables/PAY_TMPLT_RULE_VALUES.md) | This is a transaction table used to store the rule values |
| [PAY_TMPLT_TABLE_INFO](Tables/PAY_TMPLT_TABLE_INFO.md) | This holds the definition of an entity within the Template Solution. E.g. A Person entity or an object can be registered… |
| [PAY_TMPLT_TABLE_RELATE](Tables/PAY_TMPLT_TABLE_RELATE.md) | This Entity stores the relationship details of tables seeded in Table Information & Table Column Information |
| [PAY_TMPLT_VERSION_F](Tables/PAY_TMPLT_VERSION_F.md) | Vesion data for template tables. |
| [PAY_TMPLT_VERSION_F_TL](Tables/PAY_TMPLT_VERSION_F_TL.md) | Vesion data for template tables. |
| [PAY_UPGRADE_LEGISLATIONS](Tables/PAY_UPGRADE_LEGISLATIONS.md) | This Table is used to enable/disable the Upgrade for particular legislation. |
| [PAY_UPGRADE_OBJECTS](Tables/PAY_UPGRADE_OBJECTS.md) | This Table is used to capture the Object change which will be used for the upgrade process. |
| [PAY_UPGRADE_OBJECTS_TL](Tables/PAY_UPGRADE_OBJECTS_TL.md) | This Table is used to capture the Object change which will be used for the upgrade process. |
| [PAY_UPGRADE_OBJECT_STATUS](Tables/PAY_UPGRADE_OBJECT_STATUS.md) | This is used to store the status of the upgrade process |
| [PAY_USED_IN_PROCESS](Tables/PAY_USED_IN_PROCESS.md) | This table contains the object information used in the process. |
| [PAY_VALUE_CRITERIA_LEVELS_F](Tables/PAY_VALUE_CRITERIA_LEVELS_F.md) | This defined the default levels of the Value by Criteria Tree |
| [PAY_VALUE_CRITERIA_LEVELS_TL](Tables/PAY_VALUE_CRITERIA_LEVELS_TL.md) | This translates the default levels of the Value by Criteria Tree |
| [PAY_VALUE_DEFS_F](Tables/PAY_VALUE_DEFS_F.md) | This table contains details of how a value is calculated in payroll processing using range items, calculation types, and… |
| [PAY_VALUE_DEFS_TL](Tables/PAY_VALUE_DEFS_TL.md) | This table contains translation information for PAY_VALUE_DEFS_F. |
| [PAY_VALUE_GROUPS](Tables/PAY_VALUE_GROUPS.md) | This table contains a logical grouping of deduction value definitions, such as an income tax group that includes the val… |
| [PAY_VALUE_GROUPS_TL](Tables/PAY_VALUE_GROUPS_TL.md) | This table contains translation information for PAY_VALUE_GROUPS. |
| [PAY_VALUE_INSTS_F](Tables/PAY_VALUE_INSTS_F.md) | This table contains details of how a value is calculated in payroll processing using range items, calculation types, and… |
| [PAY_VALUE_USAGES](Tables/PAY_VALUE_USAGES.md) | This table contains restrictions based on context values for the selection of deduction ranges into calculation units. |
| [PAY_VBC_CRITERIA_DEFS](Tables/PAY_VBC_CRITERIA_DEFS.md) | This table holds the definition of Criteria in Value by Criteria. |
| [PAY_VBC_CRITERIA_DEFS_TL](Tables/PAY_VBC_CRITERIA_DEFS_TL.md) | This table contains translation information for PAY_VBC_CRITERIA_DEFS. |
| [PAY_VBC_DEFINITIONS](Tables/PAY_VBC_DEFINITIONS.md) | This table holds the definition of Value by Criteria. |
| [PAY_VBC_DEFINITIONS_TL](Tables/PAY_VBC_DEFINITIONS_TL.md) | This table contains translation information for PAY_VBC_DEFINITIONS. |
| [PAY_VBC_VALUE_IDENTS](Tables/PAY_VBC_VALUE_IDENTS.md) | This table contains the definitions of Values in Value By Criteria. |
| [PAY_VBC_VALUE_IDENTS_TL](Tables/PAY_VBC_VALUE_IDENTS_TL.md) | This table contains translation information for PAY_VBC_VALUE_IDENTS. |
| [PAY_VENDOR_MAPPINGS](Tables/PAY_VENDOR_MAPPINGS.md) | This table contains internal values mapped to values in third-party applications that the Payroll application directly i… |
| [PAY_XLA_EVENTS](Tables/PAY_XLA_EVENTS.md) | This table contains the cost details and values of a worker's payroll results. |
