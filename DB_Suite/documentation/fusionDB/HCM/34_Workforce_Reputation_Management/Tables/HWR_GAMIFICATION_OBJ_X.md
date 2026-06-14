# HWR_GAMIFICATION_OBJ_X

This cross reference (xref) table stores relationship between Gamification objects.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrgamificationobjx-10629.html#hwrgamificationobjx-10629](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrgamificationobjx-10629.html#hwrgamificationobjx-10629)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_GAMIFICATION_OBJ_X_PK | OBJECT_NAME, OBJECT_TYPE |

## Columns

| Name | Datatype | Length | Not-null | Comments |
|---|---|---|---|---|
| OBJECT_NAME | VARCHAR2 | 400 | Yes | This is the object name of the gamification object reference tables. |
| OBJECT_TYPE | VARCHAR2 | 400 | Yes | This is the object type of the gamification object reference tables. |
| OBJECT_XREF | VARCHAR2 | 400 | Yes | This is the object reference of the gamification object reference tables. |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_GAMIFICATION_OBJ_X_U1 | Unique | FUSION_TS_TX_DATA | OBJECT_NAME, OBJECT_TYPE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
