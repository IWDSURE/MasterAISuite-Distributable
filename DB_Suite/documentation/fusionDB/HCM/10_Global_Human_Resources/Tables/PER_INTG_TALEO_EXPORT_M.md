# PER_INTG_TALEO_EXPORT_M

This table holds information about the person records that needs to be exported as part of integration.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perintgtaleoexportm-30969.html#perintgtaleoexportm-30969](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perintgtaleoexportm-30969.html#perintgtaleoexportm-30969)

## Primary Key

| Name | Columns |
|------|----------|
| PER_INTEG_TALEO_EXPORT_M_PK | TALEO_EXPORT_ID, EFFECTIVE_LATEST_CHANGE, EFFECTIVE_SEQUENCE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TALEO_EXPORT_ID | NUMBER |  | 18 | Yes | This is a system generated primary key. Surrogate key. |
| PERSON_ID | NUMBER |  | 18 |  | System generated unique identifier for a person. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. |
| DATE_OF_BIRTH | DATE |  |  |  | Date of birth of the person for export. |
| PERSON_NUMBER | VARCHAR2 | 30 |  |  | Number assigned to the person, to identify the person uniquely in any context, not dependent on being an employee, contingent worker, etc. |
| PERSON_ID1 | NUMBER |  | 18 |  | System generated unique identifier for a person. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| FIRST_NAME | VARCHAR2 | 150 |  |  | First name of the person. This value is copied from per_person_names_f. |
| PERSON_NAME_ID | NUMBER |  | 18 |  | System generated identifier for person name. |
| EFFECTIVE_START_DATE1 | DATE |  |  |  | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE1 | DATE |  |  |  | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| NAME_VERSION_NUMBER | NUMBER |  | 9 |  | Object version number from person name. |
| MIDDLE_NAMES | VARCHAR2 | 80 |  |  | Middle names of the person. This value is copied from per_person_names_f table. |
| LAST_NAME | VARCHAR2 | 150 |  |  | Last name of the person. This value is copied from per_person_names_f table. |
| EMAIL_ADDRESS | VARCHAR2 | 240 |  |  | Email address of the person. This value is copied from per_email_addresses table. |
| EMAIL_ADDRESS_ID | NUMBER |  | 18 |  | Email address identifier of the person. |
| EMAIL_VERSION_NUMBER | NUMBER |  | 9 |  | Object version number from email address. |
| DISPLAY_PHONE_NUMBER | VARCHAR2 | 4000 |  |  | Display phone number of the person. |
| PHONE_ID | NUMBER |  | 18 |  | Phone identifier of the person. |
| EXTENSION | VARCHAR2 | 60 |  |  | Extension phone number of the person. |
| NATIONAL_IDENTIFIER_NUMBER | VARCHAR2 | 30 |  |  | National identifier number of the person. |
| NATIONAL_IDENTIFIER_ID | NUMBER |  | 18 |  | National identifier of the person. |
| NID_VERSION_NUMBER | NUMBER |  | 9 |  | Object version number of national identifier. |
| USERNAME | VARCHAR2 | 100 |  |  | The latest principal username of the user |
| USER_ID | NUMBER |  | 18 |  | System generated unique identifier for the user record of a person. |
| USER_VERSION_NUMBER | NUMBER |  | 9 |  | Object version number from per_users table for the person. |
| USER_ACCOUNT_ACTIVE_FLAG | VARCHAR2 | 2 |  |  | Indicates if the person has an active user account. |
| NAME | VARCHAR2 | 240 |  |  | Denotes the translated name for the Organization Unit. |
| ORGANIZATION_ID | NUMBER |  | 18 |  | System generated unique identifier for an organization. |
| EFFECTIVE_START_DATE4 | DATE |  |  |  | Effective start date of the organization. |
| EFFECTIVE_END_DATE4 | DATE |  |  |  | Effective end date of the organization. |
| DEPT_VERSION_NUMBER | NUMBER |  | 9 |  | Object version number of the organization. |
| ORGANIZATION_CODE | VARCHAR2 | 500 |  |  | Code of the organization. This value will be unique for an organization. |
| ORGANIZATION_ID1 | NUMBER |  | 18 |  | System generated identifier for the organization. |
| EFFECTIVE_START_DATE5 | DATE |  |  |  | Effective start date of the organization. |
| EFFECTIVE_END_DATE5 | DATE |  |  |  | Effective end date of the organization. |
| CLASSIFICATION_CODE | VARCHAR2 | 40 |  |  | Classification code of the organization. |
| ORG_VERSION_NUMBER | NUMBER |  | 9 |  | Object version number of the organization. |
| NAME1 | VARCHAR2 | 240 |  |  | Translated name of the job according to session langauge. |
| JOB_ID | NUMBER |  | 18 |  | System generated identifier of the job. |
| EFFECTIVE_START_DATE6 | DATE |  |  |  | Effective start date of the job. |
| EFFECTIVE_END_DATE6 | DATE |  |  |  | Effective end date of the job of the person for export. |
| JOB_VERSION_NUMBER | NUMBER |  | 9 |  | Object version number of the job. |
| USERNAME1 | VARCHAR2 | 100 |  |  | The latest principal username of the manager. |
| USER_ID1 | NUMBER |  | 18 |  | System generated user identifier for the manager. |
| MGR_VERSION_NUMBER | NUMBER |  | 9 |  | Object version number of the user record of manager. |
| ADDRESS_LINE11 | VARCHAR2 | 240 |  |  | Address Line 1 of the person's home address. |
| ADDRESS_LINE21 | VARCHAR2 | 240 |  |  | Address Line 2 of the person's home address. |
| ADDRESS_LINE31 | VARCHAR2 | 240 |  |  | Address Line 3 of the person's home address. |
| ADDRESS_LINE41 | VARCHAR2 | 240 |  |  | Address Line 4 of the person's home address. |
| POSTAL_CODE1 | VARCHAR2 | 30 |  |  | Postal code of the person's home address. |
| REGION_11 | VARCHAR2 | 120 |  |  | Region 1 of the person's home address. |
| TIMEZONE_CODE1 | VARCHAR2 | 50 |  |  | Timezone code of the person's home address |
| COUNTRY1 | VARCHAR2 | 60 |  |  | Country of the person's home address. |
| ADDRESS_ID | NUMBER |  | 18 |  | System generated identifier of the person's home address. |
| EFFECTIVE_START_DATE3 | DATE |  |  |  | Effective start date of the person's home address. |
| EFFECTIVE_END_DATE3 | DATE |  |  |  | Effective end date of the person's home address. |
| CORRESPONDENCE_LANGUAGE | VARCHAR2 | 60 |  |  | Lookup identifies language to use for this communication. |
| ADDRESS_LINE_1 | VARCHAR2 | 240 |  |  | Address line 1 of the location. |
| ADDRESS_LINE_2 | VARCHAR2 | 240 |  |  | Address line 2 of the location. |
| ADDRESS_LINE_3 | VARCHAR2 | 240 |  |  | Address line 3 of the location. |
| ADDRESS_LINE_4 | VARCHAR2 | 240 |  |  | Address line 4 of the location. |
| COUNTRY | VARCHAR2 | 60 |  |  | Country of the location of the person for export. |
| LOCATION_CODE | VARCHAR2 | 60 |  |  | Code of the location of the person for export. |
| LOCATION_NAME | VARCHAR2 | 240 |  |  | Name of the location of the person for export. |
| POSTAL_CODE | VARCHAR2 | 30 |  |  | Postal code of the location's address. |
| REGION_1 | VARCHAR2 | 120 |  |  | Primary region in which the address is located. |
| TIMEZONE_CODE | VARCHAR2 | 50 |  |  | Specifies the standard timezone boundary under which the address falls. |
| TOWN_OR_CITY | VARCHAR2 | 60 |  |  | Name of town or city of the location. |
| LOCATION_ID | NUMBER |  | 18 |  | System generated identifier of the location. |
| EFFECTIVE_START_DATE2 | DATE |  |  |  | Effective start date of the location. |
| EFFECTIVE_END_DATE2 | DATE |  |  |  | Effective end date of the location. |
| USER_TYPE_COLLECTION | VARCHAR2 | 10 |  |  | User type collection value for the export process. |
| USER_TYPE_1 | VARCHAR2 | 240 |  |  | User type for the export process. |
| JOB_ROLE_CODE | VARCHAR2 | 20 |  |  | Job role code for the export process. |
| CONFIRM_PROFILE | VARCHAR2 | 20 |  |  | Confirm profile value for the export process. |
| INTERNAL_CANDIDATE | VARCHAR2 | 20 |  |  | Indicates if the candidate is internal. |
| CANDIDATE_PROFILE_LANGUAGE | VARCHAR2 | 10 |  |  | Profile language of the candidate. |
| EMPLOYEE_STATUS | VARCHAR2 | 20 |  |  | Status of the employee. Indicates if the employee is active. |
| CONFIGURATION_PROFILE_CODE | VARCHAR2 | 20 |  |  | Configuration profile code value for the export process. |
| MANAGER_LEVEL | NUMBER |  | 10 |  | Manager level of the person.Indicates the manager hierarchy level of the person. |
| APPLICANT_NUMBER | VARCHAR2 | 30 |  |  | Unique number for people who are applicants. This is in addition to PERSON_NUMBER. Allows global tracking of applicants.. |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | Determinant for set enabled tables and those using business unit as a partitioning key. |
| VACANCY_ID | NUMBER |  | 18 |  | Vacancy identifier for the job or position for which person is a candidate. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | System generated unique identifier for the assignment of a person. |
| EFFECTIVE_START_DATE7 | DATE |  |  |  | Effective start date of assignment. |
| EFFECTIVE_END_DATE7 | DATE |  |  |  | Effective end date of assignment. |
| EFFECTIVE_SEQUENCE | NUMBER |  | 4 | Yes | Date Effective Entity: indicates the order of different changes made during a day. The lowest value represents the earliest change in the day. |
| EFFECTIVE_LATEST_CHANGE | VARCHAR2 | 30 |  | Yes | Date Effective Entity: 'Y' indicates that this row represents the latest change in the day. |
| ASG_VERSION_NUMBER | NUMBER |  | 9 |  | Object version number of assignment. |
| HOMEADDRESSTOWNORCITY | VARCHAR2 | 60 |  |  | Name of the town or city of the person's home address. |
| ACTION_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Last update date of action for the export process. |
| ACTION_ACTION_DATE | TIMESTAMP |  |  |  | Indicates the first start date for the export process. |
| NAME_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Last update date of person name for the export process. |
| PERPPF_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Last update date of person's workrelationship for the export process. |
| USER_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Disconnected Mobile: indicates the date and time of the last update of the row. This value is different from LAST_UPDATE_DATE if the update originally happened in a different database (i.e. a different mobile database or the server). |
| PERSON_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Last update date of person for the export process. |
| EMAIL_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Last update date of person's email for the export process. |
| NID_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Last update date of person's national identifier for the export process. |
| ADDRESS_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Last update date of person's address for the export process. |
| ROLE_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Last update date of role for the export process. |
| PHONE_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Last update date of person's phone for the export process. |
| ASSIGNMENT_STATUS_TYPE | VARCHAR2 | 30 |  |  | Assignment status type of person. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_INTG_TALEO_EXPORT_M_PK | Unique | Default | TALEO_EXPORT_ID, EFFECTIVE_LATEST_CHANGE, EFFECTIVE_SEQUENCE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
