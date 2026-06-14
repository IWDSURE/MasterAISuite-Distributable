# IRC_MP_SITE_CONFIG_B

The table that contains the Site config details to publish the jobs.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpsiteconfigb-3739.html#ircmpsiteconfigb-3739](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpsiteconfigb-3739.html#ircmpsiteconfigb-3739)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MP_SITE_CONFIG_B_PK | SITE_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SITE_CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| SITE_CODE | VARCHAR2 | 200 |  | Yes | Unique site code defined by administrator. |
| SITE_TYPE | VARCHAR2 | 20 |  | Yes | Type of the site tells whether the site configuration is a Job Configuration or Gig Configuration. |
| ELIGIBILITY_OBJECT_ID | NUMBER |  | 18 |  | Eligibility Object for which profiles are attached. Foreign key to BEN_ELIG_OBJ_F table |
| ELIGIBILITY_PROFILE_ID | NUMBER |  | 18 |  | Eligibility Profile Id. Foreign key to BEN_ELIGY_PRFL table |
| STATUS_CODE | VARCHAR2 | 20 |  | Yes | Status of the site informing whether site is active or not |
| SEQUENCE_ORDER | NUMBER |  | 4 |  | Stores the sequence of the site |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MP_SITE_CONFIG_B_FK1 | Non Unique | Default | ELIGIBILITY_OBJECT_ID |
| IRC_MP_SITE_CONFIG_B_FK2 | Non Unique | Default | ELIGIBILITY_PROFILE_ID |
| IRC_MP_SITE_CONFIG_B_PK | Unique | Default | SITE_CONFIG_ID |
| IRC_MP_SITE_CONFIG_B_U1 | Unique | Default | SITE_CODE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
