import gradio as gr
from joblib import load
from mingo import label_encoder
from mingo import back_to_label
from mingo import model
from mingo import prediction


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