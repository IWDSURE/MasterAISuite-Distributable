# IRC_LI_CANDIDATE_MAPPING

Stores the candidate mapping between ORC and LinkedIn

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclicandidatemapping-31551.html#irclicandidatemapping-31551](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclicandidatemapping-31551.html#irclicandidatemapping-31551)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LI_CANDIDATE_MAPPING_PK | PERSON_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_ID | NUMBER |  | 18 | Yes | Primary Key for the table and also foreign key to IRC_CANDIDATES |
| LI_PERSON_URN | VARCHAR2 | 100 |  | Yes | LinkedIn Person Identifier, used to find user by foreign Id. |
| ADDITIONAL_INFO1 | VARCHAR2 | 2000 |  |  | To store additional info for the candidate |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LI_CANDIDATE_MAPPING_N1 | Non Unique | Default | LI_PERSON_URN |
| IRC_LI_CANDIDATE_MAPPING_N2 | Non Unique | Default | UPPER("LI_PERSON_URN") |
| IRC_LI_CANDIDATE_MAPPING_PK | Unique | Default | PERSON_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
