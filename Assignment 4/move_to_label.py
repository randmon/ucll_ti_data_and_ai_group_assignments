import pandas
import os
import shutil

# Read the csv file
try :
    df = pandas.read_csv('swarmIoT_full_labeled_dataset.csv')
except FileNotFoundError:
    print("File \"swarmIoT_full_labeled_dataset.csv\" not found")
    exit()

# Drop rows with missing values
empty_rows = df[df.isnull().any(axis=1)]
print (f"Dropping rows with missing values ({len(empty_rows)})")
df = df.dropna(subset=['choice'])

# Get the current working directory
directory = os. getcwd()
data_directory = os.path.join(directory, 'data')

# Create the ordered_data folder
if not os.path.exists('ordered_data'):
    os.mkdir('ordered_data')

# Create the 0, 1 and 2 folders
if not os.path.exists('ordered_data/0'):
    os.mkdir('ordered_data/0')
if not os.path.exists('ordered_data/1'):
    os.mkdir('ordered_data/1')
if not os.path.exists('ordered_data/2'):
    os.mkdir('ordered_data/2')

# Move the files to the correct folder
for index, row in df.iterrows():
    # Get the choice and image name
    choice = round(float(row['choice']))
    # The image name is in the format "<labelstudio_id>-<name>.jpg" or "<name>.jpg"
    image_split = row['image'].split('-')
    if len(image_split) == 2:
        image = image_split[1]
    else:
        image = image_split[0]
    
    # Check if the file exists
    image_url = f'{data_directory}/{image}'
    file = os.path.exists(image_url)

    # Move it to the correct folder
    if file:
        if choice == 0:
            shutil.move(f'data/{image}', f'ordered_data/0/{image}')
        elif choice == 1:
            shutil.move(f'data/{image}', f'ordered_data/1/{image}')
        elif choice == 2:
            shutil.move(f'data/{image}', f'ordered_data/2/{image}')
    else:
        print(f"File \"{image}\" not found")