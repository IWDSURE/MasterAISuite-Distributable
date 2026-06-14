# IRC_SERVICE_SCAN_STATUS

This table will have a single row per scan name and scan type that keeps a status for the scans.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircservicescanstatus-8853.html#ircservicescanstatus-8853](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircservicescanstatus-8853.html#ircservicescanstatus-8853)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_SERVICE_SCAN_STATUS_PK | SCAN_TYPE, SCAN_NAME |

## Columns

| Name | Datatype | Length | Not-null | Comments |
|---|---|---|---|---|
| SCAN_TYPE | VARCHAR2 | 30 | Yes | The type of scan. |
| SCAN_NAME | VARCHAR2 | 100 | Yes | The name of the scan. |
| SCAN_STATUS | VARCHAR2 | 20 | Yes | The status of the scan. |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_SERVICE_SCAN_STATUS_PK | Unique | Default | SCAN_TYPE, SCAN_NAME |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
