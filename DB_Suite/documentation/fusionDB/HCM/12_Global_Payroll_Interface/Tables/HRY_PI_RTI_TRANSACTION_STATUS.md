# HRY_PI_RTI_TRANSACTION_STATUS

To store the transaction status of all employees fetched from the ATOM Feed

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypirtitransactionstatus-3637.html#hrypirtitransactionstatus-3637](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypirtitransactionstatus-3637.html#hrypirtitransactionstatus-3637)

## Primary Key

| Name | Columns |
|------|----------|
| hry_pi_rti_transaction_st_PK | TRANSACTION_STATUS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TRANSACTION_STATUS_ID | NUMBER |  | 18 | Yes | Primary key to the table hry_pi_rti_transaction_status |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 |  | Foreign key to the table pay_pay_relationships_dn |
| PAYROLL_ID | NUMBER |  | 18 |  | Foreign key to the table per_all_payrolls_f |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to the table per_all_people_f |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to the table per_legislative_data_groups |
| STATUS | VARCHAR2 | 30 |  | Yes | Status of the person fetched from ATOM Feed |
| IS_ENQUEUED | VARCHAR2 | 2 |  |  | Status of whether the person is enqueued for processing |
| EXTERNAL_REFERENCE_ID | VARCHAR2 | 50 |  |  | Response of the ADP Delivery API |
| ITERATION_NO | NUMBER |  | 2 | Yes | Count of the number of times ADP Response API has been hit |
| ERROR_CODE | VARCHAR2 | 50 |  |  | Error Code generated from ADP Delivery API |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | Error Message generated from ADP Delivery API |
| HIRE_DATE | TIMESTAMP |  |  | Yes | Hire Date for the new hire. This is equal to the Effective Start Date for the newhire. |
| PAYROLL_ACTION_ID | NUMBER |  | 18 |  | ID of the PAY_PAYROLL_ACTIONS table for the online extract run. |
| EXTRACT_MODE | VARCHAR2 | 20 |  | Yes | Mode of the extract submission, for example, ONLINE or BATCH. |
| INTEGRATION_SETUP_NAME | VARCHAR2 | 80 |  | Yes | Name of the integrator for which the newhire is processed. |
| EVENT_TYPE | VARCHAR2 | 30 |  | Yes | Type of event for which the ATOM feed is analysed, for example, HIRE. |
| FEED_SOURCE_NAME | VARCHAR2 | 30 |  | Yes | Indicates the infrastructure from where the data came into the table, e.g., ATOM, ESS. |
| FEED_ENTRY_ID | NUMBER |  | 18 |  | ID of the feed which comes as a response to the ATOM API call. |
| FEED_ENTRY_UPD_TIMESTAMP | TIMESTAMP |  |  |  | Updated timestamp for the each of the new hire being preocessed. This is equal to the Effective Start Date for the newhire. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | column used to store the Legislation Code of the payload |
| FILE_NAME | VARCHAR2 | 100 |  |  | column used to store the file name of the payload |
| NOTIFICATION_DATE | TIMESTAMP |  |  |  | This column is intended to hold notification date of person's termination |
| ACTUAL_TERMINATION_DATE | TIMESTAMP |  |  |  | This column is intended to hold actual termination date of person's termination |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_PI_RTI_TRANS_STATUS_PK | Unique | Default | TRANSACTION_STATUS_ID |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
