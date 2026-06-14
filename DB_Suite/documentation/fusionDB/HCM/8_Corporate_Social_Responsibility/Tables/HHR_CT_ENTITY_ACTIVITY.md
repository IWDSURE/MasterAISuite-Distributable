# HHR_CT_ENTITY_ACTIVITY

This table is created to store entity activity info

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrctentityactivity-3827.html#hhrctentityactivity-3827](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrctentityactivity-3827.html#hhrctentityactivity-3827)

## Primary Key

| Name | Columns |
|------|----------|
| HHR_CT_ENTITY_ACTIVITY_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | ID |
| CT_ACTIVITY_ID | VARCHAR2 | 20 |  | Yes | CT_ACTIVITY_ID |
| ENTITY_ID | NUMBER |  | 18 | Yes | ENTITY_ID |
| ENTITY_TYPE | VARCHAR2 | 20 |  | Yes | ENTITY_TYPE |
| MODULE | VARCHAR2 | 20 |  | Yes | MODULE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HHR_CT_ENTITY_ACTIVITY_U1 | Unique | FUSION_TS_TX_DATA | ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
