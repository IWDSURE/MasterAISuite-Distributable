# CMP_MKT_VENDORS_B

Stores Vendor data for Market Survey data in the database.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktvendorsb-7780.html#cmpmktvendorsb-7780](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktvendorsb-7780.html#cmpmktvendorsb-7780)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_MKT_VENDOR_PK | VENDOR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VENDOR_ID | NUMBER |  | 18 | Yes | Primary Key |
| VENDOR_SEQ_NUM | NUMBER |  |  |  | Vendor Sequence Number |
| VENDOR_CODE | VARCHAR2 | 30 |  | Yes | Vendor Code |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group Id |
| STATUS | VARCHAR2 | 30 |  | Yes | Vendor Status |
| CONTACT_NAME_1 | VARCHAR2 | 80 |  |  | Contact Name 1 |
| CONTACT_EMAIL_1 | VARCHAR2 | 80 |  |  | Contact Email 1 |
| CONTACT_PHONE_1 | VARCHAR2 | 20 |  |  | Contact Phone 1 |
| CONTACT_NAME_2 | VARCHAR2 | 80 |  |  | Contact Name 2 |
| CONTACT_EMAIL_2 | VARCHAR2 | 80 |  |  | Contact Email 2 |
| CONTACT_PHONE_2 | VARCHAR2 | 20 |  |  | Contact Phone 2 |
| WEBSITE | VARCHAR2 | 50 |  |  | Vendor website |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_MKT_VENDORS_B_U1 | Unique | Default | VENDOR_CODE |
| CMP_MKT_VENDOR_U1 | Unique | Default | VENDOR_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
