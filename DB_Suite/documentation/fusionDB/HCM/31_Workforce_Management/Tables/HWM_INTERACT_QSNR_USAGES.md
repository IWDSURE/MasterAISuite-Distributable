# HWM_INTERACT_QSNR_USAGES

Stores cross refence ids between Time card repository,  Attestation group set  and Talent's questioner table

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwminteractqsnrusages-18061.html#hwminteractqsnrusages-18061](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwminteractqsnrusages-18061.html#hwminteractqsnrusages-18061)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_INTERACT_QSNR_USAGES_PK | ITR_QSR_USG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ITR_QSR_USG_ID | NUMBER |  | 18 | Yes | Primary Key |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| ITR_SET_ID | NUMBER |  | 18 | Yes | ITR_SET_ID |
| RESPONSE_STATUS | VARCHAR2 | 30 |  | Yes | RESPONSE_STATUS |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | QUESTIONNAIRE_ID |
| QSTNR_VERSION_NUM | NUMBER |  | 18 |  | QSTNR_VERSION_NUM |
| QSTNR_PARTICIPANT_ID | NUMBER |  | 18 |  | QSTNR_PARTICIPANT_ID |
| ATTN_TE_ID | NUMBER |  | 18 |  | Time event or entry identifier associated to an attestation |
| TM_BLDG_BLK_ID | NUMBER |  | 18 |  | TM_BLDG_BLK_ID |
| TM_BLDG_BLK_VERSION | NUMBER |  | 9 |  | TM_BLDG_BLK_VERSION |
| TM_REC_GRP_ID | NUMBER |  | 18 |  | TM_REC_GRP_ID |
| BLDG_BLK_TYPE | VARCHAR2 | 32 |  |  | BLDG_BLK_TYPE |
| DELETE_FLAG | VARCHAR2 | 1 |  |  | DELETE_FLAG |
| ORIGINAL_RESPONSE_SOURCE | VARCHAR2 | 30 |  |  | ORIGINAL_RESPONSE_SOURCE |
| RESOURCE_ID | NUMBER |  | 18 | Yes | RESOURCE_ID |
| SUBRESOURCE_ID | NUMBER |  | 18 |  | SUBRESOURCE_ID |
| DISPLAY_LEVEL | VARCHAR2 | 30 |  |  | DISPLAY_LEVEL |
| ACTUAL_PUNCH_TIME | VARCHAR2 | 30 |  |  | COLUMN1 |
| START_TIME | TIMESTAMP |  |  |  | START_TIME |
| STOP_TIME | TIMESTAMP |  |  |  | STOP_TIME |
| MEASURE | NUMBER |  |  |  | MEASURE |
| PART_DATE | TIMESTAMP |  |  |  | partition key |
| PART_GRP_TYPE_ID | NUMBER |  | 18 |  | partition key |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_INTERACT_QSNR_USAGES_N1 | Non Unique | Default | RESOURCE_ID, TRUNC("START_TIME"), TRUNC("STOP_TIME") |
| HWM_INTERACT_QSNR_USAGES_N2 | Non Unique | Default | ITR_SET_ID |
| HWM_INTERACT_QSNR_USAGES_N3 | Non Unique | Default | TM_BLDG_BLK_ID, NVL("DELETE_FLAG",'N') |
| HWM_INTERACT_QSNR_USAGES_N4 | Non Unique | Default | TM_REC_GRP_ID, NVL("DELETE_FLAG",'N'), RESPONSE_STATUS |
| HWM_INTERACT_QSNR_USAGES_PK | Unique | FUSION_TS_TX_DATA | ITR_QSR_USG_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
