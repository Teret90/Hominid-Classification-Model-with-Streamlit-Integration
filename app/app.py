import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from sklearn.preprocessing import LabelEncoder
from PIL import Image 
#import evaluation.py
#from evaluation.py import calcular_metricas
#from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score, roc_auc_score

    # Crear una barra lateral para la navegación entre pestañas
st.sidebar.title('Navegación')
pestañas = ['Predicciones del Modelo', 'Desempeño del Modelo']  # Nombres de las pestañas
seleccion = st.sidebar.selectbox('Ir a:', pestañas)

# Mostrar contenido de la pestaña seleccionada


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
    st.title("Evolución humana: Modelo Clasificación de Homininos fósiles\n")

    imagen_path = "../img/img1.png"  
    def cargar_imagen(imagen_path):
        st.image(imagen_path, caption='Clasificación de homínidos.Fuente: https://www.museoevolucionhumana.com/media/files/Evolucion.pdf', use_column_width=True)

        
    cargar_imagen(imagen_path)



    st.title("Datación")
    st.write("Selecciona el tiempo en el que vivieron los homininos:")

    tiempo_seleccionado = st.slider("Tiempo (en millones de años)", min_value=min_time, max_value=max_time, value=(min_time + max_time) / 2)

    tiempo_transformado = transformar_tiempo(tiempo_seleccionado)

    st.write(f"Tiempo seleccionado: {tiempo_seleccionado} millones de años")
    st.write(f"Tiempo transformado: {tiempo_transformado}")

    locations = ['Africa', 'Europa', 'Asia']

    selected_location = st.selectbox("Seleccione una ubicación:", locations)

    label_encoder = LabelEncoder()

 
    label_encoder.fit(locations)

    selected_location_encoded = label_encoder.transform([selected_location])[0]
    st.write("Ubicación seleccionada:")
    st.write(selected_location)


   

    opciones_zone = ['Este', 'Sur', 'Central', 'Oeste']
    seleccion_zone = st.selectbox("Seleccione una zona:", opciones_zone)


    zone_mapping = {
        'Este': 0,
        'Sur': 1,
        'Central': 2,
        'Oeste': 3

    }

    valor_numerico_zone = zone_mapping.get(seleccion_zone)

    st.write(f"El valor numérico correspondiente para '{seleccion_zone}' es: {valor_numerico_zone}")

    habitat_mapping = {
    'peninsular': 0,
    'bosque-sabana': 0,
    'selva': 1,
    'bosque frío': 1,
    'galería forestal': 1,
    'bosque': 1,
    'mixto': 2,
    'sabana': 3
    }

    st.title("Selección de Hábitat")
    st.write("Seleccione el tipo de hábitat para predecir:")

    opciones_habitat = list(habitat_mapping.keys())

    habitat_seleccionado = st.selectbox("Seleccione el tipo de hábitat:", opciones_habitat)

    valor_numerico_habitat = habitat_mapping.get(habitat_seleccionado)
    
    st.write(f"El valor numérico correspondiente para '{habitat_seleccionado}' es: {valor_numerico_habitat}")


    min_capacidad_craneal = 0.07491
    max_capacidad_craneal = 1448.39747

    st.title("Clasificación de Hominidos")
    st.write("Selecciona la capacidad craneal para clasificar a los homínidos:")

    capacidad_craneal_seleccionada = st.slider("Capacidad Craneal (en cm³)", 
                                           min_value=min_capacidad_craneal, 
                                           max_value=max_capacidad_craneal, 
                                           value=(min_capacidad_craneal + max_capacidad_craneal) / 2)
    
    min_altura = 80.00903
    max_altura = 184.98145

    # Configurar la aplicación Streamlit
    st.title("Clasificación de Alturas")
    st.write("Selecciona la altura para clasificar a las personas:")

    # Slider para seleccionar la altura en centímetros
    altura_seleccionada = st.slider("Altura (en cm)", 
                                    min_value=min_altura, 
                                    max_value=max_altura, 
                                    value=(min_altura + max_altura) / 2)


    mapeo_tamano_incisivos = {
    'muy pequeño': 1,
    'pequeño': 2,
    'mediano grande': 3,
    'grande': 4,
    'megadoncia': 5
    }

 
    st.title("Selección de Tamaño de Incisivos")
    st.write("Seleccione el tamaño de incisivos para predecir:")

    opciones_tamano_incisivos = list(mapeo_tamano_incisivos.keys())

    tamano_incisivos_seleccionado = st.selectbox("Seleccione el tamaño de incisivos:", opciones_tamano_incisivos)

    valor_numerico_tamano_incisivos = mapeo_tamano_incisivos.get(tamano_incisivos_seleccionado)
   
    st.write(f"El valor numérico correspondiente para '{tamano_incisivos_seleccionado}' es: {valor_numerico_tamano_incisivos}")
    
    mapeo_forma_mandibula = {
    'Cónica': 4,
    'Forma de U': 3,
    'Moderna': 2,
    'Forma de V': 1
    }


    st.title("Selección de Forma de la Mandíbula")
    st.write("Seleccione la forma de la mandíbula para predecir:")

    opciones_forma_mandibula = list(mapeo_forma_mandibula.keys())

    forma_mandibula_seleccionada = st.selectbox("Seleccione la forma de la mandíbula:", opciones_forma_mandibula)

    valor_numerico_forma_mandibula = mapeo_forma_mandibula.get(forma_mandibula_seleccionada)

    st.write(f"El valor numérico correspondiente para '{forma_mandibula_seleccionada}' es: {valor_numerico_forma_mandibula}")

    mapeo_prognatismo = {
    'ausente': 5,
    'reducido': 4,
    'medio': 3,
    'medio-alto': 2,
    'alto': 1,
    'muy alto': 0
}

    st.title("Selección de Grado de Prognatismo")
    st.write("Seleccione el grado de prognatismo para predecir:")

    opciones_prognatismo = list(mapeo_prognatismo.keys())


    prognatismo_seleccionado = st.selectbox("Seleccione el grado de prognatismo:", opciones_prognatismo)

    valor_numerico_prognatismo = mapeo_prognatismo.get(prognatismo_seleccionado)

    st.write(f"El valor numérico correspondiente para '{prognatismo_seleccionado}' es: {valor_numerico_prognatismo}")


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

    mapeo_vertical_frontal = {
    'moderna': 2,
    'sí': 1,
    'no': 0
    }
    
    st.title("Selección de Verticalidad Frontal")
    st.write("Seleccione el tipo de verticalidad frontal para predecir:")

    opciones_vertical_frontal = list(mapeo_vertical_frontal.keys())

    vertical_frontal_seleccionada = st.selectbox("Seleccione el tipo de verticalidad frontal:", opciones_vertical_frontal)

    valor_numerico_vertical_frontal = mapeo_vertical_frontal.get(vertical_frontal_seleccionada)

    st.write(f"El valor numérico correspondiente para '{vertical_frontal_seleccionada}' es: {valor_numerico_vertical_frontal}")


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

    mapeo_tipo_herramientas = {
    'no': 0,
    'primitivas': 1,
    'modo 1': 2,
    'modo 2': 3,
    'modo 3': 4,
    'modo 4': 5}

    st.title("Selección de Tipo de Herramientas")
    st.write("Seleccione el tipo de herramientas para predecir:")

    opciones_tipo_herramientas = list(mapeo_tipo_herramientas.keys())

    tipo_herramientas_seleccionado = st.selectbox("Seleccione el tipo de herramientas:", opciones_tipo_herramientas)

    valor_numerico_tipo_herramientas = mapeo_tipo_herramientas.get(tipo_herramientas_seleccionado)

    st.write(f"El valor numérico correspondiente para '{tipo_herramientas_seleccionado}' es: {valor_numerico_tipo_herramientas}")

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

    mapeo_tipo_pies = {
    'escalada': 0,
    'caminata': 1
    }

    st.title("Selección de tipo de pies")
    st.write("Seleccione el tipo de pies para predecir:")

    opciones_tipo_pies = list(mapeo_tipo_pies.keys())

    tipo_pies_seleccionado = st.selectbox("Seleccione el tipo de pies:", opciones_tipo_pies)

    valor_numerico_tipo_pies = mapeo_tipo_pies.get(tipo_pies_seleccionado)

    st.write(f"El valor numérico correspondiente para '{tipo_pies_seleccionado}' es: {valor_numerico_tipo_pies}")

    mapeo_tipo_brazos = {
    'escalada': 0,
    'manipulación': 1,
    'manipulación con precisión': 2}

    st.title("Selección de Tipo de Brazos")
    st.write("Seleccione el tipo de brazos para predecir:")

    opciones_tipo_brazos = list(mapeo_tipo_brazos.keys())

    tipo_brazos_seleccionado = st.selectbox("Seleccione el tipo de brazos:", opciones_tipo_brazos)

    valor_numerico_tipo_brazos = mapeo_tipo_brazos.get(tipo_brazos_seleccionado)

    st.write(f"El valor numérico correspondiente para '{tipo_brazos_seleccionado}' es: {valor_numerico_tipo_brazos}")

    mapeo_dimorfismo_sexual = {
    'alto': 0,
    'medio-alto': 1,
    'reducido': 2
    }

    st.title("Selección de Dimorfismo Sexual")
    st.write("Seleccione el nivel de dimorfismo sexual para predecir:")

    opciones_dimorfismo_sexual = list(mapeo_dimorfismo_sexual.keys())
 
    dimorfismo_sexual_seleccionado = st.selectbox("Seleccione el nivel de dimorfismo sexual:", opciones_dimorfismo_sexual)

    valor_numerico_dimorfismo_sexual = mapeo_dimorfismo_sexual.get(dimorfismo_sexual_seleccionado)

    st.write(f"El valor numérico correspondiente para '{dimorfismo_sexual_seleccionado}' es: {valor_numerico_dimorfismo_sexual}")

    mapeo_cadera = {
    'muy moderna': 3,
    'moderna': 2,
    'ancho': 1,
    'delgada': 0
}

    st.title("Selección de Cadera")
    st.write("Seleccione el tipo de cadera para predecir:")

    opciones_cadera = list(mapeo_cadera.keys())

    cadera_seleccionada = st.selectbox("Seleccione el tipo de cadera:", opciones_cadera)

    valor_numerico_cadera = mapeo_cadera.get(cadera_seleccionada)
    
    st.write(f"El valor numérico correspondiente para '{cadera_seleccionada}' es: {valor_numerico_cadera}")



  
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


    mapeo_forma_caninos = {
    'cónicos': 0,       # más antigua
    'incisiformes': 1   # más reciente
    }

    st.title("Selección de Forma de los Caninos")
    st.write("Seleccione la forma de los caninos para predecir:")

    
    opciones_forma_caninos = list(mapeo_forma_caninos.keys())

    forma_caninos_seleccionada = st.selectbox("Seleccione la forma de los caninos:", opciones_forma_caninos)

    valor_numerico_forma_caninos = mapeo_forma_caninos.get(forma_caninos_seleccionada)

    st.write(f"El valor numérico correspondiente para '{forma_caninos_seleccionada}' es: {valor_numerico_forma_caninos}")

    codificador_etiquetas = LabelEncoder()


    
    st.write("Seleccione el tipo de migración:")


    opciones_migracion = ['Migrada', 'No Migrada'] 


    migracion_seleccionada = st.selectbox("Seleccione el tipo de migración:", opciones_migracion)

 
    codificador_etiquetas.fit(opciones_migracion)


    valor_numerico_migracion = codificador_etiquetas.transform([migracion_seleccionada])


    st.write(f"El valor transformado para '{migracion_seleccionada}' es: {valor_numerico_migracion}")



    tiempos = []
    locations=[]
    zone=[]
    habitat=[]
    capacidad_craneal=[]
    height=[]
    tamano_incisivos=[]
    forma_mandibula=[]
    prognatismo=[]
    forma_caninos=[]
    bipedos = []
    foramen = []
    torus=[]
    tecno = []
    tipo_tecno=[]
    dieta = []
    anatomia = []
    foots=[]
    arms=[]
    dimorfismo=[]
    cadera=[]
    esmalte_dental = []
    tamano_caninos = []
    vertical_front=[]
    migracion=[]
    
   
    tiempos.append(tiempo_seleccionado)
    locations.append(selected_location_encoded)
    zone.append(valor_numerico_zone)
    habitat.append(valor_numerico_habitat)
    capacidad_craneal.append(capacidad_craneal_seleccionada)
    height.append(altura_seleccionada)
    tamano_incisivos.append(valor_numerico_tamano_incisivos)
    forma_mandibula.append(valor_numerico_forma_mandibula)
    prognatismo.append(valor_numerico_prognatismo)
    bipedos.append(valor_numerico_biped)
    foramen.append(valor_numerico_foramen)
    torus.append(valor_numerico_torus)
    vertical_front = valor_numerico_vertical_frontal
    tecno.append(valor_numerico_tecno)
    tipo_tecno.append(valor_numerico_tipo_herramientas)
    dieta.append(valor_numerico_dieta)
    anatomia.append(valor_numerico_anatomia)
    foots.append(valor_numerico_tipo_pies)
    arms.append(valor_numerico_tipo_brazos)
    dimorfismo.append(valor_numerico_dimorfismo_sexual)
    cadera.append(valor_numerico_cadera)
    esmalte_dental.append(valor_numerico_esmalte)
    tamano_caninos.append(valor_numerico_caninos)
    forma_caninos.append(valor_numerico_forma_caninos)
    migracion.append(valor_numerico_migracion)


    df_respuestas = pd.DataFrame({
            'Time': tiempos,
            'Location_encoded':locations,
            'Zone_encoded':zone,
            'Habitat_encoded':habitat,
            'Cranial_Capacity':capacidad_craneal,
            'Height':height,
            'Incisor_Size_encoded':tamano_incisivos,
            'Jaw_Shape_encoded':forma_mandibula,
            'Torus_Supraorbital_encoded':torus,
            'Prognathism_encoded':prognatismo,
            'Foramen_encoded': foramen,
            'Canine_Size_encoded': tamano_caninos,
            'Canines_Shape_encoded':forma_caninos,
            'Tooth_Enamel_encoded': esmalte_dental,
            'Tecno_encoded': tecno,
            'tecno_type_mapping_encoded':tipo_tecno,
            'Biped_encoded': bipedos,
            'foots_encoded':foots,
            'arms_encoded':arms,
            'Diet_encoded': dieta,
            'Sexual_Dimorphism_encoded':dimorfismo,
            'Hip_encoded':cadera,
            'Vertical_Front_encoded':vertical_front,
            'Anatomy_encoded': anatomia,
            'Migrated_encoded':migracion
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
    #predicciones_proba=modelo.predic_proba(df_respuestas)
    etiquetas_prediccion = [especies[numero] for numero in predicciones]
    df_predicciones = pd.DataFrame({'Predicción clase': etiquetas_prediccion})
    
    df_predicciones.rename(columns={0: 'Predicción clase'}, inplace=True)
    st.write(df_predicciones)

if seleccion == 'Predicciones del Modelo':
    main()
    pass  
elif seleccion == 'Desempeño del Modelo':
    imagen_local = '../img/confusion_matrix.png'  # Cambia esto a la ruta de tu imagen
    st.title("Matriz de confusión del modelo")
    st.image(imagen_local, caption='Vemos el desempeño del modelo y su precisión actual clasificando etiquetas', use_column_width=True)
    df_feature_importances=pd.read_csv('../data/processed/df_feature_importances.csv')
    st.title('Importancia de las variables para el modelo')
    st.write(df_feature_importances)

    pass  
