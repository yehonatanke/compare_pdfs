# PDF Comparator

## Overview
This Python script compares two PDF files and detects differences in their content.

## Prerequisites
Make sure you have the following installed:
- Python 3.x
- PyMuPDF library (`fitz`)

You can install `fitz` using the following command:
```bash
pip install PyMuPDF
```

## Usage

1. Update the file paths in the script to point to the PDF files you want to compare.
   
   ```python
   file_path1 = "path/to/file1.pdf"
   file_path2 = "path/to/file2.pdf"
   ```
2. Run the script by executing the following command in your terminal or command prompt:
   
`python PDF_Compare.py`

## Output

The script will print the number of pages in each file and identify any differences on a page-by-page basis. If differences are found, it will display the varying content for further analysis.

## Note

-  Ensure that the PyMuPDF library is installed before running the script.
-  This script performs a basic text comparison and may not capture formatting differences.
-  Adjust the script as needed for specific use cases or enhancements.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/yehonatanke/compare_pdfs/blob/main/LICENSE) file for details.

## Author

yehonataKe
 


