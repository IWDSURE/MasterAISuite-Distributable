# PAY_MESSAGE_LINES

This table contains error messages from running a process.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paymessagelines-30109.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paymessagelines-30109.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_MESSAGE_LINES_PK | MESSAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MESSAGE_ID | NUMBER |  | 18 | Yes | MESSAGE_ID |
| LINE_SEQUENCE | NUMBER |  | 18 | Yes | Displays sequence of this line.  This is a global sequence. |
| MESSAGE_LEVEL | VARCHAR2 | 1 |  | Yes | Indicates the severity of the message, from fatal errors to general messages. |
| SOURCE_ID | NUMBER |  | 18 | Yes | Generic foreign key to the message owner. |
| SOURCE_TYPE | VARCHAR2 | 1 |  | Yes | Specifies the message owner type: assignment action, payroll action or Business Group. |
| PAYROLL_ID | NUMBER |  | 18 |  | Foreign key to PAY_PAYROLLS. |
| PARENT_MESSAGE_ID | NUMBER |  | 18 |  | PARENT_MESSAGE_ID |
| OBJECT_ID | VARCHAR2 | 30 |  |  | OBJECT_ID |
| OBJECT_TYPE | VARCHAR2 | 30 |  |  | OBJECT_TYPE |
| MESSAGE_NAME | VARCHAR2 | 30 |  |  | MESSAGE_NAME |
| ENCODED_MESSAGE | VARCHAR2 | 2000 |  |  | ENCODED_MESSAGE |
| LINE_TEXT | VARCHAR2 | 2000 |  |  | Text for the line. |
| TOKEN1 | VARCHAR2 | 30 |  |  | TOKEN1 |
| TOKEN2 | VARCHAR2 | 30 |  |  | TOKEN2 |
| TOKEN3 | VARCHAR2 | 30 |  |  | TOKEN3 |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| ORA_PART_KEY | DATE |  |  | Yes | The partition key used to determine the range interval. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_MESSAGE_LINES_N1 | Non Unique | Default | PAYROLL_ID |
| PAY_MESSAGE_LINES_N50 | Non Unique | Default | SOURCE_ID, SOURCE_TYPE |
| PAY_MESSAGE_LINES_PK | Unique | Default | MESSAGE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
