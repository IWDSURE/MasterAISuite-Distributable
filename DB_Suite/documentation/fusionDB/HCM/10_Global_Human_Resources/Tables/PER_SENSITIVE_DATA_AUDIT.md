# PER_SENSITIVE_DATA_AUDIT

This table is new for Fusion, and has been created to store the sensitive data audit.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persensitivedataaudit-26287.html#persensitivedataaudit-26287](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persensitivedataaudit-26287.html#persensitivedataaudit-26287)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SENSITIVE_DATA_AUDIT_PK | AUDIT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AUDIT_ID | NUMBER |  | 18 | Yes | System Generated Primary Key |
| AUDIT_DATE | DATE |  |  | Yes | Date indicating when this audit information is logged |
| AUDIT_TIME | TIMESTAMP |  |  | Yes | Time indicating when this audit information is logged |
| BROWSER | VARCHAR2 | 200 |  |  | User Agent Parsed for browsername Firefox/Google Chrome/ |
| OPERATING_SYSTEM | VARCHAR2 | 200 |  |  | User Agent Parsed for OS and Version Example (apple mac os x 10.14.6) |
| DEVICE_TYPE | VARCHAR2 | 200 |  |  | User Agent Parsed for Device Type |
| DEVICE_NAME | VARCHAR2 | 200 |  |  | User Agent Parsed for Device Name |
| IP_ADDRESS | VARCHAR2 | 200 |  |  | TrueClient IP header set by oracle Load Balancer captured by applcore session. Example:192.10.3.19 |
| VIEWER_USER_NAME | VARCHAR2 | 64 |  |  | Username from the applcore session |
| VIEWER_PERSON_ID | NUMBER |  | 18 |  | Person ID of the logged in person |
| VIEWED_PERSON_NUMBER | VARCHAR2 | 30 |  |  | Person Number of the person whose data is accessed. |
| VIEWED_PERSON_ID | NUMBER |  | 18 |  | Person ID of the person whose data is accessed. |
| VIEWED_PAGE_TITLE | VARCHAR2 | 400 |  |  | Title of the page where the PII data is present |
| VIEWED_PII_DATA_TYPE | VARCHAR2 | 400 |  |  | Type of PII data |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_SENSITIVE_DATA_AUDIT_U1 | Unique | Default | AUDIT_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
