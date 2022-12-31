from pypdf import PdfReader

# from pdfreader import SimplePDFViewer
import pyttsx3

# convert pdf to text
reader = PdfReader("Price_Action_Concepts.pdf")
# viewer = SimplePDFViewer(reader)
engine = pyttsx3.init()


# number of pages
num_pages = len(reader.pages) - 1

# input page number to extract
while True:
    page = input(f"Choose a page between 1 and {num_pages}: ")

    if page.isdigit() and 1 <= int(page) <= num_pages:

        chosen_page = reader.pages[int(page)].extract_text()
        print(chosen_page)
        break

    else:
        print("Try again")
        continue


# change the speed of the reader
rate = engine.getProperty("rate")
engine.setProperty("rate", rate + -10)

# save the voice over to file
engine.save_to_file(chosen_page, "tester.mp3")
