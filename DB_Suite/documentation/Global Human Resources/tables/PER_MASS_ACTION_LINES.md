# PER_MASS_ACTION_LINES

Stores changes done by a Mass Action. Each line corresponds to a specific set of changes done to a logical object.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permassactionlines-15428.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permassactionlines-15428.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_MASS_ACTION_LINES_PK | MASS_ACTION_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MASS_ACTION_LINE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| MASS_ACTION_HEADER_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_MASS_ACTION_HEADER table. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LINE_STATUS | VARCHAR2 | 30 |  |  | Identifies whether the record included in the mass update has been processed or in error. |
| LINE_TYPE | VARCHAR2 | 30 |  |  | Identifies whether line represents the mass update change or a mass update member line. |
| LEVEL_NAME_01 | VARCHAR2 | 200 |  |  | The name of a View Object on that AM (required by BatchLoader). |
| DESTINATION_AM_NAME | VARCHAR2 | 200 |  |  | The name of the AM including full classpath. |
| DESTINATION_AM_CONFIG_NAME | VARCHAR2 | 200 |  |  | The config to use with the AM, fro example MassActionsAMShared |
| PVAL001 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL002 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL003 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL004 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL005 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL006 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL007 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL008 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL009 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL010 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL011 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL012 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL013 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL014 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL015 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL016 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL017 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL018 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL019 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL020 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL021 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL022 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL023 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL024 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL025 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL026 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL027 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL028 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL029 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL030 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL031 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL032 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL033 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL034 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL035 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL036 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL037 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL038 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL039 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL040 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL041 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL042 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL043 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL044 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL045 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL046 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL047 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL048 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL049 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL050 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL051 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL052 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL053 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL054 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL055 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL056 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL057 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL058 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL059 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL060 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL061 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL062 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL063 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL064 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL065 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL066 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL067 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL068 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL069 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL070 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL071 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL072 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL073 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL074 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL075 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL076 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL077 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL078 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL079 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL080 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL081 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL082 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL083 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL084 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL085 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL086 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL087 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL088 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL089 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL090 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL091 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL092 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL093 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL094 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL095 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL096 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL097 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL098 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL099 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL100 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL101 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL102 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL103 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL104 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL105 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL106 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL107 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL108 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL109 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL110 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL111 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL112 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL113 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL114 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL115 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL116 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL117 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL118 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL119 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL120 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL121 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL122 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL123 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL124 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL125 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL126 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL127 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL128 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL129 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL130 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL131 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL132 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL133 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL134 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL135 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL136 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL137 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL138 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL139 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL140 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL141 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL142 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL143 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL144 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL145 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL146 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL147 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL148 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL149 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL150 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL151 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL152 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL153 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL154 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL155 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL156 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL157 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL158 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL159 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL160 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL161 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL162 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL163 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL164 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL165 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL166 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL167 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL168 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL169 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL170 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL171 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL172 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL173 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL174 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL175 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL176 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL177 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL178 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL179 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL180 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL181 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL182 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL183 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL184 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL185 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL186 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL187 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL188 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL189 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL190 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL191 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL192 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL193 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL194 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL195 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL196 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL197 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL198 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL199 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL200 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL201 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL202 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL203 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL204 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL205 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL206 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL207 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL208 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL209 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL210 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL211 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL212 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL213 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL214 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL215 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL216 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL217 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL218 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL219 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL220 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL221 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL222 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL223 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL224 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL225 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL226 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL227 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL228 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL229 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PVAL230 | VARCHAR2 | 2000 |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE001 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE002 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE003 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE004 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE005 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE006 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE007 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE008 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE009 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE010 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE011 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE012 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE013 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE014 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE015 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE016 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE017 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE018 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE019 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE020 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE021 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE022 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE023 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE024 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE025 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE026 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE027 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE028 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE029 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| PDATE030 | DATE |  |  |  | Descriptive field used by Batch Loader: Used to hold parameter values |
| LOADER_BATCH_ID | NUMBER |  | 18 |  | Identifies the batch processed by batch loader. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_MASS_ACTION_LINES_N1 | Non Unique | Default | MASS_ACTION_HEADER_ID |
| PER_MASS_ACTION_LINES_PK | Unique | Default | MASS_ACTION_LINE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
