# HRC_ALERT_RES_FILTER_EXPRS_VL

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertresfilterexprsvl-3660.html#hrcalertresfilterexprsvl-3660](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertresfilterexprsvl-3660.html#hrcalertresfilterexprsvl-3660)

## Columns

- ALERT_ID
- EXPRESSIONID
- FILTERID
- EXPRNAME
- EXPRVALUE

## Query

```sql
SELECT a.alert_id, f.expressionid, f.filterid, f.exprname, f.exprvalue FROM hrc_alerts_b a, XMLTABLE ( '/ResourceFilters/ResourceFilter/FilterExpression' PASSING xmltype(a.filter_expressions) COLUMNS expressionid NUMBER(18) PATH 'ExpressionId', filterid NUMBER(18) PATH 'FilterId', exprname VARCHAR2(200) PATH 'ExprName', exprvalue VARCHAR2(4000) PATH 'ExprValue' ) f WHERE filter_type = 'ORA_XML' AND alert_type = 'ORA_R' UNION SELECT po.alert_id, f.expressionid, f.filterid, f.exprname, f.exprvalue FROM hrc_alerts_b po, JSON_TABLE ( po.filter_expressions, '$' COLUMNS ( NESTED PATH '$.ResourceFilters.ResourceFilter[*]' COLUMNS ( filterid NUMBER PATH '$.FilterId', resourcepath VARCHAR ( 400 ) PATH '$.ResourcePath', conjunction VARCHAR ( 400 ) PATH '$.Conjunction', NESTED PATH '$.FilterExpression[*]' COLUMNS ( expressionid NUMBER ( 18 ) PATH '$.ExpressionId', exprname VARCHAR ( 200 ) PATH '$.ExprName', exprvalue VARCHAR ( 4000 ) PATH '$.ExprValue' ) ) ) ) AS f WHERE filter_type = 'ORA_JSON' AND alert_type = 'ORA_R'
```

---

[← Back to Index](../14_HCM_Common_Views_Index.md)
