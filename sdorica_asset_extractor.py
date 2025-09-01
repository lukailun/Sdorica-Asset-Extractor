#!/usr/bin/env python3
"""
Unity Asset Bundle Extractor
Extracts assets from Unity Asset Bundle files using UnityPy
Supports both single files and batch processing of directories
"""

import UnityPy
import os
import sys
import glob
from pathlib import Path

def extract_assets_from_bundle(bundle_path, output_path):
    """
    Extract assets from a single Unity Asset Bundle
    
    Args:
        bundle_path (str): Path to the Unity Asset Bundle file
        output_path (str): Directory to save extracted assets
    
    Returns:
        int: Number of assets extracted
    """
    if not os.path.exists(bundle_path):
        print(f"Error: Bundle file not found: {bundle_path}")
        return 0
    
    try:
        env = UnityPy.load(bundle_path)
        print(f"Processing bundle: {os.path.basename(bundle_path)}")
        
        extracted_count = 0
        
        for obj in env.objects:
            if obj.type.name in ['Texture2D', 'Sprite', 'AudioClip', 'TextAsset']:
                try:
                    data = obj.read()
                    
                    # Get the name from the object or use a default
                    name = getattr(data, 'name', None) or getattr(data, 'm_Name', None) or f"asset_{obj.path_id}"
                    
                    # # Only process assets with names ending in "figure" or containing "AVG_background" or "loading_back"
                    if not name.endswith('figure') and not ('AVG_background' in name) and not ('loading_back' in name):
                        continue
                    
                    # Add bundle name prefix to avoid conflicts
                    bundle_name = os.path.splitext(os.path.basename(bundle_path))[0]
                    
                    # Handle different asset types
                    if obj.type.name == 'Texture2D':
                        # Extract texture as PNG
                        dest = os.path.join(output_path, f"{bundle_name}_{name}.png")
                        data.image.save(dest)
                        print(f"  Extracted texture: {bundle_name}_{name}.png")
                    
                    elif obj.type.name == 'Sprite':
                        # Extract sprite as PNG
                        dest = os.path.join(output_path, f"{bundle_name}_{name}.png")
                        data.image.save(dest)
                        print(f"  Extracted sprite: {bundle_name}_{name}.png")
                    
                    elif obj.type.name == 'AudioClip':
                        # Extract audio
                        dest = os.path.join(output_path, f"{bundle_name}_{name}.wav")
                        with open(dest, 'wb') as f:
                            f.write(data.samples)
                        print(f"  Extracted audio: {bundle_name}_{name}.wav")
                    
                    elif obj.type.name == 'TextAsset':
                        # Extract text files
                        dest = os.path.join(output_path, f"{bundle_name}_{name}.txt")
                        with open(dest, 'wb') as f:
                            f.write(data.script)
                        print(f"  Extracted text: {bundle_name}_{name}.txt")
                    
                    extracted_count += 1
                    
                except Exception as e:
                    print(f"  Error extracting {obj.type.name}: {e}")
                    continue
        
        return extracted_count
        
    except Exception as e:
        print(f"Error loading bundle {bundle_path}: {e}")
        return 0

def batch_extract_from_directory(parent_dir, output_dir):
    """
    Find all .ab files in parent directory and extract all assets to a single flattened folder
    
    Args:
        parent_dir (str): Parent directory containing .ab files
        output_dir (str): Directory to save all extracted assets
    
    Returns:
        tuple: (total_bundles_processed, total_assets_extracted)
    """
    if not os.path.exists(parent_dir):
        print(f"Error: Parent directory not found: {parent_dir}")
        return 0, 0
    
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Find all .ab files recursively
    ab_files = []
    for root, dirs, files in os.walk(parent_dir):
        for file in files:
            if file.endswith('.ab'):
                ab_files.append(os.path.join(root, file))
    
    if not ab_files:
        print(f"No .ab files found in {parent_dir}")
        return 0, 0
    
    print(f"Found {len(ab_files)} .ab files to process:")
    for ab_file in ab_files:
        print(f"  {os.path.relpath(ab_file, parent_dir)}")
    
    print(f"\nExtracting all assets to: {output_dir}")
    print("=" * 60)
    
    total_bundles = 0
    total_assets = 0
    
    for ab_file in ab_files:
        assets_extracted = extract_assets_from_bundle(ab_file, output_dir)
        if assets_extracted > 0:
            total_bundles += 1
            total_assets += assets_extracted
        print()  # Empty line between bundles
    
    print("=" * 60)
    print(f"Batch extraction complete!")
    print(f"Processed {total_bundles} bundles successfully")
    print(f"Extracted {total_assets} assets total")
    print(f"All assets saved to: {output_dir}")
    
    return total_bundles, total_assets

def extract_assets(bundle_path, output_path):
    """
    Legacy function for backward compatibility
    """
    return extract_assets_from_bundle(bundle_path, output_path)

def main():
    """Main function to run the extractor"""
    if len(sys.argv) != 2:
        print("Unity Asset Bundle Extractor")
        print("Usage:")
        print("  Single file: python up.py <bundle_file.ab>")
        print("  Batch mode:  python up.py <parent_directory>")
        print()
        print("Examples:")
        print("  python up.py /path/to/bundle.ab")
        print("  python up.py /path/to/Sdorica/")
        print()
        print("Output directories are auto-generated:")
        print("  - For files: creates '<filename>_extracted' directory")
        print("  - For directories: creates '<dirname>_extracted' directory")
        return
    
    input_path = sys.argv[1]
    
    # Always auto-generate output path
    if os.path.isfile(input_path):
        # For single file: create output directory based on filename
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        parent_dir = os.path.dirname(input_path)
        output_path = os.path.join(parent_dir, f"{base_name}_extracted")
    elif os.path.isdir(input_path):
        # For directory: create output directory at same level as input directory
        parent_dir = os.path.dirname(input_path.rstrip('/'))
        dir_name = os.path.basename(input_path.rstrip('/'))
        output_path = os.path.join(parent_dir, f"{dir_name}_extracted")
    else:
        print(f"Error: Input path does not exist: {input_path}")
        return
    
    if os.path.isfile(input_path):
        # Single file mode
        print("Single file mode")
        print(f"Input: {input_path}")
        print(f"Output: {output_path}")
        assets_extracted = extract_assets_from_bundle(input_path, output_path)
        if assets_extracted > 0:
            print(f"Successfully extracted {assets_extracted} assets to {output_path}")
    elif os.path.isdir(input_path):
        # Batch directory mode
        print("Batch directory mode")
        print(f"Input: {input_path}")
        print(f"Output: {output_path}")
        batch_extract_from_directory(input_path, output_path)
    else:
        print(f"Error: Input path does not exist: {input_path}")

if __name__ == "__main__":
    main()
