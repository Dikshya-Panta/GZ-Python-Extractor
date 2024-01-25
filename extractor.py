import gzip
import shutil
import os

def extract_gz(gz_file_path, output_directory):
    """
    Extracts a .gz file to a specified directory.
    """
    file_name = os.path.basename(gz_file_path)
    extracted_file_path = os.path.join(output_directory, file_name.replace('.gz', ''))

    with gzip.open(gz_file_path, 'rb') as f_in:
        with open(extracted_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    print(f"File extracted to: {extracted_file_path}")

def extract_all_gz(directory):
    """
    Extracts all .gz files in the specified directory.
    """
    for file in os.listdir(directory):
        if file.endswith('.gz'):
            gz_file_path = os.path.join(directory, file)
            extract_gz(gz_file_path, directory)

# Example Usage
directory = 'D:\\sampleextraction'  # Replace with the directory containing your .gz files
extract_all_gz(directory)
