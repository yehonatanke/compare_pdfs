import fitz  # PyMuPDF


def compare_pdfs(file_path1, file_path2):
    # Detect if there have been changes
    diff_detector = False

    # Open the PDF files
    pdf1 = fitz.open(file_path1)
    pdf2 = fitz.open(file_path2)

    # Get the number of pages in each PDF
    num_pages1 = pdf1.page_count
    num_pages2 = pdf2.page_count

    # Print the number of pages in each PDF
    print(f"Number of pages in File 1: {num_pages1}")
    print(f"Number of pages in File 2: {num_pages2}")

    # Iterate through each page and compare text
    for page_num in range(min(num_pages1, num_pages2)):
        page1 = pdf1[page_num]
        page2 = pdf2[page_num]

        # Extract text from each page
        text1 = page1.get_text("text")
        text2 = page2.get_text("text")

        # Compare the text of the two pages
        if text1 != text2:
            diff_detector = True
            print(f"Differences found on page {page_num + 1}:")

            # Printing the differing content
            print(f"File 1 content:\n{text1}")
            print(f"File 2 content:\n{text2}")

    print("Comparison complete.")
    if diff_detector:
        print("Differences between the files were detected, the contents are detailed above.")
    else:
        print("There files are the same.")

    # Close the PDF files
    pdf1.close()
    pdf2.close()


# Usage
# Change 'path/to/file1.pdf' to your file path
file_path1 = "path/to/file1.pdf"
file_path2 = "path/to/file2.pdf"
compare_pdfs(file_path1, file_path2)
