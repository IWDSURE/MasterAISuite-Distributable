# HRY_PI_DELIVERY_RESULT_DTLS

To store the error details or success status for an employee to be transferred to ADP

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypideliveryresultdtls-21128.html#hrypideliveryresultdtls-21128](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypideliveryresultdtls-21128.html#hrypideliveryresultdtls-21128)

## Primary Key

| Name | Columns |
|------|----------|
| HRY_PI_DELIVERY_RESULT_DT_PK | DELIVERY_RESULT_DTLS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DELIVERY_RESULT_DTLS_ID | NUMBER |  | 18 | Yes | Primary key to the table hry_pi_delivery_results_dtls |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to the table per_all_people_f |
| DELIVERY_SOURCE_ID | VARCHAR2 | 50 |  | Yes | Stores Payroll Action Id of extract Archive Process |
| DELIVERY_SOURCE_TYPE | VARCHAR2 | 10 |  | Yes | Determines the source of the error. |
| PAYROLL_ID | NUMBER |  | 18 |  | Foreign key to the table pay_all_payrolls_f |
| ERROR_CODE | VARCHAR2 | 60 |  |  | Stores the error code for high-level recognition of the issue. |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | Stores the error message string as received from vendor / while validating payload to be sent to vendor. |
| EVENT_TYPE | VARCHAR2 | 30 |  |  | Stores the type of event for the request. for example, HIRE. |
| MESSAGE_IDENTIFIER | NUMBER |  | 18 |  | A number to uniquely identifify record with combination of MESSAGE_NUMBER. |
| RESP_MESSAGE_NUMBER | VARCHAR2 | 60 |  |  | Message identifier from ADP as received from ADP Real time delivery response. |
| RESP_MESSAGE_CATEGORY | VARCHAR2 | 30 |  |  | Message category from ADP as received from ADP Real time delivery response. |
| RESP_SEVERITY | VARCHAR2 | 20 |  |  | Severity of the error as received from ADP Real time delivery response. |
| RESP_RECORD_TYPE | VARCHAR2 | 80 |  |  | Type of record as received from ADP Real time delivery response. |
| RESP_FUNCTIONAL_AREA | VARCHAR2 | 4000 |  |  | Description of the type of record as received from ADP Real time delivery response. |
| RESP_DIAGNOSIS | VARCHAR2 | 4000 |  |  | Stores the cause of the error generated. |
| RESP_PROCEDURE | VARCHAR2 | 4000 |  |  | Stores the remedy of the error. |
| RESP_EXT_TRANSACTION_ID | VARCHAR2 | 50 |  |  | Acknowledgement ID sent as part of ADP Delivery API. |
| RESP_LOAD_STATUS | VARCHAR2 | 20 |  |  | Status of whether the newhire 's processing is completed at ADP's end. |
| RESP_OVERALL_STATUS | VARCHAR2 | 40 |  |  | Status of the result of a particular newhire's processing at ADP's end. |
| RESP_SET_LSRD | VARCHAR2 | 2 |  |  | ADP Response API attribute. Possible values are Y / N. |
| RESP_RELAUNCHABLE | VARCHAR2 | 2 |  |  | ADP Response API attribute. Possible values are Y / N. |
| RESP_SKIP_REVIEW | VARCHAR2 | 2 |  |  | ADP Response API attribute. Possible values are Y / N. |
| RESP_SKIP_REVIEW_REASON | VARCHAR2 | 2000 |  |  | ADP Response API attribute for returning the reason to skip review. |
| RESP_WHO | VARCHAR2 | 80 |  |  | Stores the user roles who are eligible to fix the error. |
| NEW_HIRE_EMAIL | VARCHAR2 | 80 |  |  | Email address of the newly hired employee. |
| HR_EMAIL | VARCHAR2 | 80 |  |  | Email address of the HR representative. |
| PAY_ADMIN_EMAIL | VARCHAR2 | 80 |  |  | Email address of the Payroll Administrator. |
| LINE_MANAGER_EMAIL | VARCHAR2 | 80 |  |  | Email address of the Line Manager. |
| NOTIFICATION_EMAIL | VARCHAR2 | 80 |  |  | Email address of the Actionees to be notified. |
| NOTIFICATION_DATE | TIMESTAMP |  |  |  | Stores the date when the notification was generated. |
| STATUS | VARCHAR2 | 80 |  | Yes | Status of the error, i.e. the stage of rectification where it is currently in. |
| SUBMITTED_DATE | TIMESTAMP |  |  |  | Date when the status is generated and recorded. |
| NOTIFICATION_MESSAGE | VARCHAR2 | 4000 |  |  | Stores the message body to be sent as part of the notification. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Foreign key to the table per_enterprises |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_PI_DELIVERY_RESULT_DT_PK | Unique | Default | DELIVERY_RESULT_DTLS_ID |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
