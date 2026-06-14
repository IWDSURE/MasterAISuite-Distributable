# HWM_TCAT_CMPS

This table stores all the components.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcatcmps-3867.html#hwmtcatcmps-3867](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcatcmps-3867.html#hwmtcatcmps-3867)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TCAT_CMPS_PK | TCAT_CMP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TCAT_CMP_ID | NUMBER |  | 18 | Yes | TCAT_CMPS_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TCAT_ID | NUMBER |  | 18 | Yes | FK to HWM_TCATS_B.TCAT_ID |
| DISPLAY_SEQUENCE | NUMBER |  | 18 |  | We need a sequence column to retain the ordering of components the user is comfortable with. But can the users reorder sort etc? |
| TM_ATRB_FLD_ID | NUMBER |  | 18 | Yes | FK to HWM_TM_ATRB_FLDS_B |
| VALUE_TYPE | VARCHAR2 | 50 |  | Yes | Column to store Specific Value, null value, any value or value set CODE |
| VALUE_ID | NUMBER |  | 18 |  | Column to store the literal value id or the value set id |
| NESTED_TCAT_ID | NUMBER |  | 18 |  | FK to HWM_TCATS |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise Id |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TCAT_CMPS_U1 | Unique | Default | TCAT_CMP_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
