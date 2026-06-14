# WLF_LI_VIDEOS_F

Table to store of technical details of learning item of type videos.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflivideosf-12170.html#wlflivideosf-12170](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflivideosf-12170.html#wlflivideosf-12170)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_VIDEOS_F_PK | VIDEO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VIDEO_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LEARNING_ITEM_ID | NUMBER |  | 18 |  | LEARNING_ITEM_ID |
| CONTENT_ID | NUMBER |  | 18 |  | CONTENT_ID |
| VIDEO_MEDIA_STATUS | VARCHAR2 | 30 |  |  | VIDEO_MEDIA_STATUS |
| THUMBNAIL_EXTRACTION_STATUS | VARCHAR2 | 30 |  |  | THUMBNAIL_EXTRACTION_STATUS |
| ENCRYPTION_KEY | VARCHAR2 | 100 |  |  | ENCRYPTION_KEY |
| PROVIDER_ID | NUMBER |  | 18 |  | Transcoding provider identifier. |
| FRAME_RATE | NUMBER |  | 18 |  | Frame rate in fps of the video. |
| FRAME_WIDTH | NUMBER |  | 18 |  | Frame width in pixels of the video. |
| FRAME_HEIGHT | NUMBER |  | 18 |  | Frame height in pixels of the video. |
| VIDEO_CODEC | VARCHAR2 | 32 |  |  | Video codec of the video. |
| VIDEO_BITRATE | NUMBER |  | 18 |  | Video bit-rate of the video. |
| VIDEO_TRANSCODING_QUAL | VARCHAR2 | 30 |  |  | Video transcoding quality selector |
| SCREEN_CAPTURE_FLAG | CHAR | 1 |  |  | Indicates if the video mostly contains screen captures |
| AUDIO_CODEC | VARCHAR2 | 32 |  |  | Audio codec of the video. |
| AUDIO_BITRATE | NUMBER |  | 18 |  | Audio bit-rate in kbps of the video. |
| AUDIO_CHANNELS | NUMBER |  | 18 |  | Number of audio channels of the video. |
| AUDIO_SAMPLE_RATE | NUMBER |  | 18 |  | Audio sample rate in Hz of the video. |
| ORIGINAL_FILE_NAME | VARCHAR2 | 200 |  |  | Original file name of video. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| STORAGE_LOCATION | VARCHAR2 | 4000 |  |  | This column to store location of Storage server path where actual content (Video/Image) available |
| STORAGE_PROVIDER | VARCHAR2 | 64 |  |  | This column represents Storage server name where  actual content (Video/Image) is stored. Example Akamai, UCM etc |
| STREAMING_PROVIDER | VARCHAR2 | 64 |  |  | The stream packaging provider of the video. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_VIDEOS_F_N1 | Non Unique | Default | VIDEO_MEDIA_STATUS |
| WLF_LI_VIDEOS_F_N2 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_LI_VIDEOS_F_N3 | Non Unique | WLF_LI_VIDEOS_F_N3 | CONTENT_ID |
| WLF_LI_VIDEOS_F_U1 | Unique | Default | VIDEO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
