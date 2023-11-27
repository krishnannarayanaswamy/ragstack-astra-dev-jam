from langchain.document_loaders.base import Document
from langchain.utilities import ApifyWrapper
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import AstraDB
import os

token=os.environ['ASTRA_DB_APPLICATION_TOKEN']
api_endpoint=os.environ['ASTRA_DB_API_ENDPOINT']
openai_api_key=os.environ["OPENAI_API_KEY"]
apify_api_key=os.environ["APIFY_API_TOKEN"]

vstore = AstraDB(
    embedding=OpenAIEmbeddings(),
    collection_name="astra_vector_jam",
    api_endpoint=api_endpoint,
    token=token,
)
apify = ApifyWrapper()

loader = apify.call_actor(
    actor_id="apify/website-content-crawler",
    run_input={"startUrls": [{"url": "https://cassio.org/"}]},
    dataset_mapping_function=lambda item: Document(
        page_content=item["text"] or "", metadata={"source": item["url"]}
    ),
)

docs = loader.load()

inserted_ids = vstore.add_documents(docs)
print(f"\nInserted {len(inserted_ids)} documents.")