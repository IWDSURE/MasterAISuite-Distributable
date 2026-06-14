# HHR_CT_INTEGRATION

This table is created to store the users integration info

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrctintegration-30842.html#hhrctintegration-30842](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrctintegration-30842.html#hhrctintegration-30842)

## Primary Key

| Name | Columns |
|------|----------|
| hhr_ct_integration_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | ID |
| MODULE | VARCHAR2 | 20 |  | Yes | MODULE |
| IS_ENABLED | NUMBER |  | 1 | Yes | IS_ENABLED |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hhr_ct_integration_U1 | Unique | FUSION_TS_TX_DATA | MODULE |
| hhr_ct_integration_U2 | Unique | FUSION_TS_TX_DATA | ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
