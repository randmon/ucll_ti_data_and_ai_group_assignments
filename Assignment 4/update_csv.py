# Check CSV file
import os
import pandas as pd

# Read the csv file
try :
    df = pd.read_csv('swarmIoT_full_labeled_dataset.csv')
except FileNotFoundError:
    print("File \"swarmIoT_full_labeled_dataset.csv\" not found")
    exit()

# Check missing values
empty_rows = df[df.isnull().any(axis=1)]
print (f"Rows with missing values ({len(empty_rows)})")

# Fix image names to "<name>.jpg"
for index, row in df.iterrows():
    # The image name is in the format "<labelstudio_id>-<name>.jpg" or "<name>.jpg"
    image_split = row['image'].split('-')
    if len(image_split) == 2:
        df.at[index, 'image'] = image_split[1]

# Check if the files exist
directory = os. getcwd()
data_directory = os.path.join(directory, 'data')
count = 0
for index, row in df.iterrows():
    # Get the image name
    image = row['image']
    
    # Check if the file exists
    image_url = f'{data_directory}/{image}'
    file = os.path.exists(image_url)
    
    # Print the missing files
    # if not file:
    #     print(f"File \"{image}\" not found")

    # Count the missing files
    if not file:
        count += 1

print(f"Missing images ({count})")

# Check duplicated images
duplicated_images = df[df.duplicated(['image'])]
print (f"Duplicated images ({len(duplicated_images)})")

# Remove duplicated images
df = df.drop_duplicates(subset=['image'], keep='first')

# Save the csv file
df.to_csv('swarmIoT_full_labeled_dataset.csv', index=False)
