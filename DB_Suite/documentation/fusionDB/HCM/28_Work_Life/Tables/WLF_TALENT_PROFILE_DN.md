# WLF_TALENT_PROFILE_DN

This table stores the talent profile competencies along with proficiency rating information

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlftalentprofiledn-30742.html#wlftalentprofiledn-30742](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlftalentprofiledn-30742.html#wlftalentprofiledn-30742)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_TALENT_PROFILE_DN_PK | TALENT_PROFILE_DN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TALENT_PROFILE_DN_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| PROFILE_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Specifies talent profile type |
| PROFILE_ID | NUMBER |  | 18 | Yes | Specifies identifier of talent profile |
| PROFILE_NAME | VARCHAR2 | 250 |  |  | Specifies name of the profile |
| CONTENT_TYPE_ID | NUMBER |  | 18 | Yes | Foreign Key to HRT_CONTENT_TYPES_B |
| CONTENT_ITEM_ID | NUMBER |  | 18 |  | Foreign Key to HRT_CONTENT_ITEMS_B |
| CONTENT_ITEM_TEXT | VARCHAR2 | 250 |  |  | Specifies content item text value of type free-form text |
| RATING1 | NUMBER |  | 5 |  | Specifies profile item numeric rating |
| RATING2 | NUMBER |  | 5 |  | Specifies profile item numeric rating |
| RATING3 | NUMBER |  | 5 |  | Specifies profile item numeric rating |
| IMPORTANCE | NUMBER |  | 18 |  | Relative importance of profile item |
| METRIC_DATE | DATE |  |  | Yes | Specifies the effective date of the calculated metrics |
| IS_SKILL_CENTER_ITEM | VARCHAR2 | 1 |  |  | Specifies if the skill is assigned from the skill center |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_TALENT_PROFILE_DN_N1 | Non Unique | WLF_TALENT_PROFILE_DN_N1 | PROFILE_TYPE_CODE, PROFILE_ID |
| WLF_TALENT_PROFILE_DN_N2 | Non Unique | WLF_TALENT_PROFILE_DN_N3 | CONTENT_TYPE_ID, CONTENT_ITEM_ID |
| WLF_TALENT_PROFILE_DN_N3 | Non Unique | WLF_TALENT_PROFILE_DN_N4 | METRIC_DATE |
| WLF_TALENT_PROFILE_DN_U1 | Unique | WLF_TALENT_PROFILE_DN_U1 | TALENT_PROFILE_DN_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
