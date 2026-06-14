# HWR_VLTR_PER_PROFILE_B

This table stores base  volunteer information

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrperprofileb-29175.html#hwrvltrperprofileb-29175](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrperprofileb-29175.html#hwrvltrperprofileb-29175)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_PER_PROFILE_B_PK | VOLUNTEER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| VOLUNTEER_ID | NUMBER |  | 18 | Yes | VOLUNTEER_ID |  |
| USER_NAME | VARCHAR2 | 100 |  |  | Volunteer User Name |  |
| HCM_PERSON_ID | NUMBER |  | 18 |  | HCM_PERSON_ID |  |
| ATTACHMENT_ID | NUMBER |  | 18 |  | ATTACHMENT_ID | Obsolete |
| IS_INTERESTED_IN_PROJECT_LEAD | NUMBER |  | 1 |  | IS_INTERESTED_IN_PROJECT_LEAD |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| NOTIFICATION_EMAIL | VARCHAR2 | 5 |  |  | This is used to store Yes or no value as the preference to be notified through email | Obsolete |
| NOTIFICATION_VLNTR_APPS | VARCHAR2 | 5 |  |  | This is used to store Yes or no value as the preference to be notified through Volunteer application | Obsolete |
| T_SIZE | VARCHAR2 | 20 |  |  | t-shirt size |  |
| T_STYLE | VARCHAR2 | 20 |  |  | t-shirt style |  |
| CT_USER_ID | VARCHAR2 | 20 |  |  | CT_USER_ID |  |
| IS_AGRMNT_ACCEPTED | NUMBER |  | 1 |  | IS_AGRMNT_ACCEPTED |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_PER_PROFILE_B_U1 | Unique | FUSION_TS_TX_IDX | VOLUNTEER_ID |
| HWR_VLTR_PER_PROFILE_B_U2 | Unique | FUSION_TS_TX_IDX | USER_NAME |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
