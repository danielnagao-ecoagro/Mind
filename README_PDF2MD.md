# PDF to Markdown Converter

Converte arquivos PDF em Markdown estruturado usando Claude para formatação.

## Setup

### 1. Instalar `uv` (se não tiver)
```bash
pip install uv
```

### 2. Executar o setup
```bash
setup.bat
```

Isso vai:
- Criar um ambiente virtual em `.venv`
- Instalar as dependências (pdfplumber, anthropic)

### 3. Ativar o ambiente
```bash
.\.venv\Scripts\activate
```

## Uso

```bash
python scripts/pdf_to_markdown.py
```

O script vai:
1. Ler todos os PDFs em `Mind/Fonte temp`
2. Extrair o texto com `pdfplumber`
3. Formatar com Claude usando a API
4. Salvar em `Mind/Apostilas/` como arquivos `.md`

## Variáveis de Ambiente

Você precisa ter uma chave da API Anthropic configurada:
```bash
set ANTHROPIC_API_KEY=sua_chave_aqui
```

Ou adicione em um arquivo `.env` na raiz do projeto.
