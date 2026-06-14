# HRMS Tables Documentation Extractor - Usage Guide

## Overview

This script extracts complete documentation for Oracle Fusion HRMS tables from Oracle's documentation website and generates local markdown files.

## Input Format

The script now accepts a simple text file containing URLs, one per line.

### Creating the URLs File

Create a file named `urlsList.txt` (or any name you prefer) with the following format:

```text
# Comments start with #
# Empty lines are ignored

https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/tablename1-12345.html
https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/tablename2-67890.html
https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/tablename3-11111.html
```

**Rules:**
- One URL per line
- Lines starting with `#` are treated as comments
- Empty lines are ignored
- No special formatting required

## Usage Examples

### Basic Usage (uses default urlsList.txt)
```bash
python extract_hrms_tables_v2.py
```

### Specify Custom URLs File
```bash
python extract_hrms_tables_v2.py --urls-file payroll_tables.txt
```

### Test URL Extraction (without fetching documentation)
```bash
python extract_hrms_tables_v2.py --test-extract
```

### Process Specific Range of Tables
```bash
# Process tables 50-99 (50 tables starting from index 50)
python extract_hrms_tables_v2.py --start-from 50 --limit 50
```

### Dry Run (see what would be created)
```bash
python extract_hrms_tables_v2.py --dry-run
```

### Combine Options
```bash
python extract_hrms_tables_v2.py --urls-file benefits_tables.txt --start-from 10 --limit 20
```

## Output

The script generates:

1. **Individual Table Files**: `tables/{TABLE_NAME}.md`
   - One file per table with complete documentation
   - Includes: description, schema details, columns, primary keys, indexes

2. **Master Index**: `HRMS_Tables_Index.md`
   - Alphabetically organized list of all tables
   - Clickable links to individual table files

## Use Cases

### HRMS Tables
```bash
# Create urlsList_hrms.txt with HRMS table URLs
python extract_hrms_tables_v2.py --urls-file urlsList_hrms.txt
```

### Payroll Tables
```bash
# Create urlsList_payroll.txt with Payroll table URLs
python extract_hrms_tables_v2.py --urls-file urlsList_payroll.txt
```

### Benefits Tables
```bash
# Create urlsList_benefits.txt with Benefits table URLs
python extract_hrms_tables_v2.py --urls-file urlsList_benefits.txt
```

## Configuration

You can modify the script's configuration at the top of the file:

```python
# Configuration
URLS_FILE = Path("D:/HRD_TechCarrot_2/FusionDB/urlsList.txt")  # Default URLs file
OUTPUT_DIR = Path("D:/HRD_TechCarrot_2/FusionDB")              # Output directory
TABLES_DIR = OUTPUT_DIR / "tables"                              # Tables subdirectory
INDEX_FILE = OUTPUT_DIR / "HRMS_Tables_Index.md"               # Index filename
DELAY_BETWEEN_REQUESTS = 2                                      # Delay in seconds
```

## Command-Line Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `--urls-file` | Path to URLs file | `--urls-file myTables.txt` |
| `--test-extract` | Test URL extraction only | `--test-extract` |
| `--dry-run` | Show what would be created | `--dry-run` |
| `--start-from` | Start from table index (0-based) | `--start-from 100` |
| `--limit` | Limit number of tables | `--limit 50` |

## Tips

1. **Large Sets**: For large numbers of tables, use `--start-from` and `--limit` to process in batches
2. **Testing**: Always use `--test-extract` first to verify URLs are read correctly
3. **Comments**: Use comments in your URLs file to organize tables by category
4. **Multiple Runs**: You can run the script multiple times with different URLs files for different table categories

## Example Workflow

```bash
# 1. Create your URLs file
# Edit urlsList.txt and add your table URLs

# 2. Test extraction
python extract_hrms_tables_v2.py --test-extract

# 3. Do a dry run
python extract_hrms_tables_v2.py --dry-run

# 4. Process first 10 tables as a test
python extract_hrms_tables_v2.py --limit 10

# 5. Process all tables
python extract_hrms_tables_v2.py
```

## Troubleshooting

**Error: URLs file not found**
- Ensure `urlsList.txt` exists in the correct location
- Or specify the file path with `--urls-file`

**No URLs found**
- Check that URLs are not commented out
- Ensure URLs are on separate lines
- Verify file encoding is UTF-8

**Rate limiting errors**
- Increase `DELAY_BETWEEN_REQUESTS` in the script
- Process tables in smaller batches using `--limit`
