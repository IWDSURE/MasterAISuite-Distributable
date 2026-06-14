# BEN_ENT_ABS_ATTENDNS_TYPS

Intersection table for BEN_ENTITLEMENT and PER_ABSENCE_ATTENDANCE_TYPES

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benentabsattendnstyps-21869.html#benentabsattendnstyps-21869](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benentabsattendnstyps-21869.html#benentabsattendnstyps-21869)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ENT_ABS_ATTENDNS_TYPS_PK | BEN_ENT_ABS_ATT_TYP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BEN_ENT_ABS_ATT_TYP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| ENTITLEMENT_ID | NUMBER |  | 18 | Yes | ENTITLEMENT_ID |
| ABSENCE_ATTENDANCE_TYPE_ID | NUMBER |  | 18 | Yes | ABSENCE_ATTENDANCE_TYPE_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ENT_ABS_ATTENDNS_TYPS_PK | Unique | Default | BEN_ENT_ABS_ATT_TYP_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
