# PER_INCR_KEY_PRSN_GT

This Global Temporary is used to save persons info collected by the keyword search crawler during incremental option.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perincrkeyprsngt-27098.html#perincrkeyprsngt-27098](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perincrkeyprsngt-27098.html#perincrkeyprsngt-27098)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_ID | NUMBER |  | 18 | Yes | This column stores the Person Identifier. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign Key to PER_ALL_ASSIGNMENTS_M table. |
| START_DATE | DATE |  |  |  | Date to calculate the keywords. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
