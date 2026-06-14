# CMP_PLAN_ACCESS_RESTRICT_V

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpplanaccessrestrictv-6189.html#cmpplanaccessrestrictv-6189](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpplanaccessrestrictv-6189.html#cmpplanaccessrestrictv-6189)

## Columns

- PLAN_ID
- ACCESS_CODE
- ROLE_TYPE

## Query

```sql
select plan_access.plan_id plan_id, min(plan_access.access_code) access_code, plan_access.role_type role_type from cmp_plan_access plan_access, per_roles_dn per_roles, fnd_session_roles fnd_roles, cmp_plans_b aplans where plan_access.comp_type = 'CWB' and plan_access.role_guid = per_roles.role_guid and per_roles.role_common_name = fnd_roles.role_name and fnd_roles.session_id = fnd_global.session_id and plan_access.custom_id is null and plan_access.plan_id = aplans.plan_id and NVL(aplans.plan_security_enabled_flag, 'N') = 'Y' group by plan_access.plan_id, plan_access.role_type UNION select plans.plan_id plan_id, 'FULL_ACCESS' access_code, plan_access.role_type role_type from cmp_plans_b plans, (select 'M' role_type from dual union select 'A' role_type from dual union select 'I' role_type from dual) plan_access where plans.comp_type = 'CWB' and nvl(plans.plan_security_enabled_flag, 'N') = 'N'
```

---

[← Back to Index](../7_Compensation_Views_Index.md)
