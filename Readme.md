# House Rocket insight project


## Problema de negócio

A House Rocket é uma empresa fictícia de compra e venda de imóveis cujo CEO gostaria de maximizar seu lucro e diminuir perdas encontrando bons negócios. Foi solicitada à equipe de ciência de dados a análise de portfólio de imóveis disponíveis para compra e retorno com uma lista de sugestões de compra e venda para atender à demanda. Será entregue um app online para que todos os membros envolvidos no processo de compra e venda possam ter uma fácil visualização das seguintes funcionalidades: 

<ul>
<li>Tabela de sugestão com compra e preço de venda de imóveis;</li>
<li>Mapa para visualização geográfica das propriedades disponíveis;</li>
<li>Uma análise de hipóteses de negócios;</li>
<li>Apresentação do lucro que a empresa poderá obter seguindo a lista de sugestão</li>
</ul>



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
<li>Imóveis que apresentarem incoerência entre números de quartos e área total em comparação à média por quantidade de quartos serão considerados erros de digitação e serão deletados;
</li>
<li>Imóveis construídos antes de 1955 foram considerados velhos;</li>
<li>Imóveis com classificação (grade) 7 foram considerados medianos aqueles com classificação de 11 a 13 foram considerados de alta qualidade;</li>
<li>Imóveis com condição (condition) de 1 a 2 foram considerados em más condições e aqueles de 4 a 5 foram considerados em boas condições</li>
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
 <li>Transformação dos dados;</li>
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
<h3><li><strong>Imóveis com vista para o mar são 212.42% mais caros que imóveis sem vista para o mar, considerando o preço médio</strong></li> </h3>

Com o preço médio superior ao previsto, que era de 30%, é necessário um investimento maior para adicionar esse tipo de imóvel para o portfólio da empresa.

 
<h3><strong><li>Preços de imóveis com vista para o mar têm um crescimento mês a mês maior que as que não têm</strong></li></h3> 

Enquanto os imóveis que não têm vista para o mar apresentam um crescimento de 0.2% ao mês em média, as que têm crescem a 4.81%, em média. Apesar de ser necessário um maior investimento, imóveis com vista para o mar geram bom retorno a médio e longo prazos.


<h3><strong><li>Imóveis com uma classificação considerada alta têm um crescimento mês a mês maior que aquelas que têm classificação média</strong></li></h3>

Enquanto os imóveis com classificação média têm um crescimento médio de 0.74% ao mês, as com alta classificação crescem em média 1.20% ao mês, uma diferença de 60.87%, de maneira que eles podem ser uma boa adição para o portfólio em termos de investimento a médio ou longo investimento


<h3><strong><li>Imóveis em más condições são mais baratos que aqueles em boas condições</strong></li></h3>

Imóveis em más condições são em média 66.64 % mais baratos em comparação àqueles em boas condições, então podem ser adquiridos com um baixo investimento e reformados para revenda mantendo um bom lucro.
</ul>

<i>Todas as hipóteses testadas podem ser vistas no [notebook](https://github.com/lavinomenezes/House_rocket_insight_project/blob/main/notebooks/House_rocket_notebook.ipynb) para ver a descrição total, ou um breve resumo em [Hipóteses](https://github.com/lavinomenezes/House_rocket_insight_project/blob/main/Hipoteses.md)</i>

## Resultados financeiros


Existe um total de 21.461 imóveis disponíveis para compra, de cujo montante 10.498 foram sugeridos para compra. A tabela abaixo descreve os valores resultantes da análise.



| Imóveis dispóniveis | Sugestões para compra | Investimento | Retorno | Lucro |
|:----------------------:|:--------------------:|:-------------:|:--------:|:--------:|
| 21,461 | 10,498 | $5,656,988,504.00 | $6,622,652,682.20 | $965,664,178.2 |




##  Conclusão

Neste projeto foram selecionados imóveis para compra e sugeridos preços de revenda. Também foram testadas hipóteses para entender melhor o comportamento dos preços e o resultado foi entregue para o CEO. A lista de sugestões, assim como os testes dos <i>insights</i> acima descritos, estão disponíveis online em [House rocket insight report](https://house-rocket-insight-report.herokuapp.com/) para serem acessados pelo CEO ou qualquer outro membro da empresa que venha a quem as informações interessem.








##  Próximos passos

<ul>
<li>Aumentar a quantidade de informações relevantes sobre os imóveis;
</li>
<li>Explorar mais a fundo as hipóteses promissoras; 
</li>
<li>Testar novas hipóteses;</li>
<li>Explorar modelos de <i>machine learning</i> para prever o comportamento dos preços dos imóveis</li>
</ul>
