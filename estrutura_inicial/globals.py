# import pandas as pd
# import os

# if("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
#     df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True)
#     df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True)
#     df_despesas["Data"] = pd.to_datetime(df_despesas["Data"])
#     df_receitas["Data"] = pd.to_datetime(df_receitas["Data"])
#     df_despesas["Data"] = df_despesas["Data"].apply(lambda x: x.date())
#     df_receitas["Data"] = df_receitas["Data"].apply(lambda x: x.date())
    
    
# else:
#     data_structure = {'Valor':[],
#         'Efetuado':[],
#         'Fixo':[],
#         'Data':[],
#         'Categoria':[],
#         'Descricão':[],}
#     df_receitas = pd.DataFrame(data_structure)
#     df_despesas = pd.DataFrame(data_structure)
#     df_despesas.to_csv("df_despesas.csv")
#     df_receitas.to_csv("df_receitas.csv")
    
# if("df_cat_receita.csv" in os.listdir()) and ("df_cat_despesa.csv" in os.listdir()):
#     df_cat_receita = pd.read_csv("df_cat_receita.csv", index_col=0)
#     df_cat_despesa = pd.read_csv("df_cat_despesa.csv", index_col=0)
#     cat_receita = df_cat_receita.values.tolist()
#     cat_despesa = df_cat_despesa.values.tolist()

# else:
#      cat_receita = {'Categoria': ["Salário", "Investimentos", "Comissão"]}
#      cat_despesa = {'Categoria': ["Alimentação", "Aluguel", "Gasolina", "Saúde", "Lazer"]}  
     
#      df_cat_receita = pd.DataFrame(cat_receita)
#      df_cat_despesa = pd.DataFrame(cat_despesa) 
#      df_cat_receita.to_csv("df_cat_receita.csv")
#      df_cat_despesa.to_csv("df_cat_despesa.csv")
     
     
      
        
    
    
import pandas as pd
import os

# Função para verificar a presença dos arquivos e criar DataFrames
def carregar_ou_criar_dataframe(nome_arquivo, colunas):
    if nome_arquivo in os.listdir():
        df = pd.read_csv(nome_arquivo, index_col=0, parse_dates=["Data"])
        # Garantir que a coluna "Data" seja tratada como data
        df["Data"] = pd.to_datetime(df["Data"], errors='coerce').dt.date
    else:
        df = pd.DataFrame(columns=colunas)
        df.to_csv(nome_arquivo)
    return df

# Colunas esperadas para os DataFrames
colunas = ['Valor', 'Efetuado', 'Fixo', 'Data', 'Categoria', 'Descrição']

# Carregar ou criar os DataFrames
df_despesas = carregar_ou_criar_dataframe("df_despesas.csv", colunas)
df_receitas = carregar_ou_criar_dataframe("df_receitas.csv", colunas)

# Carregar ou criar os DataFrames de categorias
def carregar_ou_criar_categorias(nome_arquivo, categorias):
    if nome_arquivo in os.listdir():
        df = pd.read_csv(nome_arquivo, index_col=0)
        categorias_lista = df['Categoria'].tolist()
    else:
        df = pd.DataFrame(categorias)
        df.to_csv(nome_arquivo)
        categorias_lista = df['Categoria'].tolist()
    return df, categorias_lista

# Categorias padrão
categorias_receita = {'Categoria': ["Salário", "Investimentos", "Comissão"]}
categorias_despesa = {'Categoria': ["Alimentação", "Aluguel", "Gasolina", "Saúde", "Lazer"]}

# Carregar ou criar os DataFrames de categorias
df_cat_receita, cat_receita = carregar_ou_criar_categorias("df_cat_receita.csv", categorias_receita)
df_cat_despesa, cat_despesa = carregar_ou_criar_categorias("df_cat_despesa.csv", categorias_despesa)
    