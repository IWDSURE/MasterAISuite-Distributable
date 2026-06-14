# PAY_MIG_STAGING_ELEMENTS

This table contains information that is useful for element migration itself and related areas. It contains a mapping between a PeopleSoft earning or deduction and the Fusion element that it will be migrated to. It contains the status of the migration, including whether an element should be migrated and has been migrated successfully. It also contains information that is common between all elements, such as the primary classifications and the legislative data group.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paymigstagingelements-29727.html#paymigstagingelements-29727](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paymigstagingelements-29727.html#paymigstagingelements-29727)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_MIG_STAGING_ELEMENTS_PK | STAGING_ELEMENTS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STAGING_ELEMENTS_ID | NUMBER |  | 18 | Yes | Primary key. |
| TRANSFERRED_FLAG | VARCHAR2 | 30 |  | Yes | Indicates whether the associated definition has been either transferred via template or created manually by customer. We cannot re-run for any that have been transferred already. |
| MIGRATE_DEFINITION_FLAG | VARCHAR2 | 30 |  | Yes | Indicates that the user wishes to transfer the earning. |
| DEFINITION_TYPE | VARCHAR2 | 30 |  | Yes | Indicates if this is an earnings or deduction definition. |
| SOURCE_ELEMENT_NAME | VARCHAR2 | 18 |  | Yes | Populated with whatever is considered the unique name of the earnings definition. |
| SOURCE_ELEMENT_ID | NUMBER |  | 18 | Yes | Will be populated with the identifier of the PeopleSoft source definition record. |
| SOURCE_SHORT_DESC | VARCHAR2 | 18 |  |  | Value from PeopleSoft database. Not relevant for GPUK. |
| SOURCE_DESCRIPTION | VARCHAR2 | 80 |  |  | Value from PeopleSoft database. |
| ELEMENT_NAME | VARCHAR2 | 80 |  | Yes | Name of element to create on fusion.
(PAY_ELEMENT_TYPES_F.BASE_ELEMENT_NAME). |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | Primary key ID of element created (PAY_ELEMENT_TYPES_F.ELEMENT_TYPE_ID). This will be populated when the element is actually created on the Fusion system. It is intended to make it easy to map between the PeopleSoft and Fusion definitions. |
| REPORTING_NAME | VARCHAR2 | 80 |  |  | The reporting name of the created element. |
| LEGISLATIVE_DATA_GROUP_NAME | VARCHAR2 | 80 |  | Yes | Legislative data group name that element will belong to. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| PRIMARY_CLASSIFICATION_NAME | VARCHAR2 | 80 |  | Yes | Primary classification name that element will belong to. |
| PRIMARY_CLASSIFICATION_ID | NUMBER |  | 18 |  | Foreign key to PAY_ELE_CLASSIFICATIONS.CLASSIFICATION_ID (for a primary classification, i.e. where PAY_ELE_CLASSIFICATIONS.PARENT_CLASSIFICATION_ID is NULL). |
| SECONDARY_CLASSIFICATION_NAME | VARCHAR2 | 160 |  |  | Secondary classification name that element will belong to. |
| SECONDARY_CLASSIFICATION_ID | NUMBER |  | 18 |  | Foreign key to PAY_ELE_CLASSIFICATIONS.CLASSIFICATION_ID. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Description of element to create on fusion. |
| INPUT_CURRENCY_CODE | VARCHAR2 | 30 |  |  | Input currency for the element. |
| OUTPUT_CURRENCY_CODE | VARCHAR2 | 30 |  | Yes | Output currency for the element. |
| STANDARD_LINK_FLAG | VARCHAR2 | 30 |  | Yes | This sets the PAY_ELEMENT_TYPES_F.STANDARD_LINK_FLAG (which would also default PAY_ELEMENT_LINKS_F.STANDARD_LINK_FLAG). |
| STARTING_TIME_DEF_SHORT_CODE | VARCHAR2 | 80 |  | Yes | Starting time definition short code value. Equivalent to PAY_TIME_DEFINITIONS.SHORT_NAME. |
| STARTING_TIME_DEF_ID | NUMBER |  | 18 |  | Foreign key reference to PAY_TIME_DEFINITIONS.TIME_DEFINITION_ID. |
| ENDING_TIME_DEF_SHORT_CODE | VARCHAR2 | 80 |  | Yes | Ending time definition short code value. Equivalent to PAY_TIME_DEFINITIONS.SHORT_NAME. |
| ENDING_TIME_DEF_ID | NUMBER |  | 18 |  | Foreign key reference to PAY_TIME_DEFINITIONS.TIME_DEFINITION_ID. |
| EMPLOYMENT_LEVEL | VARCHAR2 | 30 |  | Yes | Which level in three tier model will entries for this definition be attached. |
| PROCESSING_TYPE | VARCHAR2 | 30 |  | Yes | Recurring (R) or non-recurring (N) definition. |
| ONCE_EACH_PERIOD_FLAG | VARCHAR2 | 1 |  | Yes | Processed only once per period? |
| MULTIPLE_ENTRIES_ALLOWED_FLAG | VARCHAR2 | 30 |  | Yes | Whether or not more than one entry for this definition can exist over same span of time. |
| INVOL_DEDUCTION_CODE | VARCHAR2 | 30 |  |  | The PeopleSoft involuntary deduction code. If set, indicates the definition is to be used for voluntary deduction mapping for a particular deduction type. |
| PLAN_TYPE | VARCHAR2 | 2 |  |  | Required for PNA migration. |
| DED_CLASS | VARCHAR2 | 1 |  |  | Required for PNA migration. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_MIG_STAGING_ELEMENTS_N2 | Non Unique | Default | SOURCE_ELEMENT_NAME |
| PAY_MIG_STAGING_ELEMENTS_N3 | Non Unique | Default | SOURCE_ELEMENT_ID |
| PAY_MIG_STAGING_ELEMENTS_PK | Unique | Default | STAGING_ELEMENTS_ID |
| PAY_MIG_STAGING_ELEMENTS_U1 | Unique | Default | LEGISLATIVE_DATA_GROUP_ID, ELEMENT_NAME |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
