# 🧪 LangChain + Qwen (HuggingFace) — Lab Project

> ⚠️ **Status: Em desenvolvimento (Lab)**  
> Este projeto está em fase experimental. APIs, estrutura e comportamentos podem mudar a qualquer momento.

---

## 📌 Sobre o projeto

Pipeline conversacional construído com **LangChain** integrado ao modelo **Qwen** via **HuggingFace Hub**, com foco em exploração e testes de capacidades de linguagem natural para aplicações internas da Solutions Lab.

---

## 🛠️ Stack

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.10+ |
| Framework LLM | LangChain |
| Modelo | Qwen (via HuggingFace Hub) |
| Gerenciamento de dependências | pip / venv |

---

## 📁 Estrutura do projeto

```
project-root/
│
├── src/
│   ├── chain.py          # Definição da chain principal
│   ├── prompt.py         # Templates de prompt
│   └── utils.py          # Funções auxiliares
│
├── notebooks/
│   └── experiments.ipynb # Experimentos e testes exploratórios
│
├── .env.example          # Variáveis de ambiente necessárias
├── requirements.txt
└── README.md
```

---

## ⚙️ Pré-requisitos

- Python 3.10+
- Conta no [HuggingFace](https://huggingface.co/) com acesso ao modelo Qwen
- Token de API da HuggingFace (`HF_TOKEN`)

---

## 🚀 Instalação

```bash
# Clone o repositório
git clone https://github.com/solutionslab/<repo-name>.git
cd <repo-name>

# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt
```

---

## 🔑 Configuração das variáveis de ambiente

Copie o arquivo de exemplo e preencha com suas credenciais:

```bash
cp .env.example .env
```

Conteúdo do `.env`:

```env
HF_TOKEN=seu_token_aqui
HF_MODEL_ID=Qwen/Qwen1.5-7B-Chat  # ou outro variant do Qwen
```

---

## 🧩 Uso básico

```python
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen1.5-7B-Chat",
    task="text-generation",
    huggingfacehub_api_token="<HF_TOKEN>",
    max_new_tokens=512,
    temperature=0.7,
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente útil."),
    ("human", "{input}"),
])

chain = prompt | llm

response = chain.invoke({"input": "O que são AI Agents?"})
print(response)
```

---

## 📦 Dependências principais

```txt
langchain
langchain-huggingface
huggingface-hub
python-dotenv
```

> Arquivo completo em `requirements.txt`.

---

## 🧪 Estado atual do lab

- [x] Conexão com HuggingFace Hub estabelecida
- [x] Chain básica funcional com Qwen
- [ ] Testes com diferentes variantes do Qwen (7B, 14B, 72B)
- [ ] Implementação de memória conversacional
- [ ] Integração com ferramentas externas (Tools / Agents)
- [ ] Avaliação de performance e latência
- [ ] Containerização (Docker)

---

## ⚠️ Avisos de lab

- Este projeto **não está em produção** e não deve ser tratado como solução finalizada.
- Custos de API do HuggingFace podem variar dependendo do modelo e volume de requisições.
- Modelos Qwen maiores (14B+) podem exigir endpoints dedicados no HuggingFace Inference API.

---


[solutionslab.site](https://solutionslab.site)
