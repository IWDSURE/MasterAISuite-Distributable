# BEN_LER_F

BEN_LER_F identifies  all of the possible life event reasons that may cause a change to a person's eligibility, electabiliy, coverage, rates or premiums.   For example,  birth of a child, adoption of a child, marriage, reached maximum age to be in plan, new hire, rehire, divorced, death, spouse lost coverage, promotion, salary increase, age change.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerf-10151.html#benlerf-10151](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerf-10151.html#benlerf-10151)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_LER_F_PK | LER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| LER_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| COBRA_QUAL_CODE | VARCHAR2 | 30 |  |  | Cobra Qualification Type |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| NAME | VARCHAR2 | 240 |  |  | Name of the life event reason. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| TYP_CD | VARCHAR2 | 30 |  |  | Life event reason type. |  |
| CK_RLTD_PER_ELIG_FLAG | VARCHAR2 | 30 |  | Yes | Check related person eligiblility Y or N. |  |
| LER_EVAL_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| CM_APLY_FLAG | VARCHAR2 | 30 |  | Yes | Communications Apply Y or N. |  |
| OVRIDG_LE_FLAG | VARCHAR2 | 30 |  | Yes | Overriding Life Event Y or N. |  |
| WHN_TO_PRCS_CD | VARCHAR2 | 30 |  |  | When to process. |  |
| LER_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LER_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Life Event Attributes (BEN_LER_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| PTNL_LER_TRTMT_CD | VARCHAR2 | 30 |  |  | Potential life event reason treatment. |  |
| DESC_TXT | VARCHAR2 | 2000 |  |  | Description. |  |
| TMLNS_PERD_CD | VARCHAR2 | 30 |  |  | Timeliness period. |  |
| TMLNS_EVAL_CD | VARCHAR2 | 30 |  |  | Timeliness evaluation code. |  |
| TMLNS_PERD_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| TMLNS_DYS_NUM | NUMBER |  | 18 |  | Timeliness days. |  |
| OCRD_DT_DET_CD | VARCHAR2 | 30 |  |  | Occurred date determination code. |  |
| QUALG_EVT_FLAG | VARCHAR2 | 30 |  | Yes | Qualifying Event Y or N. |  |
| SLCTBL_SLF_SVC_CD | VARCHAR2 | 30 |  |  | Selectable for Self Service |  |
| LER_STAT_CD | VARCHAR2 | 30 |  |  | Life Event Status |  |
| SHORT_CODE | VARCHAR2 | 30 |  |  | Short Code |  |
| SHORT_NAME | VARCHAR2 | 30 |  |  | short Name |  |
| LF_EVT_OPER_CD | VARCHAR2 | 30 |  |  | Life event operation. |  |
| GLOBAL_FLAG | VARCHAR2 | 30 |  |  | Indicates exposure to legal entities. |  |
| PROD_CD | VARCHAR2 | 30 |  |  | Product Code |  |
| SELF_ASSIGNED_EVENT_FLAG | VARCHAR2 | 30 |  | Yes | 'Y' in case the event can be self assigned, Default N |  |
| INSTRUCTION_TEXT | VARCHAR2 | 200 |  |  | Stores instruction meant for SS users in case the event is self assignable. |  |
| CONFIG_NUM_1 | NUMBER |  |  |  | Number field for future use. |  |
| CONFIG_NUM_2 | NUMBER |  |  |  | Number field for future use. |  |
| CONFIG_NUM_3 | NUMBER |  |  |  | Number field for future use. |  |
| CONFIG_NUM_4 | NUMBER |  |  |  | Number field for future use. |  |
| CONFIG_NUM_5 | NUMBER |  |  |  | Number field for future use. |  |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Character field for future use. |  |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Character field for future use. |  |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Character field for future use. |  |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Character field for future use. |  |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Character field for future use. |  |
| CONFIG_DATE_1 | DATE |  |  |  | Date field for future use. |  |
| CONFIG_DATE_2 | DATE |  |  |  | Date field for future use. |  |
| CONFIG_DATE_3 | DATE |  |  |  | Date field for future use. |  |
| CONFIG_DATE_4 | DATE |  |  |  | Date field for future use. |  |
| CONFIG_DATE_5 | DATE |  |  |  | Date field for future use. |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_LER_F_FK2 | Non Unique | Default | NAME |
| BEN_LER_F_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| BEN_LER_F_PK | Unique | Default | LER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| BEN_LER_F_PK1 | Unique | Default | LER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
