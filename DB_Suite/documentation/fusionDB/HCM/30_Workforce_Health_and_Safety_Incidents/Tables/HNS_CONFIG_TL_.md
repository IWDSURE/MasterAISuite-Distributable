# HNS_CONFIG_TL_

HNS CONF SETUP. This multi lingual table stores configuration steps information.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsconfigtl-19876.html#hnsconfigtl-19876](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsconfigtl-19876.html#hnsconfigtl-19876)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_CONFIG_TL_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, CONFIG_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CONFIG_ID | NUMBER |  | 18 | Yes | Unique configuration identifier.Primary key for HNS_CONFIG_TL table. | Active |
| CONFIG_NAME | VARCHAR2 | 200 |  |  | Configuration Name.This is a multi lingual column. | Active |
| CONFIG_DESCRIPTION | VARCHAR2 | 240 |  |  | Configruation Description. This is a multi lingual column. | Active |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. | Active |
| SOURCE_LANG | VARCHAR2 | 4 |  |  | Indicates the code of the language in which the contents of the translatable columns were originally created. | Active |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |  |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |  |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_CONFIG_TLN1_ | Non Unique | Default | CONFIG_ID, LANGUAGE, LAST_UPDATE_DATE |
| HNS_CONFIG_TL_UK1_ | Unique | FUSION_TS_SEED | LAST_UPDATE_DATE, LAST_UPDATED_BY, CONFIG_ID, LANGUAGE |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
