# BEN_WV_PRTN_RSN_CTFN_PL_F

BEN_WV_PRTN_RSN_CTFN_PL_F  identifies the certification that may be required when a person waives coverage in a plan for a specified reason as opposed to actively electing a "Waive" plan.  For example, if an  eligible person waives participation in a plan for the reason of "have other coverage", he or she may be required to provide proof of coverage in an external plan.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benwvprtnrsnctfnplf-11713.html#benwvprtnrsnctfnplf-11713](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benwvprtnrsnctfnplf-11713.html#benwvprtnrsnctfnplf-11713)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_WV_PRTN_RSN_CTFN_PL_F_PK | WV_PRTN_RSN_CTFN_PL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WV_PRTN_RSN_CTFN_PL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PFD_FLAG | VARCHAR2 | 30 |  | Yes | Preferred Y or N. |
| LACK_CTFN_SSPND_WVR_FLAG | VARCHAR2 | 30 |  | Yes | Lack of certification suspend waiver Y or N. |
| RQD_FLAG | VARCHAR2 | 30 |  | Yes | Required Y or N. |
| CTFN_RQD_WHEN_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| WV_PRTN_CTFN_TYP_CD | VARCHAR2 | 30 |  | Yes | Waive participation certification type. |
| WV_PRTN_RSN_PL_ID | NUMBER |  | 18 |  | Foreign key to BEN_WV_PRTN_RSN_PL_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Columns |
|---|---|---|
| BEN_WV_PRSN_CTN_PL_F_N1 | Non Unique | WV_PRTN_RSN_PL_ID |
| BEN_WV_PRSN_CTN_PL_F_PK | Unique | WV_PRTN_RSN_CTFN_PL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
