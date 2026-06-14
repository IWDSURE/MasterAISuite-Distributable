# IRC_CAND_SEC_PROFILE_VALUES

This table will store actual values for any candidate search profiles that have been created from the FSM UI.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandsecprofilevalues-19451.html#irccandsecprofilevalues-19451](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandsecprofilevalues-19451.html#irccandsecprofilevalues-19451)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_SEC_PROF_VALUES_PK | CAND_SEC_PROFILE_VALUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAND_SEC_PROFILE_VALUE_ID | NUMBER |  | 18 | Yes | Primary key for this table |
| CAND_SEC_PROFILE_ID | NUMBER |  | 18 | Yes | Foreign Key to IRC_CAND_SEC_PROFILES |
| SECURE_BY_RECRUITING_TYPE_VAL | VARCHAR2 | 240 |  |  | Stores a single value for recruitng type for a candidate search security profile configured in FSM |
| SECURE_BY_PERSON_TYPE_VAL | VARCHAR2 | 240 |  |  | Stores a single value for person type for a candidate search security profile configured in FSM |
| SECURE_BY_CAND_COUNTRY_VAL | VARCHAR2 | 240 |  |  | Stores a single value for candidate country for a candidate search security profile configured in FSM |
| SECURE_BY_GRADE_LEVEL_VAL | VARCHAR2 | 240 |  |  | Stores a single value for grade level for a candidate search security profile configured in FSM |
| SECURE_BY_BUSINESS_UNIT_VAL | VARCHAR2 | 240 |  |  | Stores a single value for business unit for a candidate search security profile configured in FSM |
| SECURE_BY_JOB_FAMILY_VAL | VARCHAR2 | 240 |  |  | Stores a single value for job family for a candidate search security profile configured in FSM |
| SECURE_BY_JOB_FUNC_VAL | VARCHAR2 | 240 |  |  | Stores a single value for job function for a candidate search security profile configured in FSM |
| SECURE_BY_LEGAL_EMPLOYER_VAL | VARCHAR2 | 240 |  |  | Stores a single value for legal employer for a candidate search security profile configured in FSM |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_SEC_PROF_VALUES_FK1 | Non Unique | Default | CAND_SEC_PROFILE_ID |
| IRC_CAND_SEC_PROF_VALUES_PK | Unique | Default | CAND_SEC_PROFILE_VALUE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
