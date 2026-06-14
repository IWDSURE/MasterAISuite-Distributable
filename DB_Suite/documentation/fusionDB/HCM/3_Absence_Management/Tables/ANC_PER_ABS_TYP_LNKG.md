# ANC_PER_ABS_TYP_LNKG

This table holds information of  the person absence linkages.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabstyplnkg-14585.html#ancperabstyplnkg-14585](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabstyplnkg-14585.html#ancperabstyplnkg-14585)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_ABS_TYP_LNKG_PK | PER_ABS_TYP_LINKAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ABS_TYP_LINKAGE_ID | NUMBER |  | 18 | Yes | PER_ABS_TYP_LINKAGE_ID |
| PER_ABSENCE_ENTRY_ID | NUMBER |  | 18 | Yes | References person absence entry identifier |
| LINK_CHAIN_ID | NUMBER |  | 18 |  | Chain id for linked absences |
| LNKD_PER_ABS_ENTRY_ID | NUMBER |  | 18 | Yes | Linked person absence entry identfier |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| LNKG_REASON | VARCHAR2 | 30 |  |  | Reason |
| LNKG_REASON_ID | NUMBER |  | 18 |  | LNKG_REASON_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ABS_AGGREGATION_ID | NUMBER |  | 18 |  | To map the aggregation id |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_ABS_TYP_LNKG_U1 | Unique | FUSION_TS_TX_DATA | PER_ABS_TYP_LINKAGE_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
