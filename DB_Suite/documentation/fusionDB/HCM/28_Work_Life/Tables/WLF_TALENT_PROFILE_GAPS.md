# WLF_TALENT_PROFILE_GAPS

This table stores person talent profile content item gaps

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlftalentprofilegaps-25822.html#wlftalentprofilegaps-25822](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlftalentprofilegaps-25822.html#wlftalentprofilegaps-25822)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_TALENT_PROFILE_GAPS_PK | TALENT_PROFILE_GAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TALENT_PROFILE_GAP_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| ESS_JOB_ID | NUMBER |  | 18 |  | Identifier for the ESS Job evaluating the talent profile gaps |
| TALENT_PROF_GAP_SUMMARY_ID | NUMBER |  | 18 | Yes | References TALENT_PROF_GAP_ID from WLF_TALENT_PROF_GAP_SUMMARY table |
| PERSON_ID | NUMBER |  | 18 | Yes | Specifies identifier of the person |
| WORK_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Person work assignment id |
| IS_CURATED_SKILL_GAP | VARCHAR2 | 1 |  |  | Specifies if the gap is corresponding to a curated skill or not |
| IS_REQUIRED | VARCHAR2 | 1 |  |  | Specifies if the gap is corresponding to a required skill or qualification in the role profile |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_TALENT_PROFILE_GAPS_N1 | Non Unique | Default | WORK_ASSIGNMENT_ID, PERSON_ID |
| WLF_TALENT_PROFILE_GAPS_N2 | Non Unique | Default | TALENT_PROF_GAP_SUMMARY_ID |
| WLF_TALENT_PROFILE_GAPS_N3 | Non Unique | Default | ESS_JOB_ID |
| WLF_TALENT_PROFILE_GAPS_U1 | Unique | Default | TALENT_PROFILE_GAP_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
