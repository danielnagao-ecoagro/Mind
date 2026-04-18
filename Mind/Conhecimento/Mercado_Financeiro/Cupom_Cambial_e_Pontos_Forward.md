---
categoria: Mercado Financeiro
tags: [mercado, cambio, derivativos, ndf, cupom_cambial]
fonte_principal: material didatico consolidado
fonte_tipo: material_didatico
ultima_atualizacao: 2026-04-18
data_base_fonte: 2026-04-18
status_revisao: vigente
volatilidade: media
---

# Cupom Cambial e Pontos Forward

O [[NDF_Non_Deliverable_Forward|NDF]] em câmbio depende de uma taxa a termo que não nasce apenas do spot. Ela incorpora o diferencial entre o carregamento em moeda local e o carregamento na moeda estrangeira. Em prática de mercado, isso aparece na leitura de cupom cambial e de pontos forward.

## Intuição econômica

Se duas moedas têm custos de carregamento diferentes, a taxa a termo precisa refletir esse diferencial para evitar arbitragem. Por isso, o forward de dólar contra real normalmente difere do câmbio spot mesmo sem mudança de percepção direcional sobre a moeda.

## Pontos forward

Os pontos forward representam a diferença entre:

`Forward - Spot`

Se o spot está em `5,40` e o forward justo para 90 dias está em `5,48`, os pontos forward são `0,08` por dólar. Em algumas mesas, isso é expresso em pontos, pips ou centavos, conforme a convenção operacional.

## Cupom cambial

O cupom cambial é uma forma de enxergar o retorno implícito de uma aplicação em moeda estrangeira trazida para o ambiente doméstico. Em termos simplificados, ele conecta:
- o câmbio spot
- o câmbio forward
- a taxa doméstica
- a taxa externa

Didaticamente, ele ajuda a responder: qual é o diferencial de carregamento entre estar em reais e estar em dólar ao longo de um prazo?

## Relação com a paridade de taxas

Uma forma simplificada da relação é:

`F = S x (1 + i_dom x t) / (1 + i_ext x t)`

Logo, quanto maior a taxa doméstica em relação à externa, maior tende a ser o forward em relação ao spot, tudo o mais constante.

## Exemplo simplificado

Considere:
- spot = `5,40`
- taxa doméstica anualizada = `12,00%`
- taxa externa anualizada = `5,00%`
- prazo = `0,25`

Forward justo aproximado:

`F = 5,40 x (1 + 0,12 x 0,25) / (1 + 0,05 x 0,25)`

`F = 5,40 x 1,03 / 1,0125 ≈ 5,49`

Pontos forward aproximados:

`5,49 - 5,40 = 0,09`

## Por que isso importa no NDF

Sem entender cupom cambial e pontos forward, a [[Precificacao_de_NDF|precificação de NDF]] fica incompleta. O valor do contrato não depende apenas do spot de hoje, mas da taxa justa a termo para o prazo remanescente. Quando o cupom abre ou fecha, o MtM do NDF também muda mesmo que o spot fique quase estável.

## Erros recorrentes

- tratar o forward como mera expectativa direcional de spot
- ignorar o efeito do diferencial de juros entre moedas
- comparar pontos forward de prazos diferentes sem ajuste de convenção
- esquecer que uma mudança de cupom pode alterar o MtM sem grande movimento do câmbio à vista

## Referências e Links
- [[Indice_Mercado|Mercado Financeiro]]
- [[NDF_Non_Deliverable_Forward|NDF - Non-Deliverable Forward]]
- [[Precificacao_de_NDF|Precificação de NDF]]
- [[Contabilidade_e_Controle/Marcacao_a_Mercado_Diaria_de_NDF|Marcação a Mercado Diária de NDF]]
- [[Curva_de_Juros_e_Spread|Curva de Juros e Spread]]
- [[Economia/Cambio_e_Comercio_Internacional|Câmbio e Comércio Internacional]]

---
[[Indice_Mercado|Voltar para Mercado Financeiro]]
[[Mind/Conhecimento/indice|Índice Principal]]

#mercado #cambio #ndf #cupom_cambial #forward
