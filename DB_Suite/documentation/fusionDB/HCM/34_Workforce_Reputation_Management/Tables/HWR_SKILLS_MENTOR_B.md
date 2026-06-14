# HWR_SKILLS_MENTOR_B

This Table stores the details of the Mentor for skills.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrskillsmentorb-24911.html#hwrskillsmentorb-24911](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrskillsmentorb-24911.html#hwrskillsmentorb-24911)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SKILLS_MENTOR_B_PK | MENTOR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MENTOR_ID | NUMBER |  | 18 | Yes | This stores the Unique Identifier of the Mentor |
| MENTOR_GBL_PRFL_ID | NUMBER |  | 18 |  | This stores the Mentor's Global Profile Id |
| MENTOR_FUS_PRFL_ID | NUMBER |  | 18 |  | This stores the Mentor's Fusion Profile Id |
| MENTOREE_GBL_PRFL_ID | NUMBER |  | 18 |  | This stores the mentoree global profile Id. |
| MENTOREE_FUS_PRFL_ID | NUMBER |  | 18 |  | This stores the mentoree Fusion  profile Id. |
| SOURCE_ID | NUMBER |  | 18 |  | This column used to store the id of communication source. |
| CONVERSATION_ID | VARCHAR2 | 100 |  |  | This column used to store the id of conversation. |
| MENTORSHIP_STATUS | VARCHAR2 | 30 |  |  | This is current staus of mentor. |
| SKILLS | VARCHAR2 | 4000 |  |  | Skill column: This store mentor's skills . |
| IS_UPDATED | NUMBER |  | 1 |  | This is the flag to indicated if the mentorship request is new(0) or is upgrade(1) |
| MENTORSHIP_TYPE | VARCHAR2 | 100 |  |  | This is the type of mentorship |
| MANAGER_ID | NUMBER |  | 18 |  | This is the person_id of Manager, when mentorship initiated by the manger for his direct report |
| LAST_ACTIVITY_DATE | TIMESTAMP |  |  | Yes | This stores the last activity date. |
| MENTOR_ATTR_1 | VARCHAR2 | 4000 |  |  | This stores mentor's attribute 1. This is used to store the message sent by mentee to mentor. |
| MENTOR_ATTR_2 | VARCHAR2 | 512 |  |  | This stores mentor's attribute 2. |
| MENTOR_ATTR_3 | VARCHAR2 | 512 |  |  | This stores mentor's attribute 3. |
| MENTOR_ATTR_4 | VARCHAR2 | 512 |  |  | This stores mentor's attribute 4. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SKILLS_MENTOR_B_N1 | Non Unique | FUSION_TS_TX_DATA | MENTOR_GBL_PRFL_ID |
| HWR_SKILLS_MENTOR_B_N2 | Non Unique | FUSION_TS_TX_DATA | MENTOREE_GBL_PRFL_ID |
| HWR_SKILLS_MENTOR_B_N3 | Non Unique | FUSION_TS_TX_DATA | MENTOR_FUS_PRFL_ID |
| HWR_SKILLS_MENTOR_B_N4 | Non Unique | FUSION_TS_TX_DATA | MENTOREE_FUS_PRFL_ID |
| HWR_SKILLS_MENTOR_B_U1 | Unique | FUSION_TS_TX_DATA | MENTOR_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
