# ==============
# Imports
# ==============
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
import geopandas
import plotly.express as px
import locale
import plotly.graph_objects as go


# ==============
# View configuration
# ==============
st.set_page_config(page_title="House rocket insight report",
                   layout="wide")


# ==============
# Read the files
# ==============


def get_data(path):
    return pd.read_csv(path)


@st.cache(allow_output_mutation=True)
def get_geofile(url_):
    geo = geopandas.read_file(url_)
    return geo

# ==============
# help functions
# ==============

def set_currency(currency):
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')
    return locale.currency(currency, grouping=True)


def dif(val1 , val2):
    perc = round(100*(val2 - val1)/val1,2)
    return perc


def MoM(dataset_):
    dataset_['MoM_%'] = 0
    for i in range(1,len(dataset_)):
        dataset_.loc[i,'MoM_%'] = dif(dataset_.iloc[i-1,1],dataset_.iloc[i,1])
    return dataset_


# ==============
# language
# ==============


def language():
    st.sidebar.subheader('To read in english select')
    lan = st.sidebar.checkbox('English')

    english = {'ov':{'ov_0':'Filter by atribute',
                     'ov_1':'Enter season',
                     'ov_2':['winter','spring','summer','fall'],
                     'ov_3':'Enter zipcode',
                     'ov_4':'Only Houses with water view',
                     'ov_5':'Suggestion for buying',
                     'ov_6':['id','date','zipcode','waterfront','condition','season','price','median_price_zip','median_price_season','selling_price','profit'],
                     'ov_7': ['yes', 'no']

    },
                'mi': { 'mi_0': 'Main information',
                       'mi_1': 'Total Real estate avaliable',
                       'mi_2': 'Total Real estate suggested to be purchase',
                       'mi_3': 'Investment',
                       'mi_4': 'Return',
                       'mi_5': 'Profit',
    },
               'map':{'map_0':'Region overview',
                      'map_1':'Locations',
                      'map_2':"Price U$ {0} on: {1} Intern space: {2} sqtf, Bedrooms: {3}, "
                                                       "Bathrooms: {4} , Year built: {5}",
                      'map_3': 'Price distribution'

               },
               'hp':{'hp_0': 'Main business insights',
                     'hp_1': 'Real estate with waterfront are ',
                     'hp_2': ' % more expensive on average',
                     'hp_3': 'Waterfront',
                     'hp_4': 'Without waterfront',
                     'hp_5': 'Real estate without waterfront',
                     'hp_6': 'Real estate with waterfront',
                     'hp_7': 'Average price',
                     'hp_8': "Real estate with waterfront has a average growth month-on-month(MoM) bigger than that without",
                     'hp_9': "Average MoM",
                     'hp_10': "Last 12 months cumulative",
                     'hp_11': "Real estate with a high quality grade, has a growth month-on-month",
                     'hp_12': " %  bigger, on average, than those with average grade",
                     'hp_13': "Average grade",
                     'hp_14': "High grade",
                     'hp_15': "Real estate with average grade",
                     'hp_16': "Real estate with high grade",
                     'hp_17': "Real estate in bad conditions are ",
                     'hp_18': " % more cheap, on average, than those in good conditions",
                     'hp_19': ['Bad condition', 'Good condition'],
                     'hp_20': 'Condition',
                     'hp_21': 'Price',
                     'hp_22': 'Real estate in bad conditions',
                     'hp_23': 'Real estate in good conditions'

               },
               'ai': {'ai_0': 'Additional information',
                      'ai_1': "This is a report done for a insight project of a fictitious company called House rocket, in which it's business model consist of"
                                "buying and selling Real estate where the CEO of the company would like to maximize the company's profit by finding good deals.",
                      'ai_2': 'This web app is the result of House Rocket Insights Project made by Lavino Menezes.',
                      'ai_3': "The entire project's context and other files are available in",
                      'ai_4': 'Other Projects: ',
                      'ai_5': 'Contact me: '
                     }
    }


    portu = {'ov':{'ov_0':'Filtre por atributo',
                   'ov_1':'Seleciona a estação',
                   'ov_2':['inverno','primavera','verão','outono'],
                   'ov_3':'Selecione o zipcode',
                   'ov_4':'Apenas imóveis com vista para o mar',
                   'ov_5':'Sugestão para compra',
                   'ov_6':['id','data','zipcode','vista_para_o_mar','condição','estação','preço','mediana_preço_zip','mediana_preço_estação','preço_de_venda','lucro'],
                   'ov_7': ['sim','não']

    },
            'mi': { 'mi_0': 'Informações principais',
                     'mi_1': 'Total de Imóveis disponíveis',
                     'mi_2': 'Total de Imóveis sugeridas para compra',
                     'mi_3': 'Investimento',
                     'mi_4': 'Retorno',
                     'mi_5': 'Lucro',
    },
             'map':{'map_0': 'Visão geral da região',
                    'map_1': 'Localizações',
                    'map_2': "Preço U$ {0} em: {1} Espaço interno: {2} sqtf, Quartos: {3}, Banheiros: {4}, Ano de construção: {5}",
                    'map_3': 'Distribuição de preços'

             },
             'hp':{'hp_0': 'Principais insights de negócio',
                   'hp_1': 'Imóveis com vista par o mar são ',
                   'hp_2': ' % mais caros considerando o preço médio',
                   'hp_3': 'Vista para o mar',
                   'hp_4': 'Sem vista para o mar',
                   'hp_5': 'Imóveis  sem vista para o mar',
                   'hp_6': 'Imóveis  com vista para o mar',
                   'hp_7': 'Preço médio',
                   'hp_8': 'Imóveis com vista para o mar tem um crescimento mês a mês(MoM) maior que as que não tem',
                   'hp_9': 'MoM médio',
                   'hp_10': 'Cumulativo dos últimos 12 meses',
                   'hp_11': 'Imóveis com uma classificação considerada alta tem um crescimento mês a mês ',
                   'hp_12': ' % maior que aqueles que têm classificação média',
                   'hp_13': 'Classificação média',
                   'hp_14': 'Classificação alta',
                   'hp_15': 'Imóveis com classificação média',
                   'hp_16': 'Imóveis com classificação alta',
                   'hp_17': 'Imóveis em más condições são ',
                   'hp_18': ' % mais baratos que aqueles em boas condições',
                   'hp_19': ['Má condição', 'Boa condição'],
                   'hp_20': 'Condição',
                   'hp_21': 'Preço',
                   'hp_22': 'Imóveis em más condições',
                   'hp_23': 'Imóveis em boas condições'

             },
             'ai': {'ai_0': 'Informação adicional',
                    'ai_1': "Esse é um relatorio resultado de um projeto de insight de uma empresa fictícia chamada 'House rocket', que o modelo de negócio consiste em"
                            " compra e venda de imóveis onde o CEO da empresa quer maximizar os lucros buscando bons negócios.",
                    'ai_2': "Esse web app é resultado do House Rocket Insights Project feito por Lavino Menezes.",
                    'ai_3': "Todo o contexto e outros arquivos do projeto estão disponíveis em: ",
                    'ai_4': 'Outros projetos: ',
                    'ai_5': 'Contato: '
              }
    }

    if lan:
        return english
    else:
        return portu

# ==============
# data transform
# ==============


def transform_columns(dataset_):
    dataset_['date'] = pd.to_datetime(dataset_['date'])
    dataset_['yr_built'] = dataset_['yr_built'].astype(str)
    dataset_['yr_built'] = dataset_['yr_built'].apply(lambda x: x + "-01-01")
    dataset_['yr_built'] = pd.to_datetime(dataset_['yr_built'])
    dataset_['yr_renovated'] = dataset_['yr_renovated'].astype(str)
    dataset_['yr_renovated'] = dataset_['yr_renovated'].apply(lambda x: '0' if x == '0' else x + "-01-01")
    dataset_['yr_renovated'] = dataset_['yr_renovated'].apply(
        lambda x: pd.to_datetime('1970-01-01', format="%Y-%m-%d") if x == '0' else pd.to_datetime(x))
    dataset_['yr_renovated'] = pd.to_datetime(dataset_['yr_renovated'])
    return dataset_

# ==============
# clean data
# ==============


def clean_data(dataset_):
    dataset_.drop_duplicates(subset='id', inplace=True)
    dataset_ = dataset_.drop(columns=['sqft_living15', 'sqft_lot15'], axis=1).copy()
    dataset_ = dataset_.loc[(dataset_['bedrooms'] != 11) & (dataset_['bedrooms'] != 33)]
    return dataset_

# ==============
# add features
# ==============


def add_features(dataset_):
    # month, year_month, year
    dataset_['month'] = pd.to_datetime(dataset_['date']).dt.month
    dataset_['year_month'] = pd.to_datetime(dataset_['date']).dt.strftime("%Y-%m")
    dataset_['year'] = pd.to_datetime(dataset_['date']).dt.year

    # seasons
    winter_month = [12, 1, 2]
    spring_month = [3, 4, 5]
    summer_month = [6, 7, 8]
    fall_month = [9, 10, 11]
    dataset_['season'] = dataset_['month'].apply(lambda x: 'winter' if x in winter_month else
    ('spring' if x in spring_month else
     ('summer' if x in summer_month else
      ('fall' if x in fall_month else 'NA'))))

    # house age
    dataset_['house_age'] = dataset_['yr_built'].apply(lambda x: 'old' if x <= pd.to_datetime('1955-01-01') else 'new')
    # basement
    dataset_['basement'] = dataset_['sqft_basement'].apply(lambda x: 'yes' if x > 0 else 'no')
    #waterfront
    dataset_['waterfront'] = dataset_['waterfront'].apply(lambda x: 'yes' if x == 1 else 'no')

    return dataset_

# ==============
# selling suggestion
# ==============

def suggest_sell(dataset_):
    df_zip = dataset_[['price', 'zipcode']].groupby('zipcode').median().reset_index()
    df_zip.columns = ['zipcode', 'median_price_zip']
    df_season = dataset_[['price', 'zipcode', 'season']].groupby(['zipcode', 'season']).median().reset_index()
    df_season.columns = ['zipcode', 'season', 'median_price_season']
    # buy
    aux = pd.merge(dataset_, df_zip, on='zipcode', how='inner')
    df_buy = aux[['id', 'date', 'price', 'zipcode', 'median_price_zip', 'condition']].copy()
    df_buy['status'] = 'NA'
    for i in range(len(df_buy)):
        if ((df_buy.loc[i, 'price'] < df_buy.loc[i, 'median_price_zip']) & (df_buy.loc[i, 'condition'] >= 3)):
            df_buy.loc[i, 'status'] = 'buy'
        else:
            df_buy.loc[i, 'status'] = 'not buy'
    # sell
    aux = pd.merge(aux, df_season, on=['zipcode', 'season'], how='inner')
    df_sell = aux.copy()
    df_sell['status'] = df_buy['status']
    df_sell = df_sell[df_sell['status'] == 'buy'].reset_index()
    df_sell.drop('index', inplace=True, axis=1)

    for i in range(len(df_sell)):
        if ((df_sell.loc[i, 'price'] < df_sell.loc[i, 'median_price_season'])):
            df_sell.loc[i, 'selling_price'] = 1.3 * df_sell.loc[i, 'price']
        else:
            df_sell.loc[i, 'selling_price'] = 1.1 * df_sell.loc[i, 'price']
    df_sell['profit'] = df_sell['selling_price'] - df_sell['price']
    return df_sell

# ==============
# data overview
# ==============

def overview(dataset_,lang):
    dataset_ = dataset_[['id', 'date', 'zipcode', 'waterfront', 'condition', 'season', 'price', 'median_price_zip','median_price_season', 'status', 'selling_price', 'profit']]
    dataset_.loc[dataset_['season'] == 'winter', 'season']=lang['ov']['ov_2'][0]
    dataset_.loc[dataset_['season'] == 'spring', 'season']=lang['ov']['ov_2'][1]
    dataset_.loc[dataset_['season'] == 'summer', 'season']=lang['ov']['ov_2'][2]
    dataset_.loc[dataset_['season'] == 'fall', 'season']=lang['ov']['ov_2'][3]
    dataset_.loc[dataset_['waterfront'] == 'yes', 'waterfront']=lang['ov']['ov_7'][0]
    dataset_.loc[dataset_['waterfront'] == 'no', 'waterfront']=lang['ov']['ov_7'][1]

    st.title("House Rocket Insight report")
    st.sidebar.subheader(lang['ov']['ov_0'])
    f_season = st.sidebar.multiselect(lang['ov']['ov_1'], dataset_['season'].unique())
    f_zipcode = st.sidebar.multiselect(lang['ov']['ov_3'], dataset_['zipcode'].unique())
    f_waterview = st.sidebar.checkbox(lang['ov']['ov_4'])
    if f_waterview:
        dataset_ = dataset_[(dataset_['waterfront']=='yes') | (dataset_['waterfront']=='sim')]
    else:
        dataset_ = dataset_

    if (f_zipcode != []) & (f_season != []):
        data = dataset_[(dataset_['zipcode'].isin(f_zipcode)) & (dataset_['season'].isin(f_season))]

    elif (f_zipcode != []) & (f_season == []):
        data = dataset_.loc[dataset_['zipcode'].isin(f_zipcode), :]
    elif (f_zipcode == []) & (f_season != []):
        data = dataset_[dataset_['season'].isin(f_season)]
    else:
        data = dataset_.copy()

    # Set the dataframe view configuration in the web app
    data['date'] = pd.to_datetime(data['date']).dt.strftime("%Y-%m-%d")
    st.header(lang['ov']['ov_5'])
    data = data[['id','date','zipcode','waterfront','condition','season','price','median_price_zip','median_price_season','selling_price','profit']]
    data.columns = lang['ov']['ov_6']
    st.dataframe(data,height=400)

# ==============
# business information
# ==============

def main_information(dataset_,raw,lang):
    st.title(lang['mi']['mi_0'])
    col4, col5 = st.columns(2)
    col4.metric(lang['mi']['mi_1'],len(raw))
    col5.metric(lang['mi']['mi_2'],len(dataset_))

    col1, col2, col3 = st.columns(3)
    col1.metric(lang['mi']['mi_3'], set_currency(round(dataset_['price'].sum(),1)))
    col2.metric(lang['mi']['mi_4'], set_currency(round(dataset_['selling_price'].sum(),1)))
    col3.metric(lang['mi']['mi_5'],set_currency(round(dataset_['profit'].sum(),1)),str(dif(dataset_['price'].sum(),dataset_['selling_price'].sum()))+" %")

# ==============
# maps
# ==============

def maps(dataset_,geofile,lang):
    st.title(lang['map']['map_0'])

    c1, c2 = st.columns(2)
    c1.header(lang['map']['map_1'])

    df_dens = dataset_.copy()

    density_map = folium.Map(location=[dataset_['lat'].mean(), dataset_['long'].mean()], default_zoom_star=15)
    make_cluster = MarkerCluster().add_to(density_map)

    for name, row in df_dens.iterrows():
        folium.Marker([row['lat'], row['long']], popup=lang['map']['map_2'].format( row['price'],
                                                                                    row['date'],
                                                                                    row['sqft_living'],
                                                                                    row['bedrooms'],
                                                                                    row['bathrooms'],
                                                                                    row['yr_built'])).add_to(make_cluster)

    with c1:
        folium_static(density_map)

    # Region Price map

    c2.header(lang['map']['map_3'])

    zip_price = dataset_[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
    zip_price.columns = ['ZIP', 'PRICE']
    df_price = zip_price.copy()
    geofile = geofile[geofile['ZIP'].isin(df_price['ZIP'].tolist())]

    region_price_map = folium.Map(location=[dataset_['lat'].mean(), dataset_['long'].mean()], default_zoom_star=15)
    folium.Choropleth(geo_data=geofile,
                      data=df_price,
                      columns=['ZIP', 'PRICE'],
                      key_on='feature.properties.ZIP',
                      fill_color='YlOrRd',
                      fill_opacity=0.7,
                      line_opacity=0.2,
                      legend_name="AVG Price").add_to(region_price_map)

    with c2:
        folium_static(region_price_map)

    return None

# ==============
# hyphoteses
# ==============


def hipothesys(dataset_,lang):

    st.title(lang['hp']['hp_0'])
    # H1 =================================================================================
    h1 = dataset_[['price', 'waterfront']].groupby('waterfront').mean().reset_index()
    no_water = h1.iloc[0, 1]
    with_water = h1.iloc[1, 1]
    st.header(lang['hp']['hp_1']+ str(dif(no_water,with_water)) +lang['hp']['hp_2'])

    x0 = data[data['waterfront'] == 'yes']['price']
    x1 = data[data['waterfront'] == 'no']['price']

    fig = go.Figure()
    fig.add_trace(go.Box(x=x0, name=lang['hp']['hp_3'],
                         marker_color='indianred'))
    fig.add_trace(go.Box(x=x1, name=lang['hp']['hp_4'],
                         marker_color='lightseagreen'))
    fig.update_layout(
        xaxis_title="Price",
        yaxis_title=""
    )
    st.plotly_chart(fig, use_container_width=True)
    col1, col2 = st.columns(2)
    col1.subheader(lang['hp']['hp_5'])
    col2.subheader(lang['hp']['hp_6'])
    col6, col7 = st.columns(2)
    col6.metric(lang['hp']['hp_7'],set_currency(no_water))
    col7.metric(lang['hp']['hp_7'],set_currency(with_water),str(dif(no_water,with_water))+" %")
    # ===========================================================================================================

    # H6
    # ===========================================================================================================
    st.header(lang['hp']['hp_8'])
    h6_a = dataset_.loc[dataset_['waterfront'] == 'no', ['price', 'year_month']].groupby(['year_month']).mean().reset_index()
    h6_b = dataset_.loc[dataset_['waterfront'] == 'yes', ['price', 'year_month']].groupby(['year_month']).mean().reset_index()
    h6_a = MoM(h6_a)
    h6_b = MoM(h6_b)
    dfs = {lang['hp']['hp_3']: h6_a, lang['hp']['hp_4']: h6_b}
    # plot the data
    fig_2 = go.Figure()
    for i in dfs:
        fig_2 = fig_2.add_trace(go.Scatter(x=dfs[i]["year_month"],
                                       y=dfs[i]["MoM_%"],
                                       name=i))
    st.plotly_chart(fig_2, use_container_width=True)
    col8, col9 = st.columns(2)
    col8.subheader(lang['hp']['hp_5'])
    col9.subheader(lang['hp']['hp_6'])
    col10, col11, col12, col13 = st.columns(4)
    col10.metric(lang['hp']['hp_9'],str(round(h6_a['MoM_%'].mean(),2))+' %')
    col11.metric(lang['hp']['hp_10'],str(round(h6_a['MoM_%'].sum(),2))+' %')
    col12.metric(lang['hp']['hp_9'],str(round(h6_b['MoM_%'].mean(),2))+' %',str(dif(h6_a['MoM_%'].mean(),h6_b['MoM_%'].mean()))+" %")
    col13.metric(lang['hp']['hp_10'],str(round(h6_b['MoM_%'].sum(),2))+' %',str(dif(h6_a['MoM_%'].sum(),h6_b['MoM_%'].sum()))+" %")
    # ===========================================================================================================

    # h7
    # ===========================================================================================================
    h7_a = data.loc[data['grade'] == 7, ['price', 'year_month']].groupby('year_month').mean().reset_index()
    h7_b = data.loc[
        ((data['grade'] == 10) | (data['grade'] == 11) | (data['grade'] == 12) | (data['grade'] == 13)), ['price',
                                                                                                          'year_month']].groupby(
        'year_month').mean().reset_index()
    h7_a = MoM(h7_a)
    h7_b = MoM(h7_b)
    st.header(lang['hp']['hp_11']+str(dif(h7_a['MoM_%'].sum(), h7_b['MoM_%'].sum()))+lang['hp']['hp_12'])
    dfs = {lang['hp']['hp_13']: h7_a, lang['hp']['hp_14']: h7_b}
    # plot the data
    fig_3 = go.Figure()
    for i in dfs:
        fig_3 = fig_3.add_trace(go.Scatter(x=dfs[i]["year_month"],
                                           y=dfs[i]["MoM_%"],
                                           name=i))
    st.plotly_chart(fig_3, use_container_width=True)
    col14, col15 = st.columns(2)
    col14.subheader(lang['hp']['hp_15'])
    col15.subheader(lang['hp']['hp_16'])
    col16, col17, col18, col19 = st.columns(4)
    col16.metric(lang['hp']['hp_9'], str(round(h7_a['MoM_%'].mean(), 2)) + ' %')
    col17.metric(lang['hp']['hp_10'], str(round(h7_a['MoM_%'].sum(), 2)) + ' %')
    col18.metric(lang['hp']['hp_9'], str(round(h7_b['MoM_%'].mean(), 2)) + ' %',
                 str(dif(h7_a['MoM_%'].mean(), h7_b['MoM_%'].mean())) + " %")
    col19.metric(lang['hp']['hp_10'], str(round(h7_b['MoM_%'].sum(), 2)) + ' %',
                 str(dif(h7_a['MoM_%'].sum(), h7_b['MoM_%'].sum())) + " %")
    # ===========================================================================================================

    # h8
    # ===========================================================================================================
    price_bad_cond = dataset_.loc[((dataset_['condition'] == 1) | (dataset_['condition'] == 2)), 'price'].mean()
    price_good_cond = dataset_.loc[((dataset_['condition'] == 4) | (dataset_['condition'] == 5)), 'price'].mean()
    st.header(lang['hp']['hp_17']+str(dif(price_bad_cond,price_good_cond))+lang['hp']['hp_18'])
    fig_4 = px.bar(x=lang['hp']['hp_19'], y=[price_bad_cond, price_good_cond])
    fig_4.update_layout(
        xaxis_title=lang['hp']['hp_20'],
        yaxis_title=lang['hp']['hp_21'])
    st.plotly_chart(fig_4, use_container_width=True)
    col20, col21 = st.columns(2)
    col20.subheader(lang['hp']['hp_22'])
    col21.subheader(lang['hp']['hp_23'])
    col22, col23 = st.columns(2)
    col22.metric(lang['hp']['hp_7'],set_currency(round(price_bad_cond,2)))
    col23.metric(lang['hp']['hp_7'],set_currency(round(price_good_cond,2)),str(dif(price_bad_cond,price_good_cond))+" %")
    return None

# ==============
# aditional information
# ==============

def additional_info(lang):
    st.subheader(lang['ai']['ai_0'])
    st.write(lang['ai']['ai_1'])
    st.markdown(lang['ai']['ai_2'])
    st.markdown(lang['ai']['ai_3']+'[github](https://github.com/lavinomenezes/House_rocket_insight_project)')
    st.markdown(lang['ai']['ai_4'] + '[Portfolio](https://github.com/lavinomenezes)')
    st.markdown(lang['ai']['ai_5']+'[LinkedIn](https://www.linkedin.com/in/lavinomenezes/)')
    return None

if __name__ == '__main__':


    # ==============
    # Read the files
    # ==============
    raw_data = 'kc_house_data.csv'
    raw = get_data(raw_data)

    url = "https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson"
    geofile = get_geofile(url)


    lang = language()
    data = transform_columns(raw)
    data = clean_data(data)
    data = add_features(data)
    data_sell = suggest_sell(data)

    overview(data_sell,lang)

    main_information(data_sell,raw,lang)

    maps(data_sell,geofile,lang)

    hipothesys(data,lang)

    additional_info(lang)