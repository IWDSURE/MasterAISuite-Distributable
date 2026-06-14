# WLF_TALENT_PROF_GAP_SUMMARY

This table stores person talent profile content item gaps summary

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlftalentprofgapsummary-4059.html#wlftalentprofgapsummary-4059](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlftalentprofgapsummary-4059.html#wlftalentprofgapsummary-4059)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_TALENT_PROF_GAP_SUMMARY_PK | TALENT_PROF_GAP_SUMMARY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TALENT_PROF_GAP_SUMMARY_ID | NUMBER | 18 |  | Yes | System generated unique identifier |
| OBJECT_PROFILE_ID | NUMBER |  | 18 | Yes | Specifies identifier of talent profile |
| PROFILE_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Specifies talent profile type |
| CONTENT_TYPE_ID | NUMBER |  | 18 | Yes | Foreign Key to HRT_CONTENT_TYPES_B |
| CONTENT_ITEM_ID | NUMBER |  | 18 |  | Foreign Key to HRT_CONTENT_ITEMS_B |
| CONTENT_ITEM_TEXT | VARCHAR2 | 250 |  |  | Specifies content item text value of type free-form text |
| TALENT_PROFILE_SECTION_ID | NUMBER |  | 18 |  | Specifies section id of talent profile content item |
| ROLE_PROFILE_SECTION_ID | NUMBER |  | 18 |  | Specifies section id of role profile content item |
| ROLE_PROF_MIN_REQ_RATING1 | NUMBER |  | 5 |  | Specifies role profile item numeric rating1 |
| ROLE_PROF_MIN_REQ_RATING2 | NUMBER |  | 5 |  | Specifies role profile item numeric rating2 |
| ROLE_PROF_MIN_REQ_RATING3 | NUMBER |  | 5 |  | Specifies role profile item numeric rating3 |
| ROLE_PROF_NORMALIZED_RATING1 | NUMBER |  |  |  | Specifies normalized value for role profile item numeric rating1 |
| ROLE_PROF_NORMALIZED_RATING2 | NUMBER |  |  |  | Specifies normalized value for role profile item numeric rating2 |
| ROLE_PROF_NORMALIZED_RATING3 | NUMBER |  |  |  | Specifies normalized value for role profile item numeric rating3 |
| IMPORTANCE | NUMBER |  | 18 |  | Relative importance of profile item |
| ESS_JOB_ID | NUMBER |  | 18 |  | Identifier for the ESS Job evaluating the talent profile gaps |
| GAP_TYPE | VARCHAR2 | 30 |  |  | Specifies whether the gap corresponds to current role or career of interest. |
| INCL_UNC_RES_SKILLS | VARCHAR2 | 1 |  |  | Specifies whether to include uncurated resource skills while calculating gap filling objects |
| INCL_RES_WITH_OUTCOME_ONLY | VARCHAR2 | 1 |  |  | Specifies whether to consider only resources with outcome while calculating gap filling objects |
| ORIG_CONTENT_ITEM_ID | NUMBER |  | 18 |  | Foreign Key to HRT_CONTENT_ITEMS_B |
| ORIG_CONTENT_ITEM_TEXT | VARCHAR2 | 250 |  |  | Specifies content item text value of type free-form text |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_TALENT_PROF_GAP_SUMMARY_N1 | Non Unique | Default | OBJECT_PROFILE_ID |
| WLF_TALENT_PROF_GAP_SUMMARY_N2 | Non Unique | Default | CONTENT_TYPE_ID, TALENT_PROFILE_SECTION_ID, ROLE_PROFILE_SECTION_ID, CONTENT_ITEM_ID |
| WLF_TALENT_PROF_GAP_SUMMARY_N3 | Non Unique | Default | CONTENT_ITEM_TEXT |
| WLF_TALENT_PROF_GAP_SUMMARY_N4 | Non Unique | Default | ROLE_PROF_MIN_REQ_RATING1, ROLE_PROF_MIN_REQ_RATING2, ROLE_PROF_MIN_REQ_RATING3 |
| WLF_TALENT_PROF_GAP_SUMMARY_N5 | Non Unique | Default | ESS_JOB_ID |
| WLF_TALENT_PROF_GAP_SUMMARY_N6 | Non Unique | Default | GAP_TYPE |
| WLF_TALENT_PROF_GAP_SUMMARY_U1 | Unique | Default | TALENT_PROF_GAP_SUMMARY_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
