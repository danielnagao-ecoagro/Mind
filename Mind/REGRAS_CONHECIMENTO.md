# Regras de Preenchimento da Base de Conhecimento

Este documento estabelece o padrão para a criação e edição de notas na pasta `Conhecimento`. Qualquer agente (IA ou humano) deve seguir estas diretrizes para manter a organização e a navegabilidade via Obsidian.

## 1. Codificação e Idioma
- **Encoding:** Todos os arquivos devem ser salvos em **UTF-8**. Isso é essencial para o suporte correto a acentos (ex: Agronegócio, Crédito, Operações).
- **Idioma:** O conteúdo deve ser escrito em Português (Brasil).

## 2. Padrão de Nomenclatura
- **Arquivos:** Use `Snake_Case` ou `PascalCase` para nomes de arquivos (ex: `Analise_de_Credito.md`). Evite espaços nos nomes de arquivos físicos para prevenir erros de path.
- **Títulos:** Dentro do arquivo, use o Título 1 (`#`) com o nome amigável (ex: `# Análise de Crédito`).

## 3. Estrutura da Nota
Toda nota deve seguir esta estrutura básica:
1. **Título Principal:** `# Título do Assunto`
2. **Contexto/Resumo:** Um breve parágrafo explicando o que é o tema.
3. **Conteúdo:** Organizado por subtítulos (`##`, `###`).
4. **Links Relacionados:** Uma seção ao final chamada `## Referências e Links`.
5. **Rodapé de Navegação:** Link para o índice da categoria e para o índice principal.

## 4. Sistema de Links (Wikilinks)
- **Proatividade:** Sempre que mencionar um termo técnico que possua (ou deva possuir) uma nota própria, envolva-o em `[[ ]]`.
- **Links Relativos:** Use o caminho relativo para garantir que o Obsidian encontre a nota. Exemplo: `[[Mercado_Financeiro/Selic_CDI|Taxa Selic]]`.
- **Glossário:** Termos muito específicos devem ser linkados para o `[[Glossario/Glossario|Glossário]]`.

## 5. Relações Inter-áreas
- Notas de **Crédito** devem referenciar garantias do **Agronegócio** (ex: `[[Agronegocio/Cadeia_Produtiva|CPR]]`).
- Notas de **Portfolio** (fundos específicos) devem referenciar conceitos de **Contabilidade** e **Regulatório**.

## 6. Metadados (Opcional)
Se possível, inclua um bloco YAML no topo para facilitar buscas futuras:
```yaml
---
categoria: 
tags: [agro, fidc, contabil]
ultima_atualizacao: YYYY-MM-DD
---
```

## 7. Hashtags
- **Localização:** Sempre ao final do arquivo, após o rodapé de navegação.
- **Objetivo:** Facilitar a busca e filtragem no Obsidian.
- **Formato:** Use hashtags que representem temas amplos e específicos (ex: `#agro #credito #regulacao #cvm175`).

---
*Este padrão visa transformar a base em um "Cérebro Digital" altamente conectado.*
