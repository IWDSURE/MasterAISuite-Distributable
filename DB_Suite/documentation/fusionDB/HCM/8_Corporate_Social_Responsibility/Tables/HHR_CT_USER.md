# HHR_CT_USER

This table is created to store the users info

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrctuser-27538.html#hhrctuser-27538](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrctuser-27538.html#hhrctuser-27538)

## Primary Key

| Name | Columns |
|------|----------|
| hhr_ct_user_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | ID |
| HCM_PERSON_ID | NUMBER |  | 18 | Yes | HCM_PERSON_ID |
| CT_USER_ID | VARCHAR2 | 20 |  |  | CT_USER_ID |
| CT_SYNC_STATUS | VARCHAR2 | 40 |  |  | CT_SYNC_STATUS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hhr_ct_user_U1 | Unique | FUSION_TS_TX_DATA | HCM_PERSON_ID |
| hhr_ct_user_U2 | Unique | FUSION_TS_TX_DATA | ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
