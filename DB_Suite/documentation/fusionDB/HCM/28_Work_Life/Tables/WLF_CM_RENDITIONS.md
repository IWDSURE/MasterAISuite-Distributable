# WLF_CM_RENDITIONS

Table to store of video renditions.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcmrenditions-3824.html#wlfcmrenditions-3824](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcmrenditions-3824.html#wlfcmrenditions-3824)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_CM_RENDITIONS_PK | RENDITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RENDITION_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| CONTENT_ID | NUMBER |  | 18 | Yes | Parent/video content entity id. |
| DESCRIPTOR | CLOB |  |  |  | Descriptor of the video rendition. |
| PLAYLIST | CLOB |  |  |  | Play-list information of the video rendition. |
| LOCATION | VARCHAR2 | 1024 |  |  | External storage source URL for the video rendition. |
| NUMBER_OF_SEGMENTS | NUMBER |  | 18 |  | Number of segments/chunks in the video rendition. |
| DURATION | NUMBER |  | 18 |  | The duration of the video rendition in seconds. |
| FRAME_WIDTH | NUMBER |  | 18 |  | Frame width in pixels of the video rendition. |
| FRAME_HEIGHT | NUMBER |  | 18 |  | Frame height in pixels of the video rendition. |
| VIDEO_PROTOCOL | VARCHAR2 | 32 |  |  | Protocol of the video rendition. |
| VIDEO_FORMAT | VARCHAR2 | 32 |  |  | Format of the video rendition. |
| VIDEO_CODEC | VARCHAR2 | 32 |  |  | Codec of the video rendition. |
| VIDEO_BITRATE | NUMBER |  | 18 |  | Bit-rate of the video rendition. |
| FRAME_RATE | NUMBER |  | 18 |  | Frame rate in fps of the video rendition. |
| AUDIO_FORMAT | VARCHAR2 | 32 |  |  | Audio format of the video rendition. |
| AUDIO_CODEC | VARCHAR2 | 32 |  |  | Audio codec of the video rendition. |
| AUDIO_BITRATE | NUMBER |  | 18 |  | Audio bit-rate in kbps of the video rendition. |
| AUDIO_CHANNELS | NUMBER |  | 18 |  | Number of audio channels of the video rendition. |
| AUDIO_SAMPLE_RATE | NUMBER |  | 18 |  | Audio sample rate in Hz of the video rendition. |
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
| WLF_CM_RENDITIONS_N1 | Non Unique | Default | CONTENT_ID |
| WLF_CM_RENDITIONS_PK | Unique | Default | RENDITION_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
