# Caso Numérico de Cash Flow, TIR e Spread em FIDC

Este caso conecta [[Modelagem_de_Cash_Flow_de_FIDC|cash flow]], [[TIR_Bruta_vs_TIR_Liquida_em_FIDC|TIR líquida]] e [[Excesso_de_Spread|excesso de spread]] em uma estrutura simplificada de [[FIDC_Conceitos|FIDC]].

## Premissas do caso
- carteira comprada por 1.000.000
- fluxo bruto esperado em 12 meses: 1.220.000
- despesa total esperada do fundo no período: 40.000
- perda líquida esperada da carteira: 60.000
- caixa médio ocioso e arrasto financeiro estimado: 20.000
- remuneração alvo da classe sênior no período: 130.000

## Passo 1: retorno bruto da carteira
Antes de despesas e perdas, a carteira gera:

`Resultado_bruto = 1.220.000 - 1.000.000 = 220.000`

Em termos simples, isso representa a base econômica da TIR bruta da carteira.

## Passo 2: retorno líquido da estrutura
Subtraindo despesas, perda líquida e drag de caixa:

`Resultado_liquido = 220.000 - 40.000 - 60.000 - 20.000 = 100.000`

Esse é o resultado econômico simplificado que sobra para remunerar a estrutura após as principais fricções.

## Passo 3: leitura do spread residual
Se a classe sênior precisa de 130.000 no período, o spread residual fica negativo:

`Spread_residual = 100.000 - 130.000 = -30.000`

Isso indica que a carteira não está gerando resultado suficiente para cobrir integralmente o custo da classe prioritária.

## Passo 4: interpretação de TIR
### TIR bruta
A TIR bruta deriva do fluxo dos ativos comprados, antes da estrutura.

### TIR líquida
A TIR líquida relevante para a estrutura ou para a subordinada será menor, porque o fluxo efetivo disponível já foi reduzido por despesas, perdas e arrasto de caixa.

## O que o caso mostra
- carteira com retorno bruto positivo pode ainda destruir proteção
- TIR bruta sozinha não garante folga de spread
- o teste correto é olhar o fluxo líquido após a estrutura
- spread negativo pressiona subordinação, caixa acumulado e possíveis gatilhos

## Variação rápida
Se a perda líquida cair de 60.000 para 20.000:

`Resultado_liquido = 220.000 - 40.000 - 20.000 - 20.000 = 140.000`

Nesse cenário:

`Spread_residual = 140.000 - 130.000 = 10.000`

A estrutura volta a gerar excedente econômico.

## Referências e Links
- [[Indice_FIDC|FIDC]]
- [[Matematica_Financeira_de_FIDC|Matemática Financeira de FIDC]]
- [[Modelagem_de_Cash_Flow_de_FIDC|Modelagem de Cash Flow de FIDC]]
- [[TIR_Bruta_vs_TIR_Liquida_em_FIDC|TIR Bruta vs. TIR Líquida em FIDC]]
- [[Excesso_de_Spread|Excesso de Spread]]
- [[Break_Even_de_Excesso_de_Spread|Break-Even de Excesso de Spread]]

---
[[Indice_FIDC|Voltar para FIDC]]
[[Mind/Conhecimento/indice|Índice Principal]]

#fidc #caso #cashflow #tir #spread
