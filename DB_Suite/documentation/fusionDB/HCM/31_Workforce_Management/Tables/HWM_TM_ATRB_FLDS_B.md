# HWM_TM_ATRB_FLDS_B

A time attribute field represents information stored with a time record or time record group in the repository.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmatrbfldsb-27331.html#hwmtmatrbfldsb-27331](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmatrbfldsb-27331.html#hwmtmatrbfldsb-27331)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_ATRB_FLDS_B_PK | TM_ATRB_FLD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_ATRB_FLD_ID | NUMBER |  | 18 | Yes | primary key |
| STORAGE_TYPE | NUMBER |  | 9 |  | Indicates how the values for the time attribute can be retrieved, such as whether values are stored in the data dictionary or computed when the time attribute is transient. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| TCSMRS_ID | NUMBER |  | 18 |  | TCSMRS_ID |
| NAME | VARCHAR2 | 240 |  | Yes | NAME |
| CLASS | VARCHAR2 | 32 |  | Yes | CLASS |
| PARENT_TM_ATRB_FLD_ID | NUMBER |  | 18 |  | PARENT_TM_ATRB_FLD_ID |
| GLOBAL_TM_ATRB_FLD_ID | NUMBER |  | 18 |  | GLOBAL_TM_ATRB_FLD_ID |
| VALUE_LOCATION | VARCHAR2 | 32 |  |  | VALUE_LOCATION |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 64 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ALLOWED_SCOPE | VARCHAR2 | 32 |  |  | ALLOWED_SCOPE |
| MANDATORY_FOR_TCSMRS | VARCHAR2 | 20 |  |  | MANDATORY_FOR_TCSMRS |
| ATTRIBUTE_TYPE | VARCHAR2 | 20 |  |  | ATTRIBUTE_TYPE |
| ATTRIBUTE_GROUP | VARCHAR2 | 32 |  |  | Identifies the source which created the time attribute, such as seed data,
generation process, or customer created. |
| VALUE_SET_ID | NUMBER |  | 18 |  | VALUE_SET_ID |
| COMP_DISP_CODE | VARCHAR2 | 80 |  |  | This field is used to control display in UI. |
| BASE_UNIT | VARCHAR2 | 16 |  |  | String, code of a Unit of measure type. Two possible values are Hour or Day. The Base Unit  value is filled in the setup page of the custom attribute. |
| UOM_TYPE | VARCHAR2 | 32 |  |  | String, code of a Unit of measure type. |
| UOM_BEHAVIOR | VARCHAR2 | 32 |  |  | indicate the type of behavior (standard/Single currency, multi_value). |
| UOM_UNIT | VARCHAR2 | 32 |  |  | string, code of the base unit of the Unit of measure type. Unit to store the value of the attribute. |
| UOM_CODE | VARCHAR2 | 16 |  |  | short name/code to represent uom type. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_ATRB_FLDS_B_N1 | Non Unique | Default | ATTRIBUTE_CATEGORY, ENTERPRISE_ID |
| HWM_TM_ATRB_FLDS_B_N20 | Non Unique | Default | SGUID |
| HWM_TM_ATRB_FLDS_B_U1 | Unique | Default | TM_ATRB_FLD_ID, ORA_SEED_SET1 |
| HWM_TM_ATRB_FLDS_B_U11 | Unique | Default | TM_ATRB_FLD_ID, ORA_SEED_SET2 |
| HWM_TM_ATRB_FLDS_B_U2 | Unique | Default | NAME, ENTERPRISE_ID, ORA_SEED_SET1 |
| HWM_TM_ATRB_FLDS_B_U21 | Unique | Default | NAME, ENTERPRISE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
