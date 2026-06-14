# BEN_DIAG_FF_ATCHMNT_G11_V

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendiagffatchmntg11v-8054.html#bendiagffatchmntg11v-8054](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendiagffatchmntg11v-8054.html#bendiagffatchmntg11v-8054)

## Columns

- Object Name
- Object Type
- Table Name
- Column Name
- Formula Name
- Formula Id
- Formula Type Name
- Formula Type Id
- Effective Start Date
- Effective End Date
- Enterprise ID

## Query

```sql
SELECT NAME "Object Name", 'Derived Factor' "Object Type", 'BEN_AGE_FCTR' "Table Name", 'AGE_CALC_RL' "Column Name", FFL.FORMULA_NAME "Formula Name", FFL.FORMULA_ID "Formula Id", FFT.FORMULA_TYPE_NAME "Formula Type Name", FFT.FORMULA_TYPE_ID "Formula Type Id", TO_DATE(NULL) "Effective Start Date", To_DATE(NULL) "Effective End Date", FFL.ENTERPRISE_ID "Enterprise ID" FROM BEN_AGE_FCTR AGF, FF_FORMULAS_F FFL, FF_FORMULA_TYPES FFT WHERE AGF.AGE_CALC_RL=FFL.FORMULA_ID AND FFL.FORMULA_TYPE_ID=FFT.FORMULA_TYPE_ID UNION ALL SELECT NAME "Object Name", 'Derived Factor' "Object Type", 'BEN_AGE_FCTR' "Table Name", 'AGE_DET_RL' "Column Name", FFL.FORMULA_NAME "Formula Name", FFL.FORMULA_ID "Formula Id", FFT.FORMULA_TYPE_NAME "Formula Type Name", FFT.FORMULA_TYPE_ID "Formula Type Id", TO_DATE(NULL) "Effective Start Date", TO_DATE(NULL) "Effective End Date", FFL.ENTERPRISE_ID "Enterprise ID" FROM BEN_AGE_FCTR AGF, FF_FORMULAS_F FFL, FF_FORMULA_TYPES FFT WHERE AGF.AGE_DET_RL=FFL.FORMULA_ID AND FFL.FORMULA_TYPE_ID=FFT.FORMULA_TYPE_ID UNION ALL SELECT NAME "Object Name", 'Derived Factor' "Object Type", 'BEN_COMP_LVL_FCTR' "Table Name", 'COMP_CALC_RL' "Column Name", FFL.FORMULA_NAME "Formula Name", FFL.FORMULA_ID "Formula Id", FFT.FORMULA_TYPE_NAME "Formula Type Name", FFT.FORMULA_TYPE_ID "Formula Type Id", TO_DATE(NULL) "Effective Start Date", TO_DATE(NULL) "Effective End Date", FFL.ENTERPRISE_ID "Enterprise ID" FROM BEN_COMP_LVL_FCTR CLF, FF_FORMULAS_F FFL, FF_FORMULA_TYPES FFT WHERE CLF.COMP_CALC_RL=FFL.FORMULA_ID AND FFL.FORMULA_TYPE_ID=FFT.FORMULA_TYPE_ID UNION ALL SELECT NAME "Object Name", 'Derived Factor' "Object Type", 'BEN_COMP_LVL_FCTR' "Table Name", 'COMP_LVL_DET_RL' "Column Name", FFL.FORMULA_NAME "Formula Name", FFL.FORMULA_ID "Formula Id", FFT.FORMULA_TYPE_NAME "Formula Type Name", FFT.FORMULA_TYPE_ID "Formula Type Id", TO_DATE(NULL) "Effective Start Date", TO_DATE(NULL) "Effective End Date", FFL.ENTERPRISE_ID "Enterprise ID" FROM BEN_COMP_LVL_FCTR CLF, FF_FORMULAS_F FFL, FF_FORMULA_TYPES FFT WHERE CLF.COMP_LVL_DET_RL=FFL.FORMULA_ID AND FFL.FORMULA_TYPE_ID=FFT.FORMULA_TYPE_ID UNION ALL SELECT NAME "Object Name", 'Eligy Prfl' "Object Type", 'BEN_ELIG_SCHEDD_HRS_PRTE' "Table Name", 'SCHEDD_HRS_RL' "Column Name", FFL.FORMULA_NAME "Formula Name", FFL.FORMULA_ID "Formula Id", FFT.FORMULA_TYPE_NAME "Formula Type Name", FFT.FORMULA_TYPE_ID "Formula Type Id", TO_DATE(NULL) "Effective Start Date", TO_DATE(NULL) "Effective End Date", FFL.ENTERPRISE_ID "Enterprise ID" FROM BEN_ELIGY_PRFL ELP,BEN_ELIG_SCHEDD_HRS_PRTE ESHP, FF_FORMULAS_F FFL, FF_FORMULA_TYPES FFT WHERE ELP.ELIGY_PRFL_ID=ESHP.ELIGY_PRFL_ID AND ESHP.SCHEDD_HRS_RL=FFL.FORMULA_ID AND FFL.FORMULA_TYPE_ID=FFT.FORMULA_TYPE_ID UNION ALL SELECT NAME "Object Name", 'Derived Factor' "Object Type", 'BEN_HRS_WKD_IN_PERD_FCTR' "Table Name", 'HRS_WKD_CALC_RL' "Column Name", FFL.FORMULA_NAME "Formula Name", FFL.FORMULA_ID "Formula Id", FFT.FORMULA_TYPE_NAME "Formula Type Name", FFT.FORMULA_TYPE_ID "Formula Type Id", TO_DATE(NULL) "Effective Start Date", TO_DATE(NULL) "Effective End Date", FFL.ENTERPRISE_ID "Enterprise ID" FROM BEN_HRS_WKD_IN_PERD_FCTR HWF,FF_FORMULAS_F FFL, FF_FORMULA_TYPES FFT WHERE HWF.HRS_WKD_CALC_RL=FFL.FORMULA_ID AND FFL.FORMULA_TYPE_ID=FFT.FORMULA_TYPE_ID UNION ALL SELECT NAME "Object Name", 'Derived Factor' "Object Type", 'BEN_HRS_WKD_IN_PERD_FCTR' "Table Name", 'HRS_WKD_DET_RL' "Column Name", FFL.FORMULA_NAME "Formula Name", FFL.FORMULA_ID "Formula Id", FFT.FORMULA_TYPE_NAME "Formula Type Name", FFT.FORMULA_TYPE_ID "Formula Type Id", TO_DATE(NULL) "Effective Start Date", TO_DATE(NULL) "Effective End Date", FFL.ENTERPRISE_ID "Enterprise ID" FROM BEN_HRS_WKD_IN_PERD_FCTR HWF,FF_FORMULAS_F FFL, FF_FORMULA_TYPES FFT WHERE HWF.HRS_WKD_DET_RL=FFL.FORMULA_ID AND FFL.FORMULA_TYPE_ID=FFT.FORMULA_TYPE_ID UNION ALL SELECT NAME "Object Name", 'Derived Factor' "Object Type", 'BEN_LOS_FCTR' "Table Name", 'LOS_CALC_RL' "Column Name", FFL.FORMULA_NAME "Formula Name", FFL.FORMULA_ID "Formula Id", FFT.FORMULA_TYPE_NAME "Formula Type Name", FFT.FORMULA_TYPE_ID "Formula Type Id", TO_DATE(NULL) "Effective Start Date", TO_DATE(NULL) "Effective End Date", FFL.ENTERPRISE_ID "Enterprise ID" FROM BEN_LOS_FCTR LOS,FF_FORMULAS_F FFL, FF_FORMULA_TYPES FFT WHERE LOS.LOS_CALC_RL=FFL.FORMULA_ID AND FFL.FORMULA_TYPE_ID=FFT.FORMULA_TYPE_ID UNION ALL SELECT NAME "Object Name", 'Derived Factor' "Object Type", 'BEN_LOS_FCTR' "Table Name", 'LOS_DET_RL' "Column Name", FFL.FORMULA_NAME "Formula Name", FFL.FORMULA_ID "Formula Id", FFT.FORMULA_TYPE_NAME "Formula Type Name", FFT.FORMULA_TYPE_ID "Formula Type Id", TO_DATE(NULL) "Effective Start Date", TO_DATE(NULL) "Effective End Date", FFL.ENTERPRISE_ID "Enterprise ID" FROM BEN_LOS_FCTR LOS,FF_FORMULAS_F FFL, FF_FORMULA_TYPES FFT WHERE LOS.LOS_DET_RL=FFL.FORMULA_ID AND FFL.FORMULA_TYPE_ID=FFT.FORMULA_TYPE_ID UNION ALL SELECT NAME "Object Name", 'Derived Factor' "Object Type", 'BEN_LOS_FCTR' "Table Name", 'LOS_DT_TO_USE_RL' "Column Name", FFL.FORMULA_NAME "Formula Name", FFL.FORMULA_ID "Formula Id", FFT.FORMULA_TYPE_NAME "Formula Type Name", FFT.FORMULA_TYPE_ID "Formula Type Id", TO_DATE(NULL) "Effective Start Date", TO_DATE(NULL) "Effective End Date", FFL.ENTERPRISE_ID "Enterprise ID" FROM BEN_LOS_FCTR LOS,FF_FORMULAS_F FFL, FF_FORMULA_TYPES FFT WHERE LOS.LOS_DT_TO_USE_RL=FFL.FORMULA_ID AND FFL.FORMULA_TYPE_ID=FFT.FORMULA_TYPE_ID
```

---

[← Back to Index](../4_Benefits_Views_Index.md)
