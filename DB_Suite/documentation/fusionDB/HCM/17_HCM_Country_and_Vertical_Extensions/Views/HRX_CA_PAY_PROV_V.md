# HRX_CA_PAY_PROV_V

## Details

**Schema:** FUSION

**Object owner:** HRX

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrxcapayprovv-5123.html#hrxcapayprovv-5123](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrxcapayprovv-5123.html#hrxcapayprovv-5123)

## Columns

- CODE
- MEANING

## Query

```sql
SELECT to_number(substr(geo_code.IDENTIFIER_VALUE,instr(geo_code.IDENTIFIER_VALUE,'-',1)+1,(instr(geo_code.IDENTIFIER_VALUE,'-',-1)-(instr(geo_code.IDENTIFIER_VALUE,'-',1)))-1)) code, us.IDENTIFIER_VALUE meaning FROM HZ_GEOGRAPHY_IDENTIFIERS us, HZ_GEOGRAPHY_IDENTIFIERS geo_code WHERE geo_code.GEOGRAPHY_ID = us.GEOGRAPHY_ID AND us.GEOGRAPHY_ID IN (select GEOGRAPHY_ID from HZ_GEOGRAPHIES where COUNTRY_CODE = 'CA' AND GEOGRAPHY_TYPE = 'PROVINCE' AND GEOGRAPHY_USE = 'MASTER_REF') AND us.IDENTIFIER_SUBTYPE = 'STANDARD_NAME' AND us.IDENTIFIER_TYPE = 'NAME' AND us.PRIMARY_FLAG = 'Y' AND geo_code.IDENTIFIER_TYPE = 'CODE' AND geo_code.GEOGRAPHY_USE = 'MASTER_REF' AND geo_code.IDENTIFIER_SUBTYPE = 'GEO_CODE' AND geo_code.GEOGRAPHY_TYPE = 'PROVINCE' UNION SELECT area2 code, geography_name meaning FROM PAY_AMER_GEOGRAPHIES WHERE geography_type ='INTERNATIONAL' and legislation_code ='CA'
```

---

[← Back to Index](../17_HCM_Country_and_Vertical_Extensions_Views_Index.md)
