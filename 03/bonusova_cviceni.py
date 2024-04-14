# Vypište seznam čísel každé na nový řádek zarovnané vpravo na délku nejdelšího čísla.

numbers = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]

def zarovnavac(seznam, znak):
  nejdelsi_cislo_v_seznamu = len(str(max(seznam)))
  for n in seznam:
    znaky_pred_cislem =(nejdelsi_cislo_v_seznamu - len(str(n)))*znak
    print(f"{znaky_pred_cislem}{n}")

zarovnavac(numbers, "*")