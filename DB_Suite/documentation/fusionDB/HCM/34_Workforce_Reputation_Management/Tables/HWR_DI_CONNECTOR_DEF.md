# HWR_DI_CONNECTOR_DEF

This table stores the DI (Flow based) connector definition.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiconnectordef-16129.html#hwrdiconnectordef-16129](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiconnectordef-16129.html#hwrdiconnectordef-16129)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_DI_CONNECTOR_DEF_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | This is the primary key for this table. |
| SOURCE_ID | NUMBER |  | 18 | Yes | The social media source ID. |
| NAME | VARCHAR2 | 512 |  |  | The name of the connector. |
| OPENAPI_FILE_NAME | VARCHAR2 | 512 |  |  | The OpenAPI(Swagger) file name. |
| FILE_CONTENTS | CLOB |  |  |  | The contents of the OpenAPI(Swagger) file. |
| ICON_IMG | BLOB |  |  |  | The image file for the connector icon. |
| CONNECTOR_TYPE | VARCHAR2 | 128 |  |  | Record the type of the connector, communication, social reputation, wellness. |
| OVERALL_STATUS | VARCHAR2 | 128 |  |  | The indicator showing the current status of the overall definition. |
| PROCESS_STATUS | VARCHAR2 | 128 |  |  | The indicator showing the top-level steps where the guided process to resume from. |
| FROM_SEEDED | VARCHAR2 | 4 |  |  | Indicate if a connector is created from seeded open api or not. |
| SEEDED_CONNECTOR_TYPE | VARCHAR2 | 128 |  |  | The column stores the connector type if created from the seeded template. |
| MIGRATION_STATUS | VARCHAR2 | 128 |  |  | Indicate the spectra migration status. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_DI_CONNECTOR_DEF_U1 | Unique | Default | ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
