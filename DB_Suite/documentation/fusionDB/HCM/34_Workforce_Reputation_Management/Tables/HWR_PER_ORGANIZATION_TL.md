# HWR_PER_ORGANIZATION_TL

The translation table for the organization table.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperorganizationtl-7512.html#hwrperorganizationtl-7512](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperorganizationtl-7512.html#hwrperorganizationtl-7512)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_PER_ORGANIZATION_TL_PK | HWR_ORG_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Not-null | Comments | Status |
|---|---|---|---|---|---|
| HWR_ORG_ID | VARCHAR2 | 500 | Yes | This is the primary key for the organization tables. |  |
| SOURCE_LANG | VARCHAR2 | 4 | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. | Active |
| LANGUAGE | VARCHAR2 | 4 | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. | Active |
| NAME | VARCHAR2 | 500 |  | This is the name of the organization. | Active |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_PER_ORGANIZATION_TL_U1 | Unique | FUSION_TS_TX_DATA | HWR_ORG_ID, LANGUAGE | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
