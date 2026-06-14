# HWR_WEB_POST_DETAILS

This table is to be used to store the Web Post Detail objects from the social medila websites in our database.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwebpostdetails-13765.html#hwrwebpostdetails-13765](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwebpostdetails-13765.html#hwrwebpostdetails-13765)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WEB_POST_DETAILS_PK | WEB_POST_DETAILS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WEB_POST_DETAILS_ID | NUMBER |  | 18 | Yes | This represents the Id of the web post details used to uniquely identify the record. |
| WEB_POST_ID | NUMBER |  | 18 | Yes | This is the Web Post Id identifying the web post details object from social media websites in this table. |
| SOURCE_ID | NUMBER |  | 18 | Yes | This represents the social media source from which this web post details object was obtained. |
| SOURCE_POST_ID | VARCHAR2 | 100 |  |  | This represents the web post id associated with this post. |
| SRC_CHILD_POST_ID | VARCHAR2 | 100 |  |  | This represents the web post id of the child associated with this post. |
| TYPE | VARCHAR2 | 50 |  |  | This column indicates the type of the web post details object this record is representing. |
| VALUE | VARCHAR2 | 50 |  |  | This column represents the value of the web post details object this record is representing. |
| POST_CREATED_ON | TIMESTAMP |  |  |  | This column represents the date when this web post details was created. |
| POST_UPDATED_ON | TIMESTAMP |  |  |  | This column represents the date when this web post details was updated. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WEB_POST_DETAILS_N1 | Non Unique | Default | WEB_POST_ID |
| HWR_WEB_POST_DETAILS_N2 | Non Unique | Default | SOURCE_ID |
| HWR_WEB_POST_DETAILS_U1 | Unique | Default | WEB_POST_DETAILS_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
