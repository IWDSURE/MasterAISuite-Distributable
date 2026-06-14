# HR_LOCATIONS_ALL_VL

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrlocationsallvl-3830.html#hrlocationsallvl-3830](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrlocationsallvl-3830.html#hrlocationsallvl-3830)

## Columns

- ROW_ID
- LOCATION_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- SET_ID
- LOCATION_IMAGE_URL
- INTERNAL_LOCATION_CODE
- BUSINESS_GROUP_ID
- LOCATION_CODE
- LOCATION_NAME
- DESCRIPTION
- AC_LOCATION_CODE
- ACTIVE_STATUS
- EMAIL_ADDRESS
- OFFICIAL_LANGUAGE_CODE
- SHIP_TO_LOCATION_ID
- SHIP_TO_SITE_FLAG
- RECEIVING_SITE_FLAG
- BILL_TO_SITE_FLAG
- OFFICE_SITE_FLAG
- DESIGNATED_RECEIVER_ID
- INVENTORY_ORGANIZATION_ID
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
- GEO_HIERARCHY_NODE_ID
- GEO_HIERARCHY_NODE_VALUE
- ADDRESS_ID
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
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
( SELECT loc.rowid row_id, loc.location_id, loc.effective_start_date, loc.effective_end_date, loa.set_id, loa.location_image_url, loa.internal_location_code, loa.business_group_id, lot.location_code, lot.location_name, lot.description, lot.ac_location_code, loc.active_status, loc.email_address, loc.official_language_code, loc.ship_to_location_id, loc.ship_to_site_flag, loc.receiving_site_flag, loc.bill_to_site_flag, loc.office_site_flag, loc.designated_receiver_id, loc.inventory_organization_id, loc.telephone_number_1, loc.mainphone_country_code1, loc.mainphone_area_code1, loc.mainphone_subscriber_num1, loc.mainphone_extension1, loc.telephone_number_2, loc.fax_country_code2, loc.fax_area_code2, loc.fax_subscriber_num2, loc.fax_extension2, loc.telephone_number_3, loc.otherphone_country_code3, loc.otherphone_area_code3, loc.otherphone_subscriber_num3, loc.otherphone_extension3, loc.geo_hierarchy_node_id, loc.geo_hierarchy_node_value, addr.address_id, addr.country style, addr.address_line_1, addr.address_line_2, addr.address_line_3, addr.address_line_4, addr.building, addr.floor_number, addr.country, addr.postal_code, addr.long_postal_code, addr.region_1, addr.region_2, addr.region_3, addr.town_or_city, addr.derived_locale, addr.geometry, addr.addl_address_attribute1 loc_information13, addr.addl_address_attribute2 loc_information14, addr.addl_address_attribute3 loc_information15, addr.addl_address_attribute4 loc_information16, addr.addl_address_attribute5 loc_information17, null loc_information18, null loc_information19, null loc_information20, null loc_information21, null loc_information22, null add_information11, null add_information12, null add_information13, null add_information14, null add_information15, null add_information16, null add_information17, null add_information18, null add_information19, null add_information20, addr.timezone_code, loc.attribute_category, loc.attribute1, loc.attribute2, loc.attribute3, loc.attribute4, loc.attribute5, loc.attribute6, loc.attribute7, loc.attribute8, loc.attribute9, loc.attribute10, loc.attribute11, loc.attribute12, loc.attribute13, loc.attribute14, loc.attribute15, loc.attribute16, loc.attribute17, loc.attribute18, loc.attribute19, loc.attribute20, loc.attribute21, loc.attribute22, loc.attribute23, loc.attribute24, loc.attribute25, loc.attribute26, loc.attribute27, loc.attribute28, loc.attribute29, loc.attribute30, loc.object_version_number, loc.created_by, loc.creation_date, loc.last_updated_by, loc.last_update_date, loc.last_update_login FROM per_location_details_f loc , per_location_details_f_tl lot,per_locations loa,per_addresses_f addr WHERE loc.location_id = loa.location_id AND loc.location_details_id = lot.location_details_id AND loc.effective_start_date = lot.effective_start_date AND loc.effective_end_date = lot.effective_end_date AND lot.language = userenv('LANG') and loc.main_address_id= addr.address_id AND loc.effective_start_date = addr.effective_start_date AND loc.effective_end_date = addr.effective_end_date AND TRUNC(sysdate) BETWEEN loc.effective_start_date and loc.effective_end_date)
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
