# FF_ROUTE_TO_DESCR_FLEXS

Setup table for database item creation for descriptive flexfields.

## Details

**Schema:** FUSION

**Object owner:** FF

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffroutetodescrflexs-30902.html#ffroutetodescrflexs-30902](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffroutetodescrflexs-30902.html#ffroutetodescrflexs-30902)

## Primary Key

| Name | Columns |
|------|----------|
| FF_ROUTE_TO_DESCR_FLEXS_PK | ROUTE_TO_DESCR_FLEXS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROUTE_TO_DESCR_FLEXS_ID | NUMBER |  | 18 | Yes | Unique identifier. |
| APPLICATION_ID | NUMBER |  | 18 | Yes | Foreign key to FND_APPLICATION. |
| DESCRIPTIVE_FLEXFIELD_CODE | VARCHAR2 | 40 |  | Yes | Descriptive flexfield code. |
| ROUTE_NAME | VARCHAR2 | 80 |  | Yes | Identifier for the database item route. |
| FLEX_SHORT_NAME | VARCHAR2 | 30 |  |  | Flexfield short name. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| DESCRIPTIVE_FLEX_CONTEXT_CODE | VARCHAR2 | 80 |  |  | Descriptive flexfield context code. |
| FLEX_MULTI_ROW_FLAG | VARCHAR2 | 30 |  |  | Identifies whether the given Fast Formula Route support multi row or not. |
| ADDITIONALCOL1 | VARCHAR2 | 80 |  |  | Name of the additional non flex column to generate the database item. |
| ADDITIONALCOL2 | VARCHAR2 | 80 |  |  | Name of the additional non flex column to generate the database item. |
| ADDITIONALCOL3 | VARCHAR2 | 80 |  |  | Name of the additional non flex column to generate the database item. |
| ADDITIONALCOL4 | VARCHAR2 | 80 |  |  | Name of the additional non flex column to generate the database item. |
| ADDITIONALCOL5 | VARCHAR2 | 80 |  |  | Name of the additional non flex column to generate the database item. |
| ADDITIONALCOL6 | VARCHAR2 | 80 |  |  | Name of the additional non flex column to generate the database item. |
| ADDITIONALCOL7 | VARCHAR2 | 80 |  |  | Name of the additional non flex column to generate the database item. |
| ADDITIONALCOL8 | VARCHAR2 | 80 |  |  | Name of the additional non flex column to generate the database item. |
| ADDITIONALCOL9 | VARCHAR2 | 80 |  |  | Name of the additional non flex column to generate the database item. |
| ADDITIONALCOL10 | VARCHAR2 | 80 |  |  | Name of the additional non flex column to generate the database item. |
| COLDATATYPE1 | VARCHAR2 | 80 |  |  | Data type of the corresponding additional column. |
| COLDATATYPE2 | VARCHAR2 | 80 |  |  | Data type of the corresponding additional column. |
| COLDATATYPE3 | VARCHAR2 | 80 |  |  | Data type of the corresponding additional column. |
| COLDATATYPE4 | VARCHAR2 | 80 |  |  | Data type of the corresponding additional column. |
| COLDATATYPE5 | VARCHAR2 | 80 |  |  | Data type of the corresponding additional column. |
| COLDATATYPE6 | VARCHAR2 | 80 |  |  | Data type of the corresponding additional column. |
| COLDATATYPE7 | VARCHAR2 | 80 |  |  | Data type of the corresponding additional column. |
| COLDATATYPE8 | VARCHAR2 | 80 |  |  | Data type of the corresponding additional column. |
| COLDATATYPE9 | VARCHAR2 | 80 |  |  | Data type of the corresponding additional column. |
| COLDATATYPE10 | VARCHAR2 | 80 |  |  | Data type of the corresponding additional column. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| RECORD_VERSION | NUMBER |  | 18 |  | This number should be changed every time that the row is updated. This would enable the seed data to get applied whenever any record values are changed. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FF_ROUTE_TO_DESCR_FLEXS_N1 | Non Unique | Default | DESCRIPTIVE_FLEXFIELD_CODE, DESCRIPTIVE_FLEX_CONTEXT_CODE |
| FF_ROUTE_TO_DESCR_FLEXS_N20 | Non Unique | Default | SGUID |
| FF_ROUTE_TO_DESCR_FLEXS_U1 | Unique | Default | ROUTE_TO_DESCR_FLEXS_ID, ORA_SEED_SET1 |
| FF_ROUTE_TO_DESCR_FLEXS_U11 | Unique | Default | ROUTE_TO_DESCR_FLEXS_ID, ORA_SEED_SET2 |

---

[← Back to Index](../9_Fast_Formula_Tables_Index.md)
