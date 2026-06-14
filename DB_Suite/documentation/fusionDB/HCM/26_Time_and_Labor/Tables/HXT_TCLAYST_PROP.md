# HXT_TCLAYST_PROP

The table HXT_TCLAYST_PROP table contains the additional properties of layout sets, such as layout set type, audit requirements, template used, etc.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttclaystprop-14985.html#hxttclaystprop-14985](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttclaystprop-14985.html#hxttclaystprop-14985)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_TCLAYST_PROP_PK | TCLAYST_PROP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TCLAYST_PROP_ID | NUMBER |  | 18 | Yes | TCLAYST_PROP_ID |
| ANS_SET_ID | NUMBER |  | 18 | Yes | TCLAYST_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TCLAYST_TE_TYPE | VARCHAR2 | 255 |  |  | SHORT_CODE |
| IND_TCSMRS_CODE | VARCHAR2 | 255 |  |  | OWNER |
| IND_MGR_FLAG | VARCHAR2 | 1 |  |  | COMPLETION_STATUS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| TCLAYST_PROP_CD | VARCHAR2 | 160 |  |  | used for seed data |
| MEMBERSHIP_FLAG | VARCHAR2 | 1 |  |  | Flag for enable team membership |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_TCLAYST_PROP_N20 | Non Unique | Default | SGUID |
| HXT_TCLAYST_PROP_PK | Unique | Default | TCLAYST_PROP_ID, ORA_SEED_SET1 |
| HXT_TCLAYST_PROP_PK1 | Unique | Default | TCLAYST_PROP_ID, ORA_SEED_SET2 |
| HXT_TCLAYST_PROP_U1 | Unique | Default | ANS_SET_ID, ORA_SEED_SET1 |
| HXT_TCLAYST_PROP_U11 | Unique | Default | ANS_SET_ID, ORA_SEED_SET2 |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
