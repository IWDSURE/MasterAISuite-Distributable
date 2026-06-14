# PER_SHARE_INFORMATION

This table records the items of personal, employment etc., information are to be shared for a given instance.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pershareinformation-25465.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pershareinformation-25465.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SHARE_INFORMATION_PK | SHARE_INSTANCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SHARE_INSTANCE_ID | NUMBER |  | 18 | Yes | Primary Key column |
| EXPIRATION_DATE | DATE |  |  |  | Expiration date for sharing information |
| PERSON_ID | NUMBER |  | 18 | Yes | System Identifier for the Person whose information is being shared |
| ACCESS_KEY | VARCHAR2 | 240 |  |  | Key used for login in and seeing the shared data when information is shared Externally. |
| VERIFICATION_KEY | VARCHAR2 | 240 |  |  | Key used in the URL for checking and locating an appropriate record of Share Information |
| VISITS_REMAINING | NUMBER |  | 2 |  | Counter that starts equal to NUMBER_OF_VISITS and get decreasing by 1 till 0 each time the page is accessed by Recipient |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment Identifier for the Person whose information is being shared |
| GRANTEE_EMAIL | VARCHAR2 | 240 |  |  | Records the email address to which the external Share of Information will be sent. |
| REPLY_TO_EMAIL | VARCHAR2 | 240 |  |  | Records the email address of the person who shared the information in case of external sharing. |
| GRANTEE_NAME | VARCHAR2 | 240 |  |  | Name of the External person with whom the information is shared. |
| GRANTEE_PERSON_ID | NUMBER |  | 18 |  | Records the Person Id that was granted system access in internal sharing of information. |
| ACCESS_GRANTED_BY | NUMBER |  | 18 |  | System identifier to the person who granted the access. |
| NUMBER_OF_DAYS | NUMBER |  | 2 |  | It stores the period of share information in the external sharing. |
| NUMBER_OF_VISITS | NUMBER |  | 2 |  | It stores the max. no. of visits for external person. |
| COMMENTS | VARCHAR2 | 2000 |  |  | Comments provided during the share information. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_SHARE_INFORMATION_N1 | Non Unique | Default | PERSON_ID, GRANTEE_PERSON_ID |
| PER_SHARE_INFORMATION_N2 | Non Unique | Default | GRANTEE_PERSON_ID, PERSON_ID |
| PER_SHARE_INFORMATION_PK | Unique | Default | SHARE_INSTANCE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
