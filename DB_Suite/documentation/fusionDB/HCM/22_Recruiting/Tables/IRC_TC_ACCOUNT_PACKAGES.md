# IRC_TC_ACCOUNT_PACKAGES

This table contains the data about the packages assigned to the partner accounts.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctcaccountpackages-26531.html#irctcaccountpackages-26531](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctcaccountpackages-26531.html#irctcaccountpackages-26531)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TC_ACCOUNT_PACKAGES_PK | ACCOUNT_PACKAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACCOUNT_PACKAGE_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| ACCOUNT_ID | NUMBER |  | 18 | Yes | Foreign  key to IRC_TP_PARTNER_ACCOUNTS. |
| PACKAGE_CODE | VARCHAR2 | 30 |  | Yes | Stores the package code for the tax credit package assigned to the partner account. |
| PACKAGE_NAME | VARCHAR2 | 500 |  | Yes | Stores the package name for the tax credit package assigned to the partner account. |
| PACKAGE_DESC | VARCHAR2 | 1000 |  |  | Stores the description for the tax credit package assigned to the partner account. |
| OBJECT_STATUS | VARCHAR2 | 30 |  | Yes | Stores the status of the Object as a lookup code. The corresponding lookup type is ORA_IRC_OBJECT_STATUS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TC_ACCOUNT_PACKAGES_FK1 | Non Unique | Default | ACCOUNT_ID |
| IRC_TC_ACCOUNT_PACKAGES_PK | Unique | Default | ACCOUNT_PACKAGE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
