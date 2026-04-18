# Matemática Financeira de FIDC

Esta nota organiza a trilha de aprendizado quantitativo para [[FIDC_Conceitos|FIDC]], conectando fundamentos de taxa, desconto, fluxo e retorno com as rotinas práticas de [[Calculos_Aplicados_em_Gestora_de_FIDC|cálculo em gestora]].

## O que precisa dominar antes
- [[Metodos_Quantitativos/Valor_do_Dinheiro_no_Tempo|Valor do Dinheiro no Tempo]]
- [[Metodos_Quantitativos/Conversao_de_Taxas|Conversão de Taxas]]
- [[Contabilidade_e_Controle/Calculo_de_Cotas|Cálculo de Cotas]]
- [[Mercado_Financeiro/Duration_e_Convexidade|Duration e Convexidade]]

## Perguntas que a matemática responde no FIDC
- quanto pagar por um recebível hoje
- quanto do retorno já foi apropriado no fechamento diário
- quanto caixa a carteira precisa gerar para sustentar as cotas
- qual a diferença entre retorno bruto do ativo e retorno líquido do veículo
- quanto a estrutura aguenta perder antes de consumir proteção

## Blocos centrais no FIDC
### Formação do preço de compra
O ponto de partida é entender como o [[Desagio_Cessao_PU_e_Taxa_Compra|deságio de cessão]], o [[PU_e_Valor_Presente_em_FIDC|valor presente]] e a convenção de dias afetam o preço econômico de cada direito creditório.

### Carregamento diário da carteira
Depois da aquisição, o gestor precisa apropriar juros, acompanhar [[Accrual_Pro_Rata_em_Direitos_Creditorios|accrual pro rata]] e distinguir [[Valor_na_Curva_em_FIDC|valor na curva]] de reprecificação econômica.

### Modelagem do fluxo do fundo
O retorno do investidor depende da conversão do fluxo dos ativos em caixa do fundo, da [[Modelagem_de_Cash_Flow_de_FIDC|modelagem de cash flow]], da [[Waterfall_e_Ordem_de_Pagamentos|waterfall]] e da distribuição de perdas entre classes.

### Leitura de retorno e proteção
Por fim, a análise passa por [[TIR_Bruta_vs_TIR_Liquida_em_FIDC|TIR bruta e líquida]], [[Excesso_de_Spread|excesso de spread]] e [[Break_Even_de_Excesso_de_Spread|break-even de spread]], sempre em conjunto com [[Subordinacao_e_Reforco_Credito|subordinação]] e provisões.

## Sequência lógica de cálculo
1. projetar os fluxos contratuais e esperados dos ativos
2. definir convenção de dias, taxa e premissas de perda
3. trazer o fluxo a valor presente e calcular o preço de compra
4. apropriar rendimento ao longo do tempo por accrual ou curva
5. transformar fluxo dos ativos em caixa do fundo, considerando despesas e waterfall
6. medir retorno, proteção e sensibilidade da estrutura

## Fórmulas que aparecem o tempo todo
- valor presente: `VP = Fluxo / (1 + i)^n`
- accrual por curva: `Valor_na_data = PU_inicial x (1 + i)^(dias/base)`
- cota: `Valor_da_cota = PL_da_classe / Quantidade_de_cotas`
- spread residual simplificado: `Yield_dos_ativos - custo_das_cotas - despesas - perdas`

## Onde os erros costumam acontecer
- comparar taxas em bases diferentes, como 252 contra 360
- tratar valor de face como valor econômico
- calcular TIR com fluxo regular quando a carteira liquida em datas irregulares
- ignorar drag de caixa, atraso ou perda ao estimar retorno líquido
- usar spread nominal sem considerar despesas e necessidade de subordinação

## Sequência sugerida
1. [[Desagio_Cessao_PU_e_Taxa_Compra|Deságio, Cessão, PU e Taxa de Compra]]
2. [[Accrual_Pro_Rata_em_Direitos_Creditorios|Accrual Pro Rata em Direitos Creditórios]]
3. [[Modelagem_de_Cash_Flow_de_FIDC|Modelagem de Cash Flow de FIDC]]
4. [[TIR_Bruta_vs_TIR_Liquida_em_FIDC|TIR Bruta vs. TIR Líquida em FIDC]]
5. [[Break_Even_de_Excesso_de_Spread|Break-Even de Excesso de Spread]]
6. [[Caso_Numerico_de_Cash_Flow_TIR_e_Spread_em_FIDC|Caso Numérico de Cash Flow, TIR e Spread em FIDC]]

## Variações por lastro
- [[Caso_Numerico_FIDC_Cartao_Agenda_Chargeback_e_Spread|FIDC Cartão: agenda, chargeback e spread]]
- [[Caso_Numerico_FIDC_Consignado_Averbacao_Fluxo_e_Inadimplencia|FIDC Consignado: averbação, fluxo e inadimplência]]
- [[Caso_Numerico_FIDC_NPL_Recuperacao_Prazo_e_Custo_Juridico|FIDC NPL: recuperação, prazo e custo jurídico]]

## Referências e Links
- [[Indice_FIDC|FIDC]]
- [[Calculos_Aplicados_em_Gestora_de_FIDC|Cálculos Aplicados em Gestora de FIDC]]
- [[Precificacao_de_Carteiras_de_Recebiveis|Precificação de Carteiras de Recebíveis]]
- [[Calculo_de_PL_e_Cota_em_FIDC|Cálculo de PL e Cota em FIDC]]
- [[Exemplo_Numerico_de_Precificacao_de_Recebiveis_em_FIDC|Exemplo Numérico de Precificação de Recebíveis em FIDC]]
- [[Exemplo_Numerico_de_PL_Cota_e_Amortizacao_em_FIDC|Exemplo Numérico de PL, Cota e Amortização em FIDC]]
- [[Caso_Numerico_de_Cash_Flow_TIR_e_Spread_em_FIDC|Caso Numérico de Cash Flow, TIR e Spread em FIDC]]
- [[Caso_Numerico_FIDC_Cartao_Agenda_Chargeback_e_Spread|Caso Numérico de FIDC Cartão com Agenda, Chargeback e Spread]]
- [[Caso_Numerico_FIDC_Consignado_Averbacao_Fluxo_e_Inadimplencia|Caso Numérico de FIDC Consignado com Averbação, Fluxo e Inadimplência]]
- [[Caso_Numerico_FIDC_NPL_Recuperacao_Prazo_e_Custo_Juridico|Caso Numérico de FIDC NPL com Recuperação, Prazo e Custo Jurídico]]
- [[Glossario_de_Formulas_e_Siglas_de_FIDC|Glossário de Fórmulas e Siglas de FIDC]]
- [[Metodos_Quantitativos/Indice_Quantitativo|Métodos Quantitativos]]

---
[[Indice_FIDC|Voltar para FIDC]]
[[Mind/Conhecimento/indice|Índice Principal]]

#fidc #matematica_financeira #precificacao #fluxo #retorno
