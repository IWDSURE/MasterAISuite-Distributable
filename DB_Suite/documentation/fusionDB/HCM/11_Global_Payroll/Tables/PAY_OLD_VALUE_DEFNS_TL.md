# PAY_OLD_VALUE_DEFNS_TL

This table contains translation information for PAY_VALUE_DEFINITIONS_F.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payoldvaluedefnstl-4677.html#payoldvaluedefnstl-4677](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payoldvaluedefnstl-4677.html#payoldvaluedefnstl-4677)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_VALUE_DEFINITIONS_TL_PK | VALUE_DEFN_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VALUE_DEFN_ID | NUMBER |  | 18 | Yes | VALUE_DEFN_ID |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 120 |  | Yes | NAME |
| DISPLAY_TAG | VARCHAR2 | 256 |  |  | DISPLAY_TAG |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_OLD_VALUE_DEFNS_TL_PK | Unique | Default | VALUE_DEFN_ID, LANGUAGE |
| PAY_VALUE_DEFINITIONS_TL_N1 | Non Unique | Default | UPPER("NAME"), LANGUAGE |
| PAY_VALUE_DEFINITIONS_TL_N2 | Non Unique | Default | NAME, LANGUAGE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
