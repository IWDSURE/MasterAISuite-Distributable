# PAY_RATE_CONTRIBUTORS_F

This table contains the rate contributor information. A rate contributor is a value that contributes to a rate definition.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payratecontributorsf-30591.html#payratecontributorsf-30591](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payratecontributorsf-30591.html#payratecontributorsf-30591)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_RATE_CONTRIBUTORS_F_PK | RATE_CONTRIBUTOR_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RATE_CONTRIBUTOR_ID | NUMBER |  | 18 | Yes | Primary Key for the Rate Contributor |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| RATE_DEFINITION_ID | NUMBER |  | 18 | Yes | Foreign key to the Rate Definition |
| BALANCE_TYPE_ID | NUMBER |  | 18 |  | Foreign Key to the Ba;ance Type. This indicates the contributor to the Rate |
| CONTRIBUTOR_MODE | VARCHAR2 | 5 |  | Yes | The Mode in which the contribution takes place. Declared, Actual or Projected. |
| CONTRIBUTOR_TYPE | VARCHAR2 | 30 |  |  | What Type of contributor the Value is, is it another Rate Definition |
| CONTRIBUTOR_ID | NUMBER |  | 18 |  | Foreign Key to the Contributor |
| STATUS | VARCHAR2 | 30 |  |  | Status of the Rate Contributor |
| FEED | NUMBER |  | 8 | Yes | Is it a positive or negative contribution. |
| AS_OF_DATE | NUMBER |  | 18 |  | Foreign Key to Time Definitions. |
| AS_OF_DATE_BALANCE | NUMBER |  | 18 |  | Foreign Key to Time Definitions |
| BALANCE_DIMENSION_ID | NUMBER |  | 18 |  | Foreign Key to Balance Dimensions |
| PERIODICITY | VARCHAR2 | 30 |  |  | Periodicity to be used for the calculation |
| FACTOR_TYPE | VARCHAR2 | 30 |  |  | The Type of Factor that is to be used |
| FACTOR_VALUE | VARCHAR2 | 30 |  |  | The Value of the Factor to be used |
| FACTOR_INVERSE | VARCHAR2 | 5 |  |  | Inverse the factor for calculation. |
| FACTOR_IDENTIFIER | VARCHAR2 | 30 |  |  | For Factor Type VBC this attribute can be used to identify the leaf node value. |
| LIMIT_MODE | VARCHAR2 | 30 |  |  | Behavior when the Amount is outside the minimum limits. |
| MAX_LIMIT_MODE | VARCHAR2 | 30 |  |  | Behavior when the Amount is outside the maximum limits. |
| MIN_TYPE | VARCHAR2 | 30 |  |  | The Type of Minimum value to use |
| MIN_VALUE | VARCHAR2 | 30 |  |  | The Value of the Minimum value based on the Type. |
| MIN_VALUE_IDENTIFIER | VARCHAR2 | 30 |  |  | For MIN_TYPE of VBC this attribute Identifies the leaf node for the value. |
| MAX_TYPE | VARCHAR2 | 30 |  |  | The Type of Maximum Value to be used. |
| MAX_VALUE | VARCHAR2 | 30 |  |  | The Value of the Maximum value based on the Type. |
| MAX_VALUE_IDENTIFIER | VARCHAR2 | 30 |  |  | For Max_TYPE of VBC this attribute identifies the leaf node of the value to use. |
| FTE_FLAG | VARCHAR2 | 30 |  |  | This indicates whether the amount to add to the Rate should be FTE |
| USE_FORMULA | VARCHAR2 | 30 |  |  | This indicates whether the Rate formula on the Input Value is used to calculate the value. |
| DIVISIONAL_BAL_TYPE_ID | NUMBER |  | 18 |  | THe Balance Type to be used to perform a divide on the Rate. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign Key to the Enterprise table |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign Key to the Legislative Data Group |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | The Legislation Code for this data. |
| SEQUENCE_NUMBER | NUMBER |  | 18 |  | Sequence of the Rate Contributor |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_RATE_CONTRIBUTORS_F_N1 | Non Unique | Default | RATE_DEFINITION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_RATE_CONTRIBUTORS_F_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_RATE_CONTRIBUTORS_F_PK | Unique | Default | RATE_CONTRIBUTOR_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_RATE_CONTRIBUTORS_F_PK1 | Unique | Default | RATE_CONTRIBUTOR_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
