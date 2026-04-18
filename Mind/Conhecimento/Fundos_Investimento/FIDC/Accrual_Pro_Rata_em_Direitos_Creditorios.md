# Accrual Pro Rata em Direitos Creditórios

O accrual pro rata em [[FIDC_Conceitos|FIDC]] é a apropriação diária da remuneração implícita de um ativo entre a data de aquisição e a data de liquidação ou vencimento, respeitando as [[Convencoes_de_Calculo_em_FIDC|convenções de cálculo]] do fundo.

## O que está sendo apropriado
O gestor reconhece economicamente a parcela de rendimento acumulada no período, separando o retorno já carregado do fluxo que ainda depende de tempo, adimplência e recuperação.

## Fórmula-base
Em uma leitura simplificada de carregamento pela curva:

`Valor_na_data = PU_inicial x (1 + i)^(dias_decorridos/base)`

O rendimento apropriado no período pode ser lido como:

`Accrual = Valor_na_data - Valor_no_inicio_do_periodo`

## Variáveis centrais
- preço de aquisição ou [[PU_e_Valor_Presente_em_FIDC|PU]]
- taxa contratada ou taxa interna da operação
- base de dias, como 252, 360 ou dias corridos
- número de dias transcorridos
- eventos de atraso, liquidação antecipada ou inadimplência

## Exemplo simples
Se o fundo compra um ativo por 9.800 e a taxa implícita é 24% ao ano em base 252, após 21 dias úteis o ativo não vale mais 9.800. Ele passa a refletir o rendimento carregado do período.

Em aproximação:
- PU inicial: 9.800
- taxa anual: 24%
- dias decorridos: 21
- base: 252

`Valor_na_data ≈ 9.800 x (1 + 0,24)^(21/252)`

Esse cálculo serve para o fechamento econômico, mas pode precisar de ajustes se houver atraso ou quebra da premissa de adimplência.

## Relação com o fechamento do fundo
O accrual afeta diretamente [[Valor_na_Curva_em_FIDC|valor na curva]], [[Calculo_de_PL_e_Cota_em_FIDC|PL e cota]] e reconciliação diária de posição. Se a metodologia for mal calibrada, o fundo pode aparentar rentabilidade superior ou inferior à realidade.

## Cuidados práticos
Em FIDC pulverizado, o cálculo raramente é puramente contratual. É comum precisar ajustar a apropriação para atraso, quebra de premissas, recompra, PDD e efeito real de cobrança.

## Sinais de alerta
- accrual crescendo mesmo com piora clara de atraso
- diferença recorrente entre caixa realizado e renda apropriada
- carteira marcada por curva sem ajuste para eventos de crédito
- uso de base de dias inconsistente entre compra, curva e relatório

## Referências e Links
- [[Indice_FIDC|FIDC]]
- [[Matematica_Financeira_de_FIDC|Matemática Financeira de FIDC]]
- [[Desagio_Cessao_PU_e_Taxa_Compra|Deságio, Cessão, PU e Taxa de Compra]]
- [[Convencoes_de_Calculo_em_FIDC|Convenções de Cálculo em FIDC]]
- [[Valor_na_Curva_em_FIDC|Valor na Curva em FIDC]]
- [[Rotina_Diaria_de_Fechamento_de_FIDC|Rotina Diária de Fechamento de FIDC]]
- [[Contabilidade_e_Controle/Conciliacao_de_Caixa_e_Posicao_em_FIDC|Conciliação de Caixa e Posição em FIDC]]

---
[[Indice_FIDC|Voltar para FIDC]]
[[Mind/Conhecimento/indice|Índice Principal]]

#fidc #accrual #curva #fechamento #direitos_creditorios
