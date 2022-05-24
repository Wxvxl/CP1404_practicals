"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    if "_" not in new_name:
        new_name = ""
        for i, letter in enumerate(filename):
            if letter == ".":
                new_name += ".txt"
                break

            if i and letter.isupper():
                new_name += "_"
            new_name += letter
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

    for filename in filenames:
        full_name = os.path.join(directory_name, filename)
        new_name = os.path.join(directory_name, get_fixed_filename(filename))
        os.rename(full_name, new_name)
        print("Renaming {} to {}".format(filename, new_name))

demo_walk()
