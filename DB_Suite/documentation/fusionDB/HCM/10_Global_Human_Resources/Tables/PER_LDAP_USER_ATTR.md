# PER_LDAP_USER_ATTR

Table for storing extra ldap user request attributes

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perldapuserattr-30644.html#perldapuserattr-30644](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perldapuserattr-30644.html#perldapuserattr-30644)

## Primary Key

| Name | Columns |
|------|----------|
| PER_LDAP_USER_ATTR_PK | LDAP_USER_ATTR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LDAP_USER_ATTR_ID | NUMBER |  | 18 | Yes | Mandatory primary key updatable while new key generation |
| LDAP_USER_ID | NUMBER |  | 18 | Yes | Foreign Key to LDAP user request. Mandatory. Updatable while new mandatory FK association. |
| DISPLAY_NAME_LANG | VARCHAR2 | 4 |  | Yes | Language for the disaply name |
| DISPLAY_NAME | VARCHAR2 | 240 |  | Yes | Language specific display name |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_LDAP_USER_ATTR_FK1 | Non Unique | FUSION_TS_TX_DATA | LDAP_USER_ID |
| PER_LDAP_USER_ATTR_U1 | Unique | FUSION_TS_TX_DATA | LDAP_USER_ATTR_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
