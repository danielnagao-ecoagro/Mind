# Regras de Preenchimento da Base de Conhecimento

Este documento estabelece o padrão para a criação, edição e revisão contínua de notas na pasta `Conhecimento`. Qualquer agente, IA ou humano, deve seguir estas diretrizes para manter a organização, a atualidade e a navegabilidade via Obsidian.

## 1. Codificação e Idioma
- **Encoding:** todos os arquivos devem ser salvos em **UTF-8**, preferencialmente sem BOM.
- **Idioma:** o conteúdo deve ser escrito em Português (Brasil).
- **Checagem obrigatória em lotes grandes:** após criar ou editar muitas notas, reabra uma amostra no terminal e no Obsidian para confirmar que a acentuação foi preservada.
- **Notas legadas:** se um arquivo antigo aparecer com caracteres corrompidos, confirme o encoding real antes de reescrever o conteúdo.

## 2. Padrão de Nomenclatura
- **Arquivos:** use `Snake_Case` ou `PascalCase` para nomes de arquivos. Evite espaços nos nomes físicos.
- **Títulos:** dentro do arquivo, use o Título 1 (`#`) com o nome amigável.

## 3. Estrutura da Nota
Toda nota deve seguir esta estrutura básica:
1. **Título Principal:** `# Título do Assunto`
2. **Contexto/Resumo:** um breve parágrafo explicando o tema
3. **Conteúdo:** organizado por subtítulos (`##`, `###`)
4. **Links Relacionados:** uma seção ao final chamada `## Referências e Links`
5. **Rodapé de Navegação:** link para o índice da categoria e para o índice principal

### Conectividade mínima
Toda nota nova deve ter, salvo casos muito pequenos:
- 1 link para o índice da categoria
- 1 link para `[[Mind/Conhecimento/indice|Índice Principal]]`
- pelo menos 3 links semânticos para notas relacionadas

## 4. Sistema de Links (Wikilinks)
- **Proatividade:** sempre que mencionar um termo técnico que possua, ou deva possuir, uma nota própria, envolva-o em `[[ ]]`.
- **Links relativos:** use o caminho relativo para garantir que o Obsidian encontre a nota.
- **Glossário:** termos muito específicos devem ser linkados para o `[[Glossario/Glossario|Glossário]]`.
- **Backlinks:** ao criar um conceito novo importante, atualize também notas antigas relacionadas.
- **Notas-hub:** se o assunto ficar grande demais, transforme a nota principal em hub e distribua o detalhe em notas filhas por conceito.
- **Revisão global de links:** após lotes relevantes de criação ou edição, execute uma passada global de links em `Mind/Conhecimento/`. Se houver apoio de LLM para essa etapa, use sempre o modelo mais barato que seja suficiente para revisão mecânica de wikilinks.

## 5. Relações Inter-áreas
- Notas de **Crédito** devem referenciar garantias do **Agronegócio** quando houver relação direta.
- Notas de **Portfolio** devem referenciar conceitos de **Contabilidade** e **Regulatório**.
- Notas de **Mercado** devem se conectar a **Gestão de Carteiras** quando houver relação com benchmark, alocação ou performance.
- Notas de **Regulatório** devem se conectar a **Fundos**, **Gestão** e **Compliance** quando a norma afetar esses domínios.

## 6. Expansão da Taxonomia
- Se uma nova fonte introduzir um domínio recorrente e transversal que não se encaixe bem na estrutura atual, crie nova categoria ou subcategoria.
- Não force grandes blocos conceituais para dentro de pastas inadequadas apenas para preservar a estrutura antiga.
- Ao expandir a taxonomia, atualize os índices afetados, este arquivo de regras e a skill correspondente.

## 7. Metadados
### 7.1 Padrão mínimo
Sempre que possível, inclua um bloco YAML no topo para facilitar buscas futuras:

```yaml
---
categoria:
tags: [agro, fidc, contabil]
ultima_atualizacao: YYYY-MM-DD
---
```

### 7.2 Padrão para notas voláteis
Notas regulatórias, tributárias, operacionais ou de mercado com risco maior de desatualização devem usar o bloco completo:

```yaml
---
categoria:
tags: []
fonte_principal:
fonte_tipo: norma_primaria
ultima_atualizacao: YYYY-MM-DD
data_base_fonte: YYYY-MM-DD
status_revisao: vigente
volatilidade: alta
---
```

Valores esperados:
- `fonte_tipo`: `norma_primaria|autorregulacao|documento_de_mercado|material_didatico|demonstracao_financeira|academico`
- `status_revisao`: `vigente|revisar|desatualizada|parcial`
- `volatilidade`: `alta|media|baixa`

### 7.3 Regra de baixo custo
- Se um lote já estiver lendo todos os arquivos para revisão de links, aproveite a mesma passada para normalizar YAML quando a alteração for mecânica e de baixo custo.
- Não faça retrofit amplo só para adicionar YAML em notas estáveis e periféricas.

## 8. Atualidade e Data-base
- **Separação obrigatória:** diferencie conceito estável de informação datada.
- **Datas absolutas:** prefira escrever `vigente em 2026-04-18` em vez de `atualmente`, `recentemente` ou `nova regra`.
- **Data-base:** toda nota volátil deve explicitar até quando a fonte principal foi conferida.
- **Fontes primárias:** em temas regulatórios e tributários, priorize CVM, CMN, Banco Central, leis e documentos oficiais.

## 9. Volatilidade e Cadência de Revisão
- **Alta volatilidade:** regulação, tributação, benchmarks, regras operacionais. Revisão sugerida a cada 30-90 dias.
- **Média volatilidade:** práticas de mercado, estruturas de fundos, interpretações usuais. Revisão sugerida semestral.
- **Baixa volatilidade:** teoria, fundamentos quantitativos e conceitos estáveis. Revisão anual ou quando houver conflito relevante.

Notas de alta e média volatilidade devem ser listadas em `[[Controle_de_Revisao_do_Conhecimento|Controle de Revisão do Conhecimento]]`.

## 10. Hashtags
- **Localização:** sempre ao final do arquivo, após o rodapé de navegação.
- **Objetivo:** facilitar a busca e filtragem no Obsidian.
- **Formato:** use hashtags que representem temas amplos e específicos.

## 11. Validação Final
Após um lote relevante de criação ou edição:
- confirme que toda nota nova aparece no `Indice_*.md` correto
- confirme que não existem notas órfãs sem caminho de entrada
- revise duplicatas conceituais evidentes
- valide wikilinks e navegabilidade no Obsidian
- atualize a nota `[[Controle_de_Revisao_do_Conhecimento|Controle de Revisão do Conhecimento]]` quando o lote tocar notas voláteis
- se tiver havido leitura ampla do vault, aproveite para normalizar YAML dos arquivos tocados

---
Este padrão visa transformar a base em um cérebro digital altamente conectado, auditável e sustentável ao longo do tempo.
