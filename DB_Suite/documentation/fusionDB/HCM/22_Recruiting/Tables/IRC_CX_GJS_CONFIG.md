# IRC_CX_GJS_CONFIG

Stores configuration for SEO Job posting in Hcm Recruiting

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxgjsconfig-23224.html#irccxgjsconfig-23224](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxgjsconfig-23224.html#irccxgjsconfig-23224)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_GJS_CONFIG_PK | CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| SITE_SEQUENCE_STR | VARCHAR2 | 4000 |  |  | Stores the site number sequence in their sequence number order from low to high |
| SITEMAP | CLOB |  |  |  | Stores a snapshot of the jobs sitemap last published to SEO |
| LAST_SITEMAP_PUBLISH_DATE | TIMESTAMP |  |  |  | Stores the timestamp when the jobs sitemap was last published to SEO |
| LAST_PING_DATE | TIMESTAMP |  |  |  | Stores the timestamp when there is a ping to SEO |
| LAST_PING_FAILED_DATE | TIMESTAMP |  |  |  | Stores the timestamp when there is a failed ping to SEO |
| LAST_ACTIVE_DATE | TIMESTAMP |  |  |  | Indicates the date and time the SEO was last activated. |
| LAST_ACTIVATED_BY | VARCHAR2 | 64 |  |  | Indicates the user who last activated the SEO. |
| LAST_INACTIVE_DATE | TIMESTAMP |  |  |  | Indicates the date and time the SEO was last inactivated. |
| LAST_INACTIVATED_BY | VARCHAR2 | 64 |  |  | Indicates the user who last inactivated the SEO. |
| LAST_CLEANUP_DATE | TIMESTAMP |  |  |  | Indicates the date and time the SEO snapshot cleaned up. |
| LAST_PING_STATUS_CODE | NUMBER |  |  |  | Stores HTTP status of the ping response. |
| LAST_PING_STATUS_MESSAGE | CLOB |  |  |  | Stores the HTTP status response 
note: error msg or success msg |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_GJS_CONFIG_PK | Unique | Default | CONFIG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
