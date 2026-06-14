# FF_FUNCTION_PARAMETERS

This table contains the parameters for specific formula functions.

## Details

**Schema:** FUSION

**Object owner:** FF

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/fffunctionparameters-14843.html#fffunctionparameters-14843](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/fffunctionparameters-14843.html#fffunctionparameters-14843)

## Primary Key

| Name | Columns |
|------|----------|
| FF_FUNCTION_PARAMETERS_PK | FUNCTION_ID, SEQUENCE_NUMBER |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FUNCTION_ID | NUMBER |  | 18 | Yes | Identifier for the function the parameter belongs to. Foreign key to FF_FUNCTIONS. |
| SEQUENCE_NUMBER | NUMBER |  | 2 | Yes | Number for each parameter in a specific sequence. |
| CLASS | VARCHAR2 | 1 |  | Yes | Identifies whether the parameter is an IN parameter, an OUT parameter, or an IN-OUT parameter. |
| NAME | VARCHAR2 | 30 |  | Yes | Name of the parameter. |
| CONTINUING_PARAMETER | VARCHAR2 | 1 |  | Yes | Y if there can be one or more of the parameter, else N. |
| DATA_TYPE | VARCHAR2 | 1 |  | Yes | Data type of the parameter. |
| OPTIONAL | VARCHAR2 | 1 |  | Yes | N if the parameter is mandatory, else Y. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FF_FUNCTION_PARAMETERS_PK | Unique | Default | FUNCTION_ID, SEQUENCE_NUMBER, ORA_SEED_SET1 |
| FF_FUNCTION_PARAMETERS_PK1 | Unique | Default | FUNCTION_ID, SEQUENCE_NUMBER, ORA_SEED_SET2 |

---

[← Back to Index](../9_Fast_Formula_Tables_Index.md)
