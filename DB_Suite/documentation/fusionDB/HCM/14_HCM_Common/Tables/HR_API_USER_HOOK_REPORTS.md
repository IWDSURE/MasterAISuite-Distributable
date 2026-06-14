# HR_API_USER_HOOK_REPORTS

When the API user hook pre-processor program is being executed this table will contain data. It is used as a temporary store of error conditions. Rows will be output to the user at the end of the pre-processor program.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrapiuserhookreports-18467.html#hrapiuserhookreports-18467](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrapiuserhookreports-18467.html#hrapiuserhookreports-18467)

## Primary Key

| Name | Columns |
|------|----------|
| HR_API_USER_HOOK_REPORTS_PK | SESSION_ID, LINE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SESSION_ID | NUMBER |  | 18 | Yes | Session_id for the hook report. |
| LINE | NUMBER |  | 18 | Yes | Primary Key, order sequence number. |
| TEXT | VARCHAR2 | 2000 |  |  | Text for user. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HR_API_USER_HOOK_REPORTS_PK | Unique | Default | SESSION_ID, LINE |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
