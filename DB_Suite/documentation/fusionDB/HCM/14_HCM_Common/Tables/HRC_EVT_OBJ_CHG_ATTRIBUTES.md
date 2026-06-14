# HRC_EVT_OBJ_CHG_ATTRIBUTES

A Source Object Change Attribute stores the old and new  values of a particular EO or Row Handler attribute when that attribute changes within a transaction.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtobjchgattributes-19790.html#hrcevtobjchgattributes-19790](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtobjchgattributes-19790.html#hrcevtobjchgattributes-19790)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_EVT_OBJ_CHG_ATTRS_PK | CHANGE_ATTRIBUTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHANGE_ATTRIBUTE_ID | NUMBER |  | 18 | Yes | Unique Identifier |
| ATTRIBUTE_NAME | VARCHAR2 | 80 |  |  | Name of the changed attribute |
| CHANGE_COMPONENT_ID | NUMBER |  | 18 | Yes | Identifier of parent Change Component |
| DATA_TYPE | VARCHAR2 | 30 |  | Yes | Renormalized value of Data Type |
| OLD_VALUE_N | NUMBER |  | 18 |  | Attribute Old Value (Number) |
| NEW_VALUE_N | NUMBER |  | 18 |  | Attribute New Value (Number) |
| OLD_VALUE_V | VARCHAR2 | 2000 |  |  | Attribute Old Value (Text) |
| NEW_VALUE_V | VARCHAR2 | 2000 |  |  | Attribute New Value (Text) |
| OLD_VALUE_D | DATE |  |  |  | Attribute Old Value (Date) |
| NEW_VALUE_D | DATE |  |  |  | Attribute New Value (Date) |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_EVT_OBJ_CHG_ATTRS_F2 | Non Unique | FUSION_TS_TX_DATA | CHANGE_COMPONENT_ID |
| HRC_EVT_OBJ_CHG_ATTRS_PK | Unique | FUSION_TS_TX_DATA | CHANGE_ATTRIBUTE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
