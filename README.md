# Sdorica Asset Extractor

A Python tool for extracting assets from Unity Asset Bundle (.ab) files, specifically designed for Sdorica game assets. This extractor focuses on character figure assets and supports both single file and batch processing.

## Features

- **Smart Asset Filtering**: Automatically extracts only assets with names ending in "figure"
- **Multiple Asset Types**: Supports Texture2D, Sprite, AudioClip, and TextAsset extraction
- **Batch Processing**: Process entire directories of .ab files at once
- **Auto-Generated Output**: Creates organized output directories automatically
- **Conflict Prevention**: Adds bundle name prefix to prevent filename conflicts
- **Recursive Search**: Finds .ab files in subdirectories during batch processing

## Prerequisites

- Python 3.6 or higher
- UnityPy library

## Installation

1. Clone or download this repository
2. Install the required dependency:

```bash
pip install UnityPy
```

## Usage

The extractor supports two modes: single file extraction and batch directory processing.

### Command Line Syntax

```bash
python sdorica_asset_extractor.py <input_path>
```

### Single File Mode

Extract assets from a single .ab file:

```bash
python sdorica_asset_extractor.py /path/to/bundle.ab
```

**Output**: Creates a directory named `<filename>_extracted` in the same location as the input file.

### Batch Directory Mode

Extract assets from all .ab files in a directory:

```bash
python sdorica_asset_extractor.py /path/to/Sdorica/
```

**Output**: Creates a directory named `<dirname>_extracted` at the same level as the input directory.

## Examples

### Extract from a single bundle file
```bash
python sdorica_asset_extractor.py character_alice.ab
# Creates: character_alice_extracted/
```

### Batch extract from game directory
```bash
python sdorica_asset_extractor.py /Games/Sdorica/AssetBundles/
# Creates: /Games/Sdorica/AssetBundles_extracted/
```

## Supported Asset Types

| Asset Type | Output Format | Description |
|------------|---------------|-------------|
| Texture2D  | .png          | Texture images |
| Sprite     | .png          | Sprite images |
| AudioClip  | .wav          | Audio files |
| TextAsset  | .txt          | Text/script files |

## Output Structure

All extracted assets are saved with the following naming convention:
```
<bundle_name>_<asset_name>.<extension>
```

For example:
- `character_alice_alice_figure.png`
- `weapon_sword_sword_figure.png`

## Asset Filtering

The extractor specifically looks for assets whose names end with "figure". This filtering is designed to extract character and item figures from Sdorica asset bundles while ignoring other game assets.

## Error Handling

- **Missing Files**: The tool will report if bundle files are not found
- **Corrupted Bundles**: Individual bundle errors won't stop batch processing
- **Asset Extraction Errors**: Failed asset extractions are logged but don't halt the process
- **Permission Issues**: Ensure you have read access to input files and write access to output directories

## Troubleshooting

### Common Issues

1. **"No .ab files found"**
   - Ensure the directory contains .ab files
   - Check that file extensions are exactly ".ab" (case-sensitive on some systems)

2. **"Bundle file not found"**
   - Verify the file path is correct
   - Ensure you have read permissions for the file

3. **"Error loading bundle"**
   - The .ab file may be corrupted or use an unsupported Unity version
   - Try with a different bundle file to test

4. **No assets extracted**
   - The bundle may not contain assets with names ending in "figure"
   - Check the console output for processing details

### Dependencies

If you encounter import errors, ensure UnityPy is properly installed:

```bash
pip install --upgrade UnityPy
```

## Development

### Code Structure

- `extract_assets_from_bundle()`: Handles single bundle extraction
- `batch_extract_from_directory()`: Manages batch processing
- `main()`: Command-line interface and path handling

### Extending the Tool

To modify asset filtering, edit the condition in the extraction loop:

```python
# Current filter
if not name.endswith('figure'):
    continue

# Example: Extract all assets
# if True:  # Remove the filter
```

## License

This tool is provided as-is for educational and personal use. Respect the intellectual property rights of game developers and publishers.

## Contributing

Feel free to submit issues and enhancement requests. When contributing code, please ensure compatibility with the existing command-line interface. 