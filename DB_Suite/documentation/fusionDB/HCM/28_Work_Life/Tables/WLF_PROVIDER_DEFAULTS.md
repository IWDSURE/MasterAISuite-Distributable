# WLF_PROVIDER_DEFAULTS

Table to store provider account default values.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfproviderdefaults-20392.html#wlfproviderdefaults-20392](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfproviderdefaults-20392.html#wlfproviderdefaults-20392)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_PROVIDER_DEFAULTS_PK | DEFAULT_OBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DEFAULT_OBJECT_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| PROVIDER_ACCOUNT_ID | NUMBER |  | 18 | Yes | Referece to a provider account. eg: Percipio, skill soft. |
| DEFAULT_OBJECT_VALUE | VARCHAR2 | 4000 |  |  | This column represents value of an attribute {ORA_OPEN,ORA_YES} |
| DEFAULT_OBJECT_TYPE | VARCHAR2 | 250 |  |  | This column represents name of an attribute {Visibility,Follow_Community} |
| DEFAULT_OBJECT_SUB_TYPE | VARCHAR2 | 250 |  |  | This column represents name of an attribute {ORA_TOPIC_COMMUNITY,ORA_OFFICIAL_COMMUNITY} |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_PROVIDER_DEFAULTS_N1 | Non Unique | Default | DEFAULT_OBJECT_TYPE |
| WLF_PROVIDER_DEFAULTS_U1 | Unique | Default | DEFAULT_OBJECT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
