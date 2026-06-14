# WLF_EXP_RESOURCES

Table to strore XAPI document resources

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfexpresources-14244.html#wlfexpresources-14244](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfexpresources-14244.html#wlfexpresources-14244)

## Primary Key

| Name | Columns |
|------|----------|
| wlf_exp_resources_PK | XAPI_RESOURCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| XAPI_RESOURCE_ID | NUMBER |  | 18 | Yes | Resource Id |
| XAPI_RESOURCE_TYPE | VARCHAR2 | 30 |  |  | Resource Type |
| XAPI_RESOURCE_NAME | VARCHAR2 | 255 |  |  | Resource Name |
| XAPI_ACTIVITY_ID | VARCHAR2 | 255 |  |  | Activity Id |
| XAPI_AGENT | VARCHAR2 | 1000 |  |  | Agent JSON |
| XAPI_REGISTRATION | NUMBER |  | 18 |  | Enrollment Task Id |
| XAPI_RESOURCE_DATA | VARCHAR2 | 4000 |  |  | Resource Data |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_EXP_RESOURCES_N1 | Non Unique | Default | XAPI_RESOURCE_TYPE, XAPI_RESOURCE_NAME, XAPI_AGENT |
| WLF_EXP_RESOURCES_N2 | Non Unique | Default | XAPI_RESOURCE_TYPE, XAPI_RESOURCE_NAME, XAPI_ACTIVITY_ID |
| WLF_EXP_RESOURCES_U1 | Unique | Default | XAPI_RESOURCE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
