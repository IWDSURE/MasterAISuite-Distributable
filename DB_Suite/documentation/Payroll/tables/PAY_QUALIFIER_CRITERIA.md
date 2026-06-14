# PAY_QUALIFIER_CRITERIA

This table contains details of whether a combination of element eligibility criteria is potentially matched by a combination of payroll relationship, assigned payroll, or payroll assignment criteria. It is used for efficient eligibility checking during operations to create, update, and delete elements.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payqualifiercriteria-12343.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payqualifiercriteria-12343.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_QUALIFIER_CRITERIA_PK | LINK_CRITERIA_ID, ELEMENT_CRITERIA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LINK_CRITERIA_ID | NUMBER |  | 18 | Yes | LINK_CRITERIA_ID |
| ELEMENT_CRITERIA_ID | NUMBER |  | 18 | Yes | ELEMENT_CRITERIA_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_QUALIFIER_CRITERIA_N2 | Non Unique | Default | ELEMENT_CRITERIA_ID |
| PAY_QUALIFIER_CRITERIA_PK | Unique | Default | LINK_CRITERIA_ID, ELEMENT_CRITERIA_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
