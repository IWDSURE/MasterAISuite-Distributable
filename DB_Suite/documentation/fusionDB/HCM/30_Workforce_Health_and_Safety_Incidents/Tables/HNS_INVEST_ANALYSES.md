# HNS_INVEST_ANALYSES

HNS INVEST ANALYSES. This table stores analysis related to an investigation.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsinvestanalyses-28312.html#hnsinvestanalyses-28312](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsinvestanalyses-28312.html#hnsinvestanalyses-28312)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_INVEST_ANALYSES_PK | INVEST_ANALYSIS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INVEST_ANALYSIS_ID | NUMBER |  | 18 | Yes | Unique Investigation analysis identifer. |
| INVESTIGATE_ID | NUMBER |  | 18 | Yes | Investigation identifier. Foreign key for HNS_INVESTIGATIONS_SUMMARY table. |
| SUBJECT_AREA_CODE | VARCHAR2 | 30 |  |  | Analysis identifier. (Analysis subject area). |
| SUBJECT_CODE | VARCHAR2 | 30 |  |  | Selected value for the analysis (Analysis subject). |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted flag.This column signifies whether the investment analysis  is checked for deletion. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_INVEST_ANALYSES_N1 | Non Unique | FUSION_TS_TX_DATA | INVESTIGATE_ID |
| HNS_INVEST_ANALYSES_UK1 | Unique | FUSION_TS_TX_DATA | INVEST_ANALYSIS_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
