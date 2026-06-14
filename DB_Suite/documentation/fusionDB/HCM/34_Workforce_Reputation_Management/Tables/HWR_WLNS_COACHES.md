# HWR_WLNS_COACHES

This table stores wellness coach details.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnscoaches-13532.html#hwrwlnscoaches-13532](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnscoaches-13532.html#hwrwlnscoaches-13532)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_COACHES_PK | COACH_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COACH_ID | NUMBER |  | 18 | Yes | This is a primary key for the hwr_wlns_coaches tables. |
| PERSON_ID | NUMBER |  | 18 | Yes | The person_id from fusion profile table. |
| IS_ACTIVE | VARCHAR2 | 5 |  | Yes | A flag indicating Y for true (active) or N for false (not active). |
| COACHES_ATTR_1 | VARCHAR2 | 400 |  |  | This stores the coach attribute 1. |
| COACHES_ATTR_2 | NUMBER |  | 18 |  | This stores the coach attribute 2. |
| COACHES_ATTR_3 | VARCHAR2 | 400 |  |  | This stores the coach attribute 3. |
| COACHES_ATTR_4 | NUMBER |  | 18 |  | This stores the coach attribute 4. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_COACHES_U1 | Unique | Default | COACH_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
