import os
import json
import glob

# Define the main folder path
main_folder = r"C:\Users\Johan\Downloads\package\messages"

# Find all messages.json files recursively
json_files = glob.glob(os.path.join(main_folder, "**", "messages.json"), recursive=True)

merged_data = []

# Load and merge JSON files
for file in json_files:
    with open(file, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            if isinstance(data, list):  # If JSON is a list, extend the merged list
                merged_data.extend(data)
            else:  # If JSON is a dict, append it as an entry
                merged_data.append(data)
        except json.JSONDecodeError as e:
            print(f"Error reading {file}: {e}")

# Save the merged JSON
output_file = os.path.join(main_folder, "merged_messages.json")
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(merged_data, f, indent=4, ensure_ascii=False)

print(f"Merged JSON saved to {output_file}")
