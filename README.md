# **OCI_RAG_Q/A**

## **Overview**
RAG combines information retrieval with LLM-based text generation. The system first
fetches relevant information from a dataset (retrieval) and then generates responses using
an LLM (generation). This approach improves accuracy and minimizes hallucinations.

## **How To Run**
first,run extraction.py to extract from pdf then run index.py to create chunks ,indexing and
saving them .After this,run retrieval.py to check if it is working with test input. In the last,
run main.py to run main genration.

## **System Architecture**

![Rag implementation](https://github.com/user-attachments/assets/64763ba2-7920-4663-a1c9-110c37e23959)

## **Challenges**
1.) First challenge,I got was that didn't had that much knowledge of of vector databases .So,had 
    to use quick and efficient alternative on searching came across FAISS which is not a particularly
    a vector databases as we have to manually update the saving and also no filtering and is local

2.) Second challenge,I got was using and downloading the model locally instead of using API was using 
    too much of resources on local system

3.) Third challenge,More of a mistake was using wrong formats for api calling and wasted too much time 
    checking api setting environment around it .On learning from sources got to know about correct of calling API

4.) Fourth challenge,setting up wrong version of required library mismatching with each other not able to 
    use some function as they were removed from newer version

5.) Fifth challenge,On completing with all flow and files and successfully running all the files i got to 
    problem where the model was hallucinating giving garbage generation instead of what was asked.this was 
    solved by reducing the chunk size from 1024 to 256 and overlapping from 30 percent to 5 percent and to increase 
    further accuracy of it size was increased to 512 and overlapping to 7 percent which gave me satisfied answers.

