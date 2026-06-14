# HRC_TXN_CONDITIONS_LOVMETADATA

HRC_TXN_CONDITIONS_LOVMETADATA contains all required information to generate a SQL query from a particular View Object, with a provision for applying View Criterias and Bind variables to it. This generated query drives the LOV that is displayed in the Condition Builder component. The product teams would provide the View Object name from where we can extract the query. Further they can provide View Criterias and Bind variable details to be applied on the View Object before the query is generated. Finally they provide names of two columns of the View Object's query that are displayed in the UI's LOV field. Please refer to individual columns for more informaiton.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnconditionslovmetadata-19824.html#hrctxnconditionslovmetadata-19824](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnconditionslovmetadata-19824.html#hrctxnconditionslovmetadata-19824)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_CON_LOVMET_PK | LOV_METADATA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOV_METADATA_ID | NUMBER |  | 18 | Yes | Primary Key and unique identifier required by Seed data framework. |
| SOURCE_VIEW_OBJECT_NAME | VARCHAR2 | 300 |  | Yes | This column contains the fully qualified package path name of the View Object which is the source of the LOV query. This View Object is loaded and query form it is extracted to present the LOV in the Condition Builder UI. |
| LOV_CODE | VARCHAR2 | 30 |  | Yes | This is the column name that is extracted from the VO query and is displayed in the UI. This column would act as a primary identifier to assist the user in uniquely identifying an item in the LOV. So it is adviced to the product teams to enter a cloumn name which has Unique property set. |
| LOV_MEANING | VARCHAR2 | 30 |  | Yes | This is the column name that is extracted from the VO query and is displayed in the UI along with the LOV_CODE column. When user selects a particular item in the UI, the value from this column would go into the condition expression. So when you refer the metadata from this table to a CONDITION_OPERAND column in the HRC_TXN_CONDITIONS_LOVUSAGE table it implies that value from this column would go into the expression whose other operand is CONDITION_OPERAND. |
| VIEW_OBJECT_CRITERIA_NAME_1 | VARCHAR2 | 100 |  |  | Name of the view criteria that has to be applied to the view object identified by SOURCE_VIEW_OBJECT_NAME before extracting the LOV query from it. By default the different view criterias are joined by AND. Product teams have a provision of entering up to five view  criterias. If there is a requirement for more, it is adviced to create new view criterias to club some of the available view criterias. |
| VIEW_OBJECT_CRITERIA_NAME_2 | VARCHAR2 | 100 |  |  | Name of the view criteria that has to be applied to the view object identified by SOURCE_VIEW_OBJECT_NAME before extracting the LOV query from it. |
| VIEW_OBJECT_CRITERIA_NAME_3 | VARCHAR2 | 100 |  |  | Name of the view criteria that has to be applied to the view object identified by SOURCE_VIEW_OBJECT_NAME before extracting the LOV query from it. |
| VIEW_OBJECT_CRITERIA_NAME_4 | VARCHAR2 | 100 |  |  | Name of the view criteria that has to be applied to the view object identified by SOURCE_VIEW_OBJECT_NAME before extracting the LOV query from it. |
| VIEW_OBJECT_CRITERIA_NAME_5 | VARCHAR2 | 100 |  |  | Name of the view criteria that has to be applied to the view object identified by SOURCE_VIEW_OBJECT_NAME before extracting the LOV query from it. |
| VIEW_OBJECT_BIND_VAR_NAME_1 | VARCHAR2 | 100 |  |  | This column contains the name of the bind variable that would be present in the View Object's extracted query. So if the query contains any bind variables, the details of the variable name and value are to be populated in the VIEW_OBJECT_BIND_VAR_NAME_X and VIEW_OBJECT_BIND_VAR_VAL_X columns respectively. There is a provision to enter up to 10 such pairs. As the LOV query generation is purely based on design time attributes from the metadata table the query for a particular metadata cannot be modified dynamically at runtime. So we expect a corresponding static value in the BIND_VAR_VAL_X columns. In future this can be enhanced to have a dynamic value. |
| VIEW_OBJECT_BIND_VAR_VAL_1 | VARCHAR2 | 160 |  |  | This column contains the value  of the bind variable that would be present in the View Object's extracted query. So if the query contains any bind variables, the details of the variable name and value are to be populated in the VIEW_OBJECT_BIND_VAR_NAME_X and VIEW_OBJECT_BIND_VAR_VAL_X columns respectively. There is a provision to enter up to 10 such pairs. As the LOV query generation is purely based on design time attributes from the metadata table the query for a particular metadata cannot be modified dynamically at runtime. So we expect a corresponding static value in the BIND_VAR_VAL_X columns. In future this can be enhanced to have a dynamic value. |
| VIEW_OBJECT_BIND_VAR_NAME_2 | VARCHAR2 | 100 |  |  | This column contains the name of the bind variable that would be present in the View Object's extracted query. |
| VIEW_OBJECT_BIND_VAR_VAL_2 | VARCHAR2 | 160 |  |  | This column contains the value  of the bind variable that would be present in the View Object's extracted query. |
| VIEW_OBJECT_BIND_VAR_NAME_3 | VARCHAR2 | 100 |  |  | This column contains the name of the bind variable that would be present in the View Object's extracted query. |
| VIEW_OBJECT_BIND_VAR_VAL_3 | VARCHAR2 | 160 |  |  | This column contains the value  of the bind variable that would be present in the View Object's extracted query. |
| VIEW_OBJECT_BIND_VAR_NAME_4 | VARCHAR2 | 100 |  |  | This column contains the name of the bind variable that would be present in the View Object's extracted query. |
| VIEW_OBJECT_BIND_VAR_VAL_4 | VARCHAR2 | 160 |  |  | This column contains the value  of the bind variable that would be present in the View Object's extracted query. |
| VIEW_OBJECT_BIND_VAR_NAME_5 | VARCHAR2 | 100 |  |  | This column contains the name of the bind variable that would be present in the View Object's extracted query. |
| VIEW_OBJECT_BIND_VAR_VAL_5 | VARCHAR2 | 160 |  |  | This column contains the value  of the bind variable that would be present in the View Object's extracted query. |
| VIEW_OBJECT_BIND_VAR_NAME_6 | VARCHAR2 | 100 |  |  | This column contains the name of the bind variable that would be present in the View Object's extracted query. |
| VIEW_OBJECT_BIND_VAR_VAL_6 | VARCHAR2 | 160 |  |  | This column contains the value  of the bind variable that would be present in the View Object's extracted query. |
| VIEW_OBJECT_BIND_VAR_NAME_7 | VARCHAR2 | 100 |  |  | This column contains the name of the bind variable that would be present in the View Object's extracted query. |
| VIEW_OBJECT_BIND_VAR_VAL_7 | VARCHAR2 | 160 |  |  | This column contains the value  of the bind variable that would be present in the View Object's extracted query. |
| VIEW_OBJECT_BIND_VAR_NAME_8 | VARCHAR2 | 100 |  |  | This column contains the name of the bind variable that would be present in the View Object's extracted query. |
| VIEW_OBJECT_BIND_VAR_VAL_8 | VARCHAR2 | 160 |  |  | This column contains the value  of the bind variable that would be present in the View Object's extracted query. |
| VIEW_OBJECT_BIND_VAR_NAME_9 | VARCHAR2 | 100 |  |  | This column contains the name of the bind variable that would be present in the View Object's extracted query. |
| VIEW_OBJECT_BIND_VAR_VAL_9 | VARCHAR2 | 160 |  |  | This column contains the value  of the bind variable that would be present in the View Object's extracted query. |
| VIEW_OBJECT_BIND_VAR_NAME_0 | VARCHAR2 | 100 |  |  | This column contains the name of the bind variable that would be present in the View Object's extracted query. |
| VIEW_OBJECT_BIND_VAR_VAL_0 | VARCHAR2 | 160 |  |  | This column contains the value  of the bind variable that would be present in the View Object's extracted query. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identify the ENTERPRISE  to which the composite belongs.Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_CONDITIONS_LOVMET_N20 | Non Unique | Default | SGUID |
| HRC_TXN_CON_LOVMETADATA_PK | Unique | Default | LOV_METADATA_ID, ORA_SEED_SET1 |
| HRC_TXN_CON_LOVMETADATA_PK1 | Unique | Default | LOV_METADATA_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
