# PAY_BANK_ACCNT_DETAILS_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybankaccntdetailsvl-4014.html#paybankaccntdetailsvl-4014](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybankaccntdetailsvl-4014.html#paybankaccntdetailsvl-4014)

## Columns

- ACCOUNT_TYPE
- BANK_ACCOUNT_ID
- BANK_ACCOUNT_NAME
- BANK_ACCOUNT_NAME_ALT
- BANK_ACCOUNT_NUM
- MASKED_ACCOUNT_NUM
- BANK_ACCOUNT_NUM_ELECTRONIC
- CHECK_DIGITS
- CURRENCY_CODE
- ACCOUNT_DESCRIPTION
- SECONDARY_ACCOUNT_REFERENCE
- ACCOUNT_START_DATE
- MASKED_IBAN
- IBAN_NUMBER
- ACCOUNT_END_DATE
- RECON_DIFFERENCE_CCID
- RECON_RULESET_ID
- RECON_START_DATE
- GL_CUR_EXC_RATE_TYPE
- BANK_ID
- BANK_NAME
- BANK_HOME_COUNTRY
- BANK_NUMBER
- BANK_CODE
- BRANCH_ID
- BANK_BRANCH_NAME
- BRANCH_NUMBER
- BRANCH_DESCRIPTION
- EFT_SWIFT_CODE
- EFT_USER_NUMBER
- EDI_ID_NUMBER
- EDI_LOCATION
- RFC
- BANK_ACCOUNT_TYPE

## Query

```sql
SELECT 'INTERNAL' account_type, IBA.BANK_ACCOUNT_ID BANK_ACCOUNT_ID, IBA.BANK_ACCOUNT_NAME, IBA.BANK_ACCOUNT_NAME_ALT, IBA.BANK_ACCOUNT_NUM, IBA.MASKED_ACCOUNT_NUM, IBA.BANK_ACCOUNT_NUM_ELECTRONIC, IBA.CHECK_DIGITS, IBA.CURRENCY_CODE, IBA.DESCRIPTION account_description , IBA.SECONDARY_ACCOUNT_REFERENCE, IBA.START_DATE account_start_date, IBA.MASKED_IBAN, IBA.IBAN_NUMBER iban_number, IBA.END_DATE account_end_date, IBA.RECON_DIFFERENCE_CCID, IBA.RECON_RULESET_ID, IBA.RECON_START_DATE, IBA.GL_CUR_EXC_RATE_TYPE, bankparty.party_id bank_id, bankparty.party_name bank_name, bankorgprofile.home_country bank_home_country, bankorgprofile.bank_or_branch_number bank_number, branchorgprofile.bank_code bank_code, branchparty.party_id branch_id, branchparty.party_name bank_branch_name, branchorgprofile.bank_or_branch_number branch_number, branchparty.mission_statement branch_description, branchcp.eft_swift_code eft_swift_code, branchcp.eft_user_number eft_user_number, edicp.edi_id_number edi_id_number, edicp.edi_ece_tp_location_code edi_location, rfcca.class_code rfc, IBA.bank_account_type bank_account_type FROM CE_BANK_ACCOUNTS IBA, hz_parties bankparty, hz_organization_profiles bankorgprofile, hz_code_assignments BankCA, hz_parties branchparty, hz_organization_profiles branchorgprofile, hz_contact_points branchcp, hz_contact_points edicp, hz_code_assignments rfcca WHERE IBA.PAY_USE_ALLOWED_FLAG = 'Y' AND IBA.ACCOUNT_CLASSIFICATION = 'INTERNAL' AND IBA.BANK_ID =BankParty.PARTY_ID AND NVL(IBA.NETTING_ACCT_FLAG, 'N') = 'N' AND BankCA.CLASS_CATEGORY = 'BANK_INSTITUTION_TYPE' AND BankCA.CLASS_CODE IN ('BANK', 'CLEARINGHOUSE','EMPLOYEE_BANK') AND BankCA.OWNER_TABLE_NAME = 'HZ_PARTIES' AND BankCA.OWNER_TABLE_ID = BankParty.PARTY_ID AND TRUNC(SYSDATE) BETWEEN TRUNC(bankorgprofile.effective_start_date) AND NVL(TRUNC(bankorgprofile.effective_end_date),TRUNC(SYSDATE) + 1) AND bankorgprofile.party_id = BankParty.PARTY_ID AND bankparty.party_type = 'ORGANIZATION' AND IBA.BANK_BRANCH_ID =branchparty.party_id AND branchparty.party_type = 'ORGANIZATION' AND branchparty.status = 'A' AND branchorgprofile.party_id = branchparty.party_id AND TRUNC(SYSDATE) BETWEEN TRUNC(branchorgprofile.effective_start_date) AND NVL(TRUNC(branchorgprofile.effective_end_date), TRUNC(SYSDATE) + 1) AND branchcp.owner_table_name (+) = 'HZ_PARTIES' AND branchcp.owner_table_id (+) = branchparty.party_id AND branchcp.contact_point_type (+) = 'EFT' AND edicp.owner_table_name (+) = 'HZ_PARTIES' AND edicp.owner_table_id (+) = branchparty.party_id AND edicp.contact_point_type (+) = 'EDI' AND rfcca.owner_table_name (+) = 'HZ_PARTIES' AND rfcca.owner_table_id (+) = branchparty.party_id AND rfcca.class_category (+) = 'RFC_IDENTIFIER' UNION SELECT 'EXTERNAL' account_type, EBA.EXT_BANK_ACCOUNT_ID BANK_ACCOUNT_ID, EBA.BANK_ACCOUNT_NAME, EBA.BANK_ACCOUNT_NAME_ALT, EBA.BANK_ACCOUNT_NUM, EBA.MASKED_BANK_ACCOUNT_NUM, EBA.BANK_ACCOUNT_NUM_ELECTRONIC, EBA.CHECK_DIGITS, EBA.CURRENCY_CODE, EBA.DESCRIPTION , EBA.SECONDARY_ACCOUNT_REFERENCE, EBA.START_DATE, EBA.MASKED_IBAN, EBA.iban iban_number, EBA.END_DATE, NULL, NULL, NULL, NULL, bankparty.party_id bank_id, bankparty.party_name bank_name, bankorgprofile.home_country bank_home_country, bankorgprofile.bank_or_branch_number bank_number, branchorgprofile.bank_code bank_code, branchparty.party_id branch_id, branchparty.party_name bank_branch_name, branchorgprofile.bank_or_branch_number branch_number, branchparty.mission_statement description, branchcp.eft_swift_code eft_swift_code, branchcp.eft_user_number eft_user_number, edicp.edi_id_number edi_id_number, edicp.edi_ece_tp_location_code edi_location, rfcca.class_code rfc, EBA.bank_account_type bank_account_type FROM IBY_EXT_BANK_ACCOUNTS EBA, hz_parties bankparty, hz_organization_profiles bankorgprofile, hz_code_assignments BankCA, hz_parties branchparty, hz_organization_profiles branchorgprofile, hz_contact_points branchcp, hz_contact_points edicp, hz_code_assignments rfcca WHERE EBA.bank_id =BankParty.PARTY_ID AND BankCA.CLASS_CATEGORY = 'BANK_INSTITUTION_TYPE' AND BankCA.CLASS_CODE IN ('BANK', 'CLEARINGHOUSE','EMPLOYEE_BANK') AND BankCA.OWNER_TABLE_NAME = 'HZ_PARTIES' AND BankCA.OWNER_TABLE_ID = BankParty.PARTY_ID AND TRUNC(SYSDATE) BETWEEN TRUNC(bankorgprofile.effective_start_date) AND NVL(TRUNC(bankorgprofile.effective_end_date),TRUNC(SYSDATE) + 1) AND bankorgprofile.party_id = BankParty.PARTY_ID AND bankparty.party_type = 'ORGANIZATION' AND EBA.BRANCH_ID =branchparty.party_id AND branchparty.party_type = 'ORGANIZATION' AND branchparty.status = 'A' AND branchorgprofile.party_id = branchparty.party_id AND TRUNC(SYSDATE) BETWEEN TRUNC(branchorgprofile.effective_start_date) AND NVL(TRUNC(branchorgprofile.effective_end_date), TRUNC(SYSDATE) + 1) AND branchcp.owner_table_name (+) = 'HZ_PARTIES' AND branchcp.owner_table_id (+) = branchparty.party_id AND branchcp.contact_point_type (+) = 'EFT' AND edicp.owner_table_name (+) = 'HZ_PARTIES' AND edicp.owner_table_id (+) = branchparty.party_id AND edicp.contact_point_type (+) = 'EDI' AND rfcca.owner_table_name (+) = 'HZ_PARTIES' AND rfcca.owner_table_id (+) = branchparty.party_id AND rfcca.class_category (+) = 'RFC_IDENTIFIER'
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
