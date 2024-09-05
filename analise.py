import pandas as pd
import matplotlib.pyplot as plt
def questao_um():
  indice = 13
  soma=0
  k = 0

  while k < indice:
    k += 1
    soma += k

  return soma

def questao_dois(numero):
  sequencia_fibo = [0,1]
  while True:
    sequencia = sequencia_fibo[-1] + sequencia_fibo[-2]
    if sequencia == numero:
      return f"O número {numero} pertence a sequencia!"
    elif sequencia > numero:
      return f"O número {numero} não pertence a sequencia!"
    sequencia_fibo.append(sequencia)


"""
  Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
"""
def questao_tres():
  # entrada dos dados
  df = pd.read_json('/content/dados.json')
  df.columns

  # Processamento
  df = df[df['valor'] > 0.0]
  df.min()

  valor_minimo = df['valor'].min()
  dia_do_valor_minimo = df.loc[df['valor'] == valor_minimo, 'dia'].iloc[0]

  valor_maximo = df['valor'].max()
  dia_do_valor_maximo = df.loc[df['valor'] == valor_maximo, 'dia'].iloc[0]

  media_do_faturamento = df['valor'].mean()
  numero_de_dias_acima_da_media = df[df['valor'] > media_do_faturamento].shape[0]


  # Saida
  print(f'O menor valor do faturamentodo mês foi R$ {valor_minimo:.2f} do dia {dia_do_valor_minimo}')
  print(f'O maior valor do faturamento do mês foi R$ {valor_maximo:.2f} do dia {dia_do_valor_maximo}')
  print(f'O número de dias em que o faturamento foi maior que a média mensal: {numero_de_dias_acima_da_media}')

def questao_quatro():
  data_frame = {
      'estado' : ['SP', 'RJ', 'MG', 'ES', 'Outros'],
      'valor': [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
  }
  df = pd.DataFrame(data_frame)

  total = df['valor'].sum()

  plt.pie(df['valor'], labels = df['estado'], autopct='%1.1f%%')
  plt.title('Percentual total de cada estado')
  plt.xlabel(f'Valor total R$ {total:.2f}')
  plt.show()

  # ou

  df['percentual'] = (df['valor'] / total) * 100
  df['percentual'] = df['percentual'].round(1)
  display(df)

def questao_cinco():
  nome = "Rafael Mendonça de Santana"
  invertido = nome[::-1]

  return invertido
