# HWR_ALERT_DATA_B

The purpose of this table is to map survey related attributes to the alert id so it can be used for various other use-cases to withdraw  the notification or invoke several other messages.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwralertdatab-27162.html#hwralertdatab-27162](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwralertdatab-27162.html#hwralertdatab-27162)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_ALERT_DATA_B_PK | ALERT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ALERT_ID | NUMBER |  | 18 | Yes | Alert ID will be retreived when the notification will be sent. |  |
| SURVEY_ATTRS | VARCHAR2 | 4000 |  |  | All attributes related to survey meeting will be mapped to this column in a comma separated fashion. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_ALERT_DATA_B_U1 | Unique | FUSION_TS_TX_DATA | ALERT_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
