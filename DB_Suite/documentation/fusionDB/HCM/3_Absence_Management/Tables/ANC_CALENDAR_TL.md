# ANC_CALENDAR_TL

Translation Table for Organization Calendars.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/anccalendartl-27672.html#anccalendartl-27672](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/anccalendartl-27672.html#anccalendartl-27672)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_CALENDAR_TL_PK | CALENDAR_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CALENDAR_ID | NUMBER |  | 18 | Yes | Calendar ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise ID |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 240 |  | Yes | Event Name |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | Event Description |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_CALENDAR_TL_PK | Unique | Default | CALENDAR_ID, LANGUAGE |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
