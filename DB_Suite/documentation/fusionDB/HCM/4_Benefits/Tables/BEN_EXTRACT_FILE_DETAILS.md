# BEN_EXTRACT_FILE_DETAILS

BEN_EXTRACT_FILE_DETAILS  Stores enrollment XML file data.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benextractfiledetails-19131.html#benextractfiledetails-19131](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benextractfiledetails-19131.html#benextractfiledetails-19131)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_EXTRACT_FILE_DETAILS_PK | EXTRACT_FILE_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXTRACT_FILE_DETAIL_ID | NUMBER |  | 18 | Yes | Primary key |
| SOURCE_TYPE | VARCHAR2 | 80 |  |  | Determines from where the File came from |
| FILE_TYPE | VARCHAR2 | 80 |  |  | File type could be XML or text |
| INTERNAL_FILE_NAME | VARCHAR2 | 80 |  |  | System Given Name |
| SEQUENCE | NUMBER |  | 18 |  | If the file is split, the sequence is maintained |
| FILE_FRAGMENT | CLOB |  |  |  | Actual File |
| CARRIER_ID | NUMBER |  | 18 |  | Healt Care Provider Id |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Business Group |
| FILE_LOCATION | VARCHAR2 | 80 |  |  | Indicates location of  the file finally uploaded |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | Schedular Request Id |
| PARENT_REQUEST_ID | NUMBER |  | 18 |  | Stores Parent request Id in a case where the file is split |
| VERSION | NUMBER |  | 18 |  | File Version when saved multiple time for the same ess request Id |
| CONTENT_ID | NUMBER |  | 18 |  | Content Repository id |
| GROUP_ID | NUMBER |  | 18 |  | If the File is split, the group Id will be the first Primary key Id of those files |
| SOURCE | VARCHAR2 | 80 |  |  | Indicates the file source, whether it is Java or plsql or manual |
| DOC_ID | VARCHAR2 | 80 |  |  | Store any extrnal Document Id |
| RUN_DATE | DATE |  |  |  | Stores Date when the transmission was executed |
| STATUS | VARCHAR2 | 80 |  |  | Stores if the file is active , pending or inactive |
| ATTR_CHAR01 | VARCHAR2 | 80 |  |  | For any future use |
| ATTR_CHAR02 | VARCHAR2 | 80 |  |  | For any additional use in future |
| ATTR_CHAR03 | VARCHAR2 | 80 |  |  | For any future use |
| ATTR_NUM01 | NUMBER |  | 18 |  | For any future use to store number |
| ATTR_NUM02 | NUMBER |  | 18 |  | For any future use to store number |
| ATTR_NUM03 | NUMBER |  | 18 |  | For any future use to store number |
| ATTR_DATE01 | DATE |  |  |  | Sore any future date data |
| ATTR_DATE02 | DATE |  |  |  | For any future use to store date |
| ATTR_DATE03 | DATE |  |  |  | For any future use to store date |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_EXTRACT_FILE_DETAILS_U1 | Unique | Default | EXTRACT_FILE_DETAIL_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
