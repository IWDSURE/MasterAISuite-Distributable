# HWR_PER_PRFL_GROUP_B

The profile group table stores profile group data that applies to the entire group.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperprflgroupb-4371.html#hwrperprflgroupb-4371](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperprflgroupb-4371.html#hwrperprflgroupb-4371)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_PER_PRFL_GROUP_B_PK | SOURCE_ID, PROFILE_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_GROUP_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the profile group table. |
| SOURCE_ID | NUMBER |  | 18 | Yes | The Id of the source for this profile group. |
| PRFL_GROUP_REPO | NUMBER |  | 18 |  | The unique Id for writing to repo. |
| CATEGORY | VARCHAR2 | 100 |  |  | The category of this profile group. |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | The description of this profile group. |
| LOCATION | VARCHAR2 | 1000 |  |  | The location of this profile group. |
| LOGO | VARCHAR2 | 4000 |  |  | The image url for the logo of this profile group. |
| NAME | VARCHAR2 | 1000 |  |  | The name of this profile group. |
| SHORT_DESCRIPTION | VARCHAR2 | 1000 |  |  | The short description of this profile group. |
| SMALL_LOGO | VARCHAR2 | 4000 |  |  | The image url for the small logo of this profile group. |
| PROFILE_GROUP_TYPE | VARCHAR2 | 100 |  |  | The profile group type of this profile group. |
| UPDATED_ON | TIMESTAMP |  |  |  | The date this profile group was updated on. |
| URL | VARCHAR2 | 4000 |  |  | The URL for accessing this profile group. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_PER_PRFL_GROUP_B_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, PROFILE_GROUP_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
