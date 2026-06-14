# IRC_CAND_PREFERENCES

Stores candidate preferences in Recruiting.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandpreferences-14967.html#irccandpreferences-14967](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandpreferences-14967.html#irccandpreferences-14967)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_PREFERENCES_PK | CAND_PREF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAND_PREF_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_PERSONS. |
| SITE_NUMBER | VARCHAR2 | 240 |  |  | Foreign key to IRC_CX_SITES_B table. |
| TC_AF_VERSION_ID | NUMBER |  | 18 |  | Apply Flow that was used for talent community signup. Foreign key to IRC_AF_VERSIONS table. |
| TC_LEGAL_DESC_VERSION_ID | NUMBER |  | 18 |  | To track the legal disclaimer accepted by the candidate during talent community signup. Foreign key to IRC_DESC_VERSIONS_B table. |
| OPT_IN_TC_EMAILS_FLAG | VARCHAR2 | 1 |  |  | Stores whether the candidate has opted-in or opted-out for receiving job alerts for the site. Null value means unspecified. |
| OPT_IN_TC_EMAILS_DATE | TIMESTAMP |  |  |  | Stores the date and time at which the candidate updated this preference of whether or not to receive job alerts for the site. |
| TC_CONFIRMED_FLAG | VARCHAR2 | 1 |  |  | This flag is used to determine whether talent community signup of candidate is confirmed for the site or not. |
| TC_CONFIRMED_BY_PERSON_ID | NUMBER |  | 18 |  | Foreign Key to PER_PERSONS table. |
| TC_CONFIRMED_DATE | DATE |  |  |  | To track when the talent community signup of candidate changed from Unconfirmed to Confirmed. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_PREFERENCES_FK2 | Non Unique | Default | SITE_NUMBER |
| IRC_CAND_PREFERENCES_FK3 | Non Unique | Default | TC_AF_VERSION_ID |
| IRC_CAND_PREFERENCES_FK4 | Non Unique | Default | TC_LEGAL_DESC_VERSION_ID |
| IRC_CAND_PREFERENCES_FK5 | Non Unique | Default | TC_CONFIRMED_BY_PERSON_ID |
| IRC_CAND_PREFERENCES_PK | Unique | Default | CAND_PREF_ID |
| IRC_CAND_PREFERENCES_U1 | Unique | Default | PERSON_ID, SITE_NUMBER |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
