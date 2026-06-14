# IRC_AVAIL_CXT_REQ_DFF

This table is used to store the configuration data for availability context of dimension requisition dff. Each row represents a dimension value in a context.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircavailcxtreqdff-30254.html#ircavailcxtreqdff-30254](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircavailcxtreqdff-30254.html#ircavailcxtreqdff-30254)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AVAIL_CXT_REQ_DFF_PK | OBJECT_CXT_REQ_DFF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECT_CXT_REQ_DFF_ID | NUMBER |  | 18 | Yes | Primary Key - Sequence generated key. Fusion Global sequence generator is used to generate the key at run-time. |
| OBJECT_CXT_REQ_DFF_CODE | VARCHAR2 | 36 |  | Yes | Object Context Code is used for data migration purpose. This column will be populated with a GUID value to uniquely identify a row across environments |
| OBJECT_CXT_ID | NUMBER |  | 18 | Yes | Foreign Key of IRC_AVAIL_CONTEXT |
| REQ_CONTEXT_CODE | VARCHAR2 | 80 |  | Yes | Code of the Context associated to the DFF |
| SEGMENT_CODE | VARCHAR2 | 30 |  | Yes | Code of the Segment associated to the DFF |
| TIMESTAMP_VALUE | TIMESTAMP |  |  |  | Flexfield value from the object |
| NUMBER_VALUE | NUMBER |  |  |  | Flexfield value from the object |
| DATE_VALUE | DATE |  |  |  | Flexfield value from the object |
| CHAR_VALUE | VARCHAR2 | 1000 |  |  | Flexfield value from the object |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AVAIL_CXT_REQ_DFF_N1 | Non Unique | Default | OBJECT_CXT_ID, SEGMENT_CODE, TIMESTAMP_VALUE |
| IRC_AVAIL_CXT_REQ_DFF_N2 | Non Unique | Default | OBJECT_CXT_ID, SEGMENT_CODE, NUMBER_VALUE |
| IRC_AVAIL_CXT_REQ_DFF_N3 | Non Unique | Default | OBJECT_CXT_ID, SEGMENT_CODE, DATE_VALUE |
| IRC_AVAIL_CXT_REQ_DFF_N4 | Non Unique | Default | OBJECT_CXT_ID, SEGMENT_CODE, CHAR_VALUE |
| IRC_AVAIL_CXT_REQ_DFF_PK | Unique | Default | OBJECT_CXT_REQ_DFF_ID |
| IRC_AVAIL_CXT_REQ_DFF_U1 | Unique | Default | OBJECT_CXT_REQ_DFF_CODE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
