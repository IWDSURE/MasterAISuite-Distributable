# IRC_ASMT_REQ_PACKAGES

This table contains the data about the assessment packages configured for requisitions.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircasmtreqpackages-29435.html#ircasmtreqpackages-29435](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircasmtreqpackages-29435.html#ircasmtreqpackages-29435)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_ASMT_REQ_PACKAGES_PK | REQ_PACKAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQ_PACKAGE_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| ASSESSMENT_CONFIG_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_ASMT_REQ_CONFIG table. |
| TRIGGER_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Trigger type to which the package is assigned to. |
| PACKAGE_CODE | VARCHAR2 | 30 |  | Yes | Stores the package code of the assessment package. |
| PACKAGE_SEQUENCE | NUMBER |  | 4 | Yes | Stores the package sequence of the assessment package. Value for this will be 1 for single phase assessment packages. |
| PHASE_ID | NUMBER |  | 18 |  | Foreign key IRC_PHASES_B table. PHASE_ID value will be populated for CSP assessments. |
| STATE_ID | NUMBER |  | 18 |  | Foreign key IRC_STATES_B table. STATE_ID value will be populated for CSP assessments. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_ASMT_REQ_PACKAGES_FK1 | Non Unique | Default | ASSESSMENT_CONFIG_ID |
| IRC_ASMT_REQ_PACKAGES_FK2 | Non Unique | Default | PHASE_ID |
| IRC_ASMT_REQ_PACKAGES_FK3 | Non Unique | Default | STATE_ID |
| IRC_ASMT_REQ_PACKAGES_PK | Unique | Default | REQ_PACKAGE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
