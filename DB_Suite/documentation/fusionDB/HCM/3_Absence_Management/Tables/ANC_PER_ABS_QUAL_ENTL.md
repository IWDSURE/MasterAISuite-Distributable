# ANC_PER_ABS_QUAL_ENTL

This table holds information of  the qualified entitlements person is entitled to when recording an absence

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsqualentl-16710.html#ancperabsqualentl-16710](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsqualentl-16710.html#ancperabsqualentl-16710)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_ABS_QUAL_ENTITLEM_PK | PER_ABS_QUAL_ENTL_ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ABS_QUAL_ENTL_ENTRY_ID | NUMBER |  | 18 | Yes | PER_ABS_QUAL_ENTL_ENTRY_ID |
| PER_ABSENCE_ENTRY_ID | NUMBER |  | 18 | Yes | PER_ABSENCE_ENTRY_ID of the qualification entitlement row |
| PER_ABS_TYPE_ENTRY_ID | NUMBER |  | 18 | Yes | Per_abs_type_entry_id of the qualification entitlement row |
| PERSON_ID | NUMBER |  | 18 | Yes | Person id of the qualification entitlement row |
| PLAN_ID | NUMBER |  | 18 | Yes | Qualification plan id of the qualification entitlement row |
| ENTL_BAND_DTL_SEQUENCE | NUMBER |  |  |  | Pay factor priority sequence of the qualification entitlement row |
| PAY_RATE_FACTOR | NUMBER |  |  |  | Pay factor of the qualification entitlement row |
| QUALIFIED_ENTITLEMENTS | NUMBER |  |  |  | Qualified entitlement of the qualification entitlement row |
| PLAN_PERIOD_START_DATE | TIMESTAMP |  |  |  | Plan period start date of the qualification entitlement row |
| PLAN_PERIOD_END_DATE | TIMESTAMP |  |  |  | Plan period end date of the qualification entitlement row |
| PLAN_PERIOD_USED_ENTL | NUMBER |  |  |  | Used entitlements of the qualification entitlement row |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CASE_ID | NUMBER |  | 18 |  | CASE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_ABS_QUAL_ENTL_N1 | Non Unique | FUSION_TS_TX_DATA | PER_ABSENCE_ENTRY_ID |
| ANC_PER_ABS_QUAL_ENTL_N2 | Non Unique | FUSION_TS_TX_DATA | PER_ABS_TYPE_ENTRY_ID |
| ANC_PER_ABS_QUAL_ENTL_N3 | Non Unique | FUSION_TS_TX_DATA | PLAN_ID |
| ANC_PER_ABS_QUAL_ENTL_N4 | Non Unique | FUSION_TS_TX_DATA | CASE_ID |
| ANC_PER_ABS_QUAL_ENTL_U1 | Unique | FUSION_TS_TX_DATA | PER_ABS_QUAL_ENTL_ENTRY_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
