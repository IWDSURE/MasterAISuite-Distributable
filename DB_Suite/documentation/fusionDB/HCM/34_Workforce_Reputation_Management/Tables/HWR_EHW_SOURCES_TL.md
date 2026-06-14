# HWR_EHW_SOURCES_TL

This table stores the ehw sources translation  information

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrehwsourcestl-11733.html#hwrehwsourcestl-11733](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrehwsourcestl-11733.html#hwrehwsourcestl-11733)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_EHW_SOURCES_TL_PK | SOURCE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SOURCE_ID | NUMBER |  | 18 | Yes | source ID of the EHW source connector |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| DEVICE_NAME | VARCHAR2 | 256 |  |  | This column stores the localized Device Name |
| VENDOR_NAME | VARCHAR2 | 256 |  |  | This column stores the localized Vendor Name |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_EHW_SOURCES_TL_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, LANGUAGE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
