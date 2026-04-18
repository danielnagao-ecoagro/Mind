# Caso Numérico de FIDC NPL com Recuperação, Prazo e Custo Jurídico

Este caso mostra como a matemática de [[FIDC_NPL|FIDC NPL]] depende principalmente de recuperação, prazo e custo jurídico, e muito menos do fluxo contratual original do crédito.

## Premissas do caso
- carteira inadimplida comprada por: 300.000
- valor de face original dos créditos: 1.500.000
- recuperação bruta esperada em 24 meses: 520.000
- custo jurídico e de cobrança estimado: 110.000
- valor do dinheiro no tempo e custo de oportunidade implícitos no prazo: relevantes
- retorno mínimo exigido para a tese: equivalente a 180.000 de ganho líquido sobre o capital investido ao longo do ciclo

## Passo 1: resultado bruto de recuperação

`Resultado_bruto = 520.000 - 300.000 = 220.000`

O fato de o valor de face original ser 1.500.000 não muda a lógica econômica principal. O que importa é o quanto o fundo de fato consegue recuperar.

## Passo 2: resultado líquido após custo jurídico

`Resultado_liquido = 520.000 - 300.000 - 110.000 = 110.000`

## Passo 3: leitura contra a meta da tese
Se a tese precisava gerar 180.000 de ganho líquido no ciclo:

`Gap_para_meta = 110.000 - 180.000 = -70.000`

A compra parece barata em relação ao valor de face, mas ainda assim não atinge o retorno necessário para o fundo.

## Sensibilidade a prazo
Se o mesmo fluxo de recuperação atrasar além dos 24 meses, o valor econômico cai ainda mais. Em NPL, prazo de resolução é quase tão importante quanto percentual de recuperação.

## Sensibilidade a custo jurídico
Se o custo jurídico subir de 110.000 para 170.000:

`Resultado_liquido_ajustado = 520.000 - 300.000 - 170.000 = 50.000`

O caso praticamente destrói a tese econômica.

## O que este caso ensina
- desconto grande sobre valor de face não garante retorno bom
- recuperação líquida é a variável central do NPL
- prazo e custo jurídico precisam entrar na conta desde a compra
- em NPL, erro de premissa corrói TIR com muita rapidez

## Perguntas de controle
- a curva de recuperação é realista para o tipo de lastro
- o custo jurídico contempla execução, acordos e tempo de equipe
- a documentação suporta executabilidade
- a tese foi montada sobre valor de face ou sobre recuperação líquida descontada

## Referências e Links
- [[Indice_FIDC|FIDC]]
- [[FIDC_NPL|FIDC NPL]]
- [[Matematica_Financeira_de_FIDC|Matemática Financeira de FIDC]]
- [[Precificacao_de_Carteiras_de_Recebiveis|Precificação de Carteiras de Recebíveis]]
- [[TIR_Bruta_vs_TIR_Liquida_em_FIDC|TIR Bruta vs. TIR Líquida em FIDC]]
- [[Credito_e_Risco/Default_e_Recuperacao|Default e Recuperação]]
- [[Estruturacao_e_Operacoes/Auditoria_Lastro|Auditoria de Lastro]]

---
[[Indice_FIDC|Voltar para FIDC]]
[[Mind/Conhecimento/indice|Índice Principal]]

#fidc #npl #recuperacao #custo_juridico #precificacao
