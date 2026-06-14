# 31_Workforce_Management — Tables Index

**Total Tables:** 195

| Name                                               | Description |
|----------------------------------------------------|-------------|
| [HWM_ALLOCATIONS_HDR_F](Tables/HWM_ALLOCATIONS_HDR_F.md) | Time Allocations header table is effective dated parent table to all other allocation tables. It contains allocation id,… |
| [HWM_ALLOCATIONS_HDR_TL](Tables/HWM_ALLOCATIONS_HDR_TL.md) | Time Allocations Header translate table stores time allocation translatable description column. |
| [HWM_ALLOCATION_ATTRIBUTE_F](Tables/HWM_ALLOCATION_ATTRIBUTE_F.md) | Time Allocations attributes table contains list of all Attributes used by allocation UI , by Rule level. |
| [HWM_ALLOCATION_LINES_F](Tables/HWM_ALLOCATION_LINES_F.md) | Time Allocations lines table contains detail allocation values per each Allocation Rule row. |
| [HWM_ALLOCATION_LN_ATRBS_F](Tables/HWM_ALLOCATION_LN_ATRBS_F.md) | Time Allocations Line Attributes table contains list of attributes and value for each Allocation Line row. |
| [HWM_ALLOCATION_RESOURCES_F](Tables/HWM_ALLOCATION_RESOURCES_F.md) | Time Allocations Resource table is effective dated table that associates a resource to Time allocation definition in Tim… |
| [HWM_ALLOCATION_RULES_F](Tables/HWM_ALLOCATION_RULES_F.md) | Time Allocations Rules table contains Rules based on Time Category and Allocation type. This table is parent to Time All… |
| [HWM_ANC_INTERFACE_DIAG](Tables/HWM_ANC_INTERFACE_DIAG.md) | This table is used for logging decoupling details , for exceptions or for debugging purposes |
| [HWM_ATTENDANCE_PERSON_PROCS](Tables/HWM_ATTENDANCE_PERSON_PROCS.md) | table to maintain person processing information for attendance tracking |
| [HWM_ATTENDANCE_RULE_SET_PROCS](Tables/HWM_ATTENDANCE_RULE_SET_PROCS.md) | table to maintain ruleset processing information for attendace tracking |
| [HWM_ATTENDANCE_VIOLATIONS](Tables/HWM_ATTENDANCE_VIOLATIONS.md) | table to store attendance violations |
| [HWM_BATCH_OBJECTS](Tables/HWM_BATCH_OBJECTS.md) | Instances of a process execution to load time records into the workforce management repository |
| [HWM_BATCH_OBJ_MESSAGES](Tables/HWM_BATCH_OBJ_MESSAGES.md) | Instances of a process execution to load time records into the workforce management repository |
| [HWM_BATCH_PROCESSES](Tables/HWM_BATCH_PROCESSES.md) | This table holds information about the various processes executed when loading time into the repository.  For example, t… |
| [HWM_BATCH_PROC_INSTANCES](Tables/HWM_BATCH_PROC_INSTANCES.md) | Instances of a process execution to load time records into the workforce management repository |
| [HWM_BATCH_RANGES](Tables/HWM_BATCH_RANGES.md) | Instances of a process execution to load time records into the workforce management repository |
| [HWM_BATCH_THRD_LOGS](Tables/HWM_BATCH_THRD_LOGS.md) | State of an object to be stored during process execution to load time records into the workforce management repository |
| [HWM_CHANGE_EVENTS](Tables/HWM_CHANGE_EVENTS.md) | The table stores records of changes made to specific objects (e.g., Absence, Assignment) as received from an Atom feed. … |
| [HWM_CHANGE_EVENT_SET](Tables/HWM_CHANGE_EVENT_SET.md) | The table stores metadata about event change sets, which represent a collection of changes made to specific objects (e.g… |
| [HWM_CRITERIA_BINDS](Tables/HWM_CRITERIA_BINDS.md) | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compa… |
| [HWM_DATA_SOURCES_B](Tables/HWM_DATA_SOURCES_B.md) | Base Table for the Data Sources. Each source of data from the time consumers is handled with in WFM as Data Sources. Thi… |
| [HWM_DATA_SOURCES_TL](Tables/HWM_DATA_SOURCES_TL.md) | This is a  TL table & acts the data source for the information used in repository. |
| [HWM_DATA_SOURCE_ATTRIBUTES](Tables/HWM_DATA_SOURCE_ATTRIBUTES.md) | This table stores the information about the attributes of Data Source. |
| [HWM_DATA_SOURCE_CRITERIAS](Tables/HWM_DATA_SOURCE_CRITERIAS.md) | Stores the criteria for the data sources against the appropriate usage(i.e) ADMIN, USER (or) Both. |
| [HWM_DATA_SOURCE_USAGES](Tables/HWM_DATA_SOURCE_USAGES.md) | Table storing the mapping between the Data Source and the Time Attribute Field. It also contains the mapping for the def… |
| [HWM_DS_API_CLASSES_B](Tables/HWM_DS_API_CLASSES_B.md) | Stores API Class for Dynamic Script |
| [HWM_DS_API_CLASSES_TL](Tables/HWM_DS_API_CLASSES_TL.md) | Stores translatable information on the API Class for Dynamic Script |
| [HWM_DS_SCRIPTS_F](Tables/HWM_DS_SCRIPTS_F.md) | Contains the actual script for Dynamic Scripts. |
| [HWM_DT_SRC_USG_BND_VALS](Tables/HWM_DT_SRC_USG_BND_VALS.md) | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compa… |
| [HWM_GRPS_B](Tables/HWM_GRPS_B.md) | This table contains details for HCM groups |
| [HWM_GRPS_TL](Tables/HWM_GRPS_TL.md) | Contains Translated values for Group Defintion |
| [HWM_GRP_CRITERIA](Tables/HWM_GRP_CRITERIA.md) | Contains Criteria for Group Defintion |
| [HWM_GRP_EVAL_PROCESSES](Tables/HWM_GRP_EVAL_PROCESSES.md) | Contains Group Evaluation Process Run Details |
| [HWM_GRP_INCL_GRPS](Tables/HWM_GRP_INCL_GRPS.md) | Contains Included Groups for Group Defintion |
| [HWM_GRP_INCL_MEMBERS](Tables/HWM_GRP_INCL_MEMBERS.md) | Contains Included Members for Group Defintion |
| [HWM_GRP_MEMBERS_AUDIT](Tables/HWM_GRP_MEMBERS_AUDIT.md) | Contains group members table updation Information. |
| [HWM_GRP_MEMBERS_F](Tables/HWM_GRP_MEMBERS_F.md) | Contains Group Membership Information |
| [HWM_GRP_MEMBERS_F_](Tables/HWM_GRP_MEMBERS_F_.md) | Contains Group Membership Information |
| [HWM_GRP_PROC_EVT_QUE](Tables/HWM_GRP_PROC_EVT_QUE.md) | This stores info from the Events generated. |
| [HWM_GRP_TYPE](Tables/HWM_GRP_TYPE.md) | A type of time record group.  For example, an absence header, which contains a collection of absence entries.  Or, a tim… |
| [HWM_INTERACT_QSNR_USAGES](Tables/HWM_INTERACT_QSNR_USAGES.md) | Stores cross refence ids between Time card repository,  Attestation group set  and Talent's questioner table |
| [HWM_INTERACT_SETS](Tables/HWM_INTERACT_SETS.md) | Contains  group heade information  for questioner Attestation group set |
| [HWM_INTERACT_SET_LNS](Tables/HWM_INTERACT_SET_LNS.md) | Stores list of questioner IDs and conditions for Attestation group set |
| [HWM_LAYER](Tables/HWM_LAYER.md) | A type of time collection in the repository.  For example, reported time, which corresponds to the time card time record… |
| [HWM_PER_TZ_OVERRIDES](Tables/HWM_PER_TZ_OVERRIDES.md) | This table is designed to store time zone overrides of a person against the primary assignment. |
| [HWM_PER_TZ_OVERRIDES_](Tables/HWM_PER_TZ_OVERRIDES_.md) | This table is designed to store time zone overrides of a person against the primary assignment. |
| [HWM_PROCESSES_B](Tables/HWM_PROCESSES_B.md) | This table holds information about the various processes executed when loading time into the repository.  For example, t… |
| [HWM_PROCESSES_TL](Tables/HWM_PROCESSES_TL.md) | Indicates the code of the language into which the contents of the translatable columns are translated. |
| [HWM_PROCESS_COMPONENTS](Tables/HWM_PROCESS_COMPONENTS.md) | Table can be used to add components to a  process. |
| [HWM_PROCESS_CONDITIONS](Tables/HWM_PROCESS_CONDITIONS.md) | This table indication which components needs to run in a process. |
| [HWM_PROCESS_MODES](Tables/HWM_PROCESS_MODES.md) | A process execution mode, for example, save time or absence submit. |
| [HWM_PROCESS_USAGES](Tables/HWM_PROCESS_USAGES.md) | Identifies which process components are used in a particular process mode. |
| [HWM_RP_TM_PATTERNS](Tables/HWM_RP_TM_PATTERNS.md) | A table for specifying Patterns in terms of Range & Steps. |
| [HWM_RP_TM_PERIODS_B](Tables/HWM_RP_TM_PERIODS_B.md) | Repeating Time Periods Base table |
| [HWM_RP_TM_PERIODS_TL](Tables/HWM_RP_TM_PERIODS_TL.md) | A period of time used to group time entries |
| [HWM_RP_TM_RESOLVED](Tables/HWM_RP_TM_RESOLVED.md) | This table holds the generated repeating period. |
| [HWM_RULES](Tables/HWM_RULES.md) | Contains the rules created for OTL Time Calculation, Time Entry and Time Audit rules. |
| [HWM_RULES_CNDL](Tables/HWM_RULES_CNDL.md) | Conditional Rule Set table, which holds the members of conditional Rules. |
| [HWM_RULES_CNDL_MBRS](Tables/HWM_RULES_CNDL_MBRS.md) | Conditional Rule Members of Time Calculation Rules are stored in this table. |
| [HWM_RULE_FF_WORKAREA](Tables/HWM_RULE_FF_WORKAREA.md) | Contains the rules created for OTL Time Calculation, Time Entry and Time Audit rules. |
| [HWM_RULE_FF_WORK_LOG](Tables/HWM_RULE_FF_WORK_LOG.md) | Contains the logs created for OTL Time Calculation, Time Entry and Time Audit rules. |
| [HWM_RULE_INPUTS](Tables/HWM_RULE_INPUTS.md) | Stores Rule Templates Input PArameters for Formula/Script |
| [HWM_RULE_OUTPUTS](Tables/HWM_RULE_OUTPUTS.md) | An output from a rule used in further processing |
| [HWM_RULE_RUN_INFO_HDR](Tables/HWM_RULE_RUN_INFO_HDR.md) | Contains the rules created for OTL Time Calculation, Time Entry and Time Audit rules. |
| [HWM_RULE_RUN_INFO_LINE](Tables/HWM_RULE_RUN_INFO_LINE.md) | Contains the rules created for OTL Time Calculation, Time Entry and Time Audit rules. |
| [HWM_RULE_SETS_F](Tables/HWM_RULE_SETS_F.md) | Contains the rule sets created for OTL Time Calculation, Time Entry, Time device, and Time Audit rules. |
| [HWM_RULE_SET_CONDS](Tables/HWM_RULE_SET_CONDS.md) | Contains Conditions associated to the Rule Set. Each row has a sequence of precessing the condition. |
| [HWM_RULE_SET_MBRS](Tables/HWM_RULE_SET_MBRS.md) | Contains members of Time Rule Set. Each row has a sequence of precessing the Rule or Rule set and Time category. |
| [HWM_RULE_TMPLTS](Tables/HWM_RULE_TMPLTS.md) | Specifies formula and input and output variables for use with rule instances. |
| [HWM_RULE_TMPLTS_TL](Tables/HWM_RULE_TMPLTS_TL.md) | Specifies formula and input and output variables for use with rule instances. |
| [HWM_RULE_TMPLT_INPUTS](Tables/HWM_RULE_TMPLT_INPUTS.md) | Stores Rule Templates Input PArameters for Formula/Script |
| [HWM_RULE_TMPLT_INPUTS_TL](Tables/HWM_RULE_TMPLT_INPUTS_TL.md) | Translatable information of an instance of the output from a rule template, for example, a return message indicating an … |
| [HWM_RULE_TMPLT_USAGES](Tables/HWM_RULE_TMPLT_USAGES.md) | Instance of the output from a rule template, for example, a return message indicating an issue with the time sent to the… |
| [HWM_RULE_TMPLT_USAGES_TL](Tables/HWM_RULE_TMPLT_USAGES_TL.md) | Translatable information of an instance of the output from a rule template, for example, a return message indicating an … |
| [HWM_SETUP_PROPERTIES](Tables/HWM_SETUP_PROPERTIES.md) | To store Time Decimal format as property values against Properties. |
| [HWM_TCATS_B](Tables/HWM_TCATS_B.md) | This table is used to store the time categories id. |
| [HWM_TCATS_TL](Tables/HWM_TCATS_TL.md) | This is a translatable table used to store the translated name of the time category. |
| [HWM_TCAT_CMPS](Tables/HWM_TCAT_CMPS.md) | This table stores all the components. |
| [HWM_TCAT_EXPR_RESULTS_B](Tables/HWM_TCAT_EXPR_RESULTS_B.md) | This is the base table for storing the expression results. |
| [HWM_TCAT_EXPR_RESULTS_TL](Tables/HWM_TCAT_EXPR_RESULTS_TL.md) | This is the translatable table for expression results. |
| [HWM_TCAT_LOGIC_EXPRS](Tables/HWM_TCAT_LOGIC_EXPRS.md) | This table will store the logic expression. |
| [HWM_TCAT_USAGES](Tables/HWM_TCAT_USAGES.md) | Time categories for a time record or time record group within the workforce management repository. |
| [HWM_TCD_EXP_DATA_DEF_B](Tables/HWM_TCD_EXP_DATA_DEF_B.md) | TCD Export Data Definition Basic Table |
| [HWM_TCD_EXP_DATA_DEF_TL](Tables/HWM_TCD_EXP_DATA_DEF_TL.md) | TCD Export Data Definition Translation Table |
| [HWM_TCD_EXP_DATA_ESS_PROCESS](Tables/HWM_TCD_EXP_DATA_ESS_PROCESS.md) | TCD EXPORT DATA ESS PROCESS TABLE |
| [HWM_TCD_EXP_DATA_PAY](Tables/HWM_TCD_EXP_DATA_PAY.md) | This table contains details for Time Clock Device export data for Payroll Object |
| [HWM_TCD_EXP_DATA_PAY_TXN](Tables/HWM_TCD_EXP_DATA_PAY_TXN.md) | This table contains details for Time Clock Device export data for Payroll Transactions |
| [HWM_TCD_EXP_DATA_PER](Tables/HWM_TCD_EXP_DATA_PER.md) | This table contains details for Time Clock Device export data for Person Object |
| [HWM_TCD_EXP_DATA_PER_BDG](Tables/HWM_TCD_EXP_DATA_PER_BDG.md) | This table contains details for Time Clock Device export data for Person Badge Object |
| [HWM_TCD_EXP_DATA_PER_BDG_TXN](Tables/HWM_TCD_EXP_DATA_PER_BDG_TXN.md) | This table contains details for Time Clock Device export data for Person Badge Transactions |
| [HWM_TCD_EXP_DATA_PER_TXN](Tables/HWM_TCD_EXP_DATA_PER_TXN.md) | This table contains details for Time Clock Device export data for Person Transactions |
| [HWM_TCD_EXP_DATA_SCH](Tables/HWM_TCD_EXP_DATA_SCH.md) | This table contains details for Time Clock Device export data for Schedule |
| [HWM_TCD_EXP_DATA_SCH_SHFT](Tables/HWM_TCD_EXP_DATA_SCH_SHFT.md) | This table contains details for Time Clock Device export data for Schedule Shift |
| [HWM_TCD_EXP_DATA_SCH_SHFT_TXN](Tables/HWM_TCD_EXP_DATA_SCH_SHFT_TXN.md) | TCD EXPORT DATA SCH SHFT TXN TABLE |
| [HWM_TCD_EXP_DATA_SCH_TXN](Tables/HWM_TCD_EXP_DATA_SCH_TXN.md) | This table contains details for Time Clock Device export data for Schedule Transactions |
| [HWM_TCD_EXP_DATA_TXN](Tables/HWM_TCD_EXP_DATA_TXN.md) | This table contains details for Time Clock Device export data for Transactions |
| [HWM_TCD_MAPPINGS_B](Tables/HWM_TCD_MAPPINGS_B.md) | This table contains details for Time Device Mappings |
| [HWM_TCD_MAPPINGS_TL](Tables/HWM_TCD_MAPPINGS_TL.md) | Time Card Device Mapping Translation |
| [HWM_TCD_MAPPING_DTLS](Tables/HWM_TCD_MAPPING_DTLS.md) | Time Clock Device Mapping Details |
| [HWM_TCD_MAPPING_SETS_B](Tables/HWM_TCD_MAPPING_SETS_B.md) | This table contains details for Time Device Mapping Sets |
| [HWM_TCD_MAPPING_SETS_TL](Tables/HWM_TCD_MAPPING_SETS_TL.md) | Time Clock Device Mapping Sets TL |
| [HWM_TCD_MAPPING_SET_DTLS](Tables/HWM_TCD_MAPPING_SET_DTLS.md) | Time Clock Device Mapping Set Details |
| [HWM_TCSMRS_B](Tables/HWM_TCSMRS_B.md) | Each row contains information about a Time Consumer |
| [HWM_TCSMRS_TL](Tables/HWM_TCSMRS_TL.md) | An application or module interested in receiving time records from the workfoce management repository. |
| [HWM_TCSMR_CONFIGS](Tables/HWM_TCSMR_CONFIGS.md) | Each Time Consumer Configuration Set has a row in this table for each of the Time Consumers that is a member of the set.… |
| [HWM_TCSMR_CONFIG_SETS_B](Tables/HWM_TCSMR_CONFIG_SETS_B.md) | A consumer configuration set represents a group of time consumers registering interest in time.  This is used in a setup… |
| [HWM_TCSMR_CONFIG_SETS_TL](Tables/HWM_TCSMR_CONFIG_SETS_TL.md) | A consumer configuration set represents a group of time consumers registering interest in time.  This is used in a setup… |
| [HWM_TCSMR_IN_SETS](Tables/HWM_TCSMR_IN_SETS.md) | Each row in this table is a Time Consumer belonging to a Time Consumer Set. |
| [HWM_TCSMR_SETS](Tables/HWM_TCSMR_SETS.md) | Contains the header record for a Time Consumer Set. In Fusion 1.1 there is no UI for the creation of time consumer sets |
| [HWM_TCSMR_XFR_CONFIGS](Tables/HWM_TCSMR_XFR_CONFIGS.md) | For each Time Consumer in the Time Consumer Configuration Set there is typically a transfer process that needs to be con… |
| [HWM_TCSMR_XFR_PROCESSES](Tables/HWM_TCSMR_XFR_PROCESSES.md) | Each row contains the definition of a transfer process for a given time consumer |
| [HWM_TCSMR_XFR_PROCESSES_B](Tables/HWM_TCSMR_XFR_PROCESSES_B.md) | Each row contains the definition of a transfer process for a given time consumer |
| [HWM_TCSMR_XFR_PROCESSES_TL](Tables/HWM_TCSMR_XFR_PROCESSES_TL.md) | Each row contains the definition of a transfer process for a given time consumer |
| [HWM_TEMPORAL_EVENTS](Tables/HWM_TEMPORAL_EVENTS.md) | Table used for storing temporal events |
| [HWM_TE_ALT_NAMES](Tables/HWM_TE_ALT_NAMES.md) | This table holds information relating to the workforce management alternate name definition.  In particular, it identifi… |
| [HWM_TE_ALT_NAME_GRPS](Tables/HWM_TE_ALT_NAME_GRPS.md) | This table keeps information about the actual values that are used in the repository when a user selects an alternate na… |
| [HWM_TE_ALT_NAME_VALS_B](Tables/HWM_TE_ALT_NAME_VALS_B.md) | This table keeps information about the actual values that are used in the repository when a user selects an alternate na… |
| [HWM_TE_ALT_NAME_VALS_TL](Tables/HWM_TE_ALT_NAME_VALS_TL.md) | Contains Translated values for Alternate Name Value |
| [HWM_TIMECARDS](Tables/HWM_TIMECARDS.md) | Table where time card data retrieved from related REST services are stored. These time cards display in the Visual Build… |
| [HWM_TIMECARD_FIELDS](Tables/HWM_TIMECARD_FIELDS.md) | Table where time card field data retrieved from the time card field values REST service are stored. These values display… |
| [HWM_TIME_ENTRIES](Tables/HWM_TIME_ENTRIES.md) | Table where time card entry data retrieved from related REST services are stored. These time entries display in the Visu… |
| [HWM_TL_TASK_FEATURES](Tables/HWM_TL_TASK_FEATURES.md) | This table stores list of all tasks and layouts for one layout set |
| [HWM_TL_TASK_FEATURES_B](Tables/HWM_TL_TASK_FEATURES_B.md) | This table stores list of all tasks and layouts for one layout set |
| [HWM_TL_TASK_FEATURES_TL](Tables/HWM_TL_TASK_FEATURES_TL.md) | This table stores list of all tasks and layouts for one layout set in translation table |
| [HWM_TL_TASK_RESULTS](Tables/HWM_TL_TASK_RESULTS.md) | Task results determined by answers |
| [HWM_TM_ACT_ALLOCS](Tables/HWM_TM_ACT_ALLOCS.md) | Activity allocations entered against the reported times for a person and a date |
| [HWM_TM_ACT_ALLOC_ATRBS](Tables/HWM_TM_ACT_ALLOC_ATRBS.md) | Attributes values for related versions of activity allocation |
| [HWM_TM_ACT_ALLOC_DAY_STATUSES](Tables/HWM_TM_ACT_ALLOC_DAY_STATUSES.md) | Daily statuses with regards to activity allocation |
| [HWM_TM_ACT_ALLOC_STATUSES](Tables/HWM_TM_ACT_ALLOC_STATUSES.md) | Activity allocation entries statuses |
| [HWM_TM_ATRB_FLDS_B](Tables/HWM_TM_ATRB_FLDS_B.md) | A time attribute field represents information stored with a time record or time record group in the repository. |
| [HWM_TM_ATRB_FLDS_TL](Tables/HWM_TM_ATRB_FLDS_TL.md) | Stores translatable information about the time attribute fields defined for use with time records and time record groups… |
| [HWM_TM_ATRB_FLD_CONTEXTS](Tables/HWM_TM_ATRB_FLD_CONTEXTS.md) | A new table to store all contexts of data dictionary attributes. |
| [HWM_TM_ATRB_FLD_ESS_PROCESS](Tables/HWM_TM_ATRB_FLD_ESS_PROCESS.md) | Table to track the status of the Data Dictionary ESS Process per Integrators. |
| [HWM_TM_ATRB_FLD_MSTR_REF_B](Tables/HWM_TM_ATRB_FLD_MSTR_REF_B.md) | Table to identify the master  references for all detail instance attributes. |
| [HWM_TM_ATRB_FLD_MSTR_REF_TL](Tables/HWM_TM_ATRB_FLD_MSTR_REF_TL.md) | Translation table for timecard attributes master reference. |
| [HWM_TM_ATRB_FLD_SETS](Tables/HWM_TM_ATRB_FLD_SETS.md) | A time attribute field set is used to group time attribute fields for use with an alternate name definition. |
| [HWM_TM_ATRB_FLD_SET_CMPS](Tables/HWM_TM_ATRB_FLD_SET_CMPS.md) | Members of a set of time attribute fields |
| [HWM_TM_ATRB_FLD_USAGES](Tables/HWM_TM_ATRB_FLD_USAGES.md) | A Table to identify the usages of attributes for the corresponding consumers. |
| [HWM_TM_ATRB_FLD_USAGES_B](Tables/HWM_TM_ATRB_FLD_USAGES_B.md) | A Table to identify the usages of attributes for the corresponding contexts. |
| [HWM_TM_ATRB_FLD_USAGES_TL](Tables/HWM_TM_ATRB_FLD_USAGES_TL.md) | Translation table to identify the usages of attributes for the corresponding contexts. |
| [HWM_TM_AUDITS](Tables/HWM_TM_AUDITS.md) | The Time change audit (TA) table stores one row for each time entry. |
| [HWM_TM_AUDIT_ATRBS](Tables/HWM_TM_AUDIT_ATRBS.md) | The Time change audit attributes(TAA) table stores one row for each change of an attribute for a time entry. |
| [HWM_TM_BAL_STATUS_USAGES](Tables/HWM_TM_BAL_STATUS_USAGES.md) | Time statuses that are included in a time balance. |
| [HWM_TM_COST_OVERRIDES](Tables/HWM_TM_COST_OVERRIDES.md) | Cost overrides entered against the reported times for a person and a date |
| [HWM_TM_COST_OVERRIDE_ATRBS](Tables/HWM_TM_COST_OVERRIDE_ATRBS.md) | Attributes values for related versions of Cost override |
| [HWM_TM_EMPTY_ENTRIES](Tables/HWM_TM_EMPTY_ENTRIES.md) | table to store timecard entries with only attribute values |
| [HWM_TM_EVENTS](Tables/HWM_TM_EVENTS.md) | This table stores In or Out time transaction reported using a time collection device |
| [HWM_TM_EVENT_ATRBS](Tables/HWM_TM_EVENT_ATRBS.md) | Time event attributes table for TCD |
| [HWM_TM_EVENT_CORRECTIONS](Tables/HWM_TM_EVENT_CORRECTIONS.md) | Time event attributes table for TCD |
| [HWM_TM_EVENT_REQS](Tables/HWM_TM_EVENT_REQS.md) | Time event import request table for time collection device |
| [HWM_TM_LOCKS](Tables/HWM_TM_LOCKS.md) | Corresponds to a particular period for a particular resource in the repository that is in-use by some interface in the a… |
| [HWM_TM_REC](Tables/HWM_TM_REC.md) | An amount or range of time used within workforce management, which is associated with various attributes describing what… |
| [HWM_TM_REC_CHANGES](Tables/HWM_TM_REC_CHANGES.md) | Table to store changes for time record or time events. |
| [HWM_TM_REC_CHANGE_ATRBS](Tables/HWM_TM_REC_CHANGE_ATRBS.md) | Table to store changed attributes for change requests. |
| [HWM_TM_REC_CHANGE_REQS](Tables/HWM_TM_REC_CHANGE_REQS.md) | Table to store change requests for time entries or time events. |
| [HWM_TM_REC_EVENTS](Tables/HWM_TM_REC_EVENTS.md) | Time event table for rest service devices. |
| [HWM_TM_REC_EVENT_ATRBS](Tables/HWM_TM_REC_EVENT_ATRBS.md) | Time event attributes table for rest service devices. |
| [HWM_TM_REC_EVENT_REQS](Tables/HWM_TM_REC_EVENT_REQS.md) | Time event import request table for rest service devices. |
| [HWM_TM_REC_GRP](Tables/HWM_TM_REC_GRP.md) | A grouping of time records, for example, a day groups time records occuring within that day.  A time card groups day tim… |
| [HWM_TM_REC_GRP_OFFLINE](Tables/HWM_TM_REC_GRP_OFFLINE.md) | A new table to manage time cards that have been submitted for offline processing. |
| [HWM_TM_REC_GRP_SUM](Tables/HWM_TM_REC_GRP_SUM.md) | Summarized information of complex time record and time record groups.  For example, highlights the total number of hours… |
| [HWM_TM_REC_GRP_USAGES](Tables/HWM_TM_REC_GRP_USAGES.md) | A time record associated with a particular time record group. |
| [HWM_TM_REPROCESS_EVENTS](Tables/HWM_TM_REPROCESS_EVENTS.md) | Table for storing reprocessing event data like personId, startDate, endDate, Status ActionId, Processid |
| [HWM_TM_REPROCESS_REQUEST](Tables/HWM_TM_REPROCESS_REQUEST.md) | Table for storing the reprocessing data like Status,Source and Reason for time record groups . |
| [HWM_TM_REP_ALLOW_EXPS](Tables/HWM_TM_REP_ALLOW_EXPS.md) | an allow exception record is to capture if an exception is  allowed for an time entry . |
| [HWM_TM_REP_ATRBS](Tables/HWM_TM_REP_ATRBS.md) | Qualifying information about a time record or time record group.  For example, the project worked for the duration of th… |
| [HWM_TM_REP_ATRBS_BKP](Tables/HWM_TM_REP_ATRBS_BKP.md) | Backup table for HWM_TM_REP_ATRBS. |
| [HWM_TM_REP_ATRB_USAGES](Tables/HWM_TM_REP_ATRB_USAGES.md) | An attribute usage defines which attributes are used by which time records and time record groups in the repository. |
| [HWM_TM_REP_ATRB_USAGES_BKP](Tables/HWM_TM_REP_ATRB_USAGES_BKP.md) | Backup table for HWM_TM_REP_ATRB_USAGES. |
| [HWM_TM_REP_MSGS](Tables/HWM_TM_REP_MSGS.md) | Information associated with a time record or time record group after validation or rule execution. |
| [HWM_TM_REP_MSGS_BKP](Tables/HWM_TM_REP_MSGS_BKP.md) | Backup table for HWM_TM_REP_MSGS. |
| [HWM_TM_REP_MSGS_SOURCES](Tables/HWM_TM_REP_MSGS_SOURCES.md) | Table to record the source of messages by recording the rule which creates the messages |
| [HWM_TM_REP_MSG_TKNS](Tables/HWM_TM_REP_MSG_TKNS.md) | Specific detail to use within a message associated with validation or rule execution on a time record or time record gro… |
| [HWM_TM_SOURCES](Tables/HWM_TM_SOURCES.md) | This table contains the information about the origin of the time-card entry for example Absences, Web-Entry, Data-Loader |
| [HWM_TM_SOURCE_PROCESSES](Tables/HWM_TM_SOURCE_PROCESSES.md) | The processes that may be called by the Time Source |
| [HWM_TM_STATUSES](Tables/HWM_TM_STATUSES.md) | Status of a time record or time record group within the workforce management repository. |
| [HWM_TM_STATUSES_BKP](Tables/HWM_TM_STATUSES_BKP.md) | Backup table for HWM_TM_STATUSES. |
| [HWM_TM_STATUSES_SECONDARY](Tables/HWM_TM_STATUSES_SECONDARY.md) | Secondary Statuses of a time record or time record group within the workforce management repository. |
| [HWM_TM_STATUS_CHANGES](Tables/HWM_TM_STATUS_CHANGES.md) | Transfer status changes event table for rest service. |
| [HWM_TM_STATUS_CHANGE_REQS](Tables/HWM_TM_STATUS_CHANGE_REQS.md) | Transfer status changes request table for rest service. |
| [HWM_TM_STATUS_CONDITIONS](Tables/HWM_TM_STATUS_CONDITIONS.md) | This table contains the definition of the conditions of a derived status (atomic statuses will not have a row in this ta… |
| [HWM_TM_STATUS_DEF_B](Tables/HWM_TM_STATUS_DEF_B.md) | This table contains the definition of a status. We will support 2 types of statuses, ATOMIC statuses which are set direc… |
| [HWM_TM_STATUS_DEF_TL](Tables/HWM_TM_STATUS_DEF_TL.md) | Status Definition Translation Table |
| [HWM_TM_TEMPLATES](Tables/HWM_TM_TEMPLATES.md) | table to store timecard template data |
| [HWM_TRANSACTIONS](Tables/HWM_TRANSACTIONS.md) | Instances of a process execution to load time records into the workforce management repository |
| [HWM_TZ_DISPLAY_NAMES](Tables/HWM_TZ_DISPLAY_NAMES.md) | This table contains the Long and Short display names for Time zone for different languages. |
| [HWM_WORK_DAY_DEF_B](Tables/HWM_WORK_DAY_DEF_B.md) | It contains workday definition information. |
| [HWM_WORK_DAY_DEF_TL](Tables/HWM_WORK_DAY_DEF_TL.md) | Contains work day definition information. |
| [HWM_XFRS_UNQ_RECS](Tables/HWM_XFRS_UNQ_RECS.md) | Contains Unique Records for Transfer |
| [HWM_XFRS_WORK_RECS](Tables/HWM_XFRS_WORK_RECS.md) | Contains Work Records for Transfer |
| [HWM_XFR_GRP](Tables/HWM_XFR_GRP.md) | Time record groups transferred by a particular instance, or job, of a transfer process. |
| [HWM_XFR_JOB](Tables/HWM_XFR_JOB.md) | Instance of a transfer of time from workforce management to a time consuming application |
| [HWM_XFR_READY_REC_GRP](Tables/HWM_XFR_READY_REC_GRP.md) | A new tables is needed in order to store the time card ready to transfer. |
| [HWM_XFR_READY_STATUS_EVENTS](Tables/HWM_XFR_READY_STATUS_EVENTS.md) | Insert the time card id in staging table HWM_XFR_READY_STATUS_EVENTS |
| [HWM_XFR_TRANS](Tables/HWM_XFR_TRANS.md) | A time record transferred to a consuming application |
