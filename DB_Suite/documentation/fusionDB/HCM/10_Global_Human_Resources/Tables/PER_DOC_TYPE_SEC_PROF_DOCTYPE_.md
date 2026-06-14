# PER_DOC_TYPE_SEC_PROF_DOCTYPE_

This table contains the Document Types selected in the Document Type Security Profile.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdoctypesecprofdoctype-6114.html#perdoctypesecprofdoctype-6114](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdoctypesecprofdoctype-6114.html#perdoctypesecprofdoctype-6114)

## Primary Key

| Name | Columns |
|------|----------|
| PER_DOCTYP_SEC_PROF_DOCTYP_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, DOC_TYPE_SEC_PROF_DOC_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DOC_TYPE_SEC_PROF_DOC_TYPE_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |
| DOC_TYPE_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to PER_DOC_TYPE_SECURITY_PROFILE table. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| DOCUMENT_TYPE_ID | NUMBER |  | 18 |  | Foreign Key to HR_DOCUMENT_TYPES_B table |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_DOCTP_SECPROF_DOCTPN1_ | Non Unique | Default | DOC_TYPE_SEC_PROF_DOC_TYPE_ID |
| PER_DOCTYP_SEC_PROF_DOCTYP_PK_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, DOC_TYPE_SEC_PROF_DOC_TYPE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
