# Conhecimento

Use esta skill para gerenciar a base de conhecimento técnica e setorial na pasta `Mind/Conhecimento/`. Esta base organiza informações sobre Mercado Financeiro, Fundos de Investimento (FIDC, FIAGRO, FII), Agronegócio, Crédito, Risco, Contabilidade e Operações.

## Diretrizes de Preenchimento

Antes de qualquer operação, consulte o arquivo central de regras: `Mind/REGRAS_CONHECIMENTO.md`.

### 1. Codificação e Idioma
- **Encoding:** Salve sempre em **UTF-8** para suportar acentos.
- **Idioma:** Português (Brasil).

### 2. Nomenclatura e Estrutura
- **Arquivos:** Use `Snake_Case.md` (ex: `Analise_de_Credito.md`).
- **Título:** Use `# Título Amigável` no topo do arquivo.
- **Estrutura Obrigatória:**
    1. Título (`#`)
    2. Resumo Contextual
    3. Conteúdo Organizado (`##`, `###`)
    4. Referências e Links (`## Referências e Links`)
    5. Rodapé de Navegação (Links para índices)
    6. Hashtags (Ex: `#agro #credito`)

### 3. Links e Conectividade (Cérebro Digital)
- Use `[[Caminho/Relativo/Nota|Texto Exibido]]` para criar conexões.
- **Proatividade:** Linke termos técnicos para suas respectivas notas ou para o `[[Glossario/Glossario|Glossário]]`.
- **Relacionamentos Cruzados:** Conecte o Agronegócio ao Crédito, e os Fundos à Contabilidade.

## Fluxo de Trabalho

1. **Pesquisa:** Verifique se a nota já existe usando `rg` ou `obsidian search`.
2. **Localização:** Identifique a pasta correta em `Mind/Conhecimento/` (ex: `Agronegocio/`, `Portfolio/`).
3. **Criação/Edição:** 
    - Se estiver criando, use o template definido em `REGRAS_CONHECIMENTO.md`.
    - Se estiver editando, preserve os links existentes e adicione novas conexões.
4. **Atualização do Índice:** Se criar uma nova nota principal, adicione-a ao `Indice_*.md` da pasta correspondente.
5. **Validação:** Verifique se os links criados estão corretos e se as hashtags foram incluídas.

## Categorias de Pastas
- `Mercado_Financeiro/`: Macroeconomia, taxas, indicadores.
- `Fundos_Investimento/`: Regulação (CVM 175), tipos de fundos.
- `Agronegocio/`: Cadeias produtivas, safras, logística.
- `Credito_e_Risco/`: Rating, garantias (CPR), ESG.
- `Contabilidade_e_Controle/`: COSIF, cálculo de cota, auditoria.
- `Portfolio/`: Informações específicas dos fundos da gestora.
- `Juridico_e_Regulatorio/`: Leis (Lei do Agro), Compliance, PLD.
- `Estruturacao_e_Operacoes/`: Originação, custódia, servicing.
- `Glossario/`: Definições de termos técnicos.

## Exemplo de Nota

```markdown
# CPR - Cédula de Produto Rural

A CPR é o principal instrumento de financiamento privado do agronegócio...

## Tipos
- **CPR Física:** Entrega do produto.
- **CPR Financeira:** Liquidação em dinheiro.

## Referências e Links
- [[Agronegocio/Indice_Agro|Voltar para Agronegócio]]
- [[Juridico_e_Regulatorio/Lei_do_Agro|Lei do Agro]]

---
[[Mind/Conhecimento/indice|Índice Principal]]

#agro #credito #garantias
```
