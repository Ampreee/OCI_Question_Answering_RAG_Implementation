import faiss
import os
import numpy as np
import requests
from langchain.text_splitter import RecursiveCharacterTextSplitter

key="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"
API_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"
HEADERS = {"Authorization": f"Bearer {key}"}

def embeddings(chunk):
    result=requests.post(API_URL,headers=HEADERS,json={"inputs":chunk})
    data=result.json()
    return data

with open("D:/AI_intern_assignment/data/extracted.txt","r",encoding="utf-8") as f:
    text=f.read()

split=RecursiveCharacterTextSplitter(chunk_size=512,chunk_overlap=40)
chunks=split.split_text(text)

embedding=np.array([embeddings(chunk) for chunk in chunks])

index=faiss.IndexFlatL2(embedding.shape[1])
index.add(embedding)

faiss.write_index(index,"D:/AI_intern_assignment/model/faiss_index.bin")
with open("D:/AI_intern_assignment/data/chunks.txt","w",encoding="utf-8") as f:
    for chunk in chunks:
        f.write(chunk+"\n")
print("indexing done")

