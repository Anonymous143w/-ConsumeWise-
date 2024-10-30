# ConsumeWise

ConsumeWise is a Retrieval-Augmented Generation (RAG) model built to provide accurate nutrition-wise recommendations and insights. The project leverages state-of-the-art natural language processing (NLP) techniques using the **Llama 3.2 1B-Instruct** model.

## Project Overview

The goal of ConsumeWise is to create an intelligent system that answers complex queries related to food, nutrition, and dietary requirements. By utilizing a RAG approach, the system retrieves relevant nutritional information from custom-built documents and generates accurate responses based on that data.

### Why RAG?

Traditional models like transformers are great at understanding and generating text, but they struggle with real-time information retrieval, especially when the knowledge required isn’t stored within the model’s parameters. Retrieval-Augmented Generation (RAG) enhances this by retrieving relevant chunks of information from a pre-built knowledge base (our document) and using them in the generation process. This results in more accurate and contextually rich outputs.

## Model

Initially, **Llama 3.2 3B-Instruct** was used for the generation tasks, but it had significant performance bottlenecks, with response times being extremely slow due to the model's large size. Despite producing high-quality outputs, it was impractical for real-time use.

To optimize performance, we switched to **Llama 3.2 1B-Instruct**, a smaller version of the model. While the response time improved, it still takes around **55 seconds on average** per query, which is quite slow. However, the accuracy and quality of the generated answers remain exceptional.

### Why Llama 3.2 1B-Instruct?

- **Smaller model size**: Balances quality and performance, making it more feasible for real-time applications.
- **High accuracy**: Even with the smaller model, the accuracy of the generated responses is impressive, especially given the complexity of the queries.
- **Custom document integration**: The model retrieves information from a document built through an ETL (Extract, Transform, Load) process, ensuring the data fed into the model is accurate and reliable.

## Data

The document used for retrieval is constructed by us using an ETL pipeline. The process involves:

- **Extracting** nutrition data from various trusted sources.
- **Transforming** the raw data into a structured format suitable for our RAG model.
- **Loading** this data into the retrieval system, making it easily accessible for the model during the generation process.

This custom-built knowledge base ensures the outputs are contextually accurate and aligned with real-world nutritional standards.

## Challenges

- **Response Time**: Despite switching to a smaller model, the average response time is still around 55 seconds, which can be slow for practical applications.
- **Performance vs. Accuracy Trade-off**: While the 1B-Instruct model significantly reduced response time compared to 3B-Instruct, there's still room for optimization to make it faster without compromising accuracy.

## Future Work

- **Model Optimization**: Explore techniques such as model quantization or using more advanced hardware to reduce response time further.
- **Data Expansion**: Add more nutritional data to the ETL pipeline to improve the breadth of responses.
- **Deploy to Production**: After optimizing the response time, plan to deploy ConsumeWise in a real-world application, potentially as a web app or API.
