# HRY_EXT_PARSE_DTLS

Stores the sub xmls after parsing the large xml based on the xml tag.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryextparsedtls-15113.html#hryextparsedtls-15113](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryextparsedtls-15113.html#hryextparsedtls-15113)

## Primary Key

| Name | Columns |
|------|----------|
| HRY_EXT_PARSE_DTLS_PK | PARSE_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PARSE_DETAIL_ID | NUMBER |  | 18 | Yes | Primary Key for HRY_EXT_PARSE_DETAIL. |
| OBJ_GRP_NUMBER | NUMBER |  | 18 |  | For storing the object group number that is stored during splitting so thatwhile stitching the xml back, the parent is known. |
| TRANSFORMATION_ID | NUMBER |  | 18 | Yes | Foreign key to HRY_ENT_TRANSFORMATION table |
| RAW_XML | CLOB |  |  |  | For storing the sub raw xmls after parsing |
| CHUNK_NUMBER | NUMBER |  | 18 | Yes | For storing the assigned chunk number needed for multithreading |
| ALLOCATION_STATUS | VARCHAR2 | 200 |  |  | For checking if the row is already assigned to a thread. This column will be used for multithreading. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_EXT_PARSE_DTLS_N1 | Non Unique | Default | TRANSFORMATION_ID, CHUNK_NUMBER |
| HRY_EXT_PARSE_DTLS_PK | Unique | Default | PARSE_DETAIL_ID |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
