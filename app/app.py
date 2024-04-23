import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from sklearn.preprocessing import LabelEncoder
from PIL import Image 



min_time = 0.00052926
max_time = 7.6994172

def transformar_tiempo(tiempo_seleccionado):
    # Realiza la transformación del tiempo al rango original de tu columna 'Time'
    # Aquí podrías usar una fórmula específica para tu transformación
    # Por ejemplo, podrías escalar el valor seleccionado al rango de tu columna 'Time'
    # tiempo_transformado = ...
    tiempo_transformado = tiempo_seleccionado  

    return tiempo_transformado

def main():
    st.title("Evolución humana: Modelo Clasificación de Hominoideos\n")

    imagen_path = "../img/img1.png"  
    def cargar_imagen(imagen_path):
        st.image(imagen_path, caption='Descripción opcional de la imagen', use_column_width=True)

        
    cargar_imagen(imagen_path)



    st.title("Datación")
    st.write("Selecciona el tiempo en el que vivieron los homínidos:")

    tiempo_seleccionado = st.slider("Tiempo (en millones de años)", min_value=min_time, max_value=max_time, value=(min_time + max_time) / 2)

    tiempo_transformado = transformar_tiempo(tiempo_seleccionado)

    st.write(f"Tiempo seleccionado: {tiempo_seleccionado} millones de años")
    st.write(f"Tiempo transformado: {tiempo_transformado}")


    biped_mapping = {
        'baja probabilidad': 0,
        'alta probabilidad': 1,
        'si': 2,
        'moderno':3
        }

    st.title("Bípedo")
    st.write("Selecciona la probabilidad de ser bípedo:")


    opciones_biped = ['baja probabilidad', 'alta probabilidad', 'si', 'moderno']

    seleccion_biped = st.selectbox("Selecciona la probabilidad de ser bípedo:", opciones_biped)

    valor_numerico_biped = biped_mapping.get(seleccion_biped)

    st.write(f"El valor numérico correspondiente para '{seleccion_biped}' es: {valor_numerico_biped}")

    foramen_mapping = {
        'posterior': 0,
        'semi-anterior': 1,
        'anterior': 2,
        'moderno': 3
    }


    st.title("Posición del Foramen mágnum")
    

    opciones_foramen = list(foramen_mapping.keys())

    seleccion_foramen = st.selectbox("Selecciona la posición del Foramen mágnum:", opciones_foramen)

    valor_numerico_foramen = foramen_mapping.get(seleccion_foramen)

    st.write(f"El valor numérico correspondiente para '{seleccion_foramen}' es: {valor_numerico_foramen}")


    torus_supraorbital_mapping = {
    'Ultra Protuberante':0,
    'Muy Protuberante':1,
    'Menos Protuberante':2,
    'Poco Protuberante':3,
    'Plano':4
    }

    st.title("Forma del Torus Supraorbital")
    

    opciones_torus = list(torus_supraorbital_mapping.keys())

    seleccion_torus = st.selectbox("Selecciona el tipo de Torus Supraorbital:", opciones_torus)

    valor_numerico_torus = torus_supraorbital_mapping.get(seleccion_torus)

    st.write(f"El valor numérico correspondiente para '{seleccion_torus}' es: {valor_numerico_torus}")

    tecno_mapping = {
    'no': 0,
    'si': 2,
    'probable': 1
    }


    st.title("Tecnología")

    opciones_tecno = list(tecno_mapping.keys())

    seleccion_tecno = st.selectbox("Selecciona la presencia o ausencia de avances tecnológicos:", opciones_tecno)

    valor_numerico_tecno = tecno_mapping.get(seleccion_tecno)

    st.write(f"El valor numérico correspondiente para '{seleccion_tecno}' es: {valor_numerico_tecno}")

    diet_mapping = {
        'Carnívora': 3,
        'Omnivora': 4,
        'Frutos blandas': 2,
        'Frutos duras': 0,
        'Frutos secos': 1
    }


    st.title("Dieta")
    

    opciones_dieta = list(diet_mapping.keys())

    seleccion_dieta = st.selectbox("Selecciona el tipo de dieta:", opciones_dieta)

    valor_numerico_dieta = diet_mapping.get(seleccion_dieta)

   
    st.write(f"El valor numérico correspondiente para '{seleccion_dieta}' es: {valor_numerico_dieta}")


    anatomy_mapping = {
    'Antigua': 0,
    'Mixta': 1,
    'Moderna': 2,
    'Muy moderna': 3
    }


    st.title("Características anatómicas")
 
    opciones_anatomía = list(anatomy_mapping.keys())

    seleccion_anatomia = st.selectbox("Selecciona el tipo de anatomía:", opciones_anatomía)

    valor_numerico_anatomia = anatomy_mapping.get(seleccion_anatomia)

    st.write(f"El valor numérico correspondiente para '{seleccion_anatomia}' es: {valor_numerico_anatomia}")



    st.title("Ubicación")
    

  
    opciones_ubicacion = ['Africa', 'Europa', 'Asia']

    seleccion_ubicacion = st.selectbox("Selecciona la ubicación:", opciones_ubicacion)

   
    label_encoder = LabelEncoder()

  
    ubicaciones_codificadas = label_encoder.fit_transform(opciones_ubicacion)

  
    valor_numerico_ubicacion = ubicaciones_codificadas[opciones_ubicacion.index(seleccion_ubicacion)]

    st.write(f"El valor numérico correspondiente para '{seleccion_ubicacion}' es: {valor_numerico_ubicacion}")

  
    tooth_enamel_mapping = {
        'Muy grueso': 0,
        'Grueso': 0,
        'Medio-grueso': 1,
        'Medio-fino': 1,
        'Fino': 2,
        'Muy fino': 2 
    }

    st.title("Datos sobre el esmalte dental")
    st.write("Selecciona el grosor del esmalte dental:")

    opciones_esmalte = list(tooth_enamel_mapping.keys())

  
    seleccion_esmalte_dental = st.selectbox("Selecciona el grosor del esmalte dental:", opciones_esmalte)

    valor_numerico_esmalte = tooth_enamel_mapping.get(seleccion_esmalte_dental)

    
    st.write(f"El valor numérico correspondiente para '{seleccion_esmalte_dental}' es: {valor_numerico_esmalte}")

    
    
    canine_s_mapping = {
    'Grande': 0,
    'Pequeño': 1
    }


    st.title("Tamaño de los Caninos")
    st.write("Selecciona el tamaño de los caninos:")

   
    opciones_caninos = list(canine_s_mapping.keys())

    
    seleccion_tamaño_caninos = st.selectbox("Selecciona el tamaño de los caninos:", opciones_caninos)

   
    valor_numerico_caninos = canine_s_mapping.get(seleccion_tamaño_caninos)

  
    st.write(f"El valor numérico correspondiente para '{seleccion_tamaño_caninos}' es: {valor_numerico_caninos}")




    tiempos = []
    bipedos = []
    foramen = []
    torus=[]
    tecno = []
    dieta = []
    anatomia = []
    ubicacion = []
    esmalte_dental = []
    tamano_caninos = []

   
    tiempos.append(tiempo_seleccionado)
    bipedos.append(valor_numerico_biped)
    foramen.append(valor_numerico_foramen)
    torus.append(valor_numerico_torus)
    tecno.append(valor_numerico_tecno)
    dieta.append(valor_numerico_dieta)
    anatomia.append(valor_numerico_anatomia)
    ubicacion.append(valor_numerico_ubicacion)
    esmalte_dental.append(valor_numerico_esmalte)
    tamano_caninos.append(valor_numerico_caninos)


    df_respuestas = pd.DataFrame({
            'Time': tiempos,
            'Biped_encoded': bipedos,
            'Foramen_encoded': foramen,
            'Torus_Supraorbital_encoded':torus,
            'Tecno_encoded': tecno,
            'Diet_encoded': dieta,
            'Anatomy_encoded': anatomia,
            'Location_encoded': ubicacion,
            'Tooth_Enamel_encoded': esmalte_dental,
            'Canine_Size_encoded': tamano_caninos
            })
    st.write(df_respuestas)

    filename = '../models/rf2_final.pkl'
    with open(filename, 'rb') as archivo_entrada:
        modelo = pickle.load(archivo_entrada)

        
    especies = {
        0: 'Hominino Sahelanthropus tchadensis',
        1: 'Hominino Orrorin tugenencin',
        2: 'Hominino Ardipithecus ramidus / kabadda',
        3: 'Ardipithecus Ramidus / Kadabba',
        4: 'Australopithecus Anamensis',
        5: 'Australopithecus Afarensis',
        6: 'Australopithecus Bahrelghazali',
        7: 'Australopithecus Africanus',
        8: 'Australopithecus Garhi',
        9: 'Australopithecus Sediba',
        10: 'Paranthropus Aethiopicus',
        11: 'Paranthropus Robustus',
        12: 'Paranthropus Boisei',
        13: 'Homo Habilis',
        14: 'Homo Rudolfensis',
        15: 'Homo Georgicus',
        16: 'Homo Ergaster',
        17: 'Homo Erectus',
        18: 'Homo Naledi',
        19: 'Homo Floresiensis',
        20: 'Homo Antecesor',
        21: 'Homo Heidelbergensis',
        22: 'Homo Rodhesiensis',
        23: 'Homo Neanderthalensis',
        24: 'Homo Sapiens'}
    
    st.title('Predicciones del Modelo:')
    predicciones = modelo.predict(df_respuestas)
    etiquetas_prediccion = [especies[numero] for numero in predicciones]
    df_predicciones = pd.DataFrame({'Predicción clase': etiquetas_prediccion})
    
    df_predicciones.rename(columns={0: 'Predicción clase'}, inplace=True)
    st.write(df_predicciones)



main()