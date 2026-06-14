# HWR_WLNS_NEWS_B

This table holds the wellness news

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsnewsb-5934.html#hwrwlnsnewsb-5934](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsnewsb-5934.html#hwrwlnsnewsb-5934)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_NEWS_B_PK | NEWS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| NEWS_ID | NUMBER |  | 18 | Yes | This is the primary key for the table |
| START_DATE | TIMESTAMP |  |  | Yes | This column stores the start date of the corresponding news |
| END_DATE | TIMESTAMP |  |  | Yes | This column stores the end date of the corresponding news |
| NEWS_LINK | VARCHAR2 | 100 |  |  | This column holds the link for the news |
| NEWS_IMAGE | BLOB |  |  |  | This column holds image for the news |
| ORDER_RANK | NUMBER |  | 18 |  | This column stores the rank of the news |
| IS_DELETED | VARCHAR2 | 100 |  |  | This column indicates whether the news deleted or not |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_NEWS_B_U1 | Unique | FUSION_TS_TX_DATA | NEWS_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
