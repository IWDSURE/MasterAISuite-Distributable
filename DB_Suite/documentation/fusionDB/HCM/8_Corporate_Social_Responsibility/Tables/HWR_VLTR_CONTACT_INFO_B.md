# HWR_VLTR_CONTACT_INFO_B

This is the base table that has the contact information of the project

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrcontactinfob-8188.html#hwrvltrcontactinfob-8188](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrcontactinfob-8188.html#hwrvltrcontactinfob-8188)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_CONTACT_INFO_B_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | ID |
| CONTACT_PHONE | VARCHAR2 | 400 |  |  | CONTACT_TITLES |
| CONTACT_FAX | VARCHAR2 | 400 |  |  | CONTACT_FAX |
| EMAIL | VARCHAR2 | 400 |  |  | EMAIL |
| WEBSITE | VARCHAR2 | 400 |  |  | WEBSITE |
| LOCATION_ID | NUMBER |  | 18 |  | LOCATION_ID |
| ADDRESS_TYPE | VARCHAR2 | 100 |  |  | ADDRESS_TYPE |
| ENTITY_ID | NUMBER |  | 18 | Yes | ENTITY_ID |
| ENTITY_TYPE | VARCHAR2 | 100 |  |  | ENTITY_TYPE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_CONTACT_INFO_B_N1 | Non Unique | FUSION_TS_TX_IDX | ENTITY_ID, ENTITY_TYPE |
| HWR_VLTR_CONTACT_INFO_B_U1 | Unique | FUSION_TS_TX_IDX | ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
