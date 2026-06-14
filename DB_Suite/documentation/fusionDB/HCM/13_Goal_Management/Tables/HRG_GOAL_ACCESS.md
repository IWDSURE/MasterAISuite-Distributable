# HRG_GOAL_ACCESS

Stores the details of access provided by worker on goals and their actions.

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalaccess-3563.html#hrggoalaccess-3563](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalaccess-3563.html#hrggoalaccess-3563)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_GOAL_ACCESS_PK | GOAL_ACCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| GOAL_ACCESS_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry. |  |
| GOALS_SHARED_BY | VARCHAR2 | 30 |  |  | Stores goals shared by details |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |  |
| GOAL_ID | NUMBER |  | 18 | Yes | Foreign key to HRG_GOALS |  |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ALL_PEOPLE_F, which represents the person who received access on the goal. |  |
| ACCESS_GRANT_DATE | TIMESTAMP |  |  | Yes | Date on which access is granted. |  |
| GOAL_ACTION_ACCESS_FLAG | VARCHAR2 | 30 |  | Yes | States that access is provided on goal actions or not. Possible values are Yes and No. |  |
| GOAL_ADDED_FLAG | VARCHAR2 | 30 |  |  | States that the shared goal is added by the person or not. Possible values are Yes and No. |  |
| VIEW_SHARED_GOAL_FLAG | VARCHAR2 | 30 |  |  | Based on this column, the colleague goals are displayed. Possible values are Yes and No. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_ACCESS (HRG_GOAL_ACCESS) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRG_GOAL_ACCESS_FK1 | Non Unique | Default | GOAL_ID |
| HRG_GOAL_ACCESS_N1 | Non Unique | Default | PERSON_ID |
| HRG_GOAL_ACCESS_N2 | Non Unique | Default | ACCESS_GRANT_DATE |
| HRG_GOAL_ACCESS_PK | Unique | Default | GOAL_ACCESS_ID |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
