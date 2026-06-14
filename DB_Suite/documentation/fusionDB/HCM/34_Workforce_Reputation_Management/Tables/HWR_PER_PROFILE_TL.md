# HWR_PER_PROFILE_TL

The translation table for the person profile table.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperprofiletl-18232.html#hwrperprofiletl-18232](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperprofiletl-18232.html#hwrperprofiletl-18232)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_PER_PROFILE_TL_PK | SOURCE_ID, PRFL_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PRFL_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the person profile tables. |  |
| SOURCE_ID | NUMBER |  | 18 | Yes | The Id for the social data source. |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. | Active |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. | Active |
| STREET_ADDRESS | VARCHAR2 | 500 |  |  | This is a physical address of the person. |  |
| PHONE | VARCHAR2 | 500 |  |  | This is the contact phone number of the person. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_PER_PROFILE_TL_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, PRFL_ID, LANGUAGE | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
