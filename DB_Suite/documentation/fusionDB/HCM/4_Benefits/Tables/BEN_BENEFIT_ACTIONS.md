# BEN_BENEFIT_ACTIONS

BEN_BENEFIT_ACTIONS  contains the run parameters for the benefits concurrent manager processing, such as the Participation Process and Extract Process, run by the concurrent manager.  This information is used mainly to restart the batch process.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbenefitactions-27189.html#benbenefitactions-27189](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbenefitactions-27189.html#benbenefitactions-27189)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BENEFIT_ACTIONS_PK | BENEFIT_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BENEFIT_ACTION_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_BENEFIT_ACTION. |
| PROCESS_DATE | DATE |  |  | Yes | Process Date. |
| MODE_CD | VARCHAR2 | 30 |  | Yes | Mode code. |
| DERIVABLE_FACTORS_FLAG | VARCHAR2 | 30 |  | Yes | Derivable Factors Y or N. |
| VALIDATE_FLAG | VARCHAR2 | 30 |  | Yes | Validate Y or N. |
| PERSON_ID | NUMBER |  | 18 |  | Foreign Key to PER_PEOPLE_F. |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | Foreign Key to BEN_BENEFIT_RELATIONS_F |
| PERSON_TYPE_ID | NUMBER |  | 18 |  | Foreign key to PER_PERSON_TYPES. |
| PGM_ID | NUMBER |  | 18 |  | Foreign key to BEN_PGM_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F. |
| POPL_ENRT_TYP_CYCL_ID | NUMBER |  | 18 |  | Foreign key to BEN_POPL_ENRT_TYP_CYCL_F. |
| NO_PROGRAMS_FLAG | VARCHAR2 | 30 |  | Yes | No Programs Y or N. |
| NO_PLANS_FLAG | VARCHAR2 | 30 |  | Yes | No Plans Y or N. |
| COMP_SELECTION_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| PERSON_SELECTION_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| LER_ID | NUMBER |  | 18 |  | Foreign Key to BEN_LER_F. |
| ORGANIZATION_ID | NUMBER |  | 18 |  | Foreign key to HR_ORGANIZATION_UNITS. |
| BENFTS_GRP_ID | NUMBER |  | 18 |  | Foreign key to BEN_BENFTS_GRP_F. |
| LOCATION_ID | NUMBER |  | 18 |  | Foreign key to HR_LOCATIONS. |
| PSTL_ZIP_RNG_ID | NUMBER |  | 18 |  | Foreign key to BEN_ZIP_RNG_F. |
| RPTG_GRP_ID | NUMBER |  | 18 |  | Foreign key to BEN_RPTG_GRP_F |
| PL_TYP_ID | NUMBER |  | 18 |  | Foreign key to BEN_PL_TYP_F. |
| OPT_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OPT_F. |
| ELIGY_PRFL_ID | NUMBER |  | 18 |  | Foreign key to BEN_ELIGY_PRFL_F. |
| VRBL_RT_PRFL_ID | NUMBER |  | 18 |  | Foreign key to BEN_VRBL_RT_PRFL_F |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Foreign key to HR_ORGANIZATION_UNITS. |
| PAYROLL_ID | NUMBER |  | 18 |  | Foreign key to PAY_PAYROLLS_F. |
| DEBUG_MESSAGES_FLAG | VARCHAR2 | 30 |  | Yes | Debug Messages Y or N. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row). |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CM_TRGR_TYP_CD | VARCHAR2 | 30 |  |  | Communication trigger type. |
| MIN_AGE | NUMBER |  | 18 |  | Minimum age. |
| MAX_AGE | NUMBER |  | 18 |  | Maximum age. |
| MIN_LOS | NUMBER |  | 18 |  | Mininum length of service. |
| MAX_LOS | NUMBER |  | 18 |  | Maximum length of service. |
| MIN_CMBN | NUMBER |  | 18 |  | No longer used. |
| MAX_CMBN | NUMBER |  | 18 |  | No longer used. |
| DATE_FROM | DATE |  |  |  | Date from. |
| ELIG_ENROL_CD | VARCHAR2 | 30 |  |  | Eligible or Enrolled. |
| AUDIT_LOG_FLAG | VARCHAR2 | 30 |  | Yes | Audit Log Y or N. |
| LF_EVT_OCRD_DT | VARCHAR2 | 240 |  |  | Life event occurred date. |
| CLOSE_UNEAI_FLAG | VARCHAR2 | 30 |  |  | Close Unprocessed employee action items Y or N. |
| UNEAI_EFFECTIVE_DATE | DATE |  |  |  | Close unresolved action item effective date. |
| CM_TYP_ID | NUMBER |  | 18 |  | Foreign Key to BEN_CM_TYP_F. |
| AGE_FCTR_ID | NUMBER |  | 18 |  | Foreign Key to BEN_AGE_FCTR_F. |
| LOS_FCTR_ID | NUMBER |  | 18 |  | Foreign key to BEN_LOS_FCTR_F. |
| CMBN_AGE_LOS_FCTR_ID | NUMBER |  | 18 |  | Foreign key to BEN_CMBN_AGE_LOS_FCTR_F. |
| ACTN_TYP_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTN_TYP_F. |
| USE_FCTR_TO_SEL_FLAG | VARCHAR2 | 30 |  |  | Use Factor To Select Y or N. |
| LOS_DET_TO_USE_CD | VARCHAR2 | 30 |  |  | Length of service date to use code. |
| PTNL_LER_FOR_PER_STAT_CD | VARCHAR2 | 30 |  |  | Potential life event reason for person status. |
| LMT_PRPNIP_BY_ORG_FLAG | VARCHAR2 | 30 |  |  | Limit By Person's Organization Y or N. |
| INELG_ACTION_CD | VARCHAR2 | 30 |  |  | Inelg Action Cd |
| GRANT_PRICE_VAL | NUMBER |  |  |  | Grant Price Value |
| ENRT_PERD_ID | NUMBER |  | 18 |  | Enrollment Period Id |
| ASG_EVENTS_TO_ALL_SEL_DT | VARCHAR2 | 30 |  |  | Assign Events To All Selection Date. |
| CAGR_ID | NUMBER |  | 18 |  | CAGR. |
| CONCAT_SEGS | VARCHAR2 | 2000 |  |  | Concatinated Segments. |
| GRADE_LADDER_ID | NUMBER |  | 18 |  | Grade Ladder. |
| ORG_HIERARCHY_ID | NUMBER |  | 18 |  | Organization Hierarchy. |
| ORG_STARTING_NODE_ID | NUMBER |  | 18 |  | Organization Starting Node. |
| PER_SEL_DT_CD | VARCHAR2 | 30 |  |  | Person Selection Date Code. |
| PER_SEL_DT_FROM | DATE |  |  |  | Person Selection Date from. |
| PER_SEL_DT_TO | DATE |  |  |  | Person Selection Date To |
| PER_SEL_FREQ_CD | VARCHAR2 | 30 |  |  | Person Selection Frequency Code. |
| QUAL_STATUS | VARCHAR2 | 30 |  |  | Qualification Status. |
| QUAL_TYPE | NUMBER |  |  |  | Qualification Type. |
| RATE_ID | NUMBER |  | 18 |  | Rate. |
| YEAR_FROM | NUMBER |  |  |  | Year From. |
| YEAR_TO | NUMBER |  |  |  | Year To. |
| PROGRAM_ID | NUMBER |  | 18 |  | Concurrent Program who column - program id of the program that last updated this row (foreign key to FND_CONCURRENT_PROGRAM.CONCURRENT_PROGRAM_ID). |
| PROGRAM_APPLICATION_ID | NUMBER |  | 18 |  | Concurrent Program who column - application id of the program that last updated this row (foreign key to FND_APPLICATION.APPLICATION_ID). |
| BBA_INFORMATION1 | VARCHAR2 | 250 |  |  | BBA_INFORMATION1 |
| BBA_INFORMATION2 | VARCHAR2 | 250 |  |  | BBA_INFORMATION2 |
| BBA_INFORMATION3 | VARCHAR2 | 250 |  |  | BBA_INFORMATION3 |
| BBA_INFORMATION4 | VARCHAR2 | 250 |  |  | BBA_INFORMATION4 |
| BBA_INFORMATION5 | VARCHAR2 | 250 |  |  | BBA_INFORMATION5 |
| BBA_INFORMATION6 | NUMBER |  |  |  | BBA_INFORMATION6 |
| BBA_INFORMATION7 | NUMBER |  |  |  | BBA_INFORMATION7 |
| BBA_INFORMATION8 | NUMBER |  |  |  | BBA_INFORMATION8 |
| BBA_INFORMATION9 | NUMBER |  |  |  | BBA_INFORMATION9 |
| BBA_INFORMATION10 | NUMBER |  |  |  | BBA_INFORMATION10 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BENEFIT_ACTIONS_FK10 | Non Unique | Default | LOCATION_ID |
| BEN_BENEFIT_ACTIONS_FK12 | Non Unique | Default | RPTG_GRP_ID |
| BEN_BENEFIT_ACTIONS_FK18 | Non Unique | Default | REQUEST_ID |
| BEN_BENEFIT_ACTIONS_FK8 | Non Unique | Default | ORGANIZATION_ID |
| BEN_BENEFIT_ACTIONS_FK9 | Non Unique | Default | BENFTS_GRP_ID |
| BEN_BENEFIT_ACTIONS_N1 | Non Unique | Default | PERSON_ID |
| BEN_BENEFIT_ACTIONS_N10 | Non Unique | Default | ELIGY_PRFL_ID |
| BEN_BENEFIT_ACTIONS_N11 | Non Unique | Default | VRBL_RT_PRFL_ID |
| BEN_BENEFIT_ACTIONS_N12 | Non Unique | Default | PAYROLL_ID |
| BEN_BENEFIT_ACTIONS_N14 | Non Unique | Default | BENEFIT_RELATION_ID |
| BEN_BENEFIT_ACTIONS_N2 | Non Unique | Default | PERSON_TYPE_ID |
| BEN_BENEFIT_ACTIONS_N3 | Non Unique | Default | PGM_ID |
| BEN_BENEFIT_ACTIONS_N4 | Non Unique | Default | PL_ID |
| BEN_BENEFIT_ACTIONS_N5 | Non Unique | Default | POPL_ENRT_TYP_CYCL_ID |
| BEN_BENEFIT_ACTIONS_N6 | Non Unique | Default | LER_ID |
| BEN_BENEFIT_ACTIONS_N7 | Non Unique | Default | PSTL_ZIP_RNG_ID |
| BEN_BENEFIT_ACTIONS_N8 | Non Unique | Default | PL_TYP_ID |
| BEN_BENEFIT_ACTIONS_N9 | Non Unique | Default | OPT_ID |
| BEN_BENEFIT_ACTIONS_PK1 | Unique | Default | BENEFIT_ACTION_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
