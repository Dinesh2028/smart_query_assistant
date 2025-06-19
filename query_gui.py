import tkinter as tk
from query_assistant import get_query_chain

root = tk.Tk()
root.title("Smart Database Query Assistant")

tk.Label(root, text="Enter your question:").pack()
question_entry = tk.Entry(root, width=50)
question_entry.pack()

result_text = tk.Text(root, height=10, width=60)
result_text.pack()

def ask_question():
    question = question_entry.get()
    try:
        sql_query, results = get_query_chain(question)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"SQL Query:\n{sql_query}\n\nResults:\n{results}")
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e}")

tk.Button(root, text="Ask", command=ask_question).pack()
root.mainloop()