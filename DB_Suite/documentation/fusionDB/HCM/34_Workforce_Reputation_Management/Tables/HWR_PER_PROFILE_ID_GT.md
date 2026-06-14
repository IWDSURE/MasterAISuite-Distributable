# HWR_PER_PROFILE_ID_GT

The profile id global temporary table stores profile ids for a session.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperprofileidgt-19311.html#hwrperprofileidgt-19311](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperprofileidgt-19311.html#hwrperprofileidgt-19311)

## Columns

| Name | Datatype | Length | Not-null | Comments |
|---|---|---|---|---|
| PRFL_ID | VARCHAR2 | 500 |  | This is the temporary profile ID value. |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
