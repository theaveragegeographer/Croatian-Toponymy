# Getting Started with Croatian Toponymy Research

This guide will help you begin using this repository for Croatian family history research.

## Quick Start

### 1. Set Up Your Environment

#### Option A: Python Environment

```bash
# Create a virtual environment
python3 -m venv venv

# Activate it
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install required packages
pip install pandas geopandas shapely fiona pyproj matplotlib
```

#### Option B: R Environment

```r
# Install required packages
install.packages(c("sf", "sp", "dplyr", "ggplot2", "tidyr"))
```

### 2. Organize Your Data

Place your data files in the appropriate directories:

```
data/
├── shapefiles/          # Put .shp files here
│   ├── counties.shp
│   ├── settlements.shp
│   └── ...
├── raw/                 # Put original data here
│   ├── census_data.csv
│   ├── parish_records.xlsx
│   └── ...
└── processed/           # Cleaned data goes here
    └── ...
```

### 3. Run Example Scripts

Try the example scripts to see how they work:

```bash
# Test the surname matcher
python scripts/analysis/surname_placename_matcher.py

# Test the data cleaner
python scripts/processing/data_cleaner.py
```

## Your First Analysis

### Example: Finding Ancestral Locations

Let's say your surname is "Kovač" and you want to find related placenames:

1. **Prepare Your Data**
   - Get a list of Croatian settlements (from Croatian State Geodetic Administration)
   - Save it to `data/raw/settlements.csv`

2. **Search for Matches**
   - Use the surname matcher script
   - Look for settlements with "Kovač" in the name
   - Examples: Kovačevac, Kovačići, Kovači, etc.

3. **Map the Results**
   - Load settlement coordinates
   - Create a map showing all matches
   - Look for geographic clusters

4. **Cross-Reference**
   - Check historical records for these locations
   - Look for census data with surname distributions
   - Verify with family records

## Common Workflows

### Workflow 1: Surname Distribution Analysis

1. Collect surname frequency data by region
2. Join with administrative boundary shapefiles
3. Create a choropleth map showing concentrations
4. Identify regions with highest surname density
5. Research historical records from those regions

### Workflow 2: Migration Pattern Analysis

1. Gather birth locations from multiple generations
2. Geocode the locations
3. Create a map showing locations over time
4. Analyze movement patterns
5. Correlate with historical events (wars, economic changes)

### Workflow 3: Placename Etymology Research

1. List all placenames similar to your surname
2. Research the meaning and origin of each
3. Identify linguistic patterns
4. Connect to regional dialects or historical influences
5. Build a timeline of name usage

## Data Sources

### Where to Find Croatian Data

1. **Croatian State Geodetic Administration (DGU)**
   - Website: https://dgu.gov.hr/
   - Official spatial data
   - Administrative boundaries
   - Settlement locations

2. **Croatian Bureau of Statistics**
   - Census data
   - Population statistics
   - Settlement information

3. **OpenStreetMap**
   - Current placenames
   - Geographic features
   - Free to use

4. **FamilySearch.org**
   - Digitized Croatian parish records
   - Free access with account
   - Extensive Croatian collections

5. **Croatian State Archives**
   - Historical records
   - Some digitized materials
   - Requires registration for online access

### Recommended Shapefiles to Download

- Croatian administrative boundaries (županije, općine)
- Settlement locations (naselja)
- Major rivers and water bodies
- Historical boundaries (if available)

## Tips for Success

### Research Tips

1. **Start Broad**: Begin with common surnames and placenames
2. **Document Sources**: Always note where data came from
3. **Verify Multiple Ways**: Cross-check findings with different sources
4. **Consider History**: Know the historical context of your regions
5. **Connect with Others**: Join Croatian genealogy communities

### Technical Tips

1. **Keep Backups**: Always backup your data and scripts
2. **Version Control**: Use git to track your changes
3. **Comment Your Code**: Document what your scripts do
4. **Start Simple**: Begin with basic analysis before complex methods
5. **Ask for Help**: Reach out to the community with questions

### Data Management Tips

1. **Consistent Naming**: Use clear, consistent file names
2. **Document Metadata**: Include source, date, and processing info
3. **Keep Raw Data**: Never overwrite original data files
4. **Use Standard Formats**: CSV, GeoJSON, Shapefile are widely supported
5. **Mind Encodings**: Croatian characters need UTF-8 encoding

## Next Steps

1. **Read the Methodology**: See `docs/METHODOLOGY.md` for detailed research methods
2. **Customize Scripts**: Adapt the example scripts to your specific needs
3. **Build Your Database**: Systematically collect and organize data
4. **Create Maps**: Visualize your findings
5. **Document Findings**: Keep detailed notes in `docs/`

## Getting Help

- Check the README files in each directory
- Review example scripts for usage patterns
- Consult the methodology documentation
- Reach out to Croatian genealogy communities
- Consider consulting with professional genealogists

## Contributing Back

If you develop useful scripts or methodologies:
- Share them in this repository
- Document your approach
- Help others with similar research goals
- Contribute to the community knowledge base

Happy researching! May you discover your Croatian roots!
