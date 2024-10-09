faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento.values())

percentual = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}

for estado, perc in percentual.items():
    print(f"{estado}: {perc:.2f}%")
