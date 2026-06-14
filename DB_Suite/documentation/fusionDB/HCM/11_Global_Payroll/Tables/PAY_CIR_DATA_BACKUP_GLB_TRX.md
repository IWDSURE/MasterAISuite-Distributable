# PAY_CIR_DATA_BACKUP_GLB_TRX

This table backup cir data whose effective start date is after global transfer date for later processing.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycirdatabackupglbtrx-19911.html#paycirdatabackupglbtrx-19911](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycirdatabackupglbtrx-19911.html#paycirdatabackupglbtrx-19911)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_CIR_DATA_BACKUP_GLB_TRX_PK | CIR_DATA_BACKUP_GLB_TRX_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CIR_DATA_BACKUP_GLB_TRX_ID | NUMBER |  | 18 | Yes | Table surrogate key id CIR_DATA_BACKUP_GLB_TRX_ID |
| MASS_ACTION_HEADER_ID | NUMBER |  | 18 |  | Identifier for the mass global transfer batch. To be populated during copy future phase. |
| MASS_ACTION_LINE_ID | NUMBER |  | 18 |  | Identifier for the mass global transfer line (person level). To be populated during copy future phase. |
| SOURCE_PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 | Yes | Payroll Relationship Id of the source |
| ENTITY_NAME | VARCHAR2 | 30 |  | Yes | This would be the table name e.g. PAY_DIR_CARDS_F, PAY_DIR_CARD_COMPONENTS_F etc |
| SOURCE_SURROGATE_KEY_ID | NUMBER |  | 18 | Yes | This is the surrogate key ID i.e. dir_card_id, dir_card_comp_id etc of the source (from where we are copying the data) |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ACTION_TYPE | VARCHAR2 | 30 |  | Yes | Possible values are:  CREATE, UPDATE (i.e. date effective update) |
| ATTRIBUTE_NAME | VARCHAR2 | 30 |  | Yes | Name of the attribute that is being stored e.g. DIR_CARD_COMP_DEF_ID.  If new physical record but no change in any attribute from previous record then store "DUMMY" here. |
| OLD_VALUE_CHAR | VARCHAR2 | 4000 |  |  | If attribute is char, then store the old value of the attribute here in case of both INSERT and INSERT_UPDATE (i.e. date effective update) |
| NEW_VALUE_CHAR | VARCHAR2 | 4000 |  |  | If attribute is char, then store the new value of the attribute here in case of INSERT_UPDATE |
| OLD_VALUE_NUMBER | NUMBER |  |  |  | If attribute is number, then store the old value of the attribute here in case of both INSERT and INSERT_UPDATE (i.e. date effective update) |
| NEW_VALUE_NUMBER | NUMBER |  |  |  | If attribute is number, then store the new value of the attribute here in case of INSERT_UPDATE |
| OLD_VALUE_DATE | DATE |  |  |  | If attribute is date, then store the old value of the attribute here in case of both INSERT and INSERT_UPDATE (i.e. date effective update) |
| NEW_VALUE_DATE | DATE |  |  |  | If attribute is date, then store the new value of the attribute here in case of INSERT_UPDATE |
| DEST_PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 |  | Target Payroll Relationship Id. To be populated during copy future phase. |
| DESTINATION_SURROGATE_KEY_ID | NUMBER |  | 18 |  | This is the surrogate key ID i.e. dir_card_id, dir_card_comp_id etc of the target (where we are copying the data to).  If the card, component is being re-used it could be the same id as the source.  To be populated during copy future phase. |
| COPY_STATUS | VARCHAR2 | 30 |  |  | This represents the status of future copy to destination (i.e. during copyFutureCIRChangesForGLBTransfer). Possible values are SUCCESS, FAILURE. To be populated during copy future phase. |
| COPY_INFORMATION | VARCHAR2 | 4000 |  |  | Log messages that give more information about the copy status. To be populated during copy future phase. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID. Flag used to mark obsolete data when upgrading the seed data in customer pod |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_CIR_DATA_BACKUP_GLB_TRX_N1 | Non Unique | Default | SOURCE_SURROGATE_KEY_ID |
| PAY_CIR_DATA_BACKUP_GLB_TRX_N2 | Non Unique | Default | SOURCE_PAYROLL_RELATIONSHIP_ID, ENTITY_NAME |
| PAY_CIR_DATA_BACKUP_GLB_TRX_N3 | Non Unique | Default | MASS_ACTION_LINE_ID |
| PAY_CIR_DATA_BACKUP_GLB_TRX_PK | Unique | Default | CIR_DATA_BACKUP_GLB_TRX_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
