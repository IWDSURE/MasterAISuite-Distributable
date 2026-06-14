# WLF_CM_SP_DESTINATIONS_F

Table to store of content shares

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcmspdestinationsf-18744.html#wlfcmspdestinationsf-18744](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcmspdestinationsf-18744.html#wlfcmspdestinationsf-18744)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_CM_SP_DESTINATIONS_F_PK | DESTINATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DESTINATION_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| SHARE_PROFILE_ID | NUMBER |  | 18 | Yes | Share profile id this entry belons to. |
| OPERATION | VARCHAR2 | 12 |  | Yes | Destination entry operation  { INCLUDE, EXCLUDE }. |
| TYPE | VARCHAR2 | 12 |  | Yes | Destination entry type  { [PER]SON, [ORG]ANIZATION, [DIR]ECTS } |
| SHARED_TO_ID | NUMBER |  | 18 | Yes | Indicates the person identifier of destination entry. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_CM_SP_DESTINATIONS_F_N1 | Non Unique | Default | SHARE_PROFILE_ID |
| WLF_CM_SP_DESTINATIONS_F_N2 | Non Unique | Default | OPERATION |
| WLF_CM_SP_DESTINATIONS_F_PK | Unique | Default | DESTINATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
