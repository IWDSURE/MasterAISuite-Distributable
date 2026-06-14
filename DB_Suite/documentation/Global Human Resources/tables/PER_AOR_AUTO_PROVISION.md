# PER_AOR_AUTO_PROVISION

This table holds AOR records processed by auto provision ESS job which will be committed to PER_ASG_RESPONSIBILITIES table after a review is done.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraorautoprovision-6598.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraorautoprovision-6598.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_AOR_AUTO_PROVISION_PK | ASG_RESPONSIBILITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASG_RESPONSIBILITY_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| RESPONSIBILITY_NAME | VARCHAR2 | 240 |  | Yes | The name which describes this responsibility |
| RESPONSIBILITY_TYPE | VARCHAR2 | 30 |  | Yes | The responsibility type for which this record is holding the criteria |
| PERSON_ID | NUMBER |  | 18 | Yes | Person for whom this responsibility is recorded. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | The (parent) assignment which this is for |
| TEMPLATE_ID | NUMBER |  | 18 | Yes | The template for which this responsibility is created from |
| STATUS | VARCHAR2 | 30 |  | Yes | Indicates whether this responsibility is active or not.  Can use to find when a person has responsibilities that should be assigned to someone else prior to end-dating. |
| START_DATE | DATE |  |  | Yes | The start date of the responsibility |
| END_DATE | DATE |  |  |  | The end date of the responsibility |
| WORK_CONTACTS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to include this row in work contacts evaluation |
| ASSIGNMENT_CATEGORY | VARCHAR2 | 30 |  |  | The assignment types that fall under this responsibility |
| BARGAINING_UNIT | VARCHAR2 | 30 |  |  | The Union for which this responsibility applies |
| BENEFIT_GROUP_ID | NUMBER |  | 18 |  | The Benefit Group for which this responsibility applies |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | The business unit for which this responsibility applies |
| COUNTRY | VARCHAR2 | 30 |  |  | The country for which this responsibility applies. Implies all Locations within the specified country. |
| GRADE_ID | NUMBER |  | 18 |  | The Grade for which this responsibility applies |
| JOB_FAMILY_ID | NUMBER |  | 18 |  | Job Family For Areas of Responsibility Scope |
| JOB_ID | NUMBER |  | 18 |  | The Job for which this responsibility applies |
| JOB_FUNCTION_CODE | VARCHAR2 | 30 |  |  | Job Function for Areas of Responsibility Scope |
| LAST_NAME_START | VARCHAR2 | 30 |  |  | Starting letter for a range of Last Names |
| LAST_NAME_END | VARCHAR2 | 30 |  |  | Ending letter for a range of Last Names |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | The legal employer for which this responsibility applies |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | The Legislative Data Group for which this responsibility applies |
| LOCATION_ID | NUMBER |  | 18 |  | The Location for which this responsibility applies |
| ORGANIZATION_ID | NUMBER |  | 18 |  | The Department for which this responsibility applies |
| PAYROLL_ID | NUMBER |  | 18 |  | The payroll for which this responsibility applies |
| PAYROLL_STAT_UNIT_ID | NUMBER |  | 18 |  | The payroll statutory unit for which this responsibility applies |
| POSITION_ID | NUMBER |  | 18 |  | The Position for which this responsibility applies |
| RECRUITING_TYPE_CODE | VARCHAR2 | 30 |  |  | Recruiting Type for Areas of Responsibility |
| RECRUITING_LOC_HIERARCHY_ID | NUMBER |  | 18 |  | Recruiting Location Hierarchy for Areas of Responsibility scope |
| RECRUITING_ORG_HIERARCHY_ID | NUMBER |  | 18 |  | Recruiting Org Hierarchy for Areas of Responsibility |
| RECRUITING_ORG_TREE_CODE | VARCHAR2 | 1000 |  |  | Recruiting Org Hierarchy tree code |
| RECRUITING_ORG_TREE_VER | VARCHAR2 | 1000 |  |  | Recruiting Org Hierarchy tree version |
| TAX_REPORTING_UNIT_ID | NUMBER |  | 18 |  | The tax reporting unit for which this responsibility applies |
| HIERARCHY_TYPE | VARCHAR2 | 30 |  |  | The hierarchy type for which this responsibility applies. |
| ORGANIZATION_TREE_CODE | VARCHAR2 | 30 |  |  | Tree code of the organization tree |
| ORGANIZATION_HIERARCHY_ID | VARCHAR2 | 32 |  |  | The organization hierarchy for which this responsibility applies. |
| TOP_ORGANIZATION_ID | NUMBER |  | 18 |  | The top organization of the hierarchy for which this responsibility applies |
| POSITION_TREE_CODE | VARCHAR2 | 30 |  |  | The tree code of the position tree |
| POSITION_HIERARCHY_ID | VARCHAR2 | 32 |  |  | The position hierarchy for which this responsibility applies |
| TOP_POSITION_ID | NUMBER |  | 18 |  | The top position for which this responsibility applies |
| DEPARTMENT_TREE_CODE | VARCHAR2 | 30 |  |  | Tree code of the department tree |
| DEPARTMENT_HIERARCHY_ID | VARCHAR2 | 32 |  |  | The department hierarchy for which this responsibility applies. |
| TOP_DEPARTMENT_ID | NUMBER |  | 18 |  | The top department for which this responsibility applies |
| TOP_MANAGER_ID | NUMBER |  | 18 |  | The top manager for which this responsibility applies |
| HIERARCHY_LEVELS | NUMBER |  | 2 |  | The number of levels down  the hierarchy to walk. |
| INCLUDE_TOP_HIER_NODE | VARCHAR2 | 30 |  |  | Indicates whether the top node of the chosen hierarchy is included or not |
| DML_TYPE | VARCHAR2 | 30 |  | Yes | Indicates whether record is newly created, updated or inactivated. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| USAGE | VARCHAR2 | 4000 |  |  | Indicates the purpose for which the responsibility is used |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_AOR_AUTO_PROVISION_N1 | Non Unique | Default | TEMPLATE_ID |
| PER_AOR_AUTO_PROVISION_N2 | Non Unique | Default | DML_TYPE |
| PER_AOR_AUTO_PROVISION_PK | Unique | Default | ASG_RESPONSIBILITY_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
