---
categoria: Mercado Financeiro
tags: [mercado, derivativos, ndf, cambio, precificacao]
fonte_principal: material didatico consolidado
fonte_tipo: material_didatico
ultima_atualizacao: 2026-04-18
data_base_fonte: 2026-04-18
status_revisao: vigente
volatilidade: media
---

# Precificação de NDF

A precificação de um [[NDF_Non_Deliverable_Forward|NDF]] depende do diferencial entre a taxa contratada e a taxa a termo implícita pelas curvas de mercado na data de avaliação. Em termos práticos, o NDF vale próximo de zero na origem quando é fechado a mercado e passa a ter valor positivo ou negativo conforme a curva, o câmbio spot e o prazo remanescente se movem.

## Intuição econômica

Um NDF em câmbio replica economicamente uma posição a termo sem entrega física da moeda. O valor do contrato nasce da comparação entre:
- a taxa contratada no fechamento
- a taxa a termo justa para o prazo remanescente
- o notional sobre o qual a diferença será liquidada

Se o contrato foi fechado para comprar dólar futuro a uma taxa abaixo da taxa a termo de mercado observada depois, o comprador tende a ter MtM positivo. Se a taxa contratada ficou acima da taxa justa corrente, o valor tende a ser negativo para ele.

## Taxa a termo implícita

Uma forma simplificada de estimar a taxa a termo justa é usar a paridade entre curvas doméstica e externa:

`F = S x (1 + i_dom x t) / (1 + i_ext x t)`

Onde:
- `F` é a taxa a termo justa
- `S` é o câmbio spot
- `i_dom` é a taxa doméstica para o prazo
- `i_ext` é a taxa externa para o mesmo prazo
- `t` é a fração de tempo segundo a convenção adotada

Na prática, a mesa pode usar [[Curva_de_Juros_e_Spread|curva de juros]], cupom cambial, pontos forward e fontes de mercado específicas. A lógica econômica, porém, continua sendo a mesma: o NDF incorpora o custo de carregamento relativo entre as moedas.

Esse elo entre diferencial de juros e forward fica mais claro em [[Cupom_Cambial_e_Pontos_Forward|cupom cambial e pontos forward]].

## Valor presente do NDF

Uma forma didática de precificar o contrato na data de avaliação é:

`PV = N x (F_mkt - K) x DF`

Onde:
- `PV` é o valor presente do NDF para quem está comprado na moeda objeto
- `N` é o notional na base de liquidação
- `F_mkt` é a taxa a termo justa para o prazo remanescente
- `K` é a taxa contratada
- `DF` é o fator de desconto até a liquidação

Dependendo da convenção da mesa, do CSA, da moeda de liquidação e da praça, a fórmula pode ser apresentada com ajustes de base e desconto em curva específica. O ponto central é que o valor decorre da diferença entre a taxa contratada e a taxa de mercado para o prazo remanescente.

## Exemplo simplificado

Considere:
- spot = `5,40`
- taxa contratada = `5,52`
- taxa a termo justa remanescente = `5,60`
- notional = `USD 1.000.000`
- fator de desconto = `0,995`

Diferença econômica:

`(5,60 - 5,52) x 1.000.000 = 80.000`

Valor presente aproximado:

`80.000 x 0,995 = 79.600`

Nesse exemplo, o contrato tem valor positivo aproximado de `R$ 79.600` para a ponta comprada em dólar, assumindo liquidação financeira em reais e sem outros ajustes operacionais.

## Principais drivers de preço

- variação do câmbio spot
- deslocamento da curva doméstica
- deslocamento da curva externa
- redução do prazo remanescente
- convenção de dias, fixing e moeda de liquidação

## Erros recorrentes

- confundir taxa spot com taxa justa a termo
- ignorar o desconto a valor presente da liquidação
- usar convenção de dias inconsistente com a curva
- misturar notional em moeda local e estrangeira sem normalização
- tratar o NDF como se tivesse a mesma mecânica operacional de um [[Swap|swap]] com múltiplos fluxos

## Relação com MtM diário

A precificação econômica do NDF é a base da [[Contabilidade_e_Controle/Marcacao_a_Mercado_Diaria_de_NDF|marcação a mercado diária de NDF]]. O P&L diário decorre da diferença entre o valor presente calculado no fechamento anterior e o valor presente atualizado com a nova curva, novo spot e menor prazo remanescente.

Para ver essa mecânica integrada em números, consulte [[Caso_Numerico_de_NDF_com_Curva_e_MtM_Diario|caso numérico de NDF com curva e MtM diário]].

## Referências e Links
- [[Indice_Mercado|Mercado Financeiro]]
- [[NDF_Non_Deliverable_Forward|NDF - Non-Deliverable Forward]]
- [[Derivativos_e_Hedge|Derivativos e Hedge]]
- [[Termo_e_Futuro|Termo e Futuro]]
- [[Swap|Swap]]
- [[Curva_de_Juros_e_Spread|Curva de Juros e Spread]]
- [[Cupom_Cambial_e_Pontos_Forward|Cupom Cambial e Pontos Forward]]
- [[Caso_Numerico_de_NDF_com_Curva_e_MtM_Diario|Caso Numérico de NDF com Curva e MtM Diário]]
- [[Economia/Cambio_e_Comercio_Internacional|Câmbio e Comércio Internacional]]
- [[Contabilidade_e_Controle/Marcacao_a_Mercado_Diaria_de_NDF|Marcação a Mercado Diária de NDF]]
- [[Contabilidade_e_Controle/Marcacao_a_Mercado_vs_Curva|Marcação a Mercado vs. Curva]]

---
[[Indice_Mercado|Voltar para Mercado Financeiro]]
[[Mind/Conhecimento/indice|Índice Principal]]

#mercado #derivativos #ndf #cambio #precificacao
