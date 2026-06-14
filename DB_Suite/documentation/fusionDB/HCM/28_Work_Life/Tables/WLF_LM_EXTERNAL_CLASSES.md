# WLF_LM_EXTERNAL_CLASSES

This table is for external classes

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmexternalclasses-5611.html#wlflmexternalclasses-5611](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmexternalclasses-5611.html#wlflmexternalclasses-5611)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LM_EXTERNAL_CLASSES_PK | EXTERNAL_CLASSES_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXTERNAL_CLASSES_ID | NUMBER |  | 18 | Yes | Primary key |
| EXTERNAL_COURSE_ID | NUMBER |  | 18 |  | reference key from WLF_LM_EXTERNAL_COURSES |
| CONTENT_ID | NUMBER |  | 18 |  | refrence key |
| COURSE_ID | NUMBER |  | 18 |  | reference key for course |
| HASH_CODE | NUMBER |  | 18 |  | version key |
| SIGNATURE_TRACK_REGULAR_PRICE | NUMBER |  |  |  | signature track regular price |
| STATUS | VARCHAR2 | 250 |  |  | row status |
| ACTIVE | VARCHAR2 | 250 |  |  | row active |
| HOME_LINK | VARCHAR2 | 1000 |  |  | home link |
| ELIGIBLE_FOR_CERTIFICATES | VARCHAR2 | 4000 |  |  | eligible for certificates for the course |
| ELIGIBLE_FOR_SIGNATURE_TRACK | VARCHAR2 | 4000 |  |  | eligible for signature track for the course |
| CERTIFICATES_READY | VARCHAR2 | 4000 |  |  | certificates ready for the course |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LM_EXTERNAL_CLASSES_U1 | Unique | DEFAULT | EXTERNAL_CLASSES_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
