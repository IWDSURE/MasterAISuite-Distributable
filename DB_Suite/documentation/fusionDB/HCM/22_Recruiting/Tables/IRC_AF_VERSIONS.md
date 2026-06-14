# IRC_AF_VERSIONS

Base Table for Versions of Apply Flow.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircafversions-24656.html#ircafversions-24656](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircafversions-24656.html#ircafversions-24656)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AF_VERSIONS_PK | AF_VERSION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AF_VERSION_ID | NUMBER |  | 18 | Yes | Primary Key for this table. System generated. |
| APPLY_FLOW_ID | NUMBER |  | 18 | Yes | ID of the corresponding Apply Flow. Foreign Key to IRC_APPLY_FLOWS_B. |
| VERSION_NAME | VARCHAR2 | 240 |  | Yes | Stores the name of the apply flow version. |
| VERSION_STATUS_CODE | VARCHAR2 | 30 |  | Yes | Indicates the status of the apply flow version based on lookup.  The corresponding lookup type is ORA_IRC_AF_VERSION_STATUS. |
| VERSION_START_DATE | TIMESTAMP |  |  |  | Stores the date time from which apply flow  version is valid. |
| LEGAL_ENABLED_FLAG | VARCHAR2 | 1 |  |  | Stores whether Legal Description is enabled for the Apply Flow Version. |
| ESIGN_ENABLED_FLAG | VARCHAR2 | 1 |  |  | Stores if the E-Signature is enabled for Apply Flow Version. |
| OPTIN_ENABLED_FLAG | VARCHAR2 | 1 |  |  | Stores if the Opt in is enabled for Apply Flow Version. |
| TC_OPTIN_ENABLED_FLAG | VARCHAR2 | 1 |  |  | Stores if the Opt in is enabled for Talent Community Apply Flow Version. |
| SINGLE_CLICK_APPLY_FLAG | VARCHAR2 | 1 |  |  | Stores whether Apply flow is Single click enabled for the Apply Flow Version. |
| QUICK_APPLY_ENABLED_FLAG | VARCHAR2 | 1 |  |  | Stores if the Quick Apply is enabled for Apply Flow Version. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AF_VERSIONS_FK1 | Non Unique | Default | APPLY_FLOW_ID |
| IRC_AF_VERSIONS_PK | Unique | Default | AF_VERSION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
