# HWR_QRTZ_JOB_DETAILS

This is the GRC table for QRTZ_JOB_DETAILS.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtzjobdetails-17381.html#hwrqrtzjobdetails-17381](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtzjobdetails-17381.html#hwrqrtzjobdetails-17381)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_QRTZ_JOB_DETAILS_PK | JOB_NAME, JOB_GROUP |

## Columns

| Name | Datatype | Length | Not-null | Comments | Status |
|---|---|---|---|---|---|
| JOB_NAME | VARCHAR2 | 256 | Yes | This is the column JOB_NAME on table HWR_QRTZ_JOB_DETAILS. | Active |
| JOB_GROUP | VARCHAR2 | 80 | Yes | This is the column JOB_GROUP on table HWR_QRTZ_JOB_DETAILS. | Active |
| DESCRIPTION | VARCHAR2 | 120 |  | This is the column DESCRIPTION on table HWR_QRTZ_JOB_DETAILS. | Active |
| JOB_CLASS_NAME | VARCHAR2 | 128 | Yes | This is the column JOB_CLASS_NAME on table HWR_QRTZ_JOB_DETAILS. | Active |
| IS_DURABLE | VARCHAR2 | 1 | Yes | This is the column IS_DURABLE on table HWR_QRTZ_JOB_DETAILS. | Active |
| IS_VOLATILE | VARCHAR2 | 1 | Yes | This is the column IS_VOLATILE on table HWR_QRTZ_JOB_DETAILS. | Active |
| IS_STATEFUL | VARCHAR2 | 1 | Yes | This is the column IS_STATEFUL on table HWR_QRTZ_JOB_DETAILS. | Active |
| REQUESTS_RECOVERY | VARCHAR2 | 1 | Yes | This is the column REQUESTS_RECOVERY on table HWR_QRTZ_JOB_DETAILS. | Active |
| JOB_DATA | BLOB |  |  | This is the column JOB_DATA on table HWR_QRTZ_JOB_DETAILS. | Active |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_QRTZ_JOB_DETAILS_N1 | Non Unique | FUSION_TS_TX_DATA | REQUESTS_RECOVERY | Active |
| HWR_QRTZ_JOB_DETAILS_U1 | Unique | FUSION_TS_TX_DATA | JOB_NAME, JOB_GROUP | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
