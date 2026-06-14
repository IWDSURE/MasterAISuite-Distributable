# HXT_GEOFENCES_VL

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtgeofencesvl-7538.html#hxtgeofencesvl-7538](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtgeofencesvl-7538.html#hxtgeofencesvl-7538)

## Columns

- GEOFENCE_ID
- CODE
- NAME
- DESCRIPTION
- LOCATION_ID
- GEOMETRY
- RADIUS
- REF_LATITUDE
- REF_LONGITUDE
- SOURCE
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT gbt.GEOFENCE_ID, gbt.CODE, gtl.NAME, gtl.DESCRIPTION, gbt.LOCATION_ID, gbt.GEOMETRY, gbt.RADIUS, gbt.REF_LATITUDE, gbt.REF_LONGITUDE, gbt.SOURCE, gbt.OBJECT_VERSION_NUMBER, gbt.CREATED_BY, gbt.CREATION_DATE, gbt.LAST_UPDATED_BY, gbt.LAST_UPDATE_DATE, gbt.LAST_UPDATE_LOGIN FROM HXT_GEOFENCES_B gbt, HXT_GEOFENCES_TL gtl WHERE gbt.GEOFENCE_ID = gtl.GEOFENCE_ID AND gtl.LANGUAGE = userenv('LANG')
```

---

[← Back to Index](../26_Time_and_Labor_Views_Index.md)
