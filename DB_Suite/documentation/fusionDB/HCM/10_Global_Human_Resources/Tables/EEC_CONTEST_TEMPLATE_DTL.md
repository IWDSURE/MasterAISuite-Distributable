# EEC_CONTEST_TEMPLATE_DTL

This table stores the Compete As and Winner determined by options allowed for the contest template.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eeccontesttemplatedtl-23646.html#eeccontesttemplatedtl-23646](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eeccontesttemplatedtl-23646.html#eeccontesttemplatedtl-23646)

## Primary Key

| Name | Columns |
|------|----------|
| EEC_CONTEST_TEMPLATE_DTL_PK | TEMPLATE_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| TEMPLATE_LINE_ID | NUMBER |  | 18 | Yes | System generated key for this entry |  |
| TEMPLATE_ID | NUMBER |  | 18 | Yes | Foreign key to EEC_CONTEST_TEMPLATE_HDR |  |
| LINE_TYPE | VARCHAR2 | 20 |  |  | Information about whether the details belong to COMPETE_AS or WINNERDETBY |  |
| LOOKUP_TYPE | VARCHAR2 | 30 |  |  | Lookup type of the line. Takes these lookup type values EEC_PARTICIPANT_TYPE or EEC_CONTEST_TYPE |  |
| LOOKUP_CODE | VARCHAR2 | 30 |  |  | Lookup code allowed for the line |  |
| ACTIVE_FLAG | VARCHAR2 | 1 |  |  | Flag to determine whether the lookup is active or not |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| EEC_CONTEST_TEMPLATE_DTL_U1 | Unique | Default | TEMPLATE_LINE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
