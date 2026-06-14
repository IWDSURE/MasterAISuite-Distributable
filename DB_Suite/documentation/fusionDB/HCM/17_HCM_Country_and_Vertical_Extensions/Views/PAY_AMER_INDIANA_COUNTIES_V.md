# PAY_AMER_INDIANA_COUNTIES_V

## Details

**Schema:** FUSION

**Object owner:** HRX

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payamerindianacountiesv-7664.html#payamerindianacountiesv-7664](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payamerindianacountiesv-7664.html#payamerindianacountiesv-7664)

## Columns

- COUNTYCITY
- GEOCODE

## Query

```sql
select substr(initcap(city.geography_element3),1,50) || ', '|| substr(initcap(city.geography_name),1,50) CountyCity, substr(geo.identifier_value,1,50) GeoCode from hz_geographies city, hz_geography_identifiers state_name_ident ,hz_geography_identifiers geo where city.geography_type = 'CITY' and city.country_code = 'US' and city.geography_use = 'MASTER_REF' and city.geography_element2_code = 'IN' and city.geography_element2_id = state_name_ident.geography_id and state_name_ident.identifier_subtype ='STANDARD_NAME' and state_name_ident.primary_flag='Y' and city.geography_id = geo.geography_id and geo.identifier_subtype ='GEO_CODE' and geo.primary_flag='N' and geo.LANGUAGE_CODE='US' and geo.IDENTIFIER_TYPE='CODE'
```

---

[← Back to Index](../17_HCM_Country_and_Vertical_Extensions_Views_Index.md)
