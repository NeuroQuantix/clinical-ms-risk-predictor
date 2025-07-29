import kagglehub

# Download latest version
path = kagglehub.dataset_download("desalegngeb/conversion-predictors-of-cis-to-multiple-sclerosis")

print("Path to dataset files:", path)

# Save the file to the data/raw directory
import os
import shutil
data_dir = os.path.join(os.getcwd(), "data", "raw")
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
for file_name in os.listdir(path):
    full_file_name = os.path.join(path, file_name)
    if os.path.isfile(full_file_name):
        # Rename the file to CIS_MS_data.csv when moving
        dest_file = os.path.join(data_dir, "CIS_MS_data.csv")
        shutil.move(full_file_name, dest_file)
# Clean up the downloaded directory
shutil.rmtree(path)
# Print the path to the saved files
print("Files moved to:", data_dir)
print("File saved as: CIS_MS_data.csv")