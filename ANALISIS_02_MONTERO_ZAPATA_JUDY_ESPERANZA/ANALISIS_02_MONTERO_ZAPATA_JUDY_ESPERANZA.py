# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 18:23:13 2020

@author: girl-
"""

import csv

storage=[]

with open("synergy_logistics_database.csv","r") as Data:
  lector=csv.DictReader(Data)
  for dato in lector:
      storage.append(dato)
      



#función dos en uno. La consignia 2 y 3 están en este código
def multiusos(direccion,variable,año):
    
    cont=0
    profit=0
    sublista=[]
    lista_final=[]
    
    if año!='todos':
        
        suma=0
        for i in storage:
            if i['direction']==direccion and i['year']==año:
                suma+=int(i['total_value'])
                
        #Busca los elementos distintos en la base y las agrega a una lista
        for elemento in storage:
            if (elemento['direction']==direccion and elemento['year']==año and
                elemento[variable] not in sublista):
                sublista.append(elemento[variable])
                
        #Cuenta las ganancias y cuantas veces se produjo un envento
        for elemento in sublista:
            for dato in storage:
                if (elemento==dato[variable] and dato['year']==año and
                    dato['direction']==direccion):
                    cont+=1
                    profit+=int(dato['total_value'])
         
        #Aquí se agrega las ganancias y el elemento a una misma lista
            if variable=='transport_mode'or variable=='product':   
                lista_final.append([elemento,cont,profit,año])
            elif variable=='origin' or variable=='destination':
                lista_final.append([elemento,cont,profit,profit/suma*100,año])
            cont=0
            profit=0  

    elif año=='todos':
        suma=0
        for i in storage:
            if i['direction']==direccion:
                suma+=int(i['total_value'])
        
        for elemento in storage:
            if (elemento['direction']==direccion and
                elemento[variable] not in sublista):
                sublista.append(elemento[variable])
        
        for elemento in sublista:
            for dato in storage:
                if (elemento==dato[variable] and
                    dato['direction']==direccion):
                    cont+=1
                    profit+=int(dato['total_value'])
                    
            if variable=='transport_mode' or variable=='product':   
                lista_final.append([elemento,cont,profit,año])
            elif variable=='origin' or variable=='destination':
                lista_final.append([elemento,cont,profit,profit/suma*100,año])
            cont=0
            profit=0  
            
       
    lista_final.sort(reverse=True,key=lambda x:x[2])     

    # Esta parte sirve para ver donde se alcanza el 80%
    if variable=='origin' or variable=='destination':
        lista_porcentaje=[]
        suma_porcentaje=0
        i=0
        while suma_porcentaje<80:
            lista_porcentaje.append([lista_final[i][0],lista_final[i][2],
                                    lista_final[i][3],año])
            suma_porcentaje+=lista_final[i][3]
            i+=1
            
        return (lista_porcentaje)
           
    return (lista_final)   


#resultado = multiusos('Exports','origin','2020')
#print(resultado)




def rutas(direccion,año):
    cont=0
    rutas=[]
    rutas2=[]
    ganancia=0
    
    if año!='todos':
        #Busca los elementos distintos de la base de datos, agrega su ocurrencia 
        # y agrega las ganancias de la ocurrencia.
        for dato in storage:
            ruta_actual=[dato['origin'],dato['destination']]
            if (ruta_actual not in rutas2 and dato['direction']==direccion
                and dato['year']==año):
                rutas2.append(ruta_actual)
                for elemento in storage:
                    if (ruta_actual==[elemento['origin'],elemento['destination']] 
                        and elemento['year']==año and
                        elemento['direction']==direccion):
                        cont+=1
                        ganancia+=int(elemento['total_value'])
                #Se agrega una lista los elementos necesarios
                rutas.append([dato['origin'],dato['destination'],cont,ganancia,
                              dato['transport_mode'],año])
                cont=0
                ganancia=0
            
    elif año=='todos': 
          
          for dato in storage:
            ruta_actual=[dato['origin'],dato['destination']]
            if (ruta_actual not in rutas2 and dato['direction']==direccion):
                rutas2.append(ruta_actual)
                for elemento in storage:
                    if (ruta_actual==[elemento['origin'],elemento['destination']] 
                        and elemento['direction']==direccion):
                        cont+=1
                        ganancia+=int(elemento['total_value'])
                
                rutas.append([dato['origin'],dato['destination'],cont,ganancia,
                              dato['transport_mode'],año])
                cont=0
                ganancia=0
    
    rutas.sort(reverse=True,key=lambda x:x[3])
    return rutas

#resultado_rutas = rutas('Exports','todos')



msg="""  SYNERGY  LOGISTICS 

        MENÚ
        
    Elije una de las opciones que aparecen:

    1. Exportaciones por ruta (Top 10)
    2. Importaciones por ruta (Top 10)
    3. Modo de transporte exportaciones
    4. Modo de transporte importaciones
    5. Paises que generan más ganancia por exportaciones
    6. Paises que generan más ganancia por importaciones
     
    Puntos extras
    
    7. Productos más importados
    8. Productos más exportados
    
    """

print(msg)
opcion=input("Ingrese opción: ")


    

if opcion=='1':
    opcion2=input('Si deseas ver un año en específico, ingresa año. \nCaso contrario escriba "todos" \nNOTA: Si ingresa una valor distinto a los anteriores, la lista será nulan\Respuesta: ')
    if opcion2=='2020'or '2019'or'2018'or'2017'or'2016'or'2015':
        resultado_rutas=rutas('Exports',opcion2)
        print(opcion2)
    else: 
        resultado_rutas = rutas('Exports','todos')

elif opcion=='2':
    opcion2=input('Si deseas ver un año en específico, ingresa año. \nCaso contrario escriba "todos" \nNOTA: Si ingresa una valor distinto a los anteriores, la lista será nulan\Respuesta: ')
    if opcion2=='2020'or '2019'or'2018'or'2017'or'2016'or'2015':
        resultado_rutas=rutas('Imports',opcion2)
    else:
        resultado_rutas = rutas('Imports','todos')
        

elif opcion=='3':
    opcion2=input('Si deseas ver un año en específico, ingresa año. \nCaso contrario escriba "todos" \nNOTA: Si ingresa una valor distinto a los anteriores, la lista será nulan\Respuesta: ')
    if opcion2=='2020'or '2019'or'2018'or'2017'or'2016'or'2015':
        resultados=multiusos('Exports','transport_mode',opcion2) 
    else:
        resultados = multiusos('Exports','transport_mode','todos')
        

elif opcion=='4':
    opcion2=input('Si deseas ver un año en específico, ingresa año. \nCaso contrario escriba "todos" \nNOTA: Si ingresa una valor distinto a los anteriores, la lista será nulan\Respuesta: ')
    if opcion2=='2020'or '2019'or'2018'or'2017'or'2016'or'2015':
        resultados=multiusos('Imports','transport_mode',opcion2) 
    else:
        resultados = multiusos('Imports','transport_mode','todos')

elif opcion=='5':
    opcion2=input('Si deseas ver un año en específico, ingresa año. \nCaso contrario escriba "todos" \nNOTA: Si ingresa una valor distinto a los anteriores, la lista será nulan\Respuesta: ')
    if opcion2=='2020'or '2019'or'2018'or'2017'or'2016'or'2015':
        resultados=multiusos('Exports','origin',opcion2) 
    else:
        resultados = multiusos('Exports','origin','todos')        
        
elif opcion=='6':
    opcion2=input('Si deseas ver un año en específico, ingresa año. \nCaso contrario escriba "todos" \nNOTA: Si ingresa una valor distinto a los anteriores, la lista será nulan\Respuesta: ')    
    if opcion2=='2020'or '2019'or'2018'or'2017'or'2016'or'2015':
        resultados=multiusos('Imports','destination',opcion2) 
    else:
        resultados = multiusos('Imports','destination','todos')

elif opcion=='7':
    opcion2=input('Si deseas ver un año en específico, ingresa año. \nCaso contrario escriba "todos" \nNOTA: Si ingresa una valor distinto a los anteriores, la lista será nulan\Respuesta: ')     
    if opcion2=='2020'or '2019'or'2018'or'2017'or'2016'or'2015':
        resultados=multiusos('Imports','product',opcion2)
    else:
        resultados = multiusos('Imports','product','todos')

elif opcion=='8':
    opcion2=input('Si deseas ver un año en específico, ingresa año. \nCaso contrario escriba "todos" \nNOTA: Si ingresa una valor distinto a los anteriores, la lista será nulan\Respuesta: ')     
    if opcion2=='2020'or '2019'or'2018'or'2017'or'2016'or'2015':
        resultados=multiusos('Exports','product',opcion2) 
    else:
        resultados = multiusos('Exports','product','todos')


msg1="""   
    La lista "resultados_rutas" muestra los resultados 
    de la opción 1 y 2.
    
    La lista "resultados" muestra los resultados obtenidos 
    del punto 3,4,5,6,7 y 8.
    
    """
print(msg1)







