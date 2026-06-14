# IRC_LC_ACTION_USAGES_TL

translation table for corresponding 'IRC_STEP_ACTION_USAGES_B' table.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcactionusagestl-18493.html#irclcactionusagestl-18493](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcactionusagestl-18493.html#irclcactionusagestl-18493)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LC_ACTION_USAGES_TL_PK | STEP_ACTION_USAGE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| STEP_ACTION_USAGE_ID | NUMBER |  | 18 | Yes | STEP ACTION USAGE ID : Primary key part and points to _B table |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| ACTION_NAME | VARCHAR2 | 512 |  | Yes | ACTION NAME : corresponding action name to be translated |  |
| ACTION_DESCRIPTION | VARCHAR2 | 1000 |  |  | ACTION DESCRIPTION : Corresponding action description to be translated |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LC_ACTION_USAGES_TL_U1 | Unique | Default | STEP_ACTION_USAGE_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
