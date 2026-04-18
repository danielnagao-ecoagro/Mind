# Modelagem de Cash Flow de FIDC

A modelagem de cash flow de [[FIDC_Conceitos|FIDC]] traduz os fluxos esperados dos recebíveis em entradas e saídas de caixa do fundo, incorporando prazo, atraso, perda, recuperação, despesas e [[Waterfall_e_Ordem_de_Pagamentos|ordem de pagamentos]].

## Blocos do modelo
- entradas da carteira: liquidação, amortização, recuperação e pré-pagamento
- saídas do fundo: despesas, remuneração de cotas, amortizações e reforços de reserva
- perdas: inadimplência, fraudes, glosas, recompras não honradas e custos de cobrança

## Estrutura mínima de um modelo
1. calendário de vencimentos da carteira
2. premissas de atraso, default, cura e recuperação
3. regras de despesas e remuneração das cotas
4. aplicação da [[Waterfall_e_Ordem_de_Pagamentos|waterfall]] em cada período
5. saída final por classe de cota, caixa e proteção remanescente

## O que a modelagem precisa responder
- quanto caixa o fundo deve gerar em cada janela
- se a carteira sustenta a meta de retorno das classes
- qual o efeito de estresse sobre [[Excesso_de_Spread|spread]] e [[Subordinacao_e_Reforco_Credito|subordinação]]
- quando o fundo pode ativar [[Gatilhos_e_Eventos_de_Avaliacao|gatilhos]] ou reter caixa

## Fórmula de leitura simplificada
Uma visão resumida do caixa do período é:

`Caixa_liquido = Recebimentos_da_carteira + Recuperacoes - Despesas - Pagamentos_da_waterfall`

Quando esse caixa fica consistentemente abaixo do necessário para remunerar as classes prioritárias, o fundo começa a pressionar spread, reservas e subordinação.

## Exemplo conceitual
Imagine uma carteira que deveria receber 1.000 por mês:
- recebimento esperado: 1.000
- atraso e default reduzem entrada para 920
- recuperação do período soma 30
- despesas consomem 70

Antes da waterfall, o caixa líquido é 880. Se a classe sênior exigir 900, o mês já nasce deficitário e a diferença precisará ser absorvida por spread acumulado, retenção de caixa ou classe subordinada.

## Uso na prática
Sem modelagem de fluxo, métricas como [[TIR_e_XIRR_em_FIDC|TIR]], duration e retorno por classe podem ficar desconectadas da realidade operacional. Em FIDC, a matemática financeira precisa conversar com o ciclo de cobrança e com a waterfall.

## Pontes com casos específicos
Modelos de fluxo variam bastante entre [[FIDC_Cartao|FIDC de cartão]], [[FIDC_Consignado|FIDC de consignado]] e [[FIDC_NPL|FIDC NPL]], porque o padrão de liquidação, atraso e recuperação é diferente em cada lastro.

## Erros comuns
- modelar fluxo contratual sem traduzir para fluxo esperado
- ignorar defasagem entre atraso, PDD e recuperação efetiva
- tratar despesas como fixas quando parte delas varia com volume ou cobrança
- medir TIR da carteira sem aplicar a waterfall da estrutura

## Referências e Links
- [[Indice_FIDC|FIDC]]
- [[Matematica_Financeira_de_FIDC|Matemática Financeira de FIDC]]
- [[Waterfall_e_Ordem_de_Pagamentos|Waterfall e Ordem de Pagamentos]]
- [[TIR_Bruta_vs_TIR_Liquida_em_FIDC|TIR Bruta vs. TIR Líquida em FIDC]]
- [[Excesso_de_Spread|Excesso de Spread]]
- [[Mini_Caso_de_Fechamento_Diario_em_FIDC|Mini Caso de Fechamento Diário em FIDC]]

---
[[Indice_FIDC|Voltar para FIDC]]
[[Mind/Conhecimento/indice|Índice Principal]]

#fidc #cashflow #modelagem #waterfall #risco
