# HRC_LOADER_BATCH_LINES

This table contains the data for a batch load.  Each row of data in this table will become a Fusion object.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloaderbatchlines-7359.html#hrcloaderbatchlines-7359](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloaderbatchlines-7359.html#hrcloaderbatchlines-7359)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_LOADER_BATCH_LINES_PK | BATCH_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_LINE_ID | NUMBER |  | 18 | Yes | BATCH_LINE_ID |
| LOADER_BATCH_ID | NUMBER |  | 18 | Yes | LOADER_BATCH_ID |
| REQUEST_LINE_ID | NUMBER |  | 18 | Yes | REQUEST_LINE_ID |
| RUN_ID | NUMBER |  | 5 |  | RUN_ID |
| LINK_VALUE | NUMBER |  | 18 |  | LINK_VALUE |
| USER_SEQUENCE | NUMBER |  | 18 |  | USER_SEQUENCE |
| PROCESS_SEQUENCE | NUMBER |  | 18 |  | PROCESS_SEQUENCE |
| CHUNK_NUM | NUMBER |  | 10 |  | CHUNK_NUM |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LINE_ACTION | VARCHAR2 | 200 |  |  | LINE_ACTION |
| LINE_STATUS | VARCHAR2 | 200 |  |  | LINE_STATUS |
| CURRENT_LEVEL | NUMBER |  | 18 |  | CURRENT_LEVEL |
| NOTES | VARCHAR2 | 2000 |  |  | NOTES |
| ITEM_EFF_START_DATE | DATE |  |  |  | ITEM_EFF_START_DATE |
| ITEM_EFF_END_DATE | DATE |  |  |  | ITEM_EFF_END_DATE |
| ITEM_EFF_SEQ | NUMBER |  | 18 |  | ITEM_EFF_SEQ |
| ITEM_EFF_SEQ_FLAG | VARCHAR2 | 30 |  |  | ITEM_EFF_SEQ_FLAG |
| LEVEL_ID_01 | NUMBER |  | 18 |  | LEVEL_ID_01 |
| LEVEL_ID_02 | NUMBER |  | 18 |  | LEVEL_ID_02 |
| LEVEL_ID_03 | NUMBER |  | 18 |  | LEVEL_ID_03 |
| LEVEL_ID_04 | NUMBER |  | 18 |  | LEVEL_ID_04 |
| LEVEL_ID_05 | NUMBER |  | 18 |  | LEVEL_ID_05 |
| LEVEL_ID_06 | NUMBER |  | 18 |  | LEVEL_ID_06 |
| LEVEL_ID_07 | NUMBER |  | 18 |  | LEVEL_ID_07 |
| LEVEL_ID_08 | NUMBER |  | 18 |  | LEVEL_ID_08 |
| LEVEL_ID_09 | NUMBER |  | 18 |  | LEVEL_ID_09 |
| LEVEL_ID_10 | NUMBER |  | 18 |  | LEVEL_ID_10 |
| LEVEL_NAME_01 | VARCHAR2 | 200 |  |  | LEVEL_NAME_01 |
| LEVEL_NAME_02 | VARCHAR2 | 200 |  |  | LEVEL_NAME_02 |
| LEVEL_NAME_03 | VARCHAR2 | 200 |  |  | LEVEL_NAME_03 |
| LEVEL_NAME_04 | VARCHAR2 | 200 |  |  | LEVEL_NAME_04 |
| LEVEL_NAME_05 | VARCHAR2 | 200 |  |  | LEVEL_NAME_05 |
| LEVEL_NAME_06 | VARCHAR2 | 200 |  |  | LEVEL_NAME_06 |
| LEVEL_NAME_07 | VARCHAR2 | 200 |  |  | LEVEL_NAME_07 |
| LEVEL_NAME_08 | VARCHAR2 | 200 |  |  | LEVEL_NAME_08 |
| LEVEL_NAME_09 | VARCHAR2 | 200 |  |  | LEVEL_NAME_09 |
| LEVEL_NAME_10 | VARCHAR2 | 200 |  |  | LEVEL_NAME_10 |
| LEVEL_ALT_KEY_01 | VARCHAR2 | 200 |  |  | LEVEL_ALT_KEY_01 |
| LEVEL_ALT_KEY_02 | VARCHAR2 | 200 |  |  | LEVEL_ALT_KEY_02 |
| LEVEL_ALT_KEY_03 | VARCHAR2 | 200 |  |  | LEVEL_ALT_KEY_03 |
| LEVEL_ALT_KEY_04 | VARCHAR2 | 200 |  |  | LEVEL_ALT_KEY_04 |
| LEVEL_ALT_KEY_05 | VARCHAR2 | 200 |  |  | LEVEL_ALT_KEY_05 |
| LEVEL_ALT_KEY_06 | VARCHAR2 | 200 |  |  | LEVEL_ALT_KEY_06 |
| LEVEL_ALT_KEY_07 | VARCHAR2 | 200 |  |  | LEVEL_ALT_KEY_07 |
| LEVEL_ALT_KEY_08 | VARCHAR2 | 200 |  |  | LEVEL_ALT_KEY_08 |
| LEVEL_ALT_KEY_09 | VARCHAR2 | 200 |  |  | LEVEL_ALT_KEY_09 |
| LEVEL_ALT_KEY_10 | VARCHAR2 | 200 |  |  | LEVEL_ALT_KEY_10 |
| DESTINATION_AM_NAME | VARCHAR2 | 200 |  |  | DESTINATION_AM_NAME |
| DESTINATION_AM_CONFIG_NAME | VARCHAR2 | 200 |  |  | DESTINATION_AM_CONFIG_NAME |
| PVAL001 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL002 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL003 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL004 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL005 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL006 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL007 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL008 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL009 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL010 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL011 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL012 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL013 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL014 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL015 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL016 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL017 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL018 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL019 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL020 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL021 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL022 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL023 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL024 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL025 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL026 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL027 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL028 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL029 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL030 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL031 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL032 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL033 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL034 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL035 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL036 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL037 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL038 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL039 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL040 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL041 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL042 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL043 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL044 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL045 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL046 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL047 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL048 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL049 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL050 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL051 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL052 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL053 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL054 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL055 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL056 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL057 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL058 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL059 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL060 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL061 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL062 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL063 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL064 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL065 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL066 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL067 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL068 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL069 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL070 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL071 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL072 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL073 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL074 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL075 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL076 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL077 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL078 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL079 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL080 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL081 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL082 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL083 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL084 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL085 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL086 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL087 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL088 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL089 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL090 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL091 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL092 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL093 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL094 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL095 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL096 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL097 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL098 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL099 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL100 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL101 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL102 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL103 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL104 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL105 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL106 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL107 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL108 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL109 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL110 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL111 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL112 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL113 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL114 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL115 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL116 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL117 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL118 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL119 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL120 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL121 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL122 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL123 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL124 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL125 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL126 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL127 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL128 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL129 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL130 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL131 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL132 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL133 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL134 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL135 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL136 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL137 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL138 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL139 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL140 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL141 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL142 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL143 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL144 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL145 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL146 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL147 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL148 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL149 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL150 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL151 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL152 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL153 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL154 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL155 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL156 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL157 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL158 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL159 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL160 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL161 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL162 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL163 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL164 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL165 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL166 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL167 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL168 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL169 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL170 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL171 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL172 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL173 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL174 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL175 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL176 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL177 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL178 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL179 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL180 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL181 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL182 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL183 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL184 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL185 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL186 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL187 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL188 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL189 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL190 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL191 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL192 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL193 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL194 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL195 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL196 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL197 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL198 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL199 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL200 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL201 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL202 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL203 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL204 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL205 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL206 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL207 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL208 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL209 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL210 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL211 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL212 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL213 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL214 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL215 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL216 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL217 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL218 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL219 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL220 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL221 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL222 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL223 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL224 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL225 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL226 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL227 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL228 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL229 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PVAL230 | VARCHAR2 | 2000 |  |  | Contains an attribute of information to be stored in a mapped column on the target table. |
| PDATE001 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE002 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE003 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE004 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE005 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE006 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE007 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE008 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE009 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE010 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE011 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE012 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE013 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE014 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE015 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE016 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE017 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE018 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE019 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE020 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE021 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE022 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE023 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE024 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE025 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE026 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE027 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE028 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE029 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PDATE030 | DATE |  |  |  | Contains an attribute of date information to be stored in a mapped column on the target table. |
| PLONGVAL001 | VARCHAR2 | 2000 |  |  | PLONGVAL001 |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 20 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE_CHAR1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| JOB_ID | NUMBER |  | 18 |  | Job Id |
| CHANGED | VARCHAR2 | 30 |  |  | Indicates that batch row line has changed. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ORA_PART_KEY | DATE |  |  | Yes | The partition key used to determine the range interval. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_LOADER_BATCH_LINES_N1 | Non Unique | Default | LOADER_BATCH_ID, REQUEST_ID |
| HRC_LOADER_BATCH_LINES_N2 | Non Unique | Default | LOADER_BATCH_ID, CHUNK_NUM |
| HRC_LOADER_BATCH_LINES_N3 | Non Unique | Default | LOADER_BATCH_ID, LINE_STATUS |
| HRC_LOADER_BATCH_LINES_N4 | Non Unique | Default | LOADER_BATCH_ID, LEVEL_ID_01 |
| HRC_LOADER_BATCH_LINES_N5 | Non Unique | Default | LOADER_BATCH_ID, CURRENT_LEVEL |
| HRC_LOADER_BATCH_LINES_N6 | Non Unique | Default | LEVEL_ID_03, LOADER_BATCH_ID |
| HRC_LOADER_BATCH_LINES_PK | Unique | Default | BATCH_LINE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
