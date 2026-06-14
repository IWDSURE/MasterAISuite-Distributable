# IRC_REG_TN_AGENCIES

This is the table for storing Agency association for the customer which would be referenced as object in irc_avail_context.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircregtnagencies-31620.html#ircregtnagencies-31620](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircregtnagencies-31620.html#ircregtnagencies-31620)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REG_TN_AGENCIES_PK | REG_AGENCY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REG_AGENCY_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| REGISTRATION_ID | NUMBER |  | 18 | Yes | Stores the registration_id. Foreign key to irc_reg_tnetwork_config table. |
| TN_AGENCY_ID | NUMBER |  | 18 | Yes | Stores the AGENCY_ID of the Agency. |
| TN_AGENCY_CODE | VARCHAR2 | 30 |  |  | Stores the Agency Code of the Agency. |
| TN_AGENCY_NAME | VARCHAR2 | 240 |  |  | Column to store name for agency. |
| TN_AGENCY_GUID | VARCHAR2 | 32 |  |  | Stores the AGENCY_GUID of the Agency. |
| TN_AGENCY_EMAIL | VARCHAR2 | 240 |  |  | Stores the Agency Email of the Agency. |
| TN_AGENCY_CONTACT | VARCHAR2 | 240 |  |  | Stores the Agency Contact of the Agency. |
| NOTES | VARCHAR2 | 4000 |  |  | Store the notes entered by the recruiting administrator |
| OBJECT_STATUS | VARCHAR2 | 30 |  | Yes | Indicates the status of the object. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REG_TN_AGENCIES_FK1 | Non Unique | Default | REGISTRATION_ID |
| IRC_REG_TN_AGENCIES_PK | Unique | Default | REG_AGENCY_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
