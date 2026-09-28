from langchain_huggingface import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch



numero_dias = 7
numero_criancas = 2
atividades = "praia"

prompt = f"crie um roteiro de viagem para {numero_dias} dias com {numero_criancas} que busca atividades relacionadas a {atividades}."



model_id = "Qwen/Qwen2.5-1.5B-Instruct"


tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,  # troca para torch.float32 se não tiver GPU
    device_map="auto"
)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
)



modelo = HuggingFacePipeline(pipeline=pipe)
resposta = modelo.invoke(prompt)
print(resposta)
  
