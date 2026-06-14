# HWR_XP_ACTOR_B

This is the table for the experience store actors.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpactorb-20446.html#hwrxpactorb-20446](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpactorb-20446.html#hwrxpactorb-20446)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_XP_ACTOR_B_PK | ACTOR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTOR_ID | NUMBER |  | 18 | Yes | The Unique database identifier for this actor. |
| NAME | VARCHAR2 | 255 |  |  | The name representing this actor. |
| MAILBOX | VARCHAR2 | 275 |  |  | The email address that identifies this actor. The required format is "mailto:email address". |
| ACCOUNT_NAME | VARCHAR2 | 255 |  |  | The name of the account for this actor. |
| ACCOUNT_HOMEPAGE | VARCHAR2 | 2000 |  |  | The canonical home page for the system the account is on. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_XP_ACTOR_B_U1 | Unique | Default | ACTOR_ID |
| HWR_XP_ACTOR_B_U2 | Unique | Default | MAILBOX |
| HWR_XP_ACTOR_B_U3 | Unique | Default | ACCOUNT_NAME, ACCOUNT_HOMEPAGE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
