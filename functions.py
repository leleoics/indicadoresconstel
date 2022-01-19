import pandas as pd
import gspread
from google.oauth2 import service_account

json_file = "./json/planejamento-constel123-1b8f07026a82.json"
scopes = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]

def login():
    credentials = service_account.Credentials.from_service_account_file(json_file)
    scoped_credentials = credentials.with_scopes(scopes)
    gc = gspread.authorize(scoped_credentials)
    return gc

def leitor(worksheet,sheet): # Acessa a planilha, a aba específica e retorna um dataframe
    gc = login()
    planilha = gc.open(worksheet)
    aba = planilha.worksheet(sheet)
    dados = aba.get_all_values()
    dfi = pd.DataFrame(dados)
    return dfi

def indicador(df):
    head = df.iloc[3]
    header = list(head[:5])
    dfc = df[4:16]
    dfc = dfc.rename(columns={0: header[0], 1: header[1], 2: header[2], 3: header[3], 4: header[4]})
    filtered_df = dfc.loc[:,header]
    return filtered_df
    
    
def indicador4t(df):
    head = df.iloc[3]
    header = list(head[:5])
    dfc = df[13:16]
    dfc = dfc.rename(columns={0: header[0], 1: header[1], 2: header[2], 3: header[3], 4: header[4]})
    filtered_df = dfc.loc[:,header]
    return filtered_df


def desempenho_manutencao(df):
    head = df.iloc[0]
    header = list(head[:18])
    dfc = df[1:10]
    dfc = dfc.rename(columns={0: header[0], 1: header[1], 2: header[2], 3: header[3], 4: header[4],
    5: header[5], 6: header[6], 7: header[7], 8: header[8], 9: header[9], 10: header[10], 11: header[11],
    12: header[12], 13: header[13], 14: header[14], 15: header[15], 16: header[16], 17: header[17]})
    filtered_df = dfc.loc[:,header]
    return filtered_df

def desempenho_instalação_rh(df):
    head = df.iloc[0]
    header = list(head[:6])
    dfc = df[1:13]
    dfc = dfc.rename(columns={0: header[0], 1: header[1], 2: header[2], 3: header[3], 4: header[4],
    5: header[5]})
    filtered_df = dfc.loc[:,header]
    return filtered_df

def desempenho_almoxarifado(df):
    head = df.iloc[0]
    header = list(head[:8])
    dfc = df[1:73]
    dfc = dfc.rename(columns={0: header[0], 1: header[1], 2: header[2], 3: header[3], 4: header[4],
    5: header[5], 6: header[6], 7: header[7]})
    filtered_df = dfc.loc[:,header]
    return filtered_df

def desempenho_plan_proj(df):
    head = df.iloc[0]
    header = list(head[:5])
    dfc = df[1:10]
    dfc = dfc.rename(columns={0: header[0], 1: header[1], 2: header[2], 3: header[3], 4: header[4]})
    filtered_df = dfc.loc[:,header]
    return filtered_df

 