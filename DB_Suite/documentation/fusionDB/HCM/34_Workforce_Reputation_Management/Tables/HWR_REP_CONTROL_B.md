# HWR_REP_CONTROL_B

The reputation control table stores reputation management controls.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrepcontrolb-18919.html#hwrrepcontrolb-18919](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrepcontrolb-18919.html#hwrrepcontrolb-18919)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_REP_CONTROL_B_PK | REPUTATION_CONTROL_ID |

## Columns

| Name | Datatype | Length | Not-null | Comments |
|---|---|---|---|---|
| REPUTATION_CONTROL_ID | VARCHAR2 | 400 | Yes | This is the primary key for the reputation control table. |
| REPUTATION_CONTROL_KEY | VARCHAR2 | 64 | Yes | This is the key for the reputation control. |
| NAME | VARCHAR2 | 500 | Yes | The descriptive name of the reputation control. |
| DESCRIPTION | VARCHAR2 | 1000 |  | The description of the reputation control. |
| FILE_PATH | VARCHAR2 | 500 |  | The path to the file containing data for the reputation control. |
| PERCENT | NUMBER |  |  | The percent of the reputation control. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_REP_CONTROL_B_U1 | Unique | FUSION_TS_TX_DATA | REPUTATION_CONTROL_ID, ORA_SEED_SET1 |
| HWR_REP_CONTROL_B_U11 | Unique | FUSION_TS_TX_DATA | REPUTATION_CONTROL_ID, ORA_SEED_SET2 |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
