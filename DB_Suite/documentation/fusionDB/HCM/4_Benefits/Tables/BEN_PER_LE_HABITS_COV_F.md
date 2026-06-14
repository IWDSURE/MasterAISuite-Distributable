# BEN_PER_LE_HABITS_COV_F

This table to track employees smoking habbits.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benperlehabitscovf-24760.html#benperlehabitscovf-24760](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benperlehabitscovf-24760.html#benperlehabitscovf-24760)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PER_LE_HABITS_COV_F_PK | LE_HABITS_COV_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LEGAL_ENTITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LE_HABITS_COV_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PERSON_ID | NUMBER |  | 18 | Yes | This column indicates Foreign Key to PER_ALL_PEOPLE_F. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | This column indicates LEGISLATIVE_DATA_GROUP_ID. |
| TOBACCO_TYPE_USAGE | VARCHAR2 | 30 |  |  | This column indicate TOBACCO_TYPE_USAGE. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| STUDENT_STATUS | VARCHAR2 | 30 |  |  | This column indicate student status. |
| COORD_MED_CVG_END_DT | DATE |  |  |  | This column indicates COORD_MED_CVG_END_DT. |
| COORD_MED_CVG_STRT_DT | DATE |  |  |  | This column indicates COORD_MED_CVG_STRT_DT. |
| COORD_MED_EXT_ER | VARCHAR2 | 30 |  |  | This column indicates COORD_MED_EXT_ER. |
| COORD_MED_INSR_CRR_IDENT | VARCHAR2 | 30 |  |  | This column indicates COORD_MED_INSR_CRR_IDENT. |
| COORD_MED_INSR_CRR_NAM | VARCHAR2 | 30 |  |  | This column indicates COORD_MED_INSR_CRR_NAM. |
| COORD_MED_PL_NAME | VARCHAR2 | 240 |  |  | This column indicates COORD_MED_PL_NAME. |
| COORD_MED_PLN_NO | VARCHAR2 | 30 |  |  | This column indicates COORD_MED_PLN_NO. |
| COORD_NO_CVG_FLAG | VARCHAR2 | 30 |  |  | This column indicates COORD_NO_CVG_FLAG. |
| DPDNT_ADOPTION_DATE | DATE |  |  |  | This column indicates DPDNT_ADOPTION_DATE. |
| DPDNT_VLNTRY_SVCE_FLAG | VARCHAR2 | 30 |  |  | This column indicates DPDNT_VLNTRY_SVCE_FLAG. |
| RECEIPT_OF_DEATH_CERT_DATE | DATE |  |  |  | This column indicates RECEIPT_OF_DEATH_CERT_DATE. |
| ON_MILITARY_SERVICE | VARCHAR2 | 30 |  |  | This column indicates ON_MILITARY_SERVICE. |
| REGISTERED_DISABLED_FLAG | VARCHAR2 | 30 |  |  | This column indicates REGISTERED_DISABLED_FLAG. |
| DISABILITY_STATUS | VARCHAR2 | 30 |  |  | This column holds disability status. |
| CVRD_IN_ANTHR_PL | VARCHAR2 | 30 |  |  | This column holds covered in another plan flag. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS. |
| LEGAL_ENTITY_ID | NUMBER |  | 18 | Yes | This column indicates LEGAL_ENTITY_ID. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PER_LE_HABITS_COV_F_N1 | Non Unique | Default | PERSON_ID |
| BEN_PER_LE_HABITS_COV_F_PK | Unique | Default | LE_HABITS_COV_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LEGAL_ENTITY_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
