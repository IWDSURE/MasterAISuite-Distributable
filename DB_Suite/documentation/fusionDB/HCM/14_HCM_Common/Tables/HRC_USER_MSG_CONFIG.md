# HRC_USER_MSG_CONFIG

This table holds details of configuration specific to a certain user for communication messages

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcusermsgconfig-12890.html#hrcusermsgconfig-12890](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcusermsgconfig-12890.html#hrcusermsgconfig-12890)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_USER_MSG_CONFIG_PK | USER_MSG_CONFIGID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USER_MSG_CONFIGID | NUMBER |  | 18 | Yes | Unique identifier for message configuration of a particular user |
| PERSONID | NUMBER |  | 18 |  | Person id of the user for whom the corresponding message configation is stored |
| USERNAME | VARCHAR2 | 200 |  |  | Username of the user for whom the corresponding message configation is stored |
| USERGUID | VARCHAR2 | 64 |  |  | GUID of the user for whom the corresponding message configation is stored |
| CONFIGTYPE | VARCHAR2 | 200 |  |  | Type of the configuration for the specific user |
| CONFIGOBJECT | CLOB |  |  |  | Configuration object corresponding to a particular user |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_USER_MSG_CONFIG_PK | Unique | Default | USER_MSG_CONFIGID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
