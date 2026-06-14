# HRC_ALERT_RECIPIENTS

Contains alert recipients data.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrecipients-22240.html#hrcalertrecipients-22240](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrecipients-22240.html#hrcalertrecipients-22240)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ALERT_RECIPIENTS_PK | RECIPIENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECIPIENT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| TEMPLATE_ID | NUMBER |  | 18 | Yes | Template Identifier. Foreign Key to HRC_TEMPLATES_B.ALERT_ID |
| OBJECT_GUID | VARCHAR2 | 32 |  | Yes | Speicifies the object GUID. Primarily used for seed data framework. |
| DELIVER_TYPE | VARCHAR2 | 30 |  | Yes | Determines the delivery type (i.e. To, Cc). Valid values are based on the lookup of HRC_ALERT_DELIVERY_TYPE. |
| CHANNEL_TYPE | VARCHAR2 | 30 |  | Yes | Determines the delivery channel type (e.g Email, Sms, Im, Feed, Worklist). Valid values are based on the lookup of HRC_ALERT_CHANNEL_TYPE. |
| VALUE_EXPRESSION | VARCHAR2 | 2000 |  | Yes | Specifies the deliver to value expression. e.g. ${Employees.EmailAddress}, ${USER:martha.kelly@abc.com} |
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
| HRC_ALERT_RECIPIENTS_FK1 | Non Unique | Default | TEMPLATE_ID |
| HRC_ALERT_RECIPIENTS_N20 | Non Unique | Default | SGUID |
| HRC_ALERT_RECIPIENTS_PK | Unique | Default | RECIPIENT_ID, ORA_SEED_SET1 |
| HRC_ALERT_RECIPIENTS_PK1 | Unique | Default | RECIPIENT_ID, ORA_SEED_SET2 |
| HRC_ALERT_RECIPIENTS_U1 | Unique | Default | OBJECT_GUID, ORA_SEED_SET1 |
| HRC_ALERT_RECIPIENTS_U11 | Unique | Default | OBJECT_GUID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
