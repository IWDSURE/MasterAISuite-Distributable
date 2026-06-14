# IRC_CAMP_ELIG_MAPPING

Table to store the Employee communications Eligibility Profile Audience

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampeligmapping-16927.html#irccampeligmapping-16927](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampeligmapping-16927.html#irccampeligmapping-16927)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_ELIG_MAPPING_PK | ELIG_PRFL_ID, ELIG_OBJ_ID, CAMPAIGN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_PRFL_ID | NUMBER |  | 18 | Yes | Primary Key column Stores the Eligibility profile Id |
| ELIG_OBJ_ID | NUMBER |  | 18 | Yes | Stores the eligibility Object Id.Foreign Key to ben_elig_rslt_f table. |
| CAMPAIGN_ID | NUMBER |  | 18 | Yes | Foreign key to the irc_Campaigns_b |
| ELIG_PRFL_NAME | VARCHAR2 | 240 |  | Yes | Stores the Eligibility profile name. |
| AUDIENCE_COUNT | NUMBER |  | 8 |  | Stores the Audience count |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_ELIG_MAPPING_FK1 | Non Unique | Default | ELIG_OBJ_ID |
| IRC_CAMP_ELIG_MAPPING_FK2 | Non Unique | Default | CAMPAIGN_ID |
| IRC_CAMP_ELIG_MAPPING_PK | Unique | Default | ELIG_PRFL_ID, ELIG_OBJ_ID, CAMPAIGN_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
