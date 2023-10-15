import os
import re
import requests
from PyPDF2 import PdfFileReader
from bs4 import BeautifulSoup


def calculate_density(document, search_string):
    if document.endswith('.pdf'):
        return calculate_pdf_density(document, search_string)
    elif document.endswith('.txt'):
        return calculate_text_density(document, search_string)
    elif document.startswith('http') or document.startswith('https'):
        return calculate_webpage_density(document, search_string)
    else:
        return None


def calculate_pdf_density(pdf_file, search_string):
    with open(pdf_file, 'rb') as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)
        total_text = ""
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            total_text += page.extractText()

        return calculate_text_density(total_text, search_string)


def calculate_text_density(text_file, search_string):
    with open(text_file, 'r', encoding='utf-8') as text:
        text = text.read()
    text = text.lower()
    search_string = search_string.lower()

    total_length = len(text)
    string_length = len(search_string)

    if total_length == 0 or string_length == 0:
        return None

    matches = re.findall(search_string, text)
    match_length = sum(len(match) for match in matches)
    density = match_length / total_length

    return density


def calculate_webpage_density(url, search_string):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()

        return calculate_text_density(text, search_string)
    except Exception as e:
        print(f"Error fetching webpage: {str(e)}")
        return None


if __name__ == "__main__":
    document = input("Enter the path to a document (PDF, .txt) or a URL: ")
    search_string = input("Enter the search string: ")

    density = calculate_density(document, search_string)

    if density is not None:
        if density > 0.01:
            print(f"Warning: The density of '{search_string}' is {density:.2%}, which is more than 1%.")
        else:
            print(f"The density of '{search_string}' is {density:.2%}.")
    else:
        print("Invalid input or unable to process the document.")


"""This extensive document contains a plethora of information on various subjects. 
It covers topics such as history, economics, literature, and mathematics. 
Throughout its many pages, you will find numerous instances of the word "example."

The word "example" appears multiple times in this document, contributing to a density of less than 1%. 
Other words and phrases are also scattered throughout the text, creating a rich and diverse content landscape.
"""