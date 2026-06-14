# IRC_REQ_WORK_LOCATIONS

Stores all other work locations for a Requisition.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreqworklocations-6061.html#ircreqworklocations-6061](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreqworklocations-6061.html#ircreqworklocations-6061)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REQ_WORK_LOCATIONS_PK | REQ_WORK_LOCATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQ_WORK_LOCATION_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REQUISITIONS_B. |
| LOCATION_ID | NUMBER |  | 18 | Yes | Foreign key to PER_LOCATIONS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REQ_WORK_LOCATIONS_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_REQ_WORK_LOCATIONS_FK2 | Non Unique | Default | LOCATION_ID |
| IRC_REQ_WORK_LOCATIONS_PK | Unique | Default | REQ_WORK_LOCATION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
