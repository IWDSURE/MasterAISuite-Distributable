# BEN_VALD_RPT_TYP

BEN_VALD_RPT_TYP stores the reporting rules that are employed to validate a program or plan not in program by the plan design validation tool.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvaldrpttyp-28764.html#benvaldrpttyp-28764](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvaldrpttyp-28764.html#benvaldrpttyp-28764)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_VALD_RPT_TYP_PK | VALD_RPT_TYP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VALD_RPT_TYP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| RPT_CD | VARCHAR2 | 30 |  | Yes | Reporting code type. |
| MEANING | VARCHAR2 | 100 |  |  | Reporting code meaning. |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | Reporting code description. |
| PGM_RQD_FLAG | VARCHAR2 | 30 |  |  | Program required flag. |
| PTIP_RQD_FLAG | VARCHAR2 | 30 |  |  | Plan type in program required flag. |
| PL_TYP_RQD_FLAG | VARCHAR2 | 30 |  |  | Plan type required flag. |
| PLIP_RQD_FLAG | VARCHAR2 | 30 |  |  | Plan in program required flag. |
| PL_RQD_FLAG | VARCHAR2 | 30 |  |  | Plan required flag. |
| PLNIP_RQD_FLAG | VARCHAR2 | 30 |  |  | Plan not in program required flag. |
| OIPL_RQD_FLAG | VARCHAR2 | 30 |  |  | Option in plan required flag. |
| OPT_RQD_FLAG | VARCHAR2 | 30 |  |  | Option required flag. |
| COMP_LVL_CD | VARCHAR2 | 30 |  |  | Indicates the compensation level code. |
| SEQ_NUM | NUMBER |  | 18 |  | Sequence number. |
| ENABLED_FLAG | VARCHAR2 | 30 |  |  | Enabled flag. |
| VALD_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Validation attribute1 to store any additional varchar information. |
| VALD_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Validation attribute2 to store any additional varchar2 information. |
| VALD_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Validation attribute3 to store additional varchar information. |
| VALD_NUMBER1 | NUMBER |  |  |  | Validation Number1 to store additional number type information. |
| VALD_NUMBER2 | NUMBER |  |  |  | Validation Number2 to store additional number type information. |
| VALD_NUMBER3 | NUMBER |  |  |  | Validation Number3 to store additional number type information. |
| VALD_DATE1 | DATE |  |  |  | Validation Date1 to store additional date type information. |
| VALD_DATE2 | DATE |  |  |  | Validation Date2 to store additional date type information. |
| DISPLAY_CD | VARCHAR2 | 30 |  |  | Display code. |
| COLOR_CD | VARCHAR2 | 30 |  |  | Color code. A hex code which identifies the color to be used while rendering the plan design validation UI. |
| DTLS_FLAG | VARCHAR2 | 30 |  |  | Details flag. Determines if additional drill down data has to be captured for the rule. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_VALD_RPT_TYP_PK | Unique | Default | VALD_RPT_TYP_ID, ORA_SEED_SET1 |
| BEN_VALD_RPT_TYP_PK1 | Unique | Default | VALD_RPT_TYP_ID, ORA_SEED_SET2 |
| BEN_VALD_RPT_TYP_U2 | Unique | Default | RPT_CD, ORA_SEED_SET1 |
| BEN_VALD_RPT_TYP_U21 | Unique | Default | RPT_CD, ORA_SEED_SET2 |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
