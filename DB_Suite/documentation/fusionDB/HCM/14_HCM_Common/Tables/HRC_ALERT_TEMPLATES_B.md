# HRC_ALERT_TEMPLATES_B

Contains alert template definition data.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalerttemplatesb-13602.html#hrcalerttemplatesb-13602](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalerttemplatesb-13602.html#hrcalerttemplatesb-13602)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ALERT_TEMPLATES_B_PK | TEMPLATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEMPLATE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| OBJECT_GUID | VARCHAR2 | 32 |  | Yes | Speicifies the object GUID. Primarily used for seed data framework. |
| ALERT_ID | NUMBER |  | 18 | Yes | Alert Identifier. Foreign Key to HRC_ALERTS_B.ALERT_ID |
| ENABLED | VARCHAR2 | 30 |  | Yes | Determines if the Templatet is enabled or disabled. Valid values are based on the lookup type YES_NO and the default value is Y. |
| RESOURCE_NAME | VARCHAR2 | 256 |  |  | The Resource Name. |
| MIME_TYPE | VARCHAR2 | 30 |  | Yes | Valid values are based on the lookup of ORA_HRC_ALERT_MIME_TYPE. The default value should be HTML. |
| NT_FLAG | VARCHAR2 | 30 |  | Yes | Non translatable flag identifies the location of the message body either in the base or translation source. |
| NT_BODY | CLOB |  |  |  | Non translatable message body definition. |
| DEFAULT_LANGUAGE | VARCHAR2 | 4 |  |  | Specifies the default language to be used by the template. |
| ALERT_PER_TYPE | VARCHAR2 | 30 |  |  | Determines the number of notifications to send for a resource. Valid values are either one per Record or one per Recordset and based on the lookup of HRC_ALERT_PER_TYPE. The Row value can be selected for any resource. The Rowset can only be selected for child collection resources. |
| RUN_EXPRESSION | VARCHAR2 | 2000 |  |  | Specifies an expression to determine if a template should run. |
| ATTRIBUTES | CLOB |  |  |  | System maintained list of Attributes (names) used for Short Message/Subject/Body for an Event Alert. |
| STORE_MESSAGES | VARCHAR2 | 30 |  |  | Specifies if a generated message should be stored for a run. The defau;lt value is Y. |
| GROUPBY_EXPRESSION | VARCHAR2 | 2000 |  |  | To store the groupby expression which would group the template messages |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| DELETED_FLAG | VARCHAR2 | 30 |  | Yes | Used to identify for soft delete. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ALERT_TEMPLATES_B_FK1 | Non Unique | Default | ALERT_ID |
| HRC_ALERT_TEMPLATES_B_N20 | Non Unique | Default | SGUID |
| HRC_ALERT_TEMPLATES_B_PK | Unique | Default | TEMPLATE_ID, ORA_SEED_SET1 |
| HRC_ALERT_TEMPLATES_B_PK1 | Unique | Default | TEMPLATE_ID, ORA_SEED_SET2 |
| HRC_ALERT_TEMPLATES_B_U1 | Unique | Default | OBJECT_GUID, ORA_SEED_SET1 |
| HRC_ALERT_TEMPLATES_B_U11 | Unique | Default | OBJECT_GUID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
