# HWR_FLW_AUTHENTICATION

This table stores the authentication related information that user can input from data integration admin UI

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrflwauthentication-8644.html#hwrflwauthentication-8644](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrflwauthentication-8644.html#hwrflwauthentication-8644)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_FLW_AUTHENTICATION_PK | SOURCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SOURCE_ID | NUMBER |  | 18 | Yes | This is the primary key for this table. |
| HOST_URL | VARCHAR2 | 512 |  | Yes | The social media host URL. |
| OAUTH_VERSION | VARCHAR2 | 32 |  | Yes | The OAuth version. |
| REQUEST_URL | VARCHAR2 | 512 |  |  | The social media request token URL. |
| AUTHORIZATION_URL | VARCHAR2 | 512 |  |  | The social media authorization URL. |
| SCOPES | VARCHAR2 | 4000 |  |  | The social media authorization scopes. |
| RESPONSE_TYPE | VARCHAR2 | 32 |  |  | The response type parameter value for authorization. |
| ACCESS_TOKEN_URL | VARCHAR2 | 512 |  |  | The social media access token URL. |
| GRANT_TYPE | VARCHAR2 | 32 |  |  | The grant type parameter value for token request. |
| CALLBACK_URL_PARAMETER | VARCHAR2 | 512 |  |  | The callback URL parameter to distinguish the actual opt in social media. |
| PROFILE_REQUEST_URL | VARCHAR2 | 512 |  |  | The social media REST URL to get user profile. |
| PROFILE_REQUEST_PARAMETER | VARCHAR2 | 512 |  |  | The social media REST URL paramenter to get user profile. |
| AUTH_ATTR_1 | VARCHAR2 | 512 |  |  | AUTH_ATTR_1. This is the extra attribute in case if needed. |
| AUTH_ATTR_2 | VARCHAR2 | 512 |  |  | AUTH_ATTR_2. This is the extra attribute in case if needed. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_FLW_AUTHENTICATION_U1 | Unique | Default | SOURCE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
