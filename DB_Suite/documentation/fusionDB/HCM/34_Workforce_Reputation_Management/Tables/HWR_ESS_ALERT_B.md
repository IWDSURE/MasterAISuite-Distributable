# HWR_ESS_ALERT_B

This table will be used to store main information of the hwr ess job evoked alerts

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwressalertb-3005.html#hwressalertb-3005](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwressalertb-3005.html#hwressalertb-3005)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_ESS_ALERT_B_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | This is the primary key for the wellness ess job alert table |
| ALERT_NAME | VARCHAR2 | 100 |  | Yes | HWR Alert Enum name. |
| ALERT_OBJECT_ATTRS | VARCHAR2 | 4000 |  | Yes | All attribues related to hwr alert domain objects will be mapped to this column in a separated fashion. |
| ALERT_MAP_ATTRS | VARCHAR2 | 4000 |  |  | All alert map attributes related to hwr alert will be mapped to this column in a separated fashion. |
| RECIPIENT_USERNAME | VARCHAR2 | 100 |  |  | This is a username of hwr alert. |
| IS_SENT | NUMBER |  | 18 | Yes | This indicates if the alert is sent or not. 0 --> not sent; 1 --> sent. |
| HWR_ALERT_ATTR_1 | VARCHAR2 | 2000 |  |  | HWR_ALERT_ATTR_1. This is the extra attribute in case if needed. |
| HWR_ALERT_ATTR_2 | VARCHAR2 | 1000 |  |  | HWR_ALERT_ATTR_2. This is the extra attribute in case if needed. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_ESS_ALERT_B_U1 | Unique | Default | ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
