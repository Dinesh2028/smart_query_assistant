from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Step 1: Connect to the SQLite database
db = SQLDatabase.from_uri("sqlite:///sales.db")

# Step 2: Initialize Groq model
llm = ChatGroq(
    model_name="llama3-8b-8192",  # Fast and efficient model
    groq_api_key="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"  # Replace with your key (or use env variable)
)

# Step 3: Create a prompt template for SQL query generation
prompt = PromptTemplate(
    input_variables=["question", "schema"],
    template="""
    You are an expert SQL assistant. Given the following database schema and a user question, generate a correct SQL query to answer the question. Only return the SQL query, nothing else.

    Schema:
    {schema}

    User Question:
    {question}
    """
)

# Step 4: Create a chain to generate and execute queries
def get_query_chain(question):
    # Get schema of the sales table
    schema = db.get_table_info(["sales"])
    
    # Create chain: Prompt -> LLM -> Output Parser
    chain = prompt | llm | StrOutputParser()
    
    # Generate SQL query
    sql_query = chain.invoke({"question": question, "schema": schema})
    
    # Execute query and return results
    results = db.run(sql_query)
    return sql_query, results

# Step 5: Test the assistant
if __name__ == "__main__":
    while True:
        question = input("Ask a question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        
        try:
            sql_query, results = get_query_chain(question)
            print("\nGenerated SQL Query:")
            print(sql_query)
            print("\nResults:")
            print(results)
        except Exception as e:
            print(f"Error: {e}")