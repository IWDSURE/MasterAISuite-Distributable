# HRC_ALERTS_B

Contains event and resource alert definition data.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertsb-24398.html#hrcalertsb-24398](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertsb-24398.html#hrcalertsb-24398)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ALERTS_B_PK | ALERT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALERT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| ALERT_TYPE | VARCHAR2 | 30 |  | Yes | Determines the Alert Type. The valid values are based on the look type HRC_ALERT_TYPE. |
| FILTER_TYPE | VARCHAR2 | 20 |  | Yes | Determine the type of the filter expression |
| RESOURCE_APPLICATION | VARCHAR2 | 256 |  |  | The resource application (e.g. hcmCoreSetupApi). |
| RESOURCE_PATH | VARCHAR2 | 2000 |  |  | The resource path (e.g. /resources/latest/employees) |
| RUN_TYPE | VARCHAR2 | 30 |  | Yes | Determines what the alert repeat frequency. For an alert which is for a Document Resource only On demand is available. The valid values are based on the look type HRC_ALERT_RUN_TYPE. The default value is On demand. |
| RUN_EXPRESSION | VARCHAR2 | 2000 |  |  | Specifies the run expression for either a scheduled expression complying to rfc2445. For example: FREQ=YEARLY;INTERVAL=1;BYMONTH=5;BYDAY=2MO; or a feed name. |
| SCHEDULED_REQUEST_ID | NUMBER |  | 18 |  | Specifies the ESS Request ID for a schedule. If a schedule recurrence has been defined, this is the Absolute Parent ID request (i.e. the top level ESS request). |
| SCHEDULED_START | TIMESTAMP |  |  |  | Specifies the ESS start for a schedule. |
| SCHEDULED_END | TIMESTAMP |  |  |  | Specifies the ESS end for a schedule. |
| KEEP | VARCHAR2 | 30 |  | Yes | Determines if the alert should be kept active and based on YES_NO.
If Y, the KEEP_FREQ_TYPE, KEEP_VALUE must be specified. If N, the KEEP_FREQ_TYPE, KEEP_VALUE should be null. Note: If the KEEP is updated from Y to N then any existing Keeps are deleted. |
| KEEP_FREQ_TYPE | VARCHAR2 | 30 |  |  | Determines the alert keep frequency type. The valid values are based on the look type HRC_ALERT_KEEP_FREQ_TYPE. The value is mandatory if the KEEP is defined as Y. |
| KEEP_VALUE | NUMBER |  | 5 |  | Determines the alert keep value. The value is mandatory is the KEEP is defined as Y. |
| THRESHOLD | NUMBER |  | 5 |  | Determines the maximum number of Alerts that can be raised per run. A null value indicates no threshold is applied and the number of alerts raised are unlimited. |
| TEST_MODE | VARCHAR2 | 30 |  | Yes | Determines if the Alert when run is in a test mode. When in test mode, the alert will process normally but will not physically deliver payloads to consumers. Valid values are based on the lookup type YES_NO and the default value is N. |
| ENABLED | VARCHAR2 | 30 |  | Yes | Determines if the Alert is enabled or disabled. Valid values are based on the lookup type YES_NO and the default value is Y. |
| FILTER_EXPRESSIONS | CLOB |  |  |  | XML structured document of filter expressions. |
| OBJECT_GUID | VARCHAR2 | 32 |  | Yes | Speicifies the object GUID. Primarily used for seed data framework. |
| ALERT_CODE | VARCHAR2 | 1000 |  | Yes | Specifies an alert code which can be used to identify an alert |
| ALERT_ACCESS_LEVEL | VARCHAR2 | 30 |  |  | ALERT_ACCESS_LEVEL |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATE_HISTORY | VARCHAR2 | 30 |  | Yes | Specifies if Activity History should be generated. Valid values are Y or N |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| RUN_OPTIONS | CLOB |  |  |  | Contains config run option values for the run. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| DELETED_FLAG | VARCHAR2 | 30 |  | Yes | Used to identify for soft delete. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ALERTS_B_N20 | Non Unique | Default | SGUID |
| HRC_ALERTS_B_PK | Unique | Default | ALERT_ID, ORA_SEED_SET1 |
| HRC_ALERTS_B_PK1 | Unique | Default | ALERT_ID, ORA_SEED_SET2 |
| HRC_ALERTS_B_U1 | Unique | Default | OBJECT_GUID, ORA_SEED_SET1 |
| HRC_ALERTS_B_U11 | Unique | Default | OBJECT_GUID, ORA_SEED_SET2 |
| HRC_ALERTS_B_U2 | Unique | Default | ALERT_CODE, ORA_SEED_SET1 |
| HRC_ALERTS_B_U21 | Unique | Default | ALERT_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
