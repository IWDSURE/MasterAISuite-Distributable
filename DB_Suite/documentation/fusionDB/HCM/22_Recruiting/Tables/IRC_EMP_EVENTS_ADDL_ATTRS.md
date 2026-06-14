# IRC_EMP_EVENTS_ADDL_ATTRS

This table stores the additional attributes we are caputing for the employee events like Category which has Multiple rows for an event

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircempeventsaddlattrs-16302.html#ircempeventsaddlattrs-16302](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircempeventsaddlattrs-16302.html#ircempeventsaddlattrs-16302)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_EMP_EVENTS_ADDL_ATTRS_PK | EMP_EVENT_ADDL_ATTR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EMP_EVENT_ADDL_ATTR_ID | NUMBER |  | 18 | Yes | Primary Key for this table. This is an auto-generated field |
| EMP_EVENT_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_EMP_EVENTS_B table |
| ATTRIBUTE_TYPE | VARCHAR2 | 30 |  |  | The type of the attribute we are capturing. This will have values like 'CATEGORY' |
| ATTRIBUTE_CODE | VARCHAR2 | 30 |  |  | The code of the attribute we are capturing. This can come from corresponding Lookup Tables like ORA_IRC_EMP_EVENT_CATEGORY for Category. |
| ATTRIBUTE_ID | NUMBER |  | 18 |  | The id of the attribute we are capturing. This can come from corresponding Lookup Tables. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_EMP_EVENTS_ADDL_ATTRS_FK1 | Non Unique | Default | EMP_EVENT_ID |
| IRC_EMP_EVENTS_ADDL_ATTRS_PK | Unique | Default | EMP_EVENT_ADDL_ATTR_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
