# Caso Numérico de FIDC Cartão com Agenda, Chargeback e Spread

Este caso mostra como a matemática financeira de um [[FIDC_Cartao|FIDC de cartão]] depende menos de um único vencimento e mais da agenda de liquidação, do nível de contestação e do efeito de chargeback sobre caixa e spread.

## Premissas do caso
- cessão de agenda futura de recebíveis: 500.000
- deságio de compra inicial: 4%
- preço pago pelo fundo: 480.000
- liquidação distribuída em 30 dias
- chargeback esperado: 2,5% sobre o valor cedido
- despesa operacional total do ciclo: 8.000
- remuneração exigida da classe sênior no ciclo: 18.000

## Passo 1: preço de compra
Se o valor cedido é 500.000 e o fundo entra com deságio de 4%:

`Preco_de_compra = 500.000 x (1 - 0,04) = 480.000`

## Passo 2: efeito do chargeback
O chargeback esperado é:

`Chargeback_esperado = 500.000 x 2,5% = 12.500`

Logo, o fluxo bruto ajustado da agenda cai para:

`Fluxo_apos_chargeback = 500.000 - 12.500 = 487.500`

## Passo 3: resultado antes da remuneração da estrutura
Subtraindo a despesa operacional:

`Resultado_antes_da_senior = 487.500 - 480.000 - 8.000 = -500`

Mesmo com deságio aparente de 20.000, o efeito de chargeback e despesas já consome praticamente toda a folga econômica.

## Passo 4: leitura de spread
Se a classe sênior precisa de 18.000 no ciclo:

`Spread_residual = -500 - 18.000 = -18.500`

O fundo não está cobrindo a exigência da estrutura. Isso pressiona subordinação, retenção de caixa e revisão da taxa de compra.

## O que este caso ensina
- agenda de liquidação não é igual a fluxo realizável
- chargeback corrói rapidamente spread aparente
- deságio comercial pode ser insuficiente para remunerar o veículo
- em cartão, integração operacional e qualidade do originador pesam tanto quanto taxa

## Perguntas de controle
- o chargeback foi medido em base histórica ou em cenário de estresse
- a agenda cedida já considera cancelamentos e glosas
- a estrutura de despesas inclui custo de registradora e conciliação
- o caixa chega no timing necessário para a waterfall

## Referências e Links
- [[Indice_FIDC|FIDC]]
- [[FIDC_Cartao|FIDC de Recebíveis de Cartão]]
- [[Matematica_Financeira_de_FIDC|Matemática Financeira de FIDC]]
- [[Modelagem_de_Cash_Flow_de_FIDC|Modelagem de Cash Flow de FIDC]]
- [[Excesso_de_Spread|Excesso de Spread]]
- [[Estruturacao_e_Operacoes/Recebiveis_de_Cartao|Recebíveis de Cartão]]
- [[Estruturacao_e_Operacoes/Registradoras_e_Depositarias|Registradoras e Depositárias]]

---
[[Indice_FIDC|Voltar para FIDC]]
[[Mind/Conhecimento/indice|Índice Principal]]

#fidc #cartao #cashflow #chargeback #spread
