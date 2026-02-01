import shutil

# shutil.rmtree("dir")  # Remove 'dir' directory and all its contents
shutil.copy("shivraj.txt", "destination.txt")  # Copy 'source.txt' to 'destination.txt'

shutil.move("shivraj.txt", "dir/")  # Move 'shivraj.txt' to 'new_location'