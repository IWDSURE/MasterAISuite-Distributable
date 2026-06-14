# HRR_TMPL_DISPLAY_OPTN_PREFS

This table stores the color/shape preferences for display options Impact of Loss, Mobility and Risk of Loss

## Details

**Schema:** FUSION

**Object owner:** HRR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrtmpldisplayoptnprefs-15280.html#hrrtmpldisplayoptnprefs-15280](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrtmpldisplayoptnprefs-15280.html#hrrtmpldisplayoptnprefs-15280)

## Primary Key

| Name | Columns |
|------|----------|
| HRR_TMPL_DISPLAY_OPN_PREF_PK | DISPLAY_OPTN_PREF_ID, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DISPLAY_OPTN_PREF_ID | NUMBER |  | 18 | Yes | System generated primary key to this table |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise Id |
| DASHBOARD_TMPL_ID | NUMBER |  | 18 | Yes | Forigen key HRR_DASHBOARD_TMPLS_B table |
| DISPLAY_OPTN_TYPE | VARCHAR2 | 30 |  | Yes | Display option type for which preferences are being set |
| DISPLAY_OPTN_VALUE | VARCHAR2 | 30 |  | Yes | Display option value for which preferences are being set |
| DISPLAY_VALUE_COLOR | VARCHAR2 | 30 |  |  | Color for the display value |
| DISPLAY_VALUE_SHAPE | VARCHAR2 | 30 |  |  | Shape for the display value |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRR_TMPL_DISPLAY_PREFS_U1 | Unique | Default | DISPLAY_OPTN_PREF_ID, ENTERPRISE_ID |

---

[← Back to Index](../25_Talent_Review_Tables_Index.md)
