# Conhecimento

Use esta skill para gerenciar a base de conhecimento técnica e setorial na pasta `Mind/Conhecimento/`. Esta base organiza informações sobre Mercado Financeiro, Fundos de Investimento, Agronegócio, Crédito, Risco, Contabilidade, Operações, Métodos Quantitativos, Economia, Gestão de Carteiras, Tecnologia Financeira e temas regulatórios.

## Diretrizes de Preenchimento

Antes de qualquer operação, consulte o arquivo central de regras: `Mind/REGRAS_CONHECIMENTO.md`. Se as regras já estiverem explícitas na conversa, não é necessário consultar novamente.

### 1. Codificação e Idioma
- **Encoding:** salve sempre em **UTF-8**, preferencialmente sem BOM.
- **Idioma:** Português (Brasil).
- **Validação:** após lotes grandes, releia uma amostra dos arquivos no terminal e no Obsidian para verificar a acentuação.
- **Cuidado com legado:** se um arquivo antigo aparecer com caracteres corrompidos no terminal, confirme o encoding real antes de assumir que o conteúdo novo foi danificado.

### 2. Nomenclatura e Estrutura
- **Arquivos:** use `Snake_Case.md` (ex: `Analise_de_Credito.md`).
- **Título:** use `# Título Amigável` no topo do arquivo.
- **Estrutura obrigatória:**
  1. Título (`#`)
  2. Resumo contextual
  3. Conteúdo organizado (`##`, `###`)
  4. Referências e Links (`## Referências e Links`)
  5. Rodapé de navegação (links para índices)
  6. Hashtags
- **Conectividade mínima:** toda nota nova deve ter:
  1. link para o índice da categoria
  2. link para `[[Mind/Conhecimento/indice|Índice Principal]]`
  3. pelo menos 3 links semânticos para notas relacionadas, quando o tema comportar

### 3. Links, YAML e Atualidade
- Use `[[Caminho/Relativo/Nota|Texto Exibido]]` para criar conexões.
- **Proatividade:** linke termos técnicos para suas respectivas notas ou para o `[[Glossario/Glossario|Glossário]]`.
- **Relacionamentos cruzados:** conecte Agronegócio a Crédito, Fundos a Contabilidade, Regulação a Gestão, e Mercado a Carteiras quando houver relação direta.
- **Backlinks:** ao criar um conceito novo importante, atualize também notas antigas relacionadas.
- **Nota-hub:** se o assunto ficar grande demais, transforme a nota principal em hub e distribua o detalhe em notas filhas.
- **Notas voláteis:** use YAML completo com `fonte_principal`, `fonte_tipo`, `data_base_fonte`, `status_revisao` e `volatilidade`.
- **Datas absolutas:** em temas voláteis, evite “atualmente” e registre sempre uma data-base explícita.

## Fluxo de Trabalho

1. **Pesquisa:** verifique se a nota já existe usando `rg` ou `obsidian search`.
2. **Mapeamento:** compare a fonte com a taxonomia atual e verifique se o conteúdo cabe nas categorias existentes.
3. **Localização:** identifique a pasta correta em `Mind/Conhecimento/`.
   - Se a fonte introduzir um domínio recorrente e transversal, proponha nova categoria ou subcategoria.
   - Ao alterar a estrutura, atualize `Mind/REGRAS_CONHECIMENTO.md` e `.claude/skills/conhecimento.md`.
4. **Avaliação de custo e contexto:**
   - Antes de usar agentes ou LLMs auxiliares, compare custo provável de tokens, tamanho do contexto e risco de inconsistência.
   - Só delegue lotes semanticamente coesos, com contexto mínimo.
   - Não envie o PDF inteiro nem a árvore completa do vault se o lote exigir apenas uma parte.
5. **Criação/Edição:**
   - Se estiver criando, use o template definido em `REGRAS_CONHECIMENTO.md`.
   - Se estiver editando, preserve os links existentes e adicione novas conexões.
   - Reserve ao agente principal a taxonomia, deduplicação e revisão final da coerência editorial.
6. **Atualização do índice:** se criar uma nova nota principal, adicione-a ao `Indice_*.md` da pasta correspondente.
7. **Revisão de links:** ao final, revise índices, backlinks, notas órfãs e duplicidades conceituais.
8. **Passada global barata:** após lotes relevantes, faça uma revisão global de links em `Mind/Conhecimento/`. Se houver apoio de LLM, use sempre o modelo mais barato suficiente para:
   - completar links mínimos
   - reforçar backlinks óbvios
   - adicionar links para índices e hubs
9. **YAML oportunístico:** se a passada global já estiver lendo o arquivo e a alteração for simples, normalize YAML no mesmo ciclo.
10. **Controle de revisão:** atualize `[[Controle_de_Revisao_do_Conhecimento|Controle de Revisão do Conhecimento]]` quando tocar notas voláteis.
11. **Validação:** verifique se os links criados estão corretos, se as hashtags foram incluídas e se não há erros com acentuação.

## Categorias de Pastas
- `Mercado_Financeiro/`: macro, instrumentos, precificação, índices, derivativos.
- `Fundos_Investimento/`: regulação de fundos, tributação e tipos de fundos.
- `Fundos_Investimento/FIDC/`: FIDC e securitização.
- `Fundos_Investimento/FIAGRO/`: FIAGRO e aplicações no agro.
- `Fundos_Investimento/FII/`: fundos imobiliários.
- `Fundos_Investimento/FIP/`: participações e private equity.
- `Fundos_Investimento/ETF/`: ETFs e fundos de índice.
- `Agronegocio/`: cadeias produtivas, safras, logística, sustentabilidade no agro.
- `Credito_e_Risco/`: rating, análise de crédito, garantias, default, tipos de risco.
- `Contabilidade_e_Controle/`: COSIF, cota, DCF, despesas, marcação e demonstrações.
- `Metodos_Quantitativos/`: estatística, regressão, probabilidade, taxas, valor do dinheiro no tempo.
- `Economia/`: microeconomia, macroeconomia, SFN, política fiscal e monetária, câmbio.
- `Analise_Financeira_e_Corporativa/`: governança, estrutura de capital, demonstrações, orçamento de capital.
- `Gestao_de_Carteiras/`: IPS, alocação, benchmarks, rebalanceamento, performance.
- `Tecnologia_e_Inovacao_Financeira/`: crowdfunding, CVM 88, inovação financeira.
- `Portfolio/`: informações específicas dos fundos da gestora.
- `Juridico_e_Regulatorio/`: leis, compliance, ANBIMA, CVM, ASG.
- `Estruturacao_e_Operacoes/`: originação, custódia, servicing, escrituração, registradoras.
- `Glossario/`: definições de termos técnicos.

## Exemplo de Nota Volátil

```markdown
---
categoria: Juridico e Regulatorio
tags: [agro, juridico, regulacao]
fonte_principal: Lei 13.986/2020
fonte_tipo: norma_primaria
ultima_atualizacao: 2026-04-18
data_base_fonte: 2026-04-18
status_revisao: vigente
volatilidade: alta
---

# Lei do Agro (Lei 13.986/2020)

A nota resume a norma com data-base explícita e links para seus efeitos operacionais.

## Referências e Links
- [[Juridico_e_Regulatorio/Indice_Juridico|Jurídico e Regulatório]]
- [[Credito_e_Risco/CPR_Cedula_Produto_Rural|CPR]]
- [[Fundos_Investimento/FIAGRO/FIAGRO_Conceitos|FIAGRO]]

---
[[Mind/Conhecimento/indice|Índice Principal]]

#juridico #agro #regulacao
```
