# HRC_ALERT_RES_FILTERS_VL

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertresfiltersvl-3262.html#hrcalertresfiltersvl-3262](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertresfiltersvl-3262.html#hrcalertresfiltersvl-3262)

## Columns

- ALERT_ID
- FILTERID
- RESOURCEPATH
- CONJUNCTION

## Query

```sql
SELECT a.alert_id, f.filterid, f.resourcepath, f.conjunction FROM hrc_alerts_b a, XMLTABLE ( '/ResourceFilters/ResourceFilter' PASSING xmltype(a.filter_expressions) COLUMNS filterid NUMBER(18) PATH 'FilterId', resourcepath VARCHAR2(200) PATH 'ResourcePath', conjunction VARCHAR2(20) PATH 'Conjunction' ) f WHERE filter_type = 'ORA_XML' AND alert_type = 'ORA_R' UNION SELECT po.alert_id, f.filterid, f.resourcepath, f.conjunction FROM hrc_alerts_b po, JSON_TABLE ( po.filter_expressions, '$' COLUMNS ( NESTED PATH '$.ResourceFilters.ResourceFilter[*]' COLUMNS ( filterid NUMBER PATH '$.FilterId', resourcepath VARCHAR ( 200 ) PATH '$.ResourcePath', conjunction VARCHAR ( 20 ) PATH '$.Conjunction' ) ) ) AS f WHERE filter_type = 'ORA_JSON' AND alert_type = 'ORA_R'
```

---

[← Back to Index](../14_HCM_Common_Views_Index.md)
