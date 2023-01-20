import pandas
import os
import shutil

df = pandas.read_csv('swarmIoT_full_labeled_dataset.csv')
df = df.dropna(subset=['choice'])

directory = os. getcwd()
data_directory = os.path.join(directory, 'data')


for index, row in df.iterrows():  
    choice = round(float(row['choice']))
    image_split = row['image'].split('-')
    if len(image_split) == 2:
        image = image_split[1]
    else:
        image = image_split[0]

    image_url = f'{data_directory}/{image}'
    file = os.path.exists(image_url)

    if file:
        if choice == 0:
            shutil.move(f'data/{image}', f'ordered_data/0/{image}')
        elif choice == 1:
            shutil.move(f'data/{image}', f'ordered_data/1/{image}')
        elif choice == 2:
            shutil.move(f'data/{image}', f'ordered_data/2/{image}')