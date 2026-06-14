# IRC_WHATSAPP_TEMPLATE_B

Parent table that stores WhatsApp template details for Recruiting, including names, categories, statuses, and multi-language grouping.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircwhatsapptemplateb-22590.html#ircwhatsapptemplateb-22590](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircwhatsapptemplateb-22590.html#ircwhatsapptemplateb-22590)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_WHATSAPP_TEMPLATE_B_PK | WA_TEMPLATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WA_TEMPLATE_ID | NUMBER |  | 18 | Yes | Unique identifier for a WhatsApp template in Recruiting |
| WABA_TEMPLATE_NAME | VARCHAR2 | 512 |  | Yes | Name assigned to the WhatsApp template |
| WABA_CATEGORY | VARCHAR2 | 20 |  | Yes | Category of the WhatsApp template. Possible values include ORA_MARKETING, ORA_UTILITY, ORA_AUTHENTICATION |
| DESCRIPTION_TYPE_CODE | VARCHAR2 | 30 |  |  | Recruiting category for the WhatsApp template |
| DESCRIPTION_ID | NUMBER |  | 18 |  | Foreign key, reference to irc_descriptions_b.description_id |
| DESC_VERSION_ID | NUMBER |  | 18 |  | Identifier for the description library item associated with this version. Foreign key, references description_version_id in the irc_desc_versions_b table |
| TEMPLATE_STATUS | VARCHAR2 | 20 |  | Yes | Recruiting template status, allowing suspension from FA without affecting Meta's status. Possible values include ORA_ACTIVE, ORA_INACTIVE |
| PRODUCT_CONTEXT | VARCHAR2 | 40 |  |  | The product context such as HCM_COMMUNICATE, HCM_RECRUITING etc., for which the template belongs to. |
| TEMPLATE_SOURCE | VARCHAR2 | 40 |  |  | Indicates whether the template was created via content library import, FSM Import, or the UI. Possible values include ORA_CONTENT_LIBRARY_IMPORT, ORA_FSM_IMPORT, ORA_UI |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_WHATSAPP_TEMPLATE_B_FK1 | Non Unique | Default | DESCRIPTION_ID |
| IRC_WHATSAPP_TEMPLATE_B_FK2 | Non Unique | Default | DESC_VERSION_ID |
| IRC_WHATSAPP_TEMPLATE_B_N1 | Non Unique | Default | PRODUCT_CONTEXT, DESCRIPTION_TYPE_CODE, TEMPLATE_STATUS |
| IRC_WHATSAPP_TEMPLATE_B_PK | Unique | Default | WA_TEMPLATE_ID |
| IRC_WHATSAPP_TEMPLATE_B_U1 | Unique | Default | WABA_TEMPLATE_NAME |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
