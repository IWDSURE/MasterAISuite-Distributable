# PER_AOR_TEMPLATE_DETAILS

This table holds the element details of a responsibility template

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraortemplatedetails-9940.html#peraortemplatedetails-9940](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraortemplatedetails-9940.html#peraortemplatedetails-9940)

## Primary Key

| Name | Columns |
|------|----------|
| PER_AOR_TEMPLATE_DETAILS_PK | TEMPLATE_DETAILS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEMPLATE_DETAILS_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| TEMPLATE_ID | NUMBER |  | 18 | Yes | Foreign key to template table PER_AOR_TEMPLATE |
| ATTRIBUTE_NAME | VARCHAR2 | 30 |  | Yes | The name of the attribute that is used to define areas of responsibilities |
| DISPLAY_SEQUENCE | NUMBER |  | 3 |  | The ui field display order when creating an area of responsibility from a template |
| REQUIRED_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to show this attribute as required or not on creating areas of responsibility ui |
| REQUIRED_FLAG_NUMBER | VARCHAR2 | 30 |  |  | Indicates whether to show this attribute as required or not on creating areas of responsibility ui |
| REQUIRED_FLAG_2 | VARCHAR2 | 30 |  |  | Indicates whether to show this attribute as required or not on creating areas of responsibility ui |
| REQUIRED_FLAG_3 | VARCHAR2 | 30 |  |  | Indicates whether to show this attribute as required or not on creating areas of responsibility ui |
| REQUIRED_FLAG_4 | VARCHAR2 | 30 |  |  | Indicates whether to show this attribute as required or not on creating areas of responsibility ui |
| REQUIRED_FLAG_5 | VARCHAR2 | 30 |  |  | Indicates whether to show this attribute as required or not on creating areas of responsibility ui |
| REQUIRED_FLAG_6 | VARCHAR2 | 30 |  |  | Indicates whether to show this attribute as required or not on creating areas of responsibility ui |
| REQUIRED_FLAG_7 | VARCHAR2 | 30 |  |  | Indicates whether to show this attribute as required or not on creating areas of responsibility ui |
| DEFAULT_VALUE | VARCHAR2 | 1000 |  |  | Default value for this attribute on creating areas of responsibility ui |
| DEFAULT_VALUE_NUMBER | NUMBER |  | 18 |  | Default numeric value for this attribute on creating areas of responsibility template |
| DEFAULT_VALUE_2 | VARCHAR2 | 1000 |  |  | Default value for this attribute on creating areas of responsibility ui |
| DEFAULT_VALUE_3 | VARCHAR2 | 1000 |  |  | Default value for this attribute on creating areas of responsibility ui |
| DEFAULT_VALUE_4 | VARCHAR2 | 1000 |  |  | Default value for this attribute on creating areas of responsibility ui |
| DEFAULT_VALUE_5 | VARCHAR2 | 1000 |  |  | Default value for this attribute on creating areas of responsibility ui |
| DEFAULT_VALUE_6 | VARCHAR2 | 1000 |  |  | Default value for this attribute on creating areas of responsibility ui |
| DEFAULT_VALUE_7 | VARCHAR2 | 1000 |  |  | Default value for this attribute on creating areas of responsibility ui |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_AOR_TEMPLATE_DETAILS_N1 | Non Unique | Default | ATTRIBUTE_NAME |
| PER_AOR_TEMPLATE_DETAILS_PK | Unique | Default | TEMPLATE_DETAILS_ID |
| PER_AOR_TEMPLATE_DETAILS_U1 | Unique | Default | TEMPLATE_ID, ATTRIBUTE_NAME |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
