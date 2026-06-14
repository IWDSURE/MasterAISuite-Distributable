# HR_LOCATIONS

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrlocations-5501.html#hrlocations-5501](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrlocations-5501.html#hrlocations-5501)

## Columns

- LOCATION_DETAILS_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- OBJECT_VERSION_NUMBER
- BUSINESS_GROUP_ID
- ACTIVE_STATUS
- LOCATION_ID
- MAIN_ADDRESS_ID
- TELEPHONE_NUMBER_1
- MAINPHONE_COUNTRY_CODE1
- MAINPHONE_AREA_CODE1
- MAINPHONE_SUBSCRIBER_NUM1
- MAINPHONE_EXTENSION1
- TELEPHONE_NUMBER_2
- FAX_COUNTRY_CODE2
- FAX_AREA_CODE2
- FAX_SUBSCRIBER_NUM2
- FAX_EXTENSION2
- TELEPHONE_NUMBER_3
- OTHERPHONE_COUNTRY_CODE3
- OTHERPHONE_AREA_CODE3
- OTHERPHONE_SUBSCRIBER_NUM3
- OTHERPHONE_EXTENSION3
- OFFICIAL_LANGUAGE_CODE
- EMAIL_ADDRESS
- SHIP_TO_SITE_FLAG
- SHIP_TO_LOCATION_ID
- RECEIVING_SITE_FLAG
- BILL_TO_SITE_FLAG
- OFFICE_SITE_FLAG
- INVENTORY_ORGANIZATION_ID
- DESIGNATED_RECEIVER_ID
- GEO_HIERARCHY_NODE_ID
- GEO_HIERARCHY_NODE_VALUE
- ACTION_OCCURRENCE_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- ATTRIBUTE_CATEGORY
- ATTRIBUTE1
- ATTRIBUTE2
- ATTRIBUTE3
- ATTRIBUTE4
- ATTRIBUTE5
- ATTRIBUTE6
- ATTRIBUTE7
- ATTRIBUTE8
- ATTRIBUTE9
- ATTRIBUTE10
- ATTRIBUTE11
- ATTRIBUTE12
- ATTRIBUTE13
- ATTRIBUTE14
- ATTRIBUTE15
- ATTRIBUTE16
- ATTRIBUTE17
- ATTRIBUTE18
- ATTRIBUTE19
- ATTRIBUTE20
- ATTRIBUTE21
- ATTRIBUTE22
- ATTRIBUTE23
- ATTRIBUTE24
- ATTRIBUTE25
- ATTRIBUTE26
- ATTRIBUTE27
- ATTRIBUTE28
- ATTRIBUTE29
- ATTRIBUTE30
- SET_ID
- LOCATION_IMAGE_URL
- INTERNAL_LOCATION_CODE
- LOCATION_USE
- LOCATION_CODE
- LOCATION_NAME
- DESCRIPTION
- AC_LOCATION_CODE
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
- LOC_INFORMATION13
- LOC_INFORMATION14
- LOC_INFORMATION15
- LOC_INFORMATION16
- LOC_INFORMATION17
- LOC_INFORMATION18
- LOC_INFORMATION19
- LOC_INFORMATION20
- LOC_INFORMATION21
- LOC_INFORMATION22
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
( SELECT loc."LOCATION_DETAILS_ID",loc."EFFECTIVE_START_DATE",loc."EFFECTIVE_END_DATE",loc."OBJECT_VERSION_NUMBER",loc."BUSINESS_GROUP_ID",loc."ACTIVE_STATUS",loc."LOCATION_ID",loc."MAIN_ADDRESS_ID",loc."TELEPHONE_NUMBER_1",loc."MAINPHONE_COUNTRY_CODE1",loc."MAINPHONE_AREA_CODE1",loc."MAINPHONE_SUBSCRIBER_NUM1",loc."MAINPHONE_EXTENSION1",loc."TELEPHONE_NUMBER_2",loc."FAX_COUNTRY_CODE2",loc."FAX_AREA_CODE2",loc."FAX_SUBSCRIBER_NUM2",loc."FAX_EXTENSION2",loc."TELEPHONE_NUMBER_3",loc."OTHERPHONE_COUNTRY_CODE3",loc."OTHERPHONE_AREA_CODE3",loc."OTHERPHONE_SUBSCRIBER_NUM3",loc."OTHERPHONE_EXTENSION3",loc."OFFICIAL_LANGUAGE_CODE",loc."EMAIL_ADDRESS",loc."SHIP_TO_SITE_FLAG",loc."SHIP_TO_LOCATION_ID",loc."RECEIVING_SITE_FLAG",loc."BILL_TO_SITE_FLAG",loc."OFFICE_SITE_FLAG",loc."INVENTORY_ORGANIZATION_ID",loc."DESIGNATED_RECEIVER_ID",loc."GEO_HIERARCHY_NODE_ID",loc."GEO_HIERARCHY_NODE_VALUE",loc."ACTION_OCCURRENCE_ID",loc."CREATED_BY",loc."CREATION_DATE",loc."LAST_UPDATED_BY",loc."LAST_UPDATE_DATE",loc."LAST_UPDATE_LOGIN",loc."ATTRIBUTE_CATEGORY",loc."ATTRIBUTE1",loc."ATTRIBUTE2",loc."ATTRIBUTE3",loc."ATTRIBUTE4",loc."ATTRIBUTE5",loc."ATTRIBUTE6",loc."ATTRIBUTE7",loc."ATTRIBUTE8",loc."ATTRIBUTE9",loc."ATTRIBUTE10",loc."ATTRIBUTE11",loc."ATTRIBUTE12",loc."ATTRIBUTE13",loc."ATTRIBUTE14",loc."ATTRIBUTE15",loc."ATTRIBUTE16",loc."ATTRIBUTE17",loc."ATTRIBUTE18",loc."ATTRIBUTE19",loc."ATTRIBUTE20",loc."ATTRIBUTE21",loc."ATTRIBUTE22",loc."ATTRIBUTE23",loc."ATTRIBUTE24",loc."ATTRIBUTE25",loc."ATTRIBUTE26",loc."ATTRIBUTE27",loc."ATTRIBUTE28",loc."ATTRIBUTE29",loc."ATTRIBUTE30", loa.set_id, loa.location_image_url, loa.internal_location_code, 'HR' location_use, lot.location_code, lot.location_name, lot.description, lot.ac_location_code, addr.country style, addr.address_line_1, addr.address_line_2, addr.address_line_3, addr.address_line_4, addr.building, addr.floor_number, addr.country, addr.postal_code, addr.long_postal_code, addr.region_1, addr.region_2, addr.region_3, addr.town_or_city, addr.derived_locale, addr.geometry, addr.addl_address_attribute1 loc_information13, addr.addl_address_attribute2 loc_information14, addr.addl_address_attribute3 loc_information15, addr.addl_address_attribute4 loc_information16, addr.addl_address_attribute5 loc_information17, null loc_information18, null loc_information19, null loc_information20, null loc_information21, null loc_information22, null add_information11, null add_information12, null add_information13, null add_information14, null add_information15, null add_information16, null add_information17, null add_information18, null add_information19, null add_information20, addr.timezone_code FROM per_location_details_f loc , per_location_details_f_tl lot,per_locations loa,per_addresses_f addr WHERE loc.location_id = loa.location_id AND loc.location_details_id = lot.location_details_id AND loc.effective_start_date = lot.effective_start_date AND loc.effective_end_date = lot.effective_end_date AND lot.language = userenv('LANG') AND TRUNC(sysdate) BETWEEN loc.effective_start_date and loc.effective_end_date and loc.main_address_id= addr.address_id AND loc.effective_start_date = addr.effective_start_date AND loc.effective_end_date = addr.effective_end_date)
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
