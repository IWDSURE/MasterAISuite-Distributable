# BEN_VALD_HRCHY_SMRY

BEN_VALD_HRCHY_SMRY holds the validation information for a particular path in the compensation object hierarchy with respect to a reporting rule.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvaldhrchysmry-22264.html#benvaldhrchysmry-22264](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvaldhrchysmry-22264.html#benvaldhrchysmry-22264)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_VALD_HRCHY_SMRY_PK | VALD_HRCHY_SMRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VALD_HRCHY_SMRY_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| POPL_VALD_HRCHY_ID | NUMBER |  | 18 |  | Foreign key to BEN_POPL_VALD_HRCHY. |
| VALD_RPT_TYP_ID | NUMBER |  | 18 |  | Foreign key to BEN_VALD_RPT_TYP. |
| PGM_VALD_CD | NUMBER |  | 18 |  | Program validation code. |
| PTIP_VALD_CD | NUMBER |  | 18 |  | Plan type in program validation code. |
| PL_TYP_VALD_CD | NUMBER |  | 18 |  | Plan type validation code. |
| PLIP_VALD_CD | NUMBER |  | 18 |  | Plan in program validation code. |
| PL_VALD_CD | NUMBER |  | 18 |  | Plan validation code. |
| PLNIP_VALD_CD | NUMBER |  | 18 |  | Plan not in program validation code. |
| OIPL_VALD_CD | NUMBER |  | 18 |  | Option in plan validation cd. |
| OPT_VALD_CD | NUMBER |  | 18 |  | Option validation code. |
| PGM_RQD_FLAG | VARCHAR2 | 30 |  |  | Program required flag. |
| PTIP_RQD_FLAG | VARCHAR2 | 30 |  |  | Plan type in program required flag. |
| PL_TYP_RQD_FLAG | VARCHAR2 | 30 |  |  | Plan type required flag. |
| PLIP_RQD_FLAG | VARCHAR2 | 30 |  |  | Plan in program required flag. |
| PL_RQD_FLAG | VARCHAR2 | 30 |  |  | Plan required flag. |
| PLNIP_RQD_FLAG | VARCHAR2 | 30 |  |  | Plan not in program required flag. |
| OIPL_RQD_FLAG | VARCHAR2 | 30 |  |  | Option in plan required flag. |
| OPT_RQD_FLAG | VARCHAR2 | 30 |  |  | Option required flag. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SMRY_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Summary attribute1 for storing any additional varchar information. |
| SMRY_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Summary attribute2 for storing any additional varchar information. |
| SMRY_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Summary attribute3 for storing any additional varchar information. |
| SMRY_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Summary attribute4 for storing any additional varchar information. |
| SMRY_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Summary attribute5 for storing any additional varchar information. |
| SMRY_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Summary attribute number 1 for storing any additional number information. |
| SMRY_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Summary attribute number 2 for storing any additional number information. |
| SMRY_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Summary attribute number 3 for storing any additional number information. |
| SMRY_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Summary attribute number 4 for storing any additional number information. |
| SMRY_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Summary attribute number 5 for storing any additional number information. |
| SMRY_ATTRIBUTE_DATE1 | DATE |  |  |  | Summary attribute date 1 for storing any additional date information. |
| SMRY_ATTRIBUTE_DATE2 | DATE |  |  |  | Summary attribute date 2 for storing any additional date information. |
| SMRY_ATTRIBUTE_DATE3 | DATE |  |  |  | Summary attribute date 3 for storing any additional date information. |
| SMRY_ATTRIBUTE_DATE4 | DATE |  |  |  | Summary attribute date 4 for storing any additional date information. |
| SMRY_ATTRIBUTE_DATE5 | DATE |  |  |  | Summary attribute date 5 for storing any additional date information. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_VALD_HRCHY_SMRY_N1 | Non Unique | Default | POPL_VALD_HRCHY_ID, VALD_HRCHY_SMRY_ID, VALD_RPT_TYP_ID, BUSINESS_GROUP_ID |
| BEN_VALD_HRCHY_SMRY_PK | Unique | Default | VALD_HRCHY_SMRY_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
