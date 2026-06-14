# HWR_SRVY_MEETING_PREF

This table is to be used by meeting survey to determine whether a particular user has opted in or opted out.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvymeetingpref-29759.html#hwrsrvymeetingpref-29759](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvymeetingpref-29759.html#hwrsrvymeetingpref-29759)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SRVY_MEETING_OPT_PK | PRFL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PRFL_ID | VARCHAR2 | 500 |  | Yes | This is the Fusion profile id of the person being identified in this record |
| OPT_IN | NUMBER |  | 4 | Yes | OPT_IN flag. This determines if this person has opted in for Meeting survey or not. 0 --> NOT opted In. ; 1 --> Opted In |
| MEETING_PREF_ATTR_1 | VARCHAR2 | 100 |  |  | MEETING_PREF_ATTR_1. This is the extra attribute in case if needed. |
| MEETING_PREF_ATTR_2 | VARCHAR2 | 100 |  |  | MEETING_PREF_ATTR_2. This is the extra attribute in case if needed. |
| MEETING_PREF_ATTR_3 | VARCHAR2 | 100 |  |  | MEETING_PREF_ATTR_3. This is the extra attribute in case if needed. |
| MEETING_PREF_ATTR_4 | VARCHAR2 | 100 |  |  | MEETING_PREF_ATTR_4. This is the extra attribute in case if needed. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SRVY_MEETING_OPT_U1 | Unique | Default | PRFL_ID |
| HWR_SRVY_MEETING_PREF_N1 | Non Unique | Default | OPT_IN |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
