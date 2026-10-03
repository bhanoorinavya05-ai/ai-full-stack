import torch 
from diffusers import StableDiffusionPipeline
    
pipe = StableDiffusionPipeline.from_pretrained( 
        "segmind/tiny-sd",
        torch_dtype = torch.float32
    )        

image = pipe(
    "a dog wearing sunglasses",
    num_interference_steps = 8
    ).image[0]
    
image.save("demo.png")
print("Image genereted and saved as demo.png")