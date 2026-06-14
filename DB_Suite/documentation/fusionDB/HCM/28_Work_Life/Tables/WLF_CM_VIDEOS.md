# WLF_CM_VIDEOS

Table to store technical details of videos.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcmvideos-5132.html#wlfcmvideos-5132](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcmvideos-5132.html#wlfcmvideos-5132)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_CM_VIDEOS_PK | CONTENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTENT_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| PROVIDER_ID | NUMBER |  | 18 |  | Transcoding provider identifier. |
| VIDEO_STATUS | VARCHAR2 | 24 |  |  | Video processing status. {NEW, UPLOADED, TRANSCODING, COMPLETE, ERROR, CANCELLED} |
| THUMBNAILS_STATUS | VARCHAR2 | 24 |  |  | Video thumnails status: {NEW, TRANSCODING, COMPLETE, ERROR, CANCELLED} |
| LOCATION | VARCHAR2 | 1024 |  |  | External storage source URL of the video. |
| SOURCE_NAME | VARCHAR2 | 64 |  |  | Source name of the video. |
| PLAYLIST_NAME | VARCHAR2 | 64 |  |  | Playlist name of the video. |
| DURATION | NUMBER |  | 18 |  | The duration of the video in seconds. |
| DESCRIPTOR | CLOB |  |  |  | Descriptor information of the video. |
| PLAYLIST | CLOB |  |  |  | Play-list inforamtion of the video. |
| KEY_STORE | VARCHAR2 | 512 |  |  | The key(s) for protected content of the video. |
| FRAME_RATE | NUMBER |  | 18 |  | Frame rate in fps of the video. |
| FRAME_WIDTH | NUMBER |  | 18 |  | Frame width in pixels of the video. |
| FRAME_HEIGHT | NUMBER |  | 18 |  | Frame height in pixels of the video. |
| VIDEO_FORMAT | VARCHAR2 | 32 |  |  | Video format of the video. |
| VIDEO_CODEC | VARCHAR2 | 32 |  |  | Video codec of the video. |
| VIDEO_BITRATE | NUMBER |  | 18 |  | Video bit-rate of the video. |
| AUDIO_FORMAT | VARCHAR2 | 32 |  |  | Audio format of the video. |
| AUDIO_CODEC | VARCHAR2 | 32 |  |  | Audio codec of the video. |
| AUDIO_BITRATE | NUMBER |  | 18 |  | Audio bit-rate in kbps of the video. |
| AUDIO_CHANNELS | NUMBER |  | 18 |  | Number of audio channels of the video. |
| AUDIO_SAMPLE_RATE | NUMBER |  | 18 |  | Audio sample rate in Hz of the video. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_CM_VIDEOS_N1 | Non Unique | Default | VIDEO_STATUS |
| WLF_CM_VIDEOS_N2 | Non Unique | Default | THUMBNAILS_STATUS |
| WLF_CM_VIDEOS_PK | Unique | Default | CONTENT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
