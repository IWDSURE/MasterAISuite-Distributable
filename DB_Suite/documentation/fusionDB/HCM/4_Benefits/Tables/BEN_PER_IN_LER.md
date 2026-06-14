# BEN_PER_IN_LER

BEN_PER_IN_LER identifies all life events for a person, including identifying which life event, if any, is currently in progress for the specified person.  This table differs from BEN_PTNL_LER_FOR_PER  in that it identifies persons whose detected life events  have been scrubbed by the manage life event processes and classified as legitimate or, through user input, have been created.  It should be noted that persons in open and administrative enrollments are also maintained on this table.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benperinler-7781.html#benperinler-7781](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benperinler-7781.html#benperinler-7781)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PER_IN_LER_PK | PER_IN_LER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PER_IN_LER_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | This column holds BENEFIT_RELATION_ID |  |
| PER_IN_LER_STAT_CD | VARCHAR2 | 30 |  |  | Person in life event reason status. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| LF_EVT_OCRD_DT | DATE |  |  | Yes | This column holds Life event occurred date. |  |
| PROCD_DT | DATE |  |  |  | This column holds Processed date. |  |
| LER_ID | NUMBER |  | 18 | Yes | This column holds Foreign Key to BEN_LER_F. |  |
| STRTD_DT | DATE |  |  |  | This column holds Started date. |  |
| VOIDD_DT | DATE |  |  |  | This column holds Voided date value. |  |
| PERSON_ID | NUMBER |  | 18 | Yes | This column holds Foreign Key to PER_PEOPLE_F. |  |
| BCKT_DT | DATE |  |  |  | This column holds Backed out date. |  |
| CLSD_DT | DATE |  |  |  | This column holds Closed date value. |  |
| NTFN_DT | DATE |  |  |  | This column holds Notification date. |  |
| PTNL_LER_FOR_PER_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PTNL_LER_FOR_PER. |  |
| PIL_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| PIL_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Life Event Attributes (BEN_PER_IN_LER_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |  |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |  |
| PROGRAM_APP_NAME | VARCHAR2 | 30 |  |  | This column holds PROGRAM_APP_NAME |  |
| PROGRAM_NAME | VARCHAR2 | 30 |  |  | This column holds PROGRAM_NAME value |  |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row). |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| PRVS_STAT_CD | VARCHAR2 | 30 |  |  | This column holds Previous life event status. |  |
| BCKT_PER_IN_LER_ID | NUMBER |  | 18 |  | Foreign key to BEN_BCKT_PER_IN_LER. |  |
| TRGR_TABLE_PK_ID | NUMBER |  | 18 |  | This column holds Triggering Table primary key. |  |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment with life event associated. |  |
| GROUP_PL_ID | NUMBER |  | 18 |  | This column holds Group plan id. |  |
| LER_TYPE_CD | VARCHAR2 | 30 |  |  | This column holds LER_TYPE_CD value |  |
| PROD_CD | VARCHAR2 | 30 |  |  | This column holds PROD_CD value |  |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | This column holds LEGAL_ENTITY_ID |  |
| COMMENTS | VARCHAR2 | 4000 |  |  | This column holds additional COMMENTS. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PER_IN_LER_FK2 | Non Unique | Default | BCKT_PER_IN_LER_ID |
| BEN_PER_IN_LER_FK4 | Non Unique | Default | GROUP_PL_ID |
| BEN_PER_IN_LER_FK5 | Non Unique | Default | ASSIGNMENT_ID |
| BEN_PER_IN_LER_FK7 | Non Unique | Default | PTNL_LER_FOR_PER_ID |
| BEN_PER_IN_LER_FK8 | Non Unique | Default | BENEFIT_RELATION_ID |
| BEN_PER_IN_LER_N1 | Non Unique | Default | LER_ID |
| BEN_PER_IN_LER_N2 | Non Unique | Default | PERSON_ID, LF_EVT_OCRD_DT, PER_IN_LER_STAT_CD |
| BEN_PER_IN_LER_N3 | Non Unique | Default | PER_IN_LER_STAT_CD, LF_EVT_OCRD_DT |
| BEN_PER_IN_LER_N4 | Non Unique | Default | REQUEST_ID, PER_IN_LER_STAT_CD |
| BEN_PER_IN_LER_PK1 | Unique | Default | PER_IN_LER_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
