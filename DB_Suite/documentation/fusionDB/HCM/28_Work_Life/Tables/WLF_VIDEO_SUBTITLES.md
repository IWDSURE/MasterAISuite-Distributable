# WLF_VIDEO_SUBTITLES

Table for storing subtitles associated with a video

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfvideosubtitles-22931.html#wlfvideosubtitles-22931](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfvideosubtitles-22931.html#wlfvideosubtitles-22931)

## Primary Key

| Name | Columns |
|------|----------|
| wlf_video_subtitles_PK | VIDEO_SUBTITLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VIDEO_SUBTITLE_ID | NUMBER |  | 18 | Yes | Video subtitle id |
| CONTENT_ID | NUMBER |  | 18 |  | Video content id |
| SUBTITLE_LANGUAGE | VARCHAR2 | 20 |  |  | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SUBTITLES | CLOB |  |  |  | Video subtitles |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_VIDEO_SUBTITLES_U1 | Unique | wlf_video_subtitles_U1 | CONTENT_ID, SUBTITLE_LANGUAGE |
| WLF_VIDEO_SUBTITLES_U2 | Unique | WLF_VIDEO_SUBTITLES_U2 | VIDEO_SUBTITLE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
