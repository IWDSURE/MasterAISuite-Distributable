# HRT_PROFILE_KEYWORDS

This table is used to capture keywords for Areas of Expertise and Areas of Interests of an employee

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilekeywords-16104.html#hrtprofilekeywords-16104](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilekeywords-16104.html#hrtprofilekeywords-16104)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_KEYWORDS_PK | PROFILE_KEYWORD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_KEYWORD_ID | NUMBER |  | 18 | Yes | Profile Keyword Id |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROFILE_ID | NUMBER |  | 18 | Yes | Profile Id |
| KEYWORD_TYPE | VARCHAR2 | 30 |  | Yes | Keyword type can be Area of Interest, Area of Expertise |
| KEYWORDS | VARCHAR2 | 4000 |  | Yes | Keyword value |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_KEYWORDS_N1 | Non Unique | Default | PROFILE_ID |
| HRT_PROFILE_KEYWORDS_PK | Unique | Default | PROFILE_KEYWORD_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
