# IRC_FEATURE_USAGE

Table contains the details about feature usage and feature usage count with respect to functional area.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircfeatureusage-12979.html#ircfeatureusage-12979](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircfeatureusage-12979.html#ircfeatureusage-12979)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_FEATURE_USAGE_PK | FEATURE_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FEATURE_USAGE_ID | NUMBER |  | 18 | Yes | Feature Usage Id is a primary key which is automatically generated value. |
| FEATURE_CONFIG_ID | NUMBER |  | 18 | Yes | Foreign Key to IRC_FEATURE_CONFIG_B table. |
| SETTING_VALUE | VARCHAR2 | 1000 |  |  | The value of the recruting setting. |
| PROFILE_OPTION_VALUE | VARCHAR2 | 1000 |  |  | The value of the profile option. |
| FEATURE_USAGE_FLAG | VARCHAR2 | 1 |  |  | The column indicates if the feature is used. |
| FEATURE_USAGE_INFORMATION | VARCHAR2 | 1000 |  |  | The column contains additional information about the feature usage. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_FEATURE_USAGE_FK1 | Non Unique | Default | FEATURE_CONFIG_ID |
| IRC_FEATURE_USAGE_PK | Unique | Default | FEATURE_USAGE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
