# IRC_CAND_ALT_DETAILS

This table contains information about candidate alternate attribute details for e.g Alternate Email

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandaltdetails-22298.html#irccandaltdetails-22298](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandaltdetails-22298.html#irccandaltdetails-22298)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_ALT_DETAILS_PK | CAND_ALT_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAND_ALT_DETAIL_ID | NUMBER |  | 18 | Yes | Primary Key of the table. |
| PERSON_ID | NUMBER |  | 18 | Yes | PersonId of the Candidate.
Foreign Key association with IRC_CANDIDATES table. |
| ALT_EMAIL_ADDRESS | VARCHAR2 | 4000 |  | Yes | Alternate Email Address of the Candidate |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_ALT_DETAILS_PK | Unique | Default | CAND_ALT_DETAIL_ID |
| IRC_CAND_ALT_DETAILS_U1 | Unique | Default | PERSON_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
