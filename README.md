# GZ-Python-Extractor

This Python script facilitates the extraction of .gz files within a specified directory. It is designed to automate the decompression process for multiple gzip-compressed files, making it an efficient tool for handling large datasets or archives commonly encountered in research and data analysis.

**Features:**
Single File Extraction: Extracts a single .gz file to a specified output directory.
Batch Extraction: Iterates through a directory, automatically identifying and extracting all .gz files within.
Prerequisites

To use this script, ensure you have the following installed:

**Python (3.x recommended)**
Required Python modules: gzip, shutil, os
These modules are part of the Python Standard Library and should be available with a standard Python installation.

**Installation:**
No additional installation is required for this script. Simply download the .py file to your local machine, and you're ready to go.

**Function Descriptions:**

extract_gz(gz_file_path, output_directory)
This function takes the path to a .gz file and an output directory. It extracts the contents of the .gz file to the specified output directory, removing the .gz extension from the extracted file.

extract_all_gz(directory)
This function iterates through all files in the specified directory, identifies files with a .gz extension, and extracts them using the extract_gz function.
