import gradio as gr
from joblib import load
from recommentation import label_encoder
from recommentation import back_to_label
from recommentation import model
from recommentation import prediction


demo = gr.Interface(
    prediction,
    [
        "number", 
        "number",
        "number",
        "number",
    ],
    "text",
    title="Diet Recommentation",
    description="please enter your necessary details",
)



if __name__ == "__main__":
    demo.launch()