# PER_USERS

Table for storing one record per fusion system user. Maps to a single LDAP user unless the user is deleted in LDAP.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perusers-19050.html#perusers-19050](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perusers-19050.html#perusers-19050)

## Primary Key

| Name | Columns |
|------|----------|
| PER_USERS_PK | USER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USER_ID | NUMBER |  | 18 | Yes | Mandatory Primary Key Updatable While New Key Generation |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ACTIVE_FLAG | VARCHAR2 | 30 |  | Yes | Flag to mark when a user record that has been deleted in LDAP. This is not set to 'N' when a user is just suspended. |
| START_DATE | DATE |  |  | Yes | The date that the user is active from. |
| END_DATE | DATE |  |  |  | The date that the user ceases to be active in fusion. |
| USER_GUID | VARCHAR2 | 64 |  | Yes | The latest user Guid of the user. |
| USERNAME | VARCHAR2 | 100 |  |  | The latest principal username of the user |
| MULTITENANCY_USERNAME | VARCHAR2 | 255 |  |  | Display Username of the user |
| PERSON_ID | NUMBER |  | 18 |  | Person ID in HCM for this user (if available) |
| PARTY_ID | NUMBER |  | 18 |  | Party ID in TCA for this user (if available) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| HR_TERMINATED | VARCHAR2 | 30 |  |  | Implies the user is terminated in HR by HR. |
| SUSPENDED | VARCHAR2 | 30 |  |  | When the user, as part of termination, is suspended. If suspended, the user can be reactivated. |
| USER_DISTINGUISHED_NAME | VARCHAR2 | 4000 |  |  | The latest distinguished name of the user |
| USER_DATA_CHECKSUM | VARCHAR2 | 64 |  |  | User Data Checksum. |
| CREDENTIALS_EMAIL_SENT | VARCHAR2 | 30 |  | Yes | Flag to show whether credentials (username/password) has been sent out.

Y=Sent
N=Not Sent |
| EXTERNAL_ID | VARCHAR2 | 64 |  |  | EXTERNAL_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_USERS_N1 | Non Unique | FUSION_TS_TX_DATA | UPPER("USERNAME") |
| PER_USERS_N2 | Non Unique | FUSION_TS_TX_DATA | USERNAME |
| PER_USERS_N3 | Non Unique | FUSION_TS_TX_DATA | UPPER("MULTITENANCY_USERNAME") |
| PER_USERS_N4 | Non Unique | FUSION_TS_TX_DATA | MULTITENANCY_USERNAME |
| PER_USERS_N5 | Non Unique | FUSION_TS_TX_DATA | UPPER("USER_GUID") |
| PER_USERS_N6 | Non Unique | FUSION_TS_TX_DATA | EXTERNAL_ID |
| PER_USERS_PK | Unique | FUSION_TS_TX_DATA | USER_ID |
| PER_USERS_U1 | Unique | FUSION_TS_TX_DATA | PERSON_ID |
| PER_USERS_U2 | Unique | FUSION_TS_TX_DATA | USER_GUID |
| PER_USERS_U3 | Unique | FUSION_TS_TX_DATA | PARTY_ID |
| PER_USERS_U4 | Unique | FUSION_TS_TX_DATA | USER_DISTINGUISHED_NAME |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
