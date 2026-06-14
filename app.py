import gradio as gr
from query import ask


def handle_query(question):
    if not question.strip():
        return "Please enter a question.", ""

    result = ask(question)

    answer = result["answer"]

    if result["sources"]:
        sources = "\n".join(f"• {source}" for source in result["sources"])
    else:
        sources = "No sources retrieved."

    return answer, sources


with gr.Blocks() as demo:
    gr.Markdown("# Debate Judge Training Assistant")
    gr.Markdown(
        "Ask a question about PF, Original Oratory, Junior Speech, or Junior Debate rules."
    )

    question = gr.Textbox(
        label="Your question",
        placeholder="Example: What should I do during evidence checking in PF?",
        lines=2,
    )

    ask_button = gr.Button("Ask")

    answer = gr.Textbox(label="Answer", lines=8)
    sources = gr.Textbox(label="Retrieved from", lines=4)

    ask_button.click(
        handle_query,
        inputs=question,
        outputs=[answer, sources],
    )

    question.submit(
        handle_query,
        inputs=question,
        outputs=[answer, sources],
    )


demo.launch()