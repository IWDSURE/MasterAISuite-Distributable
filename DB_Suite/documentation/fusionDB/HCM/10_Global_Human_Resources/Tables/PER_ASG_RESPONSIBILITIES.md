# PER_ASG_RESPONSIBILITIES

This table holds the details of a person's areas of responsibility, defined by reference to existing workforce structures and other details.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perasgresponsibilities-9748.html#perasgresponsibilities-9748](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perasgresponsibilities-9748.html#perasgresponsibilities-9748)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ASG_RESPONSIBILITIES_PK | ASG_RESPONSIBILITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASG_RESPONSIBILITY_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| RESPONSIBILITY_NAME | VARCHAR2 | 240 |  |  | Responsibility Name |
| INCLUDE_TOP_HIER_NODE | VARCHAR2 | 30 |  |  | Indicates whether the top node of the chosen hierarchy is included or not |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | The (parent) assignment which this is for |
| PERSON_ID | NUMBER |  | 18 | Yes | Person for whom this responsibility is recorded. |
| START_DATE | DATE |  |  | Yes | The start date of the responsibility |
| END_DATE | DATE |  |  |  | The end date of the responsibility |
| RESPONSIBILITY_TYPE | VARCHAR2 | 30 |  | Yes | The responsibility type for which this record is holding the criteria |
| STATUS | VARCHAR2 | 30 |  | Yes | Indicates whether this responsibility is active or not.  Can use to find when a person has responsibilities that should be assigned to someone else prior to end-dating. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ORGANIZATION_TREE_CODE | VARCHAR2 | 30 |  |  | Tree code of the organization tree |
| ORGANIZATION_HIERARCHY_ID | VARCHAR2 | 32 |  |  | The organization hierarchy for which this responsibility applies. |
| TOP_ORGANIZATION_ID | NUMBER |  | 18 |  | The top organization of the hierarchy for which this responsibility applies |
| POSITION_TREE_CODE | VARCHAR2 | 30 |  |  | Tree code of the position tree |
| POSITION_HIERARCHY_ID | VARCHAR2 | 32 |  |  | The position hierarchy for which this responsibility applies |
| TOP_POSITION_ID | NUMBER |  | 18 |  | The top position for which this responsibility applies |
| DEPARTMENT_TREE_CODE | VARCHAR2 | 30 |  |  | Tree code of the department tree |
| DEPARTMENT_HIERARCHY_ID | VARCHAR2 | 32 |  |  | The department hierarchy for which this responsibility applies. |
| TOP_DEPARTMENT_ID | NUMBER |  | 18 |  | The top department for which this responsibility applies |
| TOP_MANAGER_ID | NUMBER |  | 18 |  | The top manager for which this responsibility applies |
| HIERARCHY_LEVELS | NUMBER |  | 2 |  | The number of levels down  the hierarchy to walk. |
| COUNTRY | VARCHAR2 | 30 |  |  | The country for which this responsibility applies. Implies all Locations within the specified country. |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | The business unit for which this responsibility applies |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | The legal employer for which this responsibility applies |
| ORGANIZATION_ID | NUMBER |  | 18 |  | The Department for which this responsibility applies |
| LOCATION_ID | NUMBER |  | 18 |  | The Location for which this responsibility applies |
| POSITION_ID | NUMBER |  | 18 |  | The Position for which this responsibility applies |
| JOB_ID | NUMBER |  | 18 |  | The Job for which this responsibility applies |
| GRADE_ID | NUMBER |  | 18 |  | The Grade for which this responsibility applies |
| BARGAINING_UNIT | VARCHAR2 | 30 |  |  | The Union for which this responsibility applies |
| ASSIGNMENT_CATEGORY | VARCHAR2 | 30 |  |  | The assignment types that fall under this responsibility |
| LAST_NAME_START | VARCHAR2 | 30 |  |  | Starting letter for a range of Last Names |
| LAST_NAME_END | VARCHAR2 | 30 |  |  | Ending letter for a range of Last Names |
| PAYROLL_ID | NUMBER |  | 18 |  | The payroll for which this responsibility applies |
| PAYROLL_STAT_UNIT_ID | NUMBER |  | 18 |  | The payroll statutory unit for which this responsibility applies |
| TAX_REPORTING_UNIT_ID | NUMBER |  | 18 |  | The tax reporting unit for which this responsibility applies |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | The Legislative Data Group for which this responsibility applies |
| BENEFIT_GROUP_ID | NUMBER |  | 18 |  | The Benefit Group for which this responsibility applies |
| JOB_FAMILY_ID | NUMBER |  | 18 |  | Job Family For Areas of Responsibility Scope |
| JOB_FUNCTION_CODE | VARCHAR2 | 30 |  |  | Job Function for Areas of Responsibility Scope |
| RECRUITING_TYPE_CODE | VARCHAR2 | 30 |  |  | Recruiting Type for Areas of Responsibility |
| RECRUITING_LOC_HIERARCHY_ID | NUMBER |  | 18 |  | Recruiting Location Hierarchy for Areas of Responsibility scope |
| RECRUITING_ORG_HIERARCHY_ID | NUMBER |  | 18 |  | Recruiting Org Hierarchy for Areas of Responsibility |
| RECRUITING_ORG_TREE_CODE | VARCHAR2 | 1000 |  |  | Stores the tree code |
| RECRUITING_ORG_TREE_VER | VARCHAR2 | 1000 |  |  | Stores the tree version |
| WORK_CONTACTS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to include this row in work contacts evaluation |
| TEMPLATE_ID | NUMBER |  | 18 |  | The template for which this responsibility is created from |
| HIERARCHY_TYPE | VARCHAR2 | 30 |  |  | The hierarchy type for which this responsibility applies. |
| AUTO_PROVISION_FLAG | VARCHAR2 | 30 |  |  | Indicates whether an AOR record is created manually or by auto provision |
| USAGE | VARCHAR2 | 4000 |  |  | Indicates the purpose for which the responsibility is used |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ASG_RESPONSIBILITIES_N19 | Non Unique | Default | RESPONSIBILITY_NAME, PERSON_ID |
| PER_ASG_RESPONSIBILITIES_N22 | Non Unique | Default | WORK_CONTACTS_FLAG, RESPONSIBILITY_TYPE, START_DATE, END_DATE, ENTERPRISE_ID |
| PER_ASG_RESPONSIBILITIES_PK | Unique | Default | ASG_RESPONSIBILITY_ID |
| PER_ASG_RESPONSIBILITY_FK1 | Non Unique | Default | ASSIGNMENT_ID |
| PER_ASG_RESPONSIBILITY_N1 | Non Unique | Default | START_DATE, RESPONSIBILITY_TYPE, END_DATE |
| PER_ASG_RESPONSIBILITY_N10 | Non Unique | Default | POSITION_ID |
| PER_ASG_RESPONSIBILITY_N11 | Non Unique | Default | JOB_ID |
| PER_ASG_RESPONSIBILITY_N12 | Non Unique | Default | GRADE_ID |
| PER_ASG_RESPONSIBILITY_N13 | Non Unique | Default | PAYROLL_ID |
| PER_ASG_RESPONSIBILITY_N14 | Non Unique | Default | PAYROLL_STAT_UNIT_ID |
| PER_ASG_RESPONSIBILITY_N15 | Non Unique | Default | TAX_REPORTING_UNIT_ID |
| PER_ASG_RESPONSIBILITY_N16 | Non Unique | Default | BENEFIT_GROUP_ID |
| PER_ASG_RESPONSIBILITY_N17 | Non Unique | Default | BARGAINING_UNIT |
| PER_ASG_RESPONSIBILITY_N18 | Non Unique | Default | LEGISLATIVE_DATA_GROUP_ID |
| PER_ASG_RESPONSIBILITY_N2 | Non Unique | Default | ORGANIZATION_HIERARCHY_ID, TOP_ORGANIZATION_ID, HIERARCHY_LEVELS |
| PER_ASG_RESPONSIBILITY_N21 | Non Unique | Default | PERSON_ID, RESPONSIBILITY_TYPE, START_DATE, END_DATE, ENTERPRISE_ID |
| PER_ASG_RESPONSIBILITY_N23 | Non Unique | Default | TEMPLATE_ID |
| PER_ASG_RESPONSIBILITY_N3 | Non Unique | Default | POSITION_HIERARCHY_ID, TOP_POSITION_ID, HIERARCHY_LEVELS |
| PER_ASG_RESPONSIBILITY_N4 | Non Unique | Default | TOP_MANAGER_ID, HIERARCHY_LEVELS |
| PER_ASG_RESPONSIBILITY_N5 | Non Unique | Default | BUSINESS_UNIT_ID |
| PER_ASG_RESPONSIBILITY_N6 | Non Unique | Default | LEGAL_ENTITY_ID |
| PER_ASG_RESPONSIBILITY_N7 | Non Unique | Default | COUNTRY |
| PER_ASG_RESPONSIBILITY_N8 | Non Unique | Default | ORGANIZATION_ID |
| PER_ASG_RESPONSIBILITY_N9 | Non Unique | Default | LOCATION_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
