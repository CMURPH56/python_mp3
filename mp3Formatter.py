import os 

directory = r"C:\Users\[path to directory that has mp3 files]"
# eg C:\Users\User\Music\Barbra Streisand\A Collection- Greatest Hits... And More
# https://datatofish.com/rename-file-python/
# rename files to get rid of numbers in front of them

for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
        if(filename[0].isdigit() and filename[1].isdigit()):
            new_file_name = filename[3:]
            old_path_to_file = directory + "/" + filename
            new_path_to_file = directory + "/" + new_file_name
            os.rename(old_path_to_file, new_path_to_file)
            