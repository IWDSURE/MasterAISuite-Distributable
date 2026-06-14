# WLF_SKILL_CENTER_ITEM_DN

This table stores the details of the skills assigned from the skill center.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfskillcenteritemdn-11398.html#wlfskillcenteritemdn-11398](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfskillcenteritemdn-11398.html#wlfskillcenteritemdn-11398)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_SKILL_CENTER_ITEM_DN_PK | SKILL_CENTER_ITEM_DN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SKILL_CENTER_ITEM_DN_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| PROFILE_ID | NUMBER |  | 18 | Yes | Identifier of the assigned skill profile. |
| SKILL | VARCHAR2 | 240 |  | Yes | Name of the assigned skill. |
| REQUIRED_LEVEL | NUMBER |  | 18 |  | The required level set by assignor. |
| ACHIEVED_LEVEL | NUMBER |  | 18 |  | Level that person has achieved for assigned skill. |
| SKILL_GROUP | VARCHAR2 | 30 |  | Yes | Specifies if the skill is a developed or developing skill. |
| IMPORTANCE | NUMBER |  | 18 |  | Specifies the relative importance of the profile item. |
| SKILL_CRITERIA_TYPE_CODE | VARCHAR2 | 30 |  |  | Specifies the skill criteria type. This corresponds to lookup code from ORA_HRT_SKILL_CRITERIA_TYPES lookup type. |
| ASSIGNED_DATE | DATE |  |  |  | Specifies the date when the skill is added to person profile. |
| METRIC_DATE | DATE |  |  | Yes | Specifies the effective date of the calculated metrics. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| SKILL_CENTER_ITEM_DN_N1 | Non Unique | Default | PROFILE_ID |
| SKILL_CENTER_ITEM_DN_U1 | Unique | Default | SKILL_CENTER_ITEM_DN_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
