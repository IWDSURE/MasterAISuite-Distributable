# HWR_WEB_POST

This table is to be used to store the Web Posts from the social medila websites in our database

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwebpost-19154.html#hwrwebpost-19154](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwebpost-19154.html#hwrwebpost-19154)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WEB_POST_PK | WEB_POST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WEB_POST_ID | NUMBER |  | 18 | Yes | This represents the Id of the web post used to uniquely identify the record. |
| SRC_POST_ID | VARCHAR2 | 100 |  |  | This represents the web post id associated with this post. |
| PRFL_ID | VARCHAR2 | 500 |  | Yes | This represents the profile id of the person who made this post. |
| SOURCE_ID | NUMBER |  | 18 | Yes | This represents the id of the social media source from where this post was obtained. |
| URL | VARCHAR2 | 100 |  |  | This represents the URL of this post in the corresponding social media site. |
| IMAGE_URL | VARCHAR2 | 1000 |  |  | This represents the url of the image associated with this web post. |
| MESSAGE | VARCHAR2 | 1000 |  |  | This represents the content of the web post that this record represents. |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | This represents the description attribute associated with this web post. |
| METADATA | VARCHAR2 | 1000 |  |  | This represents the metadata associated with the web post |
| POST_CREATED_ON | TIMESTAMP |  |  |  | This column represents the date when this web post was created. |
| POST_UPDATED_ON | TIMESTAMP |  |  |  | This column represents the date when this web post was updated. |
| POST_CREATION_TIME | TIMESTAMP |  |  |  | This column represents the time when this web post was created. |
| LIKE_COUNT | NUMBER |  | 18 |  | This column represents the like count associated with this web post. |
| SHARE_COUNT | NUMBER |  | 18 |  | This column represents the share count associated with this web post. |
| COMMENT_COUNT | NUMBER |  | 18 |  | This column represents the comment count associated with this web post. |
| TAG_COUNT | NUMBER |  | 18 |  | This column represents the tag count associated with this web post. |
| TYPE | VARCHAR2 | 50 |  |  | This column indicates the type of the web post object this record is representing. |
| CONVERSATION_ID | VARCHAR2 | 256 |  |  | This is the conversation id related with web post. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WEB_POST_N1 | Non Unique | Default | SOURCE_ID, PRFL_ID |
| HWR_WEB_POST_N2 | Non Unique | Default | PRFL_ID |
| HWR_WEB_POST_U1 | Unique | Default | WEB_POST_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
