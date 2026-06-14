# BEN_ELIG_GEN_CRIT_PRTE

BEN_ELIG_GEN_CRIT_PRTE  identifies which generic criteira are included in (most typical usage) or excluded from (least typical) an eligibility  profile. These generic criteria-related requirements must be satisfied in order for the person to be eligible to participate in the compensation  object.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneliggencritprte-30532.html#beneliggencritprte-30532](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneliggencritprte-30532.html#beneliggencritprte-30532)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_GEN_CRIT_PRTE_PK | ELIG_GEN_CRIT_PRTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_GEN_CRIT_PRTE_ID | NUMBER |  | 18 | Yes | Primary Key |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Identifies ELigibility Profile. Foreign key to BEN_ELIGY_PRFL |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| ELIG_CRITERIA_CODE | VARCHAR2 | 30 |  | Yes | Identifies eligibility criteria validated by lookup_type BEN_INELG_RSN |
| START_DATE | DATE |  |  |  | Start Date |
| END_DATE | DATE |  |  |  | End Date |
| ORDR_NUM | NUMBER |  | 18 |  | Sequence Number |
| EXCLD_FLAG | VARCHAR2 | 30 |  | Yes | Exclude flag |
| OPERATOR | VARCHAR2 | 255 |  |  | Identifies the operatior to be used for the criteria |
| CRIT_CHAR1 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR2 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR3 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR4 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR5 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR6 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR7 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR8 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR9 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR10 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR11 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR12 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR13 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR14 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR15 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR16 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR17 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR18 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR19 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR20 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR21 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR22 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR23 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR24 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR25 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR26 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR27 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR28 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR29 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_CHAR30 | VARCHAR2 | 255 |  |  | Generic column to be used for CHAR type crieria. |
| CRIT_NUMBER1 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER2 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER3 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER4 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER5 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER6 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER7 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER8 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER9 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER10 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER11 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER12 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER13 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER14 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER15 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER16 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER17 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER18 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER19 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER20 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER21 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER22 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER23 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER24 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER25 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER26 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER27 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER28 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER29 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_NUMBER30 | NUMBER |  |  |  | Generic column to be used for number type crieria. |
| CRIT_DATE1 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE2 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE3 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE4 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE5 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE6 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE7 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE8 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE9 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE10 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE11 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE12 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE13 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE14 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE15 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE16 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE17 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE18 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE19 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE20 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE21 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE22 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE23 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE24 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE25 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE26 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE27 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE28 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE29 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRIT_DATE30 | DATE |  |  |  | Generic column to be used for date type crieria. |
| CRITERIA_SCORE | NUMBER |  |  |  | Criteria Score |
| CRITERIA_WEIGHT | NUMBER |  |  |  | Criteria Weight |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_GEN_CRIT_PRTE_N1 | Non Unique | Default | ELIGY_PRFL_ID |
| BEN_ELIG_GEN_CRIT_PRTE_PK | Unique | Default | ELIG_GEN_CRIT_PRTE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
