# HWR_PER_PRFL_TO_LOCATE

The profiles to locate table stores profiles that will need to be located in sources.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperprfltolocate-25164.html#hwrperprfltolocate-25164](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperprfltolocate-25164.html#hwrperprfltolocate-25164)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_PER_PRFL_TO_LOCATE_PK | SOURCE_ID, PRFL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SOURCE_ID | NUMBER |  | 18 | Yes | The Id for the social data source. |
| PRFL_ID | VARCHAR2 | 500 |  | Yes | This is the key used by the source to identify the profile. |
| QUERY_COUNT | NUMBER |  |  |  | This is the number of times this profile was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_PER_PRFL_TO_LOCATE_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, PRFL_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
