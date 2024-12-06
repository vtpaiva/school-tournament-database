def continuos_to_discrete(field, value=None):
    """
    Converte valores contínuos em categorias discretas dependendo do campo.
    
    Parameters:
        field (int | str): O campo que determina a categoria. 
                           0 ou 'h' para altura e 1 ou 'w' para peso.
        value (float | None): O valor a ser convertido. Se for None, retorna 'QUALQUER'.
        
    Returns:
        str: A categoria correspondente ao valor fornecido.
    """
    
    if value is None:
        return 'QUALQUER'
    
    if field == 0:  
        if value < 1.5:
            return 'MUITO BAIXO'
        elif value < 1.6:
            return 'BAIXO'
        elif value < 1.7:
            return 'MEDIO-BAIXO'
        elif value < 1.8:
            return 'MEDIO'
        elif value < 1.9:
            return 'ALTO'
        else: 
            return 'MUITO ALTO'

    elif field == 1:
        if value < 50:
            return 'MUITO LEVE'
        elif value < 60:
            return 'LEVE'
        elif value < 75:
            return 'MEDIO'
        elif value < 90:
            return 'PESADO'
        elif value < 110:
            return 'MUITO PESADO'
        else:
            return 'EXTREMAMENTE PESADO'