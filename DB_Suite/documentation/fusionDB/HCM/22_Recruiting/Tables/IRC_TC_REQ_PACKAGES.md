# IRC_TC_REQ_PACKAGES

This table contains the data about the tax credits packages configured for requisitions.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctcreqpackages-13342.html#irctcreqpackages-13342](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctcreqpackages-13342.html#irctcreqpackages-13342)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TC_REQ_PACKAGES_PK | TC_REQ_PACKAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TC_REQ_PACKAGE_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| TC_REQ_CONFIG_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TC_REQ_CONFIG table. |
| PACKAGE_CODE | VARCHAR2 | 30 |  |  | Stores the package code of the assessment package. |
| TRIGGER_TYPE_CODE | VARCHAR2 | 30 |  |  | Trigger type to which the package is assigned to. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TC_REQ_PACKAGES_FK1 | Non Unique | Default | TC_REQ_CONFIG_ID |
| IRC_TC_REQ_PACKAGES_PK | Unique | Default | TC_REQ_PACKAGE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
