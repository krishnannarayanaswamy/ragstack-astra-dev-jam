# Chatbot Astra

Welcome to DataStax Gen AI Dev Jam. This Dev Jam will help you quickly become familiar with DataStax RAGStack, LLMs and Astra Vector Database. These hands-on jam normally runs with a DataStax technical coach, self-paced and hands-on learning assignments. Bring in a Gen AI use case, your data and build a Gen AI chatbot using DataStax Astra platform.
This project is a starter for creating your production ready chatbot using Astra Vector Store, LangStream, LangChain and OpenAI. It's designed to be easy to deploy and use, with a focus on performance and usability. Let's Go!

This project covers how to:
- create a web crawler to crawl, extract webpage information, embed the documents and ingest as collections into Astra Vector Store using Astra JSON Api
- use Retrieval Augmented Generation (RAG) with LangChain to inquire about the contents of the webpage as they are ingested in real-time. 

## Features

- **Astra DB Integration**: Store and retrieve data from your Astra DB database with ease.
- **OpenAI Integration**: Leverage the power of OpenAI to generate intelligent responses.
- **Easy Deployment**: Deploy your chatbot to Vercel with just a few clicks.
- **Customizable**: Modify and extend the chatbot to suit your needs.

## Getting Started

### Prerequisites

This workshop assumes you have access to:
1. [A Github account](https://github.com)
3. [Astra](https://astra.datastax.com/). We signed up for Astra

## Getting Started with Vercel

1. [Create or sign in](https://astra.datastax.com/register) to your Astra DB account.
2. Create a vector database. Store the database id, region and namespace, and token for later.
3. Create an [OpenAI account](https://platform.openai.com/signup) or [sign in](https://platform.openai.com/login).
4. Navigate to the [API key page](https://platform.openai.com/account/api-keys) and create a new **Secret Key**, optionally naming the key.
4. Deploy the app to Vercel
  
   Set your environment variables to the values created in steps 1 and 3.

## Setting up your database and seeding with data
1. Navigate to your IDE, set up the following environment variables:

- ASTRA_DB_NAMESPACE=existing Astra Namespace in a vector enabled DB
- OPENAI_API_KEY=api key for OPENAI
- ASTRA_DB_ID=Astra DB database id
- ASTRA_DB_REGION=Astra DB database region
- ASTRA_DB_APPLICATION_TOKEN=Generate app token for Astra database

2. Install Python dependencies:

```
pip install -r requirements.txt
```

3. Run the collection creation script:
```
python populate_db/create_collection.py
```
4. Run the data loading script:
```
python populate_db/load_data.py
```
