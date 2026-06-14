# IRC_AUTO_SYNC_TO_HR_TRACKING

This table is used for tracking Progress and Errors in Auto Create Offers and Move to HR .

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircautosynctohrtracking-12798.html#ircautosynctohrtracking-12798](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircautosynctohrtracking-12798.html#ircautosynctohrtracking-12798)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AUTO_SYNC_TO_HR_TRACK_PK | AUTO_SYNC_TRACKING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AUTO_SYNC_TRACKING_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| AUTO_SYNC_ID | NUMBER |  | 18 | Yes | Foreign key to irc_auto_sync_to_hr.auto_sync_id table. |
| REQUEST_NUMBER | VARCHAR2 | 64 |  |  | To store the HDL submission request number( Latest Request Number) |
| CONTENT_ID | VARCHAR2 | 60 |  |  | To store the Content ID returned from UCM after uploading the document. |
| CONTENT_UPLOAD_ERROR | VARCHAR2 | 4000 |  |  | To store any Error message while uploading to Content Server |
| HDL_SUBMIT_ERROR | VARCHAR2 | 4000 |  |  | To store any Error message while submitting a HDL Request |
| HDL_PROCESSING_ERROR | CLOB |  |  |  | To store any Error message while processing a HDL Request |
| OFFER_ACCEPT_ERROR | VARCHAR2 | 4000 |  |  | To store any Error message while Accepting an Offer via API |
| HDL_INPUT_JSON | CLOB |  |  |  | To store Json with Input Parameters sent to HDL |
| GHR_API_INPUT_JSON | CLOB |  |  |  | To store Json with Input Parameters sent to GHR |
| GHR_API_OUTPUT_JSON | CLOB |  |  |  | To store Json with Output Parameters received from GHR |
| GHR_API_ERROR | VARCHAR2 | 4000 |  |  | To store GHR API Error Message. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AUTO_SYNC_TO_HR_TRACK_FK1 | Non Unique | Default | AUTO_SYNC_ID |
| IRC_AUTO_SYNC_TO_HR_TRACK_PK | Unique | Default | AUTO_SYNC_TRACKING_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
