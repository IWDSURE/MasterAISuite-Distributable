# HWR_INVITATION_B

This table stores information related to Invitations

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrinvitationb-10783.html#hwrinvitationb-10783](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrinvitationb-10783.html#hwrinvitationb-10783)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_INVITATION_B_PK | INVITATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INVITATION_ID | NUMBER |  | 18 | Yes | This column stores the information about Invitation Id.This acts as the primary key. |
| INVITOR_PRFL_ID | NUMBER |  | 18 | Yes | This stores the Invitors Profile Id |
| INVITEE_PRFL_ID | VARCHAR2 | 1024 |  |  | This stores the information on  invitees Profile Id |
| INVITATION_STATUS | VARCHAR2 | 500 |  | Yes | This stores the information on the status of Invitation |
| INVITATION_DATE | TIMESTAMP |  |  | Yes | This stores the date of Invitation |
| IS_REGISTERED | VARCHAR2 | 4 |  | Yes | This stores whether the Invitee is Regisitered or not |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_INVITATION_B_U1 | Unique | FUSION_TS_TX_DATA | INVITATION_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
