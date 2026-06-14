# IRC_CAMP_AUDIENCE_UPLOAD

Table to store campaign audience upload list.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampaudienceupload-17713.html#irccampaudienceupload-17713](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampaudienceupload-17713.html#irccampaudienceupload-17713)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_AUDIENCE_UPLOAD_PK | AUDIENCE_UPLOAD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AUDIENCE_UPLOAD_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated |
| CAMPAIGN_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMPAIGNS_B table. |
| AUDIENCE_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMP_AUDIENCE_SOURCE table. |
| PERSON_ID | NUMBER |  | 18 |  | Stores the PERSON_ID of the audience.One of the Foreign keys to per_persons table. |
| EMAIL | VARCHAR2 | 100 |  |  | Stores work email of the audience. For now its Employee Email |
| PHONE | VARCHAR2 | 100 |  |  | Stores work phone of the audience. For now its Employee work phone |
| DATA_JSON | CLOB |  |  |  | Stores all the additional columns in a JSON format |
| STATUS | VARCHAR2 | 30 |  |  | Stores whether record is active/inactive. Will be used to differentiate valid vs invalid records. |
| ERROR_CODE | VARCHAR2 | 30 |  |  | Stores the error messages after validating the row against person record. Typical errors could be Empty Email/Work Phone or invalid Email etc |
| OBJECT_STATUS | VARCHAR2 | 30 |  | Yes | Indicates the status of the object. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_AUDIENCE_UPLOAD_FK1 | Non Unique | Default | CAMPAIGN_ID |
| IRC_CAMP_AUDIENCE_UPLOAD_FK2 | Non Unique | Default | AUDIENCE_ID |
| IRC_CAMP_AUDIENCE_UPLOAD_N1 | Non Unique | Default | PERSON_ID |
| IRC_CAMP_AUDIENCE_UPLOAD_PK | Unique | Default | AUDIENCE_UPLOAD_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
