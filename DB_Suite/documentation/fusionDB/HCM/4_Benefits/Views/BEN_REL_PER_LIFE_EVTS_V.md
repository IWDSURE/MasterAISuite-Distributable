# BEN_REL_PER_LIFE_EVTS_V

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benrelperlifeevtsv-4438.html#benrelperlifeevtsv-4438](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benrelperlifeevtsv-4438.html#benrelperlifeevtsv-4438)

## Columns

- PERSON_ID
- CONTACT_PERSON_ID
- FULL_NAME
- NAME
- LER_ID
- LF_EVT_OCRD_DT
- NTFN_DT
- PTNL_LER_FOR_PER_STAT_CD
- LER_TYPE_CD

## Query

```sql
SELECT csr.person_id, csr.contact_person_id, ppf.full_name, ler.name, ler.ler_id, pil.lf_evt_ocrd_dt,pil.ntfn_dt, pil.ptnl_ler_for_per_stat_cd, pil.ler_type_cd FROM PER_CONTACT_RELSHIPS_F csr, PER_PERSON_NAMES_F_V ppf, ben_ptnl_ler_for_per pil, ben_ler_f ler WHERE ppf.person_id = csr.contact_person_id and csr.personal_flag = 'Y' and pil.ler_id = ler.ler_id and pil.person_id = csr.contact_person_id and pil.business_group_id = csr.business_group_id and ler.business_group_id = csr.business_group_id and pil.ptnl_ler_for_per_stat_cd in ( 'DTCTD', 'UNPROCD') and csr.existing_person<>'PENDING' and pil.lf_evt_ocrd_dt between ppf.effective_start_date and ppf.effective_end_date and pil.lf_evt_ocrd_dt between ler.effective_start_date and ler.effective_end_date and pil.lf_evt_ocrd_dt between csr.effective_start_date and csr.effective_end_date
```

---

[← Back to Index](../4_Benefits_Views_Index.md)
