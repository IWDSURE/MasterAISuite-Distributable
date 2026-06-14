# WLF_RESOURCES_B

Table to store details of resources

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfresourcesb-3193.html#wlfresourcesb-3193](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfresourcesb-3193.html#wlfresourcesb-3193)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_RESOURCES_B_PK | RESOURCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RESOURCE_ID | NUMBER |  | 18 | Yes | Resource Id |
| RESOURCE_NUMBER | VARCHAR2 | 30 |  |  | UserKey to uniquely identify Learning Resource. |
| STATUS | VARCHAR2 | 30 |  |  | Status of the resource, should be ORA_ACTIVE or ORA_INACTIVE |
| RESOURCE_TYPE | VARCHAR2 | 30 |  |  | Indicates the type of resource (CLASSROOM, etc) |
| LOCATION_ID | NUMBER |  | 18 |  | LOCATION_ID |
| CONTACT_ID | NUMBER |  | 18 |  | CONTACT_ID |
| CAPACITY | NUMBER |  | 9 |  | CAPACITY |
| SOURCE_ID | NUMBER |  | 18 |  | SOURCE_ID |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | SOURCE_TYPE |
| ATTRIBUTION_ID | NUMBER |  | 18 |  | ATTRIBUTION_ID |
| ATTRIBUTION_TYPE | VARCHAR2 | 30 |  |  | ATTRIBUTION_TYPE |
| ADDRESS_ID | NUMBER |  | 18 |  | Address of the resource |
| TRAINING_VENDOR_RES_ID | NUMBER |  | 18 |  | TRAINING_VENDOR_RES_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| RS_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| RS_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| RS_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER1 |
| RS_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER2 |
| RS_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER3 |
| RS_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER4 |
| RS_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER5 |
| RS_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER6 |
| RS_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER7 |
| RS_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER8 |
| RS_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER9 |
| RS_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER10 |
| RS_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER11 |
| RS_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER12 |
| RS_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER13 |
| RS_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER14 |
| RS_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER15 |
| RS_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER16 |
| RS_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER17 |
| RS_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER18 |
| RS_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER19 |
| RS_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | RS_ATTRIBUTE_NUMBER20 |
| RS_ATTRIBUTE_DATE1 | DATE |  |  |  | RS_ATTRIBUTE_DATE1 |
| RS_ATTRIBUTE_DATE2 | DATE |  |  |  | RS_ATTRIBUTE_DATE2 |
| RS_ATTRIBUTE_DATE3 | DATE |  |  |  | RS_ATTRIBUTE_DATE3 |
| RS_ATTRIBUTE_DATE4 | DATE |  |  |  | RS_ATTRIBUTE_DATE4 |
| RS_ATTRIBUTE_DATE5 | DATE |  |  |  | RS_ATTRIBUTE_DATE5 |
| RS_ATTRIBUTE_DATE6 | DATE |  |  |  | RS_ATTRIBUTE_DATE6 |
| RS_ATTRIBUTE_DATE7 | DATE |  |  |  | RS_ATTRIBUTE_DATE7 |
| RS_ATTRIBUTE_DATE8 | DATE |  |  |  | RS_ATTRIBUTE_DATE8 |
| RS_ATTRIBUTE_DATE9 | DATE |  |  |  | RS_ATTRIBUTE_DATE9 |
| RS_ATTRIBUTE_DATE10 | DATE |  |  |  | RS_ATTRIBUTE_DATE10 |
| RS_ATTRIBUTE_DATE11 | DATE |  |  |  | RS_ATTRIBUTE_DATE11 |
| RS_ATTRIBUTE_DATE12 | DATE |  |  |  | RS_ATTRIBUTE_DATE12 |
| RS_ATTRIBUTE_DATE13 | DATE |  |  |  | RS_ATTRIBUTE_DATE13 |
| RS_ATTRIBUTE_DATE14 | DATE |  |  |  | RS_ATTRIBUTE_DATE14 |
| RS_ATTRIBUTE_DATE15 | DATE |  |  |  | RS_ATTRIBUTE_DATE15 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_RESOURCES_B_FK1 | Non Unique | Default | LOCATION_ID |
| WLF_RESOURCES_B_FK2 | Non Unique | Default | CONTACT_ID |
| WLF_RESOURCES_B_N1 | Non Unique | Default | SOURCE_ID, SOURCE_TYPE |
| WLF_RESOURCES_B_N2 | Non Unique | Default | RESOURCE_TYPE |
| WLF_RESOURCES_B_N3 | Non Unique | Default | RESOURCE_NUMBER |
| WLF_RESOURCES_B_U1 | Unique | Default | RESOURCE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
