# BEN_PSTL_ZIP_RNG

Range of postal codes. You create postal zip ranges by providing start and end zip codes.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpstlziprng-7204.html#benpstlziprng-7204](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpstlziprng-7204.html#benpstlziprng-7204)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PSTL_ZIP_RNG_PK | PSTL_ZIP_RNG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PSTL_ZIP_RNG_ID | NUMBER |  | 18 | Yes | PSTL_ZIP_RNG_ID |
| START_DATE | DATE |  |  | Yes | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| FROM_VALUE | VARCHAR2 | 90 |  | Yes | FROM_VALUE |
| TO_VALUE | VARCHAR2 | 90 |  |  | TO_VALUE |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PSTL_ZIP_RNG_N1 | Non Unique | Default | UPPER("FROM_VALUE") |
| BEN_PSTL_ZIP_RNG_PK | Unique | Default | PSTL_ZIP_RNG_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
