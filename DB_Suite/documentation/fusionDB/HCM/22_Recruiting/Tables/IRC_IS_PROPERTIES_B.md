# IRC_IS_PROPERTIES_B

This table stores the interview scheduling properties.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircispropertiesb-28538.html#ircispropertiesb-28538](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircispropertiesb-28538.html#ircispropertiesb-28538)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IS_PROPERTIES_B_PK | PROPERTY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROPERTY_ID | NUMBER |  | 18 | Yes | Primary key for this table.System generated. |
| OBJECT_TYPE | VARCHAR2 | 32 |  | Yes | Stores object type related to the property e.g. "ORA_IS_SCHEDULE". |
| OBJECT_ID | NUMBER |  | 18 | Yes | Stores the object id related to the property e.g. SCHEDULE_ID. |
| PROPERTY_CODE | VARCHAR2 | 36 |  | Yes | Stores the code used for data migration purpose. This column will be populated with a GUID value to uniquely identify a row across environments. |
| PROPERTY_NAME | VARCHAR2 | 32 |  | Yes | Stores the name of the property e.g. "STAGE_NAME". |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IS_PROPERTIES_B_PK | Unique | Default | PROPERTY_ID |
| IRC_IS_PROPERTIES_B_U1 | Unique | Default | OBJECT_TYPE, OBJECT_ID, PROPERTY_NAME |
| IRC_IS_PROPERTIES_B_U2 | Unique | Default | PROPERTY_CODE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
