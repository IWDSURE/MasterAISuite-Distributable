# HRC_SDL_USER_LAYOUT_ROLES_V

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdluserlayoutrolesv-5859.html#hrcsdluserlayoutrolesv-5859](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdluserlayoutrolesv-5859.html#hrcsdluserlayoutrolesv-5859)

## Columns

- LAYOUT_ID
- LAYOUTVISIBILITY
- LAYOUTOPERATIONS

## Query

```sql
SELECT layoutroles.layout_id , listagg (layoutroles.datasetvisibility, ' ') WITHIN GROUP (ORDER BY layout_id) layoutvisibility , listagg (layoutroles.layoutoperations, ' ') WITHIN GROUP (ORDER BY layout_id) layoutoperations FROM ( SELECT lyt.layout_id , roleval.roleid , lmaps.role_id sdlroleid ,lmaps.ROLE_MAPPING_ID , roleval.username , (decode (lmaps.view_all_data_sets, 'Y' , decode (roleval.roleid, NULL , 'ORA_VIEW_USER', 'ORA_VIEW_ALL'), 'ORA_VIEW_USER')) datasetvisibility , decode(lmaps.create_data_set,'Y',decode (roleval.roleid, NULL , '', 'ORA_CREATE'),'')||' '||decode(lmaps.save_data_set,'Y',decode (roleval.roleid, NULL , '', 'ORA_SAVE'),'')||' '||decode(lmaps.UPLOAD_DATA_SET,'Y',decode (roleval.roleid, NULL , '', 'ORA_UPLOAD'),'')||' '||decode(lmaps.ROLLBACK_DATA_SET,'Y',decode (roleval.roleid, NULL , '', 'ORA_ROLLBACK'),'') layoutoperations FROM hrc_dl_layouts_b lyt , hrc_sdl_layout_role_map lmaps , ( SELECT u.username , u.user_id , prd.role_common_name , prdtl.role_name , ur.role_id roleid FROM per_users u , per_user_roles ur , per_roles_dn prd , per_roles_dn_tl prdtl WHERE u.user_id = hrc_session_util.get_userid AND u.user_id = ur.user_id AND trunc (sysdate) BETWEEN ur.start_date AND nvl (ur.end_date, trunc (sysdate)) AND ur.role_id = prd.role_id AND prd.active_flag = 'Y' AND prd.role_id = prdtl.role_id AND prdtl.language = userenv ('LANG') ) roleval WHERE lyt.layout_id = lmaps.layout_id AND lmaps.active_status = 'Y' AND roleval.roleid = lmaps.role_id (+) ) layoutroles GROUP BY layoutroles.layout_id
```

---

[← Back to Index](../14_HCM_Common_Views_Index.md)
