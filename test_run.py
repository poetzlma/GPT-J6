import time
import torch
from transformers import GPTJForCausalLM, GPT2Tokenizer
import torch
import transformers

#Will need at least 13-14GB of Vram for CUDA
if torch.cuda.is_available():
    model =  GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B", torch_dtype=torch.float16).cuda()
else:
    model =  GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B", torch_dtype=torch.float16)

from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")

model.eval()


input_text = "Hello this is Max. I am working at PWC in Financial Services Consulting, therefore"
input_ids = tokenizer.encode(str(input_text), return_tensors='pt').cuda()

output = model.generate(
    input_ids,
    do_sample=True,
    max_length=40,
    top_p=0.7,
    top_k=0,
    temperature=1.0,
)

print(tokenizer.decode(output[0], skip_special_tokens=True))