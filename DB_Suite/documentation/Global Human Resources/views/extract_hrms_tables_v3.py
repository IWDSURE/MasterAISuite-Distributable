#!/usr/bin/env python3
"""
HRMS Tables Documentation Extractor v2

Enhanced version that extracts complete Oracle HRMS table documentation including:
- Table description
- Schema, owner, tablespace details
- Complete column information (name, datatype, length, precision, not-null, comments)
- Primary keys
- Indexes

Input: Text file (urlsList.txt) with one Oracle documentation URL per line
Output: Markdown files for each table + master index file
"""

import re
import time
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from bs4 import BeautifulSoup
import requests

# Configuration
URLS_FILE = Path("D:/HRD_TechCarrot_2/FusionDB/Global Human Resources/views/urlsList.txt")
OUTPUT_DIR = Path("D:/HRD_TechCarrot_2/FusionDB/Global Human Resources/views")
TABLES_DIR = OUTPUT_DIR / "views"
INDEX_FILE = OUTPUT_DIR / "HRMS_View_Index.md"
DELAY_BETWEEN_REQUESTS = 2  # seconds


def extract_urls_from_file(urls_file: Path) -> List[str]:
    """
    Extract table URLs from a text file.
    Each line should contain one URL.
    """
    print(f"Reading URLs from: {urls_file}")
    
    if not urls_file.exists():
        print(f"Error: URLs file not found: {urls_file}")
        return []
    
    urls = []
    with open(urls_file, 'r', encoding='utf-8') as f:
        for line in f:
            url = line.strip()
            # Skip empty lines and comments
            if url and not url.startswith('#'):
                urls.append(url)
    
    print(f"Found {len(urls)} table URLs")
    return urls


def extract_table_from_html(soup: BeautifulSoup, headers_to_find: List[str]) -> Optional[List[List[str]]]:
    """
    Extract table data based on header keywords.
    Returns list of rows, where each row is a list of cell values.
    """
    tables = soup.find_all('table')
    
    for table in tables:
        headers = [th.get_text().strip() for th in table.find_all('th')]
        
        # Check if this table has the headers we're looking for
        if any(any(keyword.lower() in h.lower() for keyword in headers_to_find) for h in headers):
            rows = []
            for tr in table.find_all('tr')[1:]:  # Skip header row
                cells = [td.get_text().strip() for td in tr.find_all('td')]
                if cells:
                    rows.append(cells)
            return rows
    
    return None


def fetch_table_documentation(url: str) -> Tuple[str, Dict[str, any]]:
    """Fetch and parse the complete documentation page for a table.
    
    Returns:
        Tuple of (table_name, table_info_dict)
    """
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract table name from H1 first
        h1 = soup.find('h1')
        table_name = h1.get_text().strip() if h1 else 'UNKNOWN_TABLE'
        
        table_info = {
            'url': url,
            'title': table_name,
            'description': '',
            'schema': '',
            'owner': '',
            'object_type': '',
            'tablespace': '',
            'columns': [],
            'primary_keys': [],
            'indexes': []
        }
        
        # Extract description (in div.body, first p.p or p.shortdesc)
        body_div = soup.find('div', class_='body')
        if body_div:
            # Try shortdesc first
            shortdesc = body_div.find('p', class_='shortdesc')
            if shortdesc and shortdesc.get_text().strip():
                table_info['description'] = shortdesc.get_text().strip()
            else:
                # Try first p.p
                desc_p = body_div.find('p', class_='p')
                if desc_p:
                    table_info['description'] = desc_p.get_text().strip()
        
        # Extract Details section (Schema, Owner, Type, Tablespace)
        details_section = soup.find('h2', string=re.compile(r'Details', re.IGNORECASE))
        if details_section:
            details_list = details_section.find_next('ul')
            if details_list:
                for li in details_list.find_all('li'):
                    text = li.get_text().strip()
                    if 'Schema:' in text:
                        table_info['schema'] = text.split('Schema:')[1].strip()
                    elif 'Object owner:' in text:
                        table_info['owner'] = text.split('Object owner:')[1].strip()
                    elif 'Object type:' in text:
                        table_info['object_type'] = text.split('Object type:')[1].strip()
                    elif 'Tablespace:' in text:
                        table_info['tablespace'] = text.split('Tablespace:')[1].strip()
        
        # Extract Primary Key information
        pk_section = soup.find('h2', string=re.compile(r'Primary Key', re.IGNORECASE))
        if pk_section:
            pk_table = pk_section.find_next('table')
            if pk_table:
                for tr in pk_table.find_all('tr')[1:]:  # Skip header
                    cells = [td.get_text().strip() for td in tr.find_all('td')]
                    if cells:
                        table_info['primary_keys'].append({
                            'name': cells[0] if len(cells) > 0 else '',
                            'columns': cells[1] if len(cells) > 1 else ''
                        })
        
        # Extract Columns information
        columns_section = soup.find('h2', string=re.compile(r'Columns', re.IGNORECASE))
        if columns_section:
            columns_table = columns_section.find_next('table')
            if columns_table:
                headers = [th.get_text().strip() for th in columns_table.find_all('th')]
                
                for tr in columns_table.find_all('tr')[1:]:  # Skip header
                    cells = [td.get_text().strip() for td in tr.find_all('td')]
                    if cells and len(cells) >= len(headers):
                        column_data = {}
                        for i, header in enumerate(headers):
                            if i < len(cells):
                                column_data[header] = cells[i]
                        table_info['columns'].append(column_data)
        
        # Extract Indexes information
        indexes_section = soup.find('h2', string=re.compile(r'Indexes', re.IGNORECASE))
        if indexes_section:
            indexes_table = indexes_section.find_next('table')
            if indexes_table:
                for tr in indexes_table.find_all('tr')[1:]:  # Skip header
                    cells = [td.get_text().strip() for td in tr.find_all('td')]
                    if cells:
                        table_info['indexes'].append({
                            'name': cells[0] if len(cells) > 0 else '',
                            'uniqueness': cells[1] if len(cells) > 1 else '',
                            'tablespace': cells[2] if len(cells) > 2 else '',
                            'columns': cells[3] if len(cells) > 3 else ''
                        })
        
        return table_name, table_info
        
    except Exception as e:
        print(f"  Error fetching {url}: {e}")
        return None, None


def create_table_markdown(table_name: str, table_info: Dict) -> str:
    """Create comprehensive markdown content for a table documentation file."""
    md = f"# {table_name}\n\n"
    
    # Description
    if table_info.get('description'):
        md += f"{table_info['description']}\n\n"
    
    # Details section
    md += "## Details\n\n"
    if table_info.get('schema'):
        md += f"**Schema:** {table_info['schema']}\n\n"
    if table_info.get('owner'):
        md += f"**Object owner:** {table_info['owner']}\n\n"
    if table_info.get('object_type'):
        md += f"**Object type:** {table_info['object_type']}\n\n"
    if table_info.get('tablespace'):
        md += f"**Tablespace:** {table_info['tablespace']}\n\n"
    
    md += f"**Source:** [{table_info['url']}]({table_info['url']})\n\n"
    
    # Primary Key section
    if table_info.get('primary_keys'):
        md += "## Primary Key\n\n"
        md += "| Name | Columns |\n"
        md += "|------|----------|\n"
        for pk in table_info['primary_keys']:
            md += f"| {pk.get('name', '')} | {pk.get('columns', '')} |\n"
        md += "\n"
    
    # Columns section
    if table_info.get('columns'):
        md += "## Columns\n\n"
        
        # Get all unique column headers
        all_headers = set()
        for col in table_info['columns']:
            all_headers.update(col.keys())
        
        # Common headers in order
        header_order = ['Name', 'Datatype', 'Length', 'Precision', 'Not-null', 'Comments']
        headers = [h for h in header_order if h in all_headers]
        
        # Add any remaining headers
        for h in sorted(all_headers):
            if h not in headers:
                headers.append(h)
        
        # Create table header
        md += "| " + " | ".join(headers) + " |\n"
        md += "|" + "|".join(["---" for _ in headers]) + "|\n"
        
        # Add rows
        for col in table_info['columns']:
            row_values = [col.get(h, '') for h in headers]
            md += "| " + " | ".join(row_values) + " |\n"
        
        md += "\n"
    
    # Indexes section
    if table_info.get('indexes'):
        md += "## Indexes\n\n"
        md += "| Index | Uniqueness | Tablespace | Columns |\n"
        md += "|-------|------------|------------|----------|\n"
        for idx in table_info['indexes']:
            md += f"| {idx.get('name', '')} | {idx.get('uniqueness', '')} | {idx.get('tablespace', '')} | {idx.get('columns', '')} |\n"
        md += "\n"
    
    # Back link
    md += "---\n\n"
    md += "[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)\n"
    
    return md


def create_index_markdown(tables: List[Tuple[str, str, str]]) -> str:
    """Create the master index markdown file."""
    md = "# Oracle Global HRMS Tables - Documentation Index\n\n"
    md += f"**Total Tables:** {len(tables)}\n\n"
    md += "This is a local documentation database for Oracle Fusion Global HRMS tables.\n\n"
    md += "Click on any table name to view its complete documentation including columns, indexes, and primary keys.\n\n"
    md += "## Tables\n\n"
    
    # Sort tables alphabetically
    sorted_tables = sorted(tables, key=lambda x: x[0])
    
    # Group by first letter
    current_letter = ''
    for table_name, description, file_path in sorted_tables:
        first_letter = table_name[0].upper()
        
        if first_letter != current_letter:
            current_letter = first_letter
            md += f"\n### {current_letter}\n\n"
        
        # Create link to table file
        desc_preview = description[:80] + "..." if len(description) > 80 else description
        md += f"- **[{table_name}]({file_path})** - {desc_preview}\n"
    
    return md


def main(args):
    """Main execution function."""
    
    urls_file = URLS_FILE
    
    if not urls_file.exists():
        print(f"Error: URLs file not found: {urls_file}")
        print(f"Please create a file at {urls_file} with one URL per line.")
        return
    
    # Extract URLs from file
    urls = extract_urls_from_file(urls_file)
    
    if args.test_extract:
        print("\nExtracted URLs:")
        for url in urls[:10]:
            print(f"  {url}")
        print(f"  ... and {len(urls) - 10} more")
        return
    
    # Create tables directory
    if not args.dry_run:
        TABLES_DIR.mkdir(exist_ok=True)
        print(f"Created directory: {TABLES_DIR}")
    
    # Process each table
    index_data = []
    start_from = args.start_from if args.start_from else 0
    limit = args.limit if args.limit else len(urls)
    
    urls_to_process = urls[start_from:start_from + limit]
    
    for i, url in enumerate(urls_to_process, start_from + 1):
        print(f"\n[{i}/{len(urls)}] Processing {url.split('/')[-1]}...")
        
        if args.dry_run:
            print(f"  Would fetch and create markdown file")
            continue
        
        # Fetch documentation and get actual table name
        table_name, table_info = fetch_table_documentation(url)
        
        if table_name and table_info:
            print(f"  Table name: {table_name}")
            
            # Create markdown content
            md_content = create_table_markdown(table_name, table_info)
            
            # Write to file using actual table name
            table_file = TABLES_DIR / f"{table_name}.md"
            with open(table_file, 'w', encoding='utf-8') as f:
                f.write(md_content)
            
            print(f"  ✓ Created: {table_file.name}")
            
            # Add to index
            description = table_info.get('description', '')
            index_data.append((table_name, description, f"tables/{table_name}.md"))
        
        # Delay between requests
        if i < len(urls):
            time.sleep(DELAY_BETWEEN_REQUESTS)
    
    # Create index file
    if not args.dry_run and index_data:
        index_content = create_index_markdown(index_data)
        with open(INDEX_FILE, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        print(f"\n✓ Created master index: {INDEX_FILE}")
        print(f"✓ Created {len(index_data)} table documentation files")
        print(f"\nDone! Open {INDEX_FILE} to browse the documentation.")
    elif args.dry_run:
        print(f"\nDry run complete. Would create:")
        print(f"  - {INDEX_FILE}")
        print(f"  - {len(urls_to_process)} table files in {TABLES_DIR}/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract HRMS table documentation from Oracle docs",
        epilog="Example: python extract_hrms_tables_v2.py --urls-file myTables.txt"
    )
    parser.add_argument('--urls-file', type=str,
                       help='Path to text file containing URLs (one per line). Default: urlsList.txt')
    parser.add_argument('--test-extract', action='store_true',
                       help='Test URL extraction without fetching documentation')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be created without creating files')
    parser.add_argument('--start-from', type=int, default=0,
                       help='Start processing from this table index (0-based)')
    parser.add_argument('--limit', type=int,
                       help='Limit number of tables to process')
    
    args = parser.parse_args()
    
    # Override URLS_FILE if specified
    global URLS_FILE
    if args.urls_file:
        URLS_FILE = Path(args.urls_file)
    
    main(args)
