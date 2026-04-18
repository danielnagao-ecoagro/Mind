---
categoria: Contabilidade e Controle
tags: [contabilidade, mtm, ndf, derivativos, cambio]
fonte_principal: material didatico consolidado
fonte_tipo: material_didatico
ultima_atualizacao: 2026-04-18
data_base_fonte: 2026-04-18
status_revisao: vigente
volatilidade: media
---

# Marcação a Mercado Diária de NDF

A marcação a mercado diária de um [[Mercado_Financeiro/NDF_Non_Deliverable_Forward|NDF]] recalcula o valor presente do derivativo em cada fechamento, refletindo spot, curva, prazo remanescente e critérios de desconto da data. Esse processo alimenta resultado, reconciliação de posição e cálculo de patrimônio em carteiras e fundos com exposição cambial.

## Objetivo do MtM diário

O objetivo é registrar quanto o contrato vale hoje, e não quanto poderá liquidar apenas no vencimento. Isso evita distorção de resultado e garante que entradas, saídas e relatórios usem um valor econômico coerente com o mercado corrente.

## Lógica operacional

O fechamento diário normalmente segue esta sequência:
1. capturar spot, curva doméstica, curva externa e parâmetros de fixing
2. recalcular a taxa a termo justa para o prazo remanescente
3. comparar a nova taxa justa com a taxa contratada
4. descontar o ajuste esperado até a data de liquidação
5. reconhecer a variação de MtM contra o fechamento anterior

## Fórmula conceitual

Uma forma simplificada de pensar o fechamento é:

`MtM_t = N x (F_t - K) x DF_t`

E o resultado diário:

`P&L_dia = MtM_t - MtM_(t-1)`

Onde:
- `N` é o notional
- `F_t` é a taxa justa na data `t`
- `K` é a taxa contratada
- `DF_t` é o fator de desconto da data `t`

## Exemplo simplificado de reconciliação diária

Dia `D-1`:
- notional = `USD 1.000.000`
- taxa contratada = `5,52`
- taxa justa remanescente = `5,58`
- fator de desconto = `0,996`

`MtM_(D-1) = 1.000.000 x (5,58 - 5,52) x 0,996 = 59.760`

Dia `D`:
- taxa justa remanescente = `5,61`
- fator de desconto = `0,997`

`MtM_D = 1.000.000 x (5,61 - 5,52) x 0,997 = 89.730`

Resultado diário aproximado:

`89.730 - 59.760 = 29.970`

Esse ganho diário reflete a atualização conjunta de spot, curva e passagem do tempo.

## O que normalmente explica a variação diária

- movimento do câmbio spot
- abertura ou fechamento de cupom cambial
- deslocamento da curva de juros local
- deslocamento da curva externa
- redução do prazo remanescente
- mudança em fixing, calendário ou convenção

## Controles importantes

- conferir se a ponta comprada ou vendida está com o sinal correto
- validar a coerência entre notional em moeda estrangeira e moeda funcional
- reconciliar MtM do sistema interno com contraparte ou administrador
- separar efeito de mercado de erro operacional de cadastro
- documentar fontes de curva e horário de fechamento

## Relação com contabilidade e fundos

Em fundos e carteiras, o MtM diário afeta:
- resultado do período
- patrimônio líquido
- valor da cota
- relatórios de risco e exposição

Por isso, o tema conversa diretamente com [[Marcacao_a_Mercado_vs_Curva|marcação a mercado vs. curva]], [[Fundos_Investimento/FIDC/Calculo_de_PL_e_Cota_em_FIDC|cálculo de PL e cota em FIDC]] e rotinas de [[Conciliacao_de_Caixa_e_Posicao_em_FIDC|conciliação de caixa e posição]] quando houver derivativos no escopo da estrutura.

Uma forma prática de visualizar a reconciliação entre um dia e outro está em [[Mercado_Financeiro/Caso_Numerico_de_NDF_com_Curva_e_MtM_Diario|caso numérico de NDF com curva e MtM diário]].

## Pontos de atenção

- NDF não deve ser tratado como ativo na curva; sua natureza exige atualização por preço justo
- convenções de dia útil e fixing podem mudar o valor mesmo sem grande movimento de spot
- comparar apenas o ajuste de vencimento sem trazer a valor presente distorce o MtM antes do vencimento
- diferenças pequenas de curva acumulam ruído relevante em books grandes

## Referências e Links
- [[Indice_Contabilidade|Contabilidade e Controle]]
- [[Mercado_Financeiro/Precificacao_de_NDF|Precificação de NDF]]
- [[Mercado_Financeiro/Cupom_Cambial_e_Pontos_Forward|Cupom Cambial e Pontos Forward]]
- [[Mercado_Financeiro/Caso_Numerico_de_NDF_com_Curva_e_MtM_Diario|Caso Numérico de NDF com Curva e MtM Diário]]
- [[Mercado_Financeiro/NDF_Non_Deliverable_Forward|NDF - Non-Deliverable Forward]]
- [[Marcacao_a_Mercado_vs_Curva|Marcação a Mercado vs. Curva]]
- [[Fundos_Investimento/FIDC/Calculo_de_PL_e_Cota_em_FIDC|Cálculo de PL e Cota em FIDC]]
- [[Fundos_Investimento/FIDC/Rotina_Diaria_de_Fechamento_de_FIDC|Rotina Diária de Fechamento de FIDC]]
- [[Mercado_Financeiro/Derivativos_e_Hedge|Derivativos e Hedge]]

---
[[Indice_Contabilidade|Voltar para Contabilidade e Controle]]
[[Mind/Conhecimento/indice|Índice Principal]]

#contabilidade #mtm #ndf #derivativos #cambio
