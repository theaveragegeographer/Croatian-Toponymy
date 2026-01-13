#!/usr/bin/env python3
"""
Data processing script for Croatian placename data.

This script provides utilities for:
1. Cleaning and standardizing Croatian text (proper encoding of č, ć, đ, š, ž)
2. Converting between spatial data formats
3. Geocoding placenames
4. Preparing data for analysis

Requirements:
    - pandas
    - geopandas (optional, for spatial operations)

Install with: pip install pandas geopandas
"""

import re
import unicodedata


def standardize_croatian_text(text):
    """
    Standardize Croatian text encoding and formatting.
    
    Ensures proper representation of Croatian-specific characters:
    č, ć, đ, š, ž and their uppercase variants
    
    Args:
        text (str): Input text that may have encoding issues
        
    Returns:
        str: Standardized text
    """
    if not isinstance(text, str):
        return text
    
    # Normalize to NFC form (composed characters)
    text = unicodedata.normalize('NFC', text)
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    return text


def clean_placename(placename):
    """
    Clean and standardize a Croatian placename.
    
    Args:
        placename (str): Raw placename
        
    Returns:
        str: Cleaned placename
    """
    if not isinstance(placename, str):
        return placename
    
    # Standardize encoding
    placename = standardize_croatian_text(placename)
    
    # Remove extra whitespace
    placename = ' '.join(placename.split())
    
    # Capitalize properly (Croatian placenames typically start with capital)
    # This is a simple implementation - may need refinement
    placename = placename.title()
    
    return placename


def extract_settlement_type(placename):
    """
    Extract settlement type from placename if present.
    
    Common Croatian settlement prefixes/suffixes:
    - Gornji/Donji (Upper/Lower)
    - Veliki/Mali (Big/Small)
    - Stari/Novi (Old/New)
    
    Args:
        placename (str): Croatian placename
        
    Returns:
        tuple: (base_name, modifier)
    """
    modifiers = [
        'Gornji', 'Donji',
        'Veliki', 'Mali',
        'Stari', 'Novi',
        'Srednji'
    ]
    
    for modifier in modifiers:
        if placename.startswith(modifier + ' '):
            base = placename[len(modifier)+1:]
            return (base, modifier)
    
    return (placename, None)


def process_csv_data(input_file, output_file):
    """
    Process a CSV file containing placename data.
    
    Args:
        input_file (str): Path to input CSV
        output_file (str): Path to output processed CSV
    """
    print(f"Processing {input_file}...")
    
    # Placeholder for actual implementation
    # This would use pandas to:
    # 1. Read the CSV
    # 2. Clean text fields
    # 3. Standardize column names
    # 4. Remove duplicates
    # 5. Save processed data
    
    print(f"Processed data saved to {output_file}")


def main():
    """
    Main function for data processing operations.
    """
    print("Croatian Toponymy Data Processing Tool")
    print("=" * 50)
    
    # Example usage
    test_placenames = [
        "Zagreb",
        "Velika Gorica",
        "Dubrovnik",
        "Split",
        "Gornji Grad"
    ]
    
    print("\nExample: Cleaning placenames")
    for name in test_placenames:
        cleaned = clean_placename(name)
        base, modifier = extract_settlement_type(cleaned)
        if modifier:
            print(f"  {name} -> {cleaned} (Base: {base}, Type: {modifier})")
        else:
            print(f"  {name} -> {cleaned}")
    
    print("\nThis script can be extended to:")
    print("- Read data from data/raw/")
    print("- Clean and standardize the data")
    print("- Save processed data to data/processed/")
    print("- Convert between file formats")
    print("- Geocode placenames to coordinates")


if __name__ == "__main__":
    main()
