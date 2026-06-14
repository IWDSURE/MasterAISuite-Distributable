# HRC_DL_REM_ENTITY_REFERENCES

SEED Table for Storing individual Business Object references in HDL Hierarchy

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlrementityreferences-8863.html#hrcdlrementityreferences-8863](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlrementityreferences-8863.html#hrcdlrementityreferences-8863)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_REM_ENT_REFER_PK | ENTITY_REFERENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTITY_REFERENCE_ID | NUMBER |  | 18 | Yes | ENTITY_REFERENCE_ID |
| ENTITY_ID | NUMBER |  | 18 | Yes | ENTITY_ID |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| LOCAL_VO_ATTRIBUTE | VARCHAR2 | 100 |  |  | LOCAL_VO_ATTRIBUTE |
| REFERENCE_HIERARCHY | VARCHAR2 | 200 |  |  | REFERENCE_HIERARCHY |
| REF_BUSINESS_OBJECT_ID | NUMBER |  | 18 |  | REF_BUSINESS_OBJECT_ID |
| DATA_QUERY | CLOB |  |  |  | DATA_QUERY |
| OVERRIDE_QUERY | CLOB |  |  |  | OVERRIDE_QUERY |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_REM_ENT_REFER_U1 | Unique | Default | ENTITY_REFERENCE_ID |
| HRC_DL_REM_ENT_REFER_U2 | Unique | Default | ENTITY_ID, REF_BUSINESS_OBJECT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
