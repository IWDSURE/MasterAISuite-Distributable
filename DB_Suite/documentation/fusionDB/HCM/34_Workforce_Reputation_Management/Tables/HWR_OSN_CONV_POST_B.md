# HWR_OSN_CONV_POST_B

This table will be used to store information regarding Posts in the OSN conversations used in Like subcomponent of Ask the Question feature.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrosnconvpostb-11601.html#hwrosnconvpostb-11601](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrosnconvpostb-11601.html#hwrosnconvpostb-11601)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_OSN_CONV_POST_B_PK | OSN_ID, POST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OSN_ID | VARCHAR2 | 100 |  | Yes | This is the ID of the OSN conversation for the OSN Post Like feature in the Ask a Question feature. |
| POST_ID | VARCHAR2 | 100 |  | Yes | This is the Post Id associated with the OSN conversation. |
| PRFL_ID | VARCHAR2 | 500 |  | Yes | This is the Fusion Id of the person who published  the post. |
| LIKE_COUNT | NUMBER |  | 18 | Yes | Number of people who have liked this post for the corresponding OSN conversation. |
| CONV_POST_ATTR_1 | VARCHAR2 | 100 |  |  | CONV_POST_ATTR_1. This is the extra attribute in case if needed. |
| CONV_POST_ATTR_2 | VARCHAR2 | 100 |  |  | CONV_POST_ATTR_2. This is the extra attribute in case if needed. |
| CONV_POST_ATTR_3 | VARCHAR2 | 100 |  |  | CONV_POST_ATTR_3. This is the extra attribute in case if needed. |
| CONV_POST_ATTR_4 | VARCHAR2 | 100 |  |  | CONV_POST_ATTR_4. This is the extra attribute in case if needed. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_OSN_CONV_POST_B_N1 | Non Unique | Default | PRFL_ID |
| HWR_OSN_CONV_POST_B_N2 | Non Unique | Default | POST_ID |
| HWR_OSN_CONV_POST_B_U1 | Unique | Default | OSN_ID, POST_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
