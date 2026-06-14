# IRC_CX_PROV_CONFIGS

This table will keep information about configurations of the external provider, each external provider can have multiple configurations(like draft configurations) it is up to admin which will be enabled.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxprovconfigs-27197.html#irccxprovconfigs-27197](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxprovconfigs-27197.html#irccxprovconfigs-27197)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_PROV_CONFIGS_PK | CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIG_ID | NUMBER |  | 18 | Yes | Identifier of the external provider config. System generated value. |
| PROVIDER_ID | NUMBER |  | 18 | Yes | Foreign key to irc_cx_providers table. |
| CONFIG_CODE | VARCHAR2 | 200 |  | Yes | Unique code of the setting can be used as alternative key needed by Migration Services. |
| CONFIG_NAME | VARCHAR2 | 240 |  | Yes | The name of the configuration , which can be defined by administrator. |
| CONFIG_DESCRIPTION | VARCHAR2 | 1000 |  |  | Description of the external provider configuration , can be filled by administrator for information purpose. |
| CONFIG_STATUS | VARCHAR2 | 40 |  | Yes | Status of the configuration , can be ORA_ACTIVE, ORA_DRAFT and so one. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_PROV_CONFIGS_FK1 | Non Unique | Default | PROVIDER_ID |
| IRC_CX_PROV_CONFIGS_PK | Unique | Default | CONFIG_ID |
| IRC_CX_PROV_CONFIGS_U1 | Unique | Default | CONFIG_CODE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
