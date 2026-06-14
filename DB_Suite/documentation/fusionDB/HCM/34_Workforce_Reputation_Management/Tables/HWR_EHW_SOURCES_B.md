# HWR_EHW_SOURCES_B

This table stores the ehw sources information

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrehwsourcesb-27804.html#hwrehwsourcesb-27804](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrehwsourcesb-27804.html#hwrehwsourcesb-27804)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_EHW_SOURCES_B_PK | SOURCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SOURCE_ID | NUMBER |  | 18 | Yes | source ID of the EHW source connector |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | DESCRIPTION |
| TYPE_ID | NUMBER |  | 18 | Yes | source connector type - manual or remote |
| STATUS_ID | NUMBER |  | 18 | Yes | status of the connector - enabled, disabled, removed |
| LOCAL_SOURCE_ID | NUMBER |  | 18 |  | Define the HWR source id for local connectors. |
| DEVICE | VARCHAR2 | 256 |  |  | This columns stores the Device Name |
| VENDOR | VARCHAR2 | 256 |  |  | This columns stores the Vendor Name |
| AUTHORIZATION_URL | VARCHAR2 | 512 |  |  | The url of the container application authorization |
| ADMINISTRATION_URL | VARCHAR2 | 512 |  |  | This is the url of the administrator app |
| DATA_SRC_CONFIG | VARCHAR2 | 256 |  |  | This is the data source configuration |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_EHW_SOURCES_B_N1 | Non Unique | FUSION_TS_TX_DATA | LOCAL_SOURCE_ID |
| HWR_EHW_SOURCES_B_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, ORA_SEED_SET1 |
| HWR_EHW_SOURCES_B_U11 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, ORA_SEED_SET2 |
| HWR_EHW_SOURCES_B_U2 | Unique | FUSION_TS_TX_DATA | DEVICE, VENDOR, TYPE_ID, LOCAL_SOURCE_ID, ORA_SEED_SET1 |
| HWR_EHW_SOURCES_B_U21 | Unique | FUSION_TS_TX_DATA | DEVICE, VENDOR, TYPE_ID, LOCAL_SOURCE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
