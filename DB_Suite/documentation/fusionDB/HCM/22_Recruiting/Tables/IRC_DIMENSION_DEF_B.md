# IRC_DIMENSION_DEF_B

The IRC_DIMENSION_DEF_B will contain all the possible dimension configurations.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdimensiondefb-27443.html#ircdimensiondefb-27443](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdimensiondefb-27443.html#ircdimensiondefb-27443)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_DIMENSION_DEF_B_PK | DIMENSION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DIMENSION_ID | NUMBER |  | 18 | Yes | Primary key for the dimension definition. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SOURCE_URL_VALUE | VARCHAR2 | 2000 |  |  | Name of the source parameter.

The value that will be passed in the URL through the parameters. |
| SOURCE_MEDIUM_URL_VALUE | VARCHAR2 | 32 |  | Yes | Name of the source medium parameter.

The value that will be passed in the URL through the parameters. |
| SOURCE_MEDIUM | VARCHAR2 | 32 |  | Yes | The associated source medium lookup value corresponding to lookup type ORA_IRC_SOURCE_TRACKING_MEDIUM. |
| URL_HEADER_REGEX | VARCHAR2 | 2000 |  |  | Contains a string value representing a regex of the referrer header values. |
| PRIORITY | VARCHAR2 | 32 |  |  | Priority of the URL interpretation from the Source Tracking API.

    READ_PARAMETERS_FIRST
    READ_REFERRER_HEADER_FIRST |
| SEQUENCE | NUMBER |  | 16 |  | For UI, we need to display the sequence that the dimension will be displayed. For example,

manual add dimension may need to have those ordered. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_DIMENSION_DEF_B_N1 | Non Unique | FUSION_TS_SEED | SOURCE_MEDIUM_URL_VALUE |
| IRC_DIMENSION_DEF_B_PK | Unique | FUSION_TS_SEED | DIMENSION_ID, ORA_SEED_SET1 |
| IRC_DIMENSION_DEF_B_PK1 | Unique | FUSION_TS_SEED | DIMENSION_ID, ORA_SEED_SET2 |
| IRC_DIMENSION_DEF_B_U1 | Unique | FUSION_TS_SEED | SOURCE_URL_VALUE, SOURCE_MEDIUM_URL_VALUE, ORA_SEED_SET1 |
| IRC_DIMENSION_DEF_B_U11 | Unique | FUSION_TS_SEED | SOURCE_URL_VALUE, SOURCE_MEDIUM_URL_VALUE, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
