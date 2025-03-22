import os
from groq import Groq
from retrieval import retrieve

groq=Groq(api_key="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")

def generate(query,docs):
    con=" ".join(docs)
    prompt=f"Context:{con}\n Question:{query} \nAnswer:"

    response=groq.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role":"system","content":"You are an OCI expert who answers question related to OCI."},
            {"role":"user","content":prompt}
        ],
        max_tokens=200,
    )
    return response.choices[0].message.content

query=input("Input: ")
docs=retrieve(query)
result=generate(query,docs)
print("\n Answer:",result)
