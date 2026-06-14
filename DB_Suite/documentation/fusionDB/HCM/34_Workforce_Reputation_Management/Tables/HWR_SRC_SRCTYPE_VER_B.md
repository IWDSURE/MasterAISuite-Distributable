# HWR_SRC_SRCTYPE_VER_B

The source type version table is used to store the versions of the types of the sources of social content.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrcsrctypeverb-8615.html#hwrsrcsrctypeverb-8615](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrcsrctypeverb-8615.html#hwrsrcsrctypeverb-8615)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SRC_SRCTYPE_VER_B_PK | SOURCE_TYPE_VERSION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SOURCE_TYPE_VERSION_ID | NUMBER |  | 18 | Yes | This is the primary key for the social data source type version tables. The number should be generated from the sequence. | Active |
| SOURCE_TYPE_VERSION_KEY | VARCHAR2 | 64 |  | Yes | The key for the source type version. | Active |
| SOURCE_TYPE_ID | NUMBER |  | 18 | Yes | This is the Id for the type of source from HWR_SRC_SRCTYPE_B. | Active |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_SRC_SRCTYPE_VER_B_N1 | Non Unique | FUSION_TS_TX_DATA | SOURCE_TYPE_ID |  |
| HWR_SRC_SRCTYPE_VER_B_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_TYPE_VERSION_ID, ORA_SEED_SET1 | Active |
| HWR_SRC_SRCTYPE_VER_B_U11 | Unique | FUSION_TS_TX_DATA | SOURCE_TYPE_VERSION_ID, ORA_SEED_SET2 |  |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
