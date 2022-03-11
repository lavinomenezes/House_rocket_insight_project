# House Rocket insight project

## Problema de negócio

Empresa fictícia de compra e venda de propriedades onde o CEO da empresa gostaria de maximizar o lucro da empresa encontrando bons negócios. Foi solicitado à equipe de ciência de dados para analisar o portfólio de imóveis disponíveis para a compra e retornasse uma lista com sugestão de compra e venda para atender a demanda do CEO de maximizar os lucros e diminuir as perdas.
Será entregue um app online para fácil visualização de todos os membros envolvidos no processo que conterá:  

<ul>
<li>Tabela de sugestão com compra e preço de venda de imóveis;</li>
<li>Mapa para visualização geográfica das propriedades disponíveis;</li>
<li>Uma análise de hipóteses de negócios.</li>
</ul>

>Ao final constará o lucro que a empresa poderá obter com a lista de sugestão


**Dataset overview**


| **Variable** | **Meaning** |
|:----------:|---------|
|id        |Unique ID for each home sold|
|date|Date of the home sale |
|price| Price of each home sold |
|bedrooms| Number of bedrooms |
|bathrooms| Number of bathrooms, where .5 accounts for a room with a toilet but no shower |
|sqft_living| Square footage of the apartments interior living space |
|sqft_lot| Square footage of the land space |
|floors |Number of floors |
|waterfront |A dummy variable for whether the apartment was overlooking the waterfront or not |
|view |An index from 0 to 4 of how good the view of the property was |
|condition |An index from 1 to 5 on the condition of the apartment, |
|grade |An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high quality level of |construction and design. |
|sqft_above |The square footage of the interior housing space that is above ground level |
|sqft_basement |The square footage of the interior housing space that is below ground level |
|yr_built |The year the house was initially built |
|yr_renovated |The year of the house’s last renovation |
|zipcode | What zipcode area the house is in |
|lat |Lattitude |
|long |Longitude |
|sqft_living15 |The square footage of interior housing living space for the nearest 15 neighbors |
|sqft_lot15 |The square footage of the land lots of the nearest 15 neighbors |



##  Questões do negócio

<ul>
<li>Quais propriedades a empresa deveria comprar e a qual preço ?
</li>
<li>Qual o melhor momento para a venda depois da compra ?
</li>
</ul>

##  Premissas do negócio

<ul>
<li>Região e estação do ano afetam os preços de venda e revenda;
</li>
<li>As informações estão limitadas numa faixa de um ano de maio de 2014 a maio de 2015;
</li>
<li>Propriedades que apresentarem incoerência  entre números de quartos e área total em comparação a média por quantidade de quartos serão considerados erros de digitação e serão deletados;
</li>
<li>Propriedades construídas antes de 1955 foram consideradas velhas;</li>
<li>Propriedade com classificação(grade) 7 foram consideradas medianas e com classificação de 11 a 13 foram consideradas de alta qualidade;</li>
<li>Propriedades com condição de 1 a 2 foram consideradas em más condições e as de 4 a 5 em boas condições;</li>


<li>Para compra  foi considerado propriedades em boas condições e preço menor que a mediana da região. O preço de revenda foi determinado da seguinte forma:</li>
 <ul>
<li>se o preço for maior que a mediana que a mediana da região + estação:</li>
 <ul>
 <li>O  preço de revenda será o preço de compra + 10%</li>
</ul>
<li>Se o preço for menor que a mediana da região + estação:</li>
<ul>
<li>O preço de revenda será o preço de compra + 30%</li>
</ul>  
 </ul>
</ul>

## Planejamento da Solução
<ul>
 <li>Coleta de dados;</li>
 <li>Limpeza dos dados;</li>
 <li>Transformação dos dados</li>
 <li>Descrição dos dados;</li>
 <li>Remoção de dados derivados de erros de digitação;</li>
 <li>Criação de novas features:</li>
 <ul>
 <li>month;</li>
 <li>year_month;</li>
 <li>year;</li>
 <li>season;</li>
 <li>house_age;</li>
 <li>basement;</li>
 <li>median_price_zipcode;</li>
 <li>median_price_season.</li>
 </ul>
 <li>Análise exploratória;</li>
 <li>Teste de hipóteses;</li>
 <li>Conclusão dos insights;</li>
 <li>Deploy do app em nuvem.</li>
</ul>

##  Os  principais insights de negócio

<ul>
<h3><li><strong>Propriedades com vista para o mar são 212,42 % mais caras na média;</strong></li> </h3>

Bem mais que o esperado que era de 30% então é necessário um investimento maior para adicionar esse tipo de propriedade para o portfólio da empresa

 
<h3><strong><li>Propriedades com vista para o mar tem um crescimento mês a mês maior que as que não tem;</strong></li></h3> 

Enquanto as propriedades sem beira-mar tem um crescimento de 0.2% ao mês em média as que possuem tem crescem a 4.81%, em média, apesar de ser necessário um maior investimento propriedades com vista para o mar são um bom investimento ao médio e longo prazo


<h3><strong><li>Propriedades com uma classificação considerada alta tem um crescimento mês a mês maior que aquelas que têm classificação média;</strong></li></h3>

Enquanto as propriedades com média classificação tem tem um crescimento de 0.74 % ao mês em média, as com alta classificação crescem a 1.20% ao mês em média, uma diferença de 60.87%, então eles podem ser uma boa adição para o portfólio em termos de médio o longo investimento


<h3><strong><li>Propriedades em más condições são mais baratas que aquelas em boas condições.</strong></li></h3>

Propriedades em más condições são em média 66,64 % mais baratas em comparação as em boas condições, então podem ser adquiridas com um baixo investimento e reformadas para revenda mantendo um bom lucro.
</ul>

All the hyphothesis tested can be be check [here]

## Resultados financeiros


Existe um total de 21,461 casas disponíveis para compras, desse montante 10.498 foram sugeridas para compra, a tabela abaixo descreve os valores resultantes da análise.



| Propriedades disponiveis | Sugestões para compra | Investimento | Retorno | Lucro |
|:----------------------:|:--------------------:|:-------------:|:--------:|:--------:|
| 21,461 | 10,498 | $5,656,988,504.00 | $6,622,652,682.20 | $965,664,178.2 |




##  Conclusão

Neste projeto foram selecionados propriedade para compra e sugerido o preço de revenda assim como hipóteses foram testadas para entender melhor o comportamento dos preços e o resultado foi entregue para o CEO,a lista de sugestões assim como os testes dos insights acima, estão disponíveis online em [House rocket insight report] para ser acessado pelo CEO e qualquer outro membro da empresa que venha a interessar.







##  Próximos passos

<ul>
<li>Aumentar a quantidade de informações relevantes sobre as propriedades;
</li>
<li>Explorar mais a fundo as hipóteses promissoras; 
</li>
<li>Testar novas hipóteses;</li>
<li>Explorar modelos de machine learning para prever o comportamento dos preços dos imóveis</li>
</ul>