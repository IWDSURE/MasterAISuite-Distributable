# HRC_SEM_INT_JOB_LOCS

This table is to store the internal job locations.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemintjoblocs-18267.html#hrcsemintjoblocs-18267](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemintjoblocs-18267.html#hrcsemintjoblocs-18267)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_INT_JOB_LOCS_PK | INT_JOB_LOC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INT_JOB_LOC_ID | NUMBER |  | 18 | Yes | This is the primary key of the internal job location table. |
| INTERNAL_JOB_ID | NUMBER |  | 18 | Yes | This column contains the Internal Job ID referenced to the Internal Job table. |
| COUNTRY_ID | VARCHAR2 | 80 |  | Yes | This is the country id of the address. |
| STATE_ID | VARCHAR2 | 80 |  |  | This is the state id of the address. |
| CITY_ID | VARCHAR2 | 80 |  |  | This is the city id of the address. |
| FQN | VARCHAR2 | 4000 |  | Yes | This column indicates the fully qualified name of the location. |
| LATITUDE | VARCHAR2 | 80 |  |  | This is the lattitude of the location. |
| LONGITUDE | VARCHAR2 | 80 |  |  | This is the longitude of the location. |
| IS_ERROR | NUMBER |  | 8 |  | This column indicates if there is an error in indexing event. |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | This column contains the error message of the indexing event. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRC_SEM_INT_JOB_LOCS_N1 | Non Unique | FUSION_TS_TX_DATA | COUNTRY_ID |  |
| HRC_SEM_INT_JOB_LOCS_N2 | Non Unique | FUSION_TS_TX_DATA | STATE_ID |  |
| HRC_SEM_INT_JOB_LOCS_N3 | Non Unique | FUSION_TS_TX_DATA | CITY_ID | Obsolete |
| HRC_SEM_INT_JOB_LOCS_N4 | Non Unique | FUSION_TS_TX_DATA | FQN |  |
| HRC_SEM_INT_JOB_LOCS_N5 | Non Unique | FUSION_TS_TX_DATA | INTERNAL_JOB_ID |  |
| HRC_SEM_INT_JOB_LOCS_U1 | Unique | FUSION_TS_TX_DATA | INT_JOB_LOC_ID |  |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
