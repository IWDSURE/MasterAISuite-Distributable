# BEN_PL_CARRIER

This table holds information of  the benefit plan carrier, and the information pertaining to how the carrier expects the extracted data to be sent.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplcarrier-18186.html#benplcarrier-18186](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplcarrier-18186.html#benplcarrier-18186)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PL_CARRIER_PK | CARRIER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CARRIER_ID | NUMBER |  | 18 | Yes | CARRIER_ID |
| EXT_CUSTOM_RULE_ID | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| REPORT_NAME | VARCHAR2 | 255 |  |  | REPORT_NAME |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| LAYOUT_ID | NUMBER |  | 18 |  | LAYOUT_ID |
| NAME | VARCHAR2 | 240 |  | Yes | NAME |
| DESCRIPTION | VARCHAR2 | 240 |  |  | DESCRIPTION |
| STAT_CD | VARCHAR2 | 30 |  |  | STAT_CD |
| PROCESSING_TYPE | VARCHAR2 | 30 |  |  | PROCESSING_TYPE |
| EXTRACT_TYPE | VARCHAR2 | 30 |  |  | EXTRACT_TYPE |
| TRANS_TYPE | VARCHAR2 | 30 |  |  | TRANS_TYPE |
| LOCATION_ID | NUMBER |  | 18 |  | LOCATION_ID |
| HRXML_FILE_NAME | VARCHAR2 | 60 |  |  | HRXML_FILE_NAME |
| FREQUENCY | VARCHAR2 | 30 |  |  | FREQUENCY |
| ARCHIVE_TYPE | VARCHAR2 | 30 |  |  | ARCHIVE_TYPE |
| SFTP_USER_NAME | VARCHAR2 | 30 |  |  | SFTP_USER_NAME |
| SFTP_PASSWORD | VARCHAR2 | 30 |  |  | SFTP_PASSWORD |
| SFTP_HOST | VARCHAR2 | 100 |  |  | SFTP_HOST |
| EMAIL_ADDRESS | VARCHAR2 | 60 |  |  | EMAIL_ADDRESS |
| ARCHIVE_DATE | DATE |  |  |  | ARCHIVE_DATE |
| ARCHIVE_DURATION | VARCHAR2 | 30 |  |  | ARCHIVE_DURATION |
| ARCHIVE_DURATION_UOM | VARCHAR2 | 30 |  |  | ARCHIVE_DURATION_UOM |
| REMOTE_FOLDER | VARCHAR2 | 255 |  |  | The folder on the ftp server  where the file needs to be placed. |
| SFTP_AUTHENTICATION_TYPE | VARCHAR2 | 30 |  |  | Identifies whether its password or public key |
| PRIVATE_KEY_FILE | VARCHAR2 | 255 |  |  | Private Key File |
| PORT | NUMBER |  | 9 |  | FTP port, defaults to 21 |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| FILE_FORMAT | CLOB |  |  |  | XML file format |
| PROVIDER_ID | VARCHAR2 | 255 |  |  | Provider Identifier |
| PRIVATE_KEY | CLOB |  |  |  | Private key |
| PUBLIC_KEY | CLOB |  |  |  | Public key |
| DELV_METHOD01 | VARCHAR2 | 80 |  |  | Delivery Method Column1 |
| DELV_METHOD02 | VARCHAR2 | 80 |  |  | Delivery method Column2 |
| DELV_METHOD03 | VARCHAR2 | 80 |  |  | Delivery Method Column3 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PL_CARRIER_U1 | Unique | Default | CARRIER_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
