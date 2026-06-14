# PER_LOC_OTHER_ADDRESSES_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocotheraddressesv-3657.html#perlocotheraddressesv-3657](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocotheraddressesv-3657.html#perlocotheraddressesv-3657)

## Columns

- LOCATION_ID
- ADDRESS_ID
- LOC_ADDRESS_USAGE_ID
- ADDRESS_USAGE_TYPE
- BUSINESS_GROUP_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- STYLE
- ADDRESS_LINE_1
- ADDRESS_LINE_2
- ADDRESS_LINE_3
- ADDRESS_LINE_4
- BUILDING
- FLOOR_NUMBER
- COUNTRY
- POSTAL_CODE
- LONG_POSTAL_CODE
- REGION_1
- REGION_2
- REGION_3
- TOWN_OR_CITY
- DERIVED_LOCALE
- GEOMETRY
- ADD_INFORMATION1
- ADD_INFORMATION2
- ADD_INFORMATION3
- ADD_INFORMATION4
- ADD_INFORMATION5
- ADD_INFORMATION6
- ADD_INFORMATION7
- ADD_INFORMATION8
- ADD_INFORMATION9
- ADD_INFORMATION10
- ADD_INFORMATION11
- ADD_INFORMATION12
- ADD_INFORMATION13
- ADD_INFORMATION14
- ADD_INFORMATION15
- ADD_INFORMATION16
- ADD_INFORMATION17
- ADD_INFORMATION18
- ADD_INFORMATION19
- ADD_INFORMATION20
- TIMEZONE_CODE

## Query

```sql
( SELECT usadd.location_id, usadd.address_id, usadd.loc_address_usage_id, usadd.address_usage_type, usadd.business_group_id, usadd.effective_start_date, usadd.effective_end_date, addr.country style, addr.address_line_1, addr.address_line_2, addr.address_line_3, addr.address_line_4, addr.building, addr.floor_number, addr.country, addr.postal_code, addr.long_postal_code, addr.region_1, addr.region_2, addr.region_3, addr.town_or_city, addr.derived_locale, addr.geometry, addr.addl_address_attribute1 add_information1, addr.addl_address_attribute2 add_information2, addr.addl_address_attribute3 add_information3, addr.addl_address_attribute4 add_information4, addr.addl_address_attribute5 add_information5, null add_information6, null add_information7, null add_information8, null add_information9, null add_information10, null add_information11, null add_information12, null add_information13, null add_information14, null add_information15, null add_information16, null add_information17, null add_information18, null add_information19, null add_information20, addr.timezone_code FROM per_addresses_f addr, per_loc_address_usages_f usadd WHERE usadd.address_id = addr.address_id AND usadd.effective_start_date = addr.effective_start_date AND usadd.effective_end_date = addr.effective_end_date and usadd.address_usage_type!='MAIN')
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
