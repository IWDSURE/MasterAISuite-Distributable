# PER_AOR_AUTOPROVISION_GT

Global Temporary table to store assignment details matching the Template criteria for AOR Autoprovisioning.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraorautoprovisiongt-8934.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraorautoprovisiongt-8934.html)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | This Column stores the AssignmentId. |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | This Column stores the LegalEntityId |
| TOP_DEPARTMENT_ID | NUMBER |  | 18 |  | This Column stores the TopDepartmentId |
| TOP_ORGANIZATION_ID | NUMBER |  | 18 |  | This Column stores the TopOrganizationId |
| LOCATION_ID | NUMBER |  | 18 |  | This Column stores the LocationId |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | This Column stores the BunisessUnitid |
| ORGANIZATION_ID | NUMBER |  | 18 |  | This Column stores the OrganizationId |
| PERSON_ID | NUMBER |  | 18 | Yes | This Column stores the PersonId. |
| ASSIGNMENT_NUMBER | VARCHAR2 | 50 |  | Yes | This Column stores the business title of the Assignment. |
| TEMPLATE_ID | NUMBER |  | 18 | Yes | This Column store the TemplateId. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | This Column stores the EnterpriseId. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
