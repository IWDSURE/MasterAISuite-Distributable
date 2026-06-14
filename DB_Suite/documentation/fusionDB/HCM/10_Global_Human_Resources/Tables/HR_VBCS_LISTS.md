# HR_VBCS_LISTS

HCM lists that store the criteria used to generate population of objects

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** hr_vbcs_lists

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrvbcslists-27119.html#hrvbcslists-27119](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrvbcslists-27119.html#hrvbcslists-27119)

## Primary Key

| Name | Columns |
|------|----------|
| hr_vbcs_lists_PK | LIST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LIST_ID | NUMBER |  | 18 | Yes | HCM List Unique Identifier |
| NAME | VARCHAR2 | 200 |  |  | Name of the HCM List |
| DESCRIPTION | VARCHAR2 | 600 |  |  | Description of the HCM List |
| OBJECT_NAME | VARCHAR2 | 50 |  |  | Defines the Object associated with the list |
| ACTIVE | VARCHAR2 | 1 |  |  | Determines whether the list is active or not |
| LIST_SCOPE | VARCHAR2 | 20 |  |  | Stores the scope of the HCM List |
| OWNER_ID | NUMBER |  |  |  | Owner ID of the person who saved the list |
| CRITERIA | CLOB |  |  |  | Stores the HCM List Criteria |
| SUBSCRIBER | VARCHAR2 | 50 |  |  | Stores the Code of the Subscriber for the current list |
| TYPE | VARCHAR2 | 20 |  |  | Stores the type of the object |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HR_VBCS_LISTS_PK | Unique | Default | LIST_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
