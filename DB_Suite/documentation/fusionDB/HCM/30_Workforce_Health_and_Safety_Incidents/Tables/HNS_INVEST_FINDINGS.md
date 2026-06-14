# HNS_INVEST_FINDINGS

HNS INVEST FINDINGS. This table stores all finding related data for an investigation.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsinvestfindings-6777.html#hnsinvestfindings-6777](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsinvestfindings-6777.html#hnsinvestfindings-6777)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_INVEST_FINDINGS_PK | FINDING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INVESTIGATE_ID | NUMBER |  | 18 | Yes | Investigation ID. Foreign key for HNS_INVESTIGATIONS_SUMMARY |
| FINDING_SUMMARY | VARCHAR2 | 1000 |  | Yes | User entered Summary date for the finding. |
| SEVERITY_LEVEL_CODE | VARCHAR2 | 30 |  |  | Level of severity for the finding. |
| FINDING_ID | NUMBER |  | 18 | Yes | Unique Identifier for HNS_INVEST_FINDINGS table. |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted flag.This column signifies whether the Investigation finding  is checked for deletion. |
| FINDING_ISSUE_FLAG | VARCHAR2 | 1 |  |  | Issue flag. Signifies whether there was a issue for the finding. |
| FINDING_NOTES | VARCHAR2 | 4000 |  |  | User entered finding notes. |
| FINDING_RESPONSE | VARCHAR2 | 4000 |  |  | User entered finding response. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_INVEST_FINDINGS_N1 | Non Unique | FUSION_TS_TX_DATA | INVESTIGATE_ID |
| HNS_INVEST_FINDINGS_UK1 | Unique | FUSION_TS_TX_DATA | FINDING_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
