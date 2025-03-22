import faiss
import requests
import numpy as np

key="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"
API_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"
HEADERS = {"Authorization": f"Bearer {key}"}

def embeddings(chunk):
    result=requests.post(API_URL,headers=HEADERS,json={"inputs":chunk})
    data=result.json()
    return np.array(data)

ind=faiss.read_index("D:/AI_intern_assignment/model/faiss_index.bin")

with open("D:/AI_intern_assignment/data/chunks.txt","r",encoding="utf-8") as f:
    chunks=f.readlines()

def retrieve(query,k=5):
    qembed=embeddings(query).reshape(1, -1)
    dist,indi=ind.search(np.array(qembed),k)
    return [chunks[i].strip() for i in indi[0]]

if __name__ == "__main__":
    query=input("test input: ")
    result=retrieve(query)
    print("\nRetrieved Docs:\n",result)
