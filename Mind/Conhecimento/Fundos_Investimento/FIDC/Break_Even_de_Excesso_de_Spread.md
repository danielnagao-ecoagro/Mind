# Break-Even de Excesso de Spread

O break-even de excesso de spread em [[FIDC_Conceitos|FIDC]] é o ponto em que o rendimento econômico dos ativos apenas cobre o custo da estrutura, as perdas esperadas e as despesas, sem geração adicional de proteção ou retorno residual.

## Como pensar o conceito
Se o spread dos ativos cair abaixo desse ponto, a estrutura deixa de gerar colchão econômico e passa a consumir subordinação, reservas ou caixa acumulado.

## Leitura simplificada
Uma forma intuitiva de escrever o break-even é:

`Yield_minimo_da_carteira = custo_das_cotas + despesas + perdas_esperadas + drag_de_caixa`

Acima desse nível, sobra spread econômico. Abaixo dele, a estrutura para de se autofinanciar.

## Componentes do break-even
- taxa média da carteira
- custo das cotas prioritárias
- despesas recorrentes do fundo
- perda esperada e custo de recuperação
- nível de caixa ocioso e arrasto de liquidez

## Exemplo simples
Suponha:
- custo das cotas prioritárias: 14% ao ano
- despesas recorrentes: 2% ao ano
- perda líquida esperada: 3% ao ano
- drag de caixa: 1% ao ano

O yield mínimo da carteira para empatar economicamente é 20% ao ano. Se a carteira render 22%, há 2% de spread excedente. Se render 18%, a estrutura fica 2% abaixo do necessário.

## Uso gerencial
Essa leitura ajuda o gestor a entender o quanto a carteira suporta deterioração antes de comprometer [[Subordinacao_e_Reforco_Credito|subordinação]], [[Waterfall_e_Ordem_de_Pagamentos|waterfall]] e valor de cota. Também é útil para analisar originação nova e renegociação de taxa de compra.

## Relação com o monitoramento
Break-even deve ser lido em conjunto com [[Indicadores_Chave_de_FIDC|indicadores-chave]], [[Stress_de_Subordinacao_em_FIDC|stress de subordinação]] e [[PDD_Esperada_vs_PDD_Realizada_em_FIDC|PDD esperada vs. realizada]].

## Onde a análise costuma falhar
- usar yield nominal da carteira sem descontar o caixa não alocado
- olhar perda histórica sem refletir deterioração recente
- ignorar despesas extraordinárias ou custo de cobrança
- confundir spread bruto do ativo com spread disponível para a estrutura

## Referências e Links
- [[Indice_FIDC|FIDC]]
- [[Matematica_Financeira_de_FIDC|Matemática Financeira de FIDC]]
- [[Excesso_de_Spread|Excesso de Spread]]
- [[TIR_Bruta_vs_TIR_Liquida_em_FIDC|TIR Bruta vs. TIR Líquida em FIDC]]
- [[Stress_de_Subordinacao_em_FIDC|Stress de Subordinação em FIDC]]
- [[Indicadores_Chave_de_FIDC|Indicadores-Chave de FIDC]]

---
[[Indice_FIDC|Voltar para FIDC]]
[[Mind/Conhecimento/indice|Índice Principal]]

#fidc #spread #breakeven #subordinacao #monitoramento
