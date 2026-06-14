# HNS_STAKEHOLDERS

HNS STAKEHOLDERS. This table stores stakeholders related data. Stakeholder is used across Incident/Action/Investigations.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsstakeholders-25030.html#hnsstakeholders-25030](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsstakeholders-25030.html#hnsstakeholders-25030)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_STAKEHOLDERS_PK | STAKEHOLDER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STAKEHOLDER_ID | NUMBER |  | 18 | Yes | STAKEHOLDER_ID unique identifier. Primary key for HNS_STAKEHOLDERS table. |
| TASK_ID | NUMBER |  | 18 | Yes | Task Assigned to the stakeholder. |
| EMPLOYEE_ID | NUMBER |  | 18 |  | Employee ID of the stakeholder . The column will be blank if the stakeholder is not an employee. |
| PERSON_ASSIGN_ID | NUMBER |  | 18 |  | Assignment ID of the stakeholder . The column will be blank if the stakeholder is not an employee. |
| TASK_TYPE_CODE | VARCHAR2 | 30 |  |  | Task Type identifier. Lookup to the Task Type FND lookup. |
| STAKEHOLDER_NAME | VARCHAR2 | 200 |  |  | The name of the person (Non employee) who is assigned as stakeholder. For Employee name will be blank. |
| STAKEHOLDER_EMAIL | VARCHAR2 | 200 |  |  | The email ID of the person (Non Employee) who is assigned as stakeholder. For Employee this will be blank. |
| STAKEHOLDER_TERRITORY_CODE | VARCHAR2 | 2 |  |  | STAKEHOLDER_TERRITORY_CODE column : Stakeholder (Non Employee) Territory code. For Employee this will be blank. |
| STAKEHOLDER_AREA_CODE | VARCHAR2 | 30 |  |  | STAKEHOLDER_AREA_CODE column : Stakeholder (Non Employee) phone area code. For Employee this will be blank. |
| STAKEHOLDER_PHONENO | VARCHAR2 | 18 |  |  | The phone number of the person (Non Employee) who is assigned as stakeholder. For Employee phone number will be blank. |
| STAKEHOLDER_PERSON_TYPE_CODE | VARCHAR2 | 30 |  |  | Stakeholder person type. Lookup from FND_LOOKUP EMP/NON EMP lookup. |
| STAKEHOLDER_CATEGORY_CODE | VARCHAR2 | 30 |  | Yes | Stakeholder Category. Lookup for Compliance/Executive/Manager Stakeholder category. |
| STAKEHOLDER_ORG_NAME | VARCHAR2 | 200 |  |  | SStakeholder Organization Name. In case stakeholder is non-employee, organization stakeholder belongs to. |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Flag to check whether is record is deleted. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_STAKEHOLDERS_N1 | Non Unique | Default | TASK_ID |
| HNS_STAKEHOLDERS_UK1 | Unique | Default | STAKEHOLDER_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
