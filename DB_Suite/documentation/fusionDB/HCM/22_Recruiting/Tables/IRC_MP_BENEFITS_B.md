# IRC_MP_BENEFITS_B

This table consist of list of benefits which will be associated with the gig.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpbenefitsb-17432.html#ircmpbenefitsb-17432](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpbenefitsb-17432.html#ircmpbenefitsb-17432)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MP_BENEFITS_B_PK | BENEFIT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BENEFIT_ID | NUMBER |  | 18 | Yes | This column is the Primary Key column of the IRC_MP_BENEFITS_B which is unique and not null. |
| GIG_ID | NUMBER |  | 18 | Yes | This column describes of a gig for which the benefit assigned, Foreign Key to IRC_MP_GIGS_B table |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MP_BENEFITS_B_FK1 | Non Unique | Default | GIG_ID |
| IRC_MP_BENEFITS_B_PK | Unique | Default | BENEFIT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
