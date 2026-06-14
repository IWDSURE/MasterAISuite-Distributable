# HWR_CSTM_SKILLS_B

This will store information regarding the custom skills associated with the users that have been identified.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcstmskillsb-28772.html#hwrcstmskillsb-28772](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcstmskillsb-28772.html#hwrcstmskillsb-28772)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CSTM_SKILLS_B_PK | SKILL_NAME, USER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SKILL_NAME | VARCHAR2 | 500 |  | Yes | This is the name of the skill that has been identified for a particular user. |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | This is the description of the skill that has been identified for a particular user. |
| USER_ID | VARCHAR2 | 500 |  | Yes | This represents the Fusion id of the user for which this skill was found. |
| IS_SEEDED | VARCHAR2 | 20 |  | Yes | This indicates whether the skill was seeded or not seeded. |
| NUM_OF_OCCURRENCES | NUMBER |  | 18 |  | This represents the number of times a particular skill has been found for a particular user. |
| IS_REJECTED | NUMBER |  | 18 | Yes | This indicates whether the skill was rejected or not. 0 --> Undecided, 1--> True/Rejected the skill, 2 --> False/Accepted the skill |
| CUSTOM_SKILL_ATTR_1 | VARCHAR2 | 100 |  |  | CUSTOM_SKILL_ATTR_1. This is the extra attribute in case if needed. |
| CUSTOM_SKILL_ATTR_2 | VARCHAR2 | 100 |  |  | CUSTOM_SKILL_ATTR_2. This is the extra attribute in case if needed. |
| CUSTOM_SKILL_ATTR_3 | VARCHAR2 | 100 |  |  | CUSTOM_SKILL_ATTR_3. This is the extra attribute in case if needed. |
| CUSTOM_SKILL_ATTR_4 | VARCHAR2 | 100 |  |  | CUSTOM_SKILL_ATTR_4. This is the extra attribute in case if needed. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_CSTM_SKILLS_B_N1 | Non Unique | Default | IS_SEEDED |
| HWR_CSTM_SKILLS_B_U1 | Unique | Default | SKILL_NAME, USER_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
