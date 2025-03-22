from pypdf import PdfReader

def extract(path):
    r=PdfReader(path)
    t=" ".join([page.extract_text() for page in r.pages if page.extract_text()])
    return t

path=extract("D:/AI_intern_assignment/data/OCI.pdf")
with open("D:/AI_intern_assignment/data/extracted.txt","w",encoding="utf-8") as f:
    f.write(path)
print("extraction completed \nFile saved to extracted")

