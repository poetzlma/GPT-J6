import time
import torch
from transformers import GPTJForCausalLM, GPT2Tokenizer
import torch
import transformers

#Will need at least 13-14GB of Vram for CUDA
if torch.cuda.is_available():
    model =  GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B",cache_dir="/mnt2/cache_dir/", torch_dtype=torch.float16).cuda()
else:
    print("GPU not available, check driver and cuda installation and reboot if neccessary")
    #model =  GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B", torch_dtype=torch.float16)

from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")

model.eval()


input_text = "In the weeks since its arrival, GPT-3 has spawned dozens of other experiments that raise the eyebrows in much the same way. It generates tweets, pens poetry, summarizes emails, answers trivia questions, translates languages and even writes its own computer programs, all with very little prompting. Some of these skills caught even the experts off guard.."
input_ids = tokenizer.encode(str(input_text), return_tensors='pt').cuda()

output = model.generate(
    input_ids,
    do_sample=True,
    max_length=400,
    top_p=0.7,
    top_k=0,
    temperature=1.0,
)

print(tokenizer.decode(output[0], skip_special_tokens=True))