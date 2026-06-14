# HRY_CONFIG_PROP_DTLS_OVERRIDE

Data to be stored for the customer overriden values

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryconfigpropdtlsoverride-5309.html#hryconfigpropdtlsoverride-5309](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryconfigpropdtlsoverride-5309.html#hryconfigpropdtlsoverride-5309)

## Primary Key

| Name | Columns |
|------|----------|
| HRY_CONFIG_PROP_DTL_OVRD_PK | PROPERTY_OVERRIDE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROPERTY_OVERRIDE_ID | NUMBER |  | 18 | Yes | Primary key to the table hry_pi_configuration_details |
| PROPERTY_DETAIL_ID | NUMBER |  | 18 |  | Foreign key to the table hry_setup_config_prop_details |
| PROPERTY_ID | NUMBER |  | 18 |  | Foreign key to the table hry_setup_config_prop_details |
| VALUE_TYPE | VARCHAR2 | 256 |  |  | Flag to Check whether to provide Fast Formula or Value Set |
| EFFECTIVE_START_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| OVERRIDE_VALUE | VARCHAR2 | 256 |  |  | It represents Value of the Property |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | This column represents Enterprise ID |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | This column represents Legislation Code |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to the table per_legislative_data_groups |
| PAYROLL_ID | NUMBER |  | 18 |  | Foreign key to the table per_all_payrolls_f |
| PERSON_ID | NUMBER |  | 18 |  | Foreign key to the table per_all_people_f |
| CONTEXT_ID | NUMBER |  | 18 |  | Extra column in case if we want to store some context id |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 150 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_CONFIG_PROP_DTL_OVRD_PK1 | Unique | Default | PROPERTY_OVERRIDE_ID |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
