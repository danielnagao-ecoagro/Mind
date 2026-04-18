---
categoria: Conhecimento
tags: [governanca, revisao, links, yaml]
ultima_atualizacao: 2026-04-18
---

# Controle de Revisão do Conhecimento

Esta nota centraliza a governança de atualização da base. O objetivo é reduzir obsolescência, manter rastreabilidade de fontes e concentrar revisões nas notas com maior volatilidade ou maior impacto operacional.

## Regras de uso
- Atualize esta nota quando um lote tocar conteúdo regulatório, tributário, operacional ou de mercado.
- Use datas absolutas em notas voláteis e registre `data_base_fonte`.
- Após lotes relevantes, faça uma passada global de links em `Mind/Conhecimento/`.
- Se houver apoio de LLM para a passada global, use sempre o modelo mais barato suficiente para revisão mecânica de links.
- Se a passada já estiver lendo o arquivo e a alteração for simples, normalize YAML no mesmo ciclo.

## Cadência sugerida
- **Alta volatilidade:** revisar a cada 30-90 dias.
- **Média volatilidade:** revisar semestralmente.
- **Baixa volatilidade:** revisar anualmente ou por gatilho.

## Gatilhos de revisão
- nova lei, resolução, anexo, ofício ou ato relevante
- atualização material de regra ANBIMA, B3, registradora ou depositária
- mudança material em regulamento, lâmina ou relatório de fundo
- conflito entre a nota e documento mais recente
- ausência de revisão por prazo acima da cadência definida

## Fila atual
| Nota | Categoria | Volatilidade | Data-base | Próxima revisão | Gatilho principal | Fonte principal | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [[Fundos_Investimento/CVM_175|CVM 175]] | Fundos de Investimento | alta | 2026-04-18 | 2026-06-18 | mudança normativa consolidada | Resolução CVM 175 | vigente |
| [[Juridico_e_Regulatorio/CVM_160|CVM 160]] | Jurídico e Regulatório | alta | 2026-04-18 | 2026-06-18 | mudança em ofertas públicas | Resolução CVM 160 | vigente |
| [[Juridico_e_Regulatorio/CVM_175_Anexo_I|CVM 175 - Anexo I]] | Jurídico e Regulatório | alta | 2026-04-18 | 2026-06-18 | ajuste de correspondência do anexo | Resolução CVM 175 | parcial |
| [[Juridico_e_Regulatorio/CVM_175_Anexo_II|CVM 175 - Anexo II]] | Jurídico e Regulatório | alta | 2026-04-18 | 2026-06-18 | ajuste de correspondência do anexo | Resolução CVM 175 | parcial |
| [[Juridico_e_Regulatorio/CVM_175_Anexo_III|CVM 175 - Anexo III]] | Jurídico e Regulatório | alta | 2026-04-18 | 2026-06-18 | ajuste de correspondência do anexo | Resolução CVM 175 | parcial |
| [[Juridico_e_Regulatorio/CVM_175_Anexo_IV|CVM 175 - Anexo IV]] | Jurídico e Regulatório | alta | 2026-04-18 | 2026-06-18 | ajuste de correspondência do anexo | Resolução CVM 175 | parcial |
| [[Juridico_e_Regulatorio/CVM_175_Anexo_V|CVM 175 - Anexo V]] | Jurídico e Regulatório | alta | 2026-04-18 | 2026-06-18 | ajuste de correspondência do anexo | Resolução CVM 175 | parcial |
| [[Fundos_Investimento/FIAGRO/FIAGRO_Conceitos|FIAGRO - Conceitos]] | Fundos de Investimento | alta | 2026-04-18 | 2026-06-18 | mudança regulatória ou tributária | Lei 14.130/2021 e CVM 175 | vigente |
| [[Fundos_Investimento/FIDC/FIDC_Conceitos|FIDC - Conceitos]] | Fundos de Investimento | alta | 2026-04-18 | 2026-06-18 | mudança regulatória ou estrutural | Resolução CVM 175 | vigente |
| [[Fundos_Investimento/Tributacao_Fundos|Tributação de Fundos]] | Fundos de Investimento | alta | 2026-04-18 | 2026-05-18 | mudança tributária | legislação tributária e regras dos veículos | revisar |
| [[Juridico_e_Regulatorio/Lei_do_Agro|Lei do Agro]] | Jurídico e Regulatório | alta | 2026-04-18 | 2026-06-18 | alteração legal ou regulamentar | Lei 13.986/2020 | vigente |
| [[Mercado_Financeiro/Taxa_Selic|Taxa Selic]] | Mercado Financeiro | media | 2026-04-18 | 2026-07-18 | revisão de contexto macro ou política monetária | Banco Central do Brasil | vigente |

## Prioridade operacional
- Priorize links e YAML apenas nas notas tocadas pelo lote.
- Faça passada global barata para reforçar conectividade mínima.
- Evite retrofit amplo em notas estáveis sem gatilho claro.

## Referências e Links
- [[indice|Índice de Conhecimento]]
- [[Fundos_Investimento/Indice_Fundos|Fundos de Investimento]]
- [[Juridico_e_Regulatorio/Indice_Juridico|Jurídico e Regulatório]]
- [[Mercado_Financeiro/Indice_Mercado|Mercado Financeiro]]

---
[[indice|Índice Principal]]

#governanca #revisao #yaml #wikilinks #conhecimento
