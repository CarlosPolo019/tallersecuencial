i = 1
while i == 3:
    valorCamisa = 0.0
    valorCamisa = float(input('Digite el valor de la camisa: '))
    if valorCamisa != 0:
        totalCamisa += valorCamisa
        i += 1
    elif valorCamisa == 0:
        if i-1 >= 3: 
            total =  totalCamisa - (0.30 * totalCamisa)
            print(f'Su compra aplica para un descuetno del: 30%')
            print(f'Cantidad de camisas compradas: {i-1}')
            print(f'Total compra sin descuento {totalCamisa}')
            print(f'Total compra con descuento {total}')
        elif i-1 >= 1:
            total =  totalCamisa - (0.10 * totalCamisa)
            print(f'Su compra aplica para un descuetno del: 10%')
            print(f'Cantidad de camisas compradas: {i-1}')
            print(f'Total compra sin descuento {totalCamisa}')
            print(f'Total compra con descuento {total}')
        else:
            print(f'No hay camisas en el carrito')
        break 

