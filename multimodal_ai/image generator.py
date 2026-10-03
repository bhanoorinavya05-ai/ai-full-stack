import streamlit as st 
import torch
from diffusers import StableDiffusionPipeline
import random

st.set_page_config(page_title="AI Image Generator", page_icon="")
st.title("AI Image Generator")

@st.cache_resource
def load_resource():
    pipe = StableDiffusionPipeline.from_pretrained("segmind/tiny-sd", torch_dtype = torch.float32)
    return pipe 

pipe = load_resource()
st.caption("Model loaded!")

st.session_state.setdefault("generated_image", None)
st.session_state.setdefault("generated_prompt", None)

prompt = st.text_input("Enter a prompt", placeholder="a cat wearing sunglasses")

generate = st.button("Generate")

if prompt and generate:
    with st.spinner("Generating image... This might take a while."):
        image = pipe(prompt, num_inference_steps=8).images[0]
    st.session_state.generated_image = image
    st.session_state.generated_prompt = prompt
        
if st.session_state.generated_image is not None:
    st.image(st.session_state.generated_image, caption = st.session_state.generated_prompt)
    
surprise_prompts =[
    "a butterfly flying in a garden",
    "a village scenery",
    "a sunset in a futuristic city",
    "a cow feeding its children",
    "an alien flying in a ufo"
]
    
if st.button("surprise Me"):
    st.session_state.surprise_prompt = random.choice(surprise_prompts)
    
if "surprise_prompt" in st.session_state:
    st.info(f"Random Prompt: {st.session_state.surprise_prompt}")        