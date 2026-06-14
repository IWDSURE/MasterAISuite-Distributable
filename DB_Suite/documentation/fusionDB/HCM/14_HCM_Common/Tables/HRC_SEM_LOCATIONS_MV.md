# HRC_SEM_LOCATIONS_MV

This table is to store the mutli-value fields associated with a location.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemlocationsmv-12069.html#hrcsemlocationsmv-12069](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemlocationsmv-12069.html#hrcsemlocationsmv-12069)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_LOCATIONS_MV_PK | LOCATION_MV_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOCATION_MV_ID | NUMBER |  | 18 | Yes | This is the primary column of Location multi-value table. |
| LOCATION_ID | NUMBER |  | 18 | Yes | This is the primary key of the location table. |
| LANGUAGE_CODE | VARCHAR2 | 9 |  |  | Indicates the code of the language into which the contents of the translatable columns are translated. |
| FQN | VARCHAR2 | 4000 |  |  | This column indicates a fully qualified name of the location. |
| IS_ERROR | NUMBER |  | 8 |  | This column indicates if there is an error in indexing event. |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | This column contains the error message of the indexing event. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SEM_LOCATIONS_MV_N1 | Non Unique | Default | LOCATION_ID |
| HRC_SEM_LOCATIONS_MV_U1 | Unique | FUSION_TS_TX_DATA | LOCATION_MV_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
