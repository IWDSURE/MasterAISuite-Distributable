# HRC_SEM_CONTACT_INFO

This table contains the contact information for a person.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemcontactinfo-29891.html#hrcsemcontactinfo-29891](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemcontactinfo-29891.html#hrcsemcontactinfo-29891)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_CONTACT_INFO_PK | CONTACTINFO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTACTINFO_ID | NUMBER |  | 18 | Yes | This column contains the primary key for the contact info table. |
| PERSON_ID | NUMBER |  | 18 |  | This column contains person id of the person table. |
| NAME | VARCHAR2 | 512 |  |  | This person contains the name of the contact info. |
| EMAIL | VARCHAR2 | 256 |  |  | This column contains the email of the person. |
| PHONE | VARCHAR2 | 80 |  |  | This column contains the phone number of the contact info. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SEM_CONTACT_INFO_N1 | Non Unique | FUSION_TS_TX_DATA | EMAIL |
| HRC_SEM_CONTACT_INFO_N2 | Non Unique | FUSION_TS_TX_DATA | PERSON_ID |
| HRC_SEM_CONTACT_INFO_U1 | Unique | FUSION_TS_TX_DATA | CONTACTINFO_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
