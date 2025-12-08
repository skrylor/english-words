import os

def merge_files(output_file, input_files):
    unique_lines = set()

    for file_path in input_files:
        if not os.path.exists(file_path):
            print(f"Warning: {file_path} not found. Skipping.")
            continue
            
        print(f"Processing {file_path}...")
        try:
            with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                for line in f:
                    # Strip whitespace from the beginning and end of the line
                    clean_line = line.strip()
                    if clean_line:  # Only add non-empty lines
                        unique_lines.add(clean_line)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    print(f"Total unique lines found: {len(unique_lines)}")
    print(f"Writing to {output_file}...")

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in sorted(unique_lines):
                f.write(line + '\n')
        print("Done.")
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")

if __name__ == "__main__":
    # List of files to merge
    files_to_merge = [
        "english2.txt",
        "english3.txt",
        "engmix.txt",
        "ukenglish.txt",
        "usa.txt",
        "words_alpha.txt"
    ]
    
    output_filename = "merged_english.txt"
    
    merge_files(output_filename, files_to_merge)
