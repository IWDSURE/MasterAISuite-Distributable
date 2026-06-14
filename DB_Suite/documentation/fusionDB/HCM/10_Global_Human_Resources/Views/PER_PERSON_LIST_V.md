# PER_PERSON_LIST_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersonlistv-5642.html#perpersonlistv-5642](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersonlistv-5642.html#perpersonlistv-5642)

## Columns

- ID
- VALUE
- DESCRIPTION

## Query

```sql
SELECT to_char(pn.person_id) AS id, pn.list_name AS value, '(' || p.person_number || ') ' || '(' || l.meaning || ') ' || CASE WHEN j.name IS NOT NULL THEN j.name || ' - ' END || CASE WHEN a.assignment_number <> a.assignment_name THEN a.assignment_number || ' - ' || a.assignment_name ELSE a.assignment_number END || decode(pn.legislation_code, NULL, '', ' (' || pn.legislation_code || ')') description FROM per_person_names_f pn, LATERAL ( SELECT * FROM ( SELECT person_id, assignment_number, assignment_name, job_id, assignment_status_type, ROW_NUMBER() OVER(PARTITION BY person_id ORDER BY decode(assignment_status_type, 'ACTIVE', '1', 'SUSPENDED', '2', '3' || assignment_status_type), effective_end_date DESC, effective_start_date DESC, ROWID ) rn FROM per_all_assignments_m a WHERE pn.person_id = a.person_id AND primary_flag = 'Y' AND assignment_type IN ( 'E', 'C' ) AND trunc(sysdate) BETWEEN effective_start_date AND effective_end_date AND effective_latest_change = 'Y' ) WHERE rn = 1 ) a, per_all_people_f p, per_jobs_f_vl j, hcm_lookups l WHERE pn.person_id = p.person_id AND pn.name_type = 'GLOBAL' AND ( trunc(sysdate) BETWEEN pn.effective_start_date AND pn.effective_end_date ) AND ( trunc(sysdate) BETWEEN p.effective_start_date AND p.effective_end_date ) AND a.job_id = j.job_id (+) AND ( trunc(sysdate) BETWEEN j.effective_start_date (+) AND j.effective_end_date (+) ) AND l.lookup_type (+) = 'PER_ASS_SYS_STATUS' AND a.assignment_status_type = l.lookup_code (+)
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
