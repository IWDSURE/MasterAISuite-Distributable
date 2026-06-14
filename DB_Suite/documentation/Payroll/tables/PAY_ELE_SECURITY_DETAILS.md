# PAY_ELE_SECURITY_DETAILS

This table holds information of payroll element security details.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelesecuritydetails-22013.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelesecuritydetails-22013.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ELE_SECURITY_DETAILS_PK | PAY_ELE_SECURITY_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAY_ELE_SECURITY_DETAIL_ID | NUMBER |  | 18 | Yes | PAY_ELE_SECURITY_DETAIL_ID |
| PAY_ELE_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | PAY_ELE_SECURITY_PROFILE_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CLASSIFICATION_ID | NUMBER |  | 18 |  | CLASSIFICATION_ID |
| INCLUSION_FLAG | VARCHAR2 | 1 |  | Yes | INCLUSION_FLAG |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | ELEMENT_TYPE_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | LEGISLATIVE_DATA_GROUP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ELE_SECURITY_DETAILS_PK | Unique | Default | PAY_ELE_SECURITY_DETAIL_ID, ORA_SEED_SET1 |
| PAY_ELE_SECURITY_DETAILS_PK1 | Unique | Default | PAY_ELE_SECURITY_DETAIL_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
