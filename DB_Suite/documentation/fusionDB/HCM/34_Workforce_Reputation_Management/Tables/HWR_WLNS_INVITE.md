# HWR_WLNS_INVITE

The wellness invite table stores the information about the invitation sent for competitions and goals

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsinvite-7106.html#hwrwlnsinvite-7106](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsinvite-7106.html#hwrwlnsinvite-7106)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_INVITE_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | ID |
| ENTITY_ID | NUMBER |  | 18 | Yes | ENTITY_ID |
| ENTITY_TYPE | VARCHAR2 | 20 |  | Yes | ENTITY_TYPE |
| SENDER_ID | VARCHAR2 | 20 |  | Yes | SENDER_ID |
| RECEIVER_ID | VARCHAR2 | 20 |  | Yes | RECEIVER_ID |
| STATUS | VARCHAR2 | 20 |  |  | STATUS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_INVITE_U1 | Unique | FUSION_TS_TX_DATA | ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
