---
categoria: Mercado Financeiro
tags: [mercado, derivativos, ndf, cambio, mtm, caso_numerico]
fonte_principal: material didatico consolidado
fonte_tipo: material_didatico
ultima_atualizacao: 2026-04-18
data_base_fonte: 2026-04-18
status_revisao: vigente
volatilidade: media
---

# Caso Numérico de NDF com Curva e MtM Diário

Este caso integra [[Precificacao_de_NDF|precificação de NDF]], [[Cupom_Cambial_e_Pontos_Forward|cupom cambial e pontos forward]] e [[Contabilidade_e_Controle/Marcacao_a_Mercado_Diaria_de_NDF|marcação a mercado diária]]. O objetivo é mostrar como spot, curva e passagem do tempo alteram o valor presente do contrato entre um fechamento e outro.

## Premissas do contrato

- posição: comprada em dólar
- notional: `USD 1.000.000`
- taxa contratada: `5,52`
- liquidação financeira em reais
- prazo original: `90` dias

## Dia 0: fechamento do contrato

Parâmetros de mercado:
- spot = `5,40`
- taxa doméstica = `12,00% a.a.`
- taxa externa = `5,00% a.a.`
- prazo = `0,25`

Forward justo aproximado:

`F_0 = 5,40 x (1 + 0,12 x 0,25) / (1 + 0,05 x 0,25)`

`F_0 ≈ 5,49`

Nesse cenário, a taxa contratada de `5,52` está acima do forward justo. Isso significa que a posição comprada em dólar nasce ligeiramente desfavorável.

Se usarmos fator de desconto próximo de `0,97`, o MtM inicial aproximado seria:

`MtM_0 = 1.000.000 x (5,49 - 5,52) x 0,97 = -29.100`

Em uma negociação real, o contrato costuma nascer perto de zero porque a taxa contratada reflete o preço justo de tela ou a negociação bilateral do momento. Aqui a diferença foi mantida propositalmente para fins didáticos.

## Dia 1: novo fechamento

Um dia depois:
- spot = `5,43`
- taxa doméstica para o prazo remanescente = `11,80% a.a.`
- taxa externa para o prazo remanescente = `5,10% a.a.`
- prazo remanescente = `89/360`

Forward justo remanescente:

`F_1 = 5,43 x (1 + 0,118 x 89/360) / (1 + 0,051 x 89/360)`

`F_1 ≈ 5,51`

Com fator de desconto aproximado de `0,971`, o novo MtM seria:

`MtM_1 = 1.000.000 x (5,51 - 5,52) x 0,971 = -9.710`

## Resultado diário

`P&L_1 = MtM_1 - MtM_0`

`P&L_1 = -9.710 - (-29.100) = +19.390`

Mesmo continuando levemente negativo, o contrato gerou ganho diário para a ponta comprada em dólar porque ficou menos fora do dinheiro.

## Leitura econômica do movimento

O resultado do dia pode ser explicado por três vetores:
- o spot subiu de `5,40` para `5,43`
- o prazo remanescente caiu, reduzindo parte do carregamento
- o diferencial entre taxa doméstica e externa mudou, alterando o forward justo

## Separação didática dos efeitos

Uma leitura útil é decompor a variação em:
- efeito spot
- efeito curva
- efeito passagem do tempo

Em ambiente de controle, essa decomposição ajuda a reconciliar:
- P&L de mesa
- MtM contábil
- diferença entre curva interna e curva da contraparte

## Como isso entra no fechamento

No fechamento diário, a equipe normalmente:
1. atualiza spot e curvas
2. recalcula o forward justo para o prazo remanescente
3. aplica o fator de desconto correto
4. compara o novo MtM com o MtM do dia anterior
5. reconhece o resultado diário

## Pontos de atenção

- uma pequena diferença de forward pode gerar P&L relevante em notionals altos
- sinal da posição precisa estar consistente com comprado ou vendido
- usar spot sem curva produz erro material de precificação
- comparar apenas a liquidação final e ignorar valor presente distorce o fechamento diário

## Referências e Links
- [[Indice_Mercado|Mercado Financeiro]]
- [[Precificacao_de_NDF|Precificação de NDF]]
- [[Cupom_Cambial_e_Pontos_Forward|Cupom Cambial e Pontos Forward]]
- [[NDF_Non_Deliverable_Forward|NDF - Non-Deliverable Forward]]
- [[Contabilidade_e_Controle/Marcacao_a_Mercado_Diaria_de_NDF|Marcação a Mercado Diária de NDF]]
- [[Contabilidade_e_Controle/Marcacao_a_Mercado_vs_Curva|Marcação a Mercado vs. Curva]]

---
[[Indice_Mercado|Voltar para Mercado Financeiro]]
[[Mind/Conhecimento/indice|Índice Principal]]

#mercado #derivativos #ndf #mtm #caso_numerico
