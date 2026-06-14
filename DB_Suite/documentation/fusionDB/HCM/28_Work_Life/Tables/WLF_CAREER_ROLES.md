# WLF_CAREER_ROLES

This table is used to store different career roles types like Job Profiles/Position Profiles/Role Guides

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcareerroles-30452.html#wlfcareerroles-30452](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcareerroles-30452.html#wlfcareerroles-30452)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_CAREER_ROLES_PK | CAREER_ROLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAREER_ROLE_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| SOURCE_ID | NUMBER |  | 18 | Yes | Career role source Id. For example, in case of Job Profiles, it is job profile id |
| SOURCE_TYPE | VARCHAR2 | 30 |  | Yes | Career role source type. One of the lookup code from lookup type ORA_WLF_CAREER_ROLE_TYPE |
| IN_ELASTIC | VARCHAR2 | 1 |  |  | Indicates if record is processed to elastic index or not |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_CAREER_ROLES_N1 | Non Unique | Default | SOURCE_ID |
| WLF_CAREER_ROLES_N2 | Non Unique | Default | SOURCE_TYPE |
| WLF_CAREER_ROLES_U1 | Unique | Default | CAREER_ROLE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
