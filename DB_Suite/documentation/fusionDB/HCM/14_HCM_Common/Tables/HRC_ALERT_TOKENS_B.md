# HRC_ALERT_TOKENS_B

Contains event alert tokens data.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalerttokensb-21056.html#hrcalerttokensb-21056](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalerttokensb-21056.html#hrcalerttokensb-21056)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ALERT_TOKENS_B_PK | TOKEN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TOKEN_ID | NUMBER |  | 18 | Yes | Token id of event alert token |
| TOKEN_NAME | VARCHAR2 | 80 |  |  | Token name of event alert token |
| MANDATORY | VARCHAR2 | 20 |  |  | Mandatory of event alert token |
| DEFAULT_VALUE | VARCHAR2 | 200 |  |  | Default Value of event alert token |
| TOKEN_LEVEL | VARCHAR2 | 20 |  | Yes | Possible values are ORA_ALERT_TOKEN and ORA_TEMPLATE_TOKEN |
| ALERT_ID | NUMBER |  | 18 | Yes | Alert ID of event alert token |
| TEMPLATE_ID | NUMBER |  | 18 |  | Template ID of event alert token |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_GUID | VARCHAR2 | 32 |  | Yes | Object Id of event alert token |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| DELETED_FLAG | VARCHAR2 | 1 |  | Yes | DELETED_FLAG |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ALERT_TOKENS_B_N20 | Non Unique | Default | SGUID |
| HRC_ALERT_TOKENS_B_PK | Unique | Default | TOKEN_ID, ORA_SEED_SET1 |
| HRC_ALERT_TOKENS_B_PK1 | Unique | Default | TOKEN_ID, ORA_SEED_SET2 |
| HRC_ALERT_TOKENS_B_U1 | Unique | Default | OBJECT_GUID, ORA_SEED_SET1 |
| HRC_ALERT_TOKENS_B_U11 | Unique | Default | OBJECT_GUID, ORA_SEED_SET2 |
| HRC_ALERT_TOKENS_B_U2 | Unique | Default | TOKEN_NAME, ALERT_ID, TEMPLATE_ID, ORA_SEED_SET1 |
| HRC_ALERT_TOKENS_B_U21 | Unique | Default | TOKEN_NAME, ALERT_ID, TEMPLATE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
