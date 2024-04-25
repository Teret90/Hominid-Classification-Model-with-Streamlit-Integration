import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from sklearn.preprocessing import LabelEncoder
from PIL import Image 


    # Creo una barra lateral para la navegación entre pestañas
st.sidebar.title('Navegación')
pestañas = ['Home','Predicciones del Modelo', 'Desempeño del Modelo']  
seleccion = st.sidebar.selectbox('Ir a:', pestañas)

# Muestro contenido de la pestaña seleccionada


min_time = 0.00052926
max_time = 7.6994172

#def transformar_tiempo(tiempo_seleccionado):
#
#    tiempo_transformado = tiempo_seleccionado  
#
#    return tiempo_transformado

def main():



    # TIEMPO
    st.title("Datación")
    st.write("Seleccione el tiempo en el que vivieron los homínidos:")

    tiempo_seleccionado = st.slider("Tiempo (en millones de años)", min_value=min_time, max_value=max_time, value=(min_time + max_time) / 2)

    #st.write(f"Tiempo seleccionado: {tiempo_seleccionado} millones de años")
    
    # UBICACIÓN:
    st.title("Localización")
    locations = ['Africa', 'Europa', 'Asia']

    selected_location = st.selectbox("Seleccione una localización:", locations)

    label_encoder = LabelEncoder()

    label_encoder.fit(locations)

    selected_location_encoded = label_encoder.transform([selected_location])[0]
    st.write("Localización seleccionada:")
    st.write(selected_location)


   # ZONA:
    st.title("Zona")
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

    # HÁBITAT

    habitat_mapping = {
    'Peninsular': 0,
    'Bosque-sabana': 0,
    'Selva': 1,
    'Bosque frío': 1,
    'Galería forestal': 1,
    'Bosque': 1,
    'Mixto': 2,
    'Sabana': 3
    }

    st.title("Hábitat")
    

    opciones_habitat = list(habitat_mapping.keys())

    habitat_seleccionado = st.selectbox("Seleccione el tipo de hábitat:", opciones_habitat)

    valor_numerico_habitat = habitat_mapping.get(habitat_seleccionado)
    
    st.write(f"El valor numérico correspondiente para '{habitat_seleccionado}' es: {valor_numerico_habitat}")

    # TIPO DE DIETA

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

    # MIGRACIÓN

    codificador_etiquetas = LabelEncoder()

    st.title("Migración")


    opciones_migracion = ['Migrada', 'No Migrada'] 


    migracion_seleccionada = st.selectbox("Seleccione si hubo o no migración:", opciones_migracion)

 
    codificador_etiquetas.fit(opciones_migracion)


    valor_numerico_migracion = codificador_etiquetas.transform([migracion_seleccionada])


    st.write(f"El valor transformado para '{migracion_seleccionada}' es: {valor_numerico_migracion}")

    #PROBABILIDAD DE USO DE TECNOLOGÍA

    tecno_mapping = {
    'No': 0,
    'Probable': 1,
    'Si': 2
    }

    st.title("Tecnología")

    opciones_tecno = list(tecno_mapping.keys())

    seleccion_tecno = st.selectbox("Selecciona la probabilidad de uso de tecnología:", opciones_tecno)

    valor_numerico_tecno = tecno_mapping.get(seleccion_tecno)

    st.write(f"El valor numérico correspondiente para '{seleccion_tecno}' es: {valor_numerico_tecno}")

    # TIPO DE HERRAMIENTAS

    mapeo_tipo_herramientas = {
    'no': 0,
    'primitivas': 1,
    'modo 1': 2,
    'modo 2': 3,
    'modo 3': 4,
    'modo 4': 5}

    st.title("Tipo de Herramientas")

    opciones_tipo_herramientas = list(mapeo_tipo_herramientas.keys())

    tipo_herramientas_seleccionado = st.selectbox("Seleccione el tipo de herramientas:", opciones_tipo_herramientas)

    valor_numerico_tipo_herramientas = mapeo_tipo_herramientas.get(tipo_herramientas_seleccionado)

    st.write(f"El valor numérico correspondiente para '{tipo_herramientas_seleccionado}' es: {valor_numerico_tipo_herramientas}")

    #ANATOMÍA

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

    # PROBABILIDAD DE BIPEDISMO

    biped_mapping = {
        'Baja probabilidad': 0,
        'Alta probabilidad': 1,
        'Si': 2,
        'Moderno':3
        }

    st.title("Bípedo")


    opciones_biped = ['Baja probabilidad', 'Alta probabilidad', 'Si', 'Moderno']

    seleccion_biped = st.selectbox("Selecciona la probabilidad de ser bípedo:", opciones_biped)

    valor_numerico_biped = biped_mapping.get(seleccion_biped)

    st.write(f"El valor numérico correspondiente para '{seleccion_biped}' es: {valor_numerico_biped}")

    # ALTURA
    min_altura = 80.00903
    max_altura = 184.98145

    
    st.title("Altura")
    

    
    altura_seleccionada = st.slider("Altura (en cm)", 
                                    min_value=min_altura, 
                                    max_value=max_altura, 
                                    value=(min_altura + max_altura) / 2)
    
    # PIES

    mapeo_tipo_pies = {
    'Escalada': 0,
    'Caminata': 1
    }

    st.title("Tipo de pies")
    

    opciones_tipo_pies = list(mapeo_tipo_pies.keys())

    tipo_pies_seleccionado = st.selectbox("Seleccione el tipo de pies:", opciones_tipo_pies)

    valor_numerico_tipo_pies = mapeo_tipo_pies.get(tipo_pies_seleccionado)

    st.write(f"El valor numérico correspondiente para '{tipo_pies_seleccionado}' es: {valor_numerico_tipo_pies}")

    # BRAZOS

    mapeo_tipo_brazos = {
    'Escalada': 0,
    'Manipulación': 1,
    'Manipulación con precisión': 2}

    st.title("Tipo de Brazos")

    opciones_tipo_brazos = list(mapeo_tipo_brazos.keys())

    tipo_brazos_seleccionado = st.selectbox("Seleccione el tipo de brazos:", opciones_tipo_brazos)

    valor_numerico_tipo_brazos = mapeo_tipo_brazos.get(tipo_brazos_seleccionado)

    st.write(f"El valor numérico correspondiente para '{tipo_brazos_seleccionado}' es: {valor_numerico_tipo_brazos}")

    # GRADO DIMORFISMO SEXUAL

    mapeo_dimorfismo_sexual = {
    'Alto': 0,
    'Medio-alto': 1,
    'Reducido': 2
    }

    st.title("Dimorfismo Sexual")

    opciones_dimorfismo_sexual = list(mapeo_dimorfismo_sexual.keys())
 
    dimorfismo_sexual_seleccionado = st.selectbox("Seleccione el grado de dimorfismo sexual:", opciones_dimorfismo_sexual)

    valor_numerico_dimorfismo_sexual = mapeo_dimorfismo_sexual.get(dimorfismo_sexual_seleccionado)

    st.write(f"El valor numérico correspondiente para '{dimorfismo_sexual_seleccionado}' es: {valor_numerico_dimorfismo_sexual}")

    # CADERA

    mapeo_cadera = {
    'Delgada': 0,
    'Ancho': 1,
    'Moderna': 2,
    'Muy moderna': 3
    }

    st.title("Tipo de cadera")

    opciones_cadera = list(mapeo_cadera.keys())

    cadera_seleccionada = st.selectbox("Seleccione el tipo de cadera:", opciones_cadera)

    valor_numerico_cadera = mapeo_cadera.get(cadera_seleccionada)
    
    st.write(f"El valor numérico correspondiente para '{cadera_seleccionada}' es: {valor_numerico_cadera}")



    # CAPACIDAD CRANEAL
    min_capacidad_craneal = 0.07491
    max_capacidad_craneal = 1448.39747

    st.title("Capacidad craneal")
    
    capacidad_craneal_seleccionada = st.slider("Seleccione la capacidad craneal (en cm³)", 
                                           min_value=min_capacidad_craneal, 
                                           max_value=max_capacidad_craneal, 
                                           value=(min_capacidad_craneal + max_capacidad_craneal) / 2)
    
    # GRADO DE PROGNATISMO

    mapeo_prognatismo = {
    'Ausente': 5,
    'Reducido': 4,
    'Medio': 3,
    'Medio-alto': 2,
    'Alto': 1,
    'Muy alto': 0
    }

    st.title("Grado de Prognatismo")

    opciones_prognatismo = list(mapeo_prognatismo.keys())


    prognatismo_seleccionado = st.selectbox("Seleccione el grado de prognatismo:", opciones_prognatismo)

    valor_numerico_prognatismo = mapeo_prognatismo.get(prognatismo_seleccionado)

    st.write(f"El valor numérico correspondiente para '{prognatismo_seleccionado}' es: {valor_numerico_prognatismo}")



    # POSICIÓN DEL FORÁMEN MÁGNUM

    foramen_mapping = {
        'Posterior': 0,
        'Semi-anterior': 1,
        'Anterior': 2,
        'Moderno': 3
    }


    st.title("Posición del Foramen mágnum")

    opciones_foramen = list(foramen_mapping.keys())

    seleccion_foramen = st.selectbox('Seleccione la posición del Foramen mágnum:', opciones_foramen)

    valor_numerico_foramen = foramen_mapping.get(seleccion_foramen)

    st.write(f"El valor numérico correspondiente para '{seleccion_foramen}' es: {valor_numerico_foramen}")

    # GRADO DE PROTUBERANCIA DEL TORUS SUPRAORBITAL

    torus_supraorbital_mapping = {
    'Ultra Protuberante':0,
    'Muy Protuberante':1,
    'Menos Protuberante':2,
    'Poco Protuberante':3,
    'Plano':4
    }

    st.title("Grado de protuberancia del Torus Supraorbital")
    

    opciones_torus = list(torus_supraorbital_mapping.keys())

    seleccion_torus = st.selectbox("Selecciona el tipo de Torus Supraorbital:", opciones_torus)

    valor_numerico_torus = torus_supraorbital_mapping.get(seleccion_torus)

    st.write(f"El valor numérico correspondiente para '{seleccion_torus}' es: {valor_numerico_torus}")

    # VERTICALIDAD FRONTAL
    mapeo_vertical_frontal = {
    'No': 0,
    'Sí': 1,
    'Moderna': 2,
    }
    
    st.title("Selección de Verticalidad Frontal")

    opciones_vertical_frontal = list(mapeo_vertical_frontal.keys())

    vertical_frontal_seleccionada = st.selectbox("Seleccione el tipo de verticalidad frontal:", opciones_vertical_frontal)

    valor_numerico_vertical_frontal = mapeo_vertical_frontal.get(vertical_frontal_seleccionada)

    st.write(f"El valor numérico correspondiente para '{vertical_frontal_seleccionada}' es: {valor_numerico_vertical_frontal}")

    # FORMA MANDÍBULA

    mapeo_forma_mandibula = {
    'Forma de V': 1,
    'Moderna': 2,
    'Forma de U': 3,   
    'Cónica': 4
    }


    st.title("Forma de la Mandíbula")

    opciones_forma_mandibula = list(mapeo_forma_mandibula.keys())

    forma_mandibula_seleccionada = st.selectbox("Seleccione la forma de la mandíbula:", opciones_forma_mandibula)

    valor_numerico_forma_mandibula = mapeo_forma_mandibula.get(forma_mandibula_seleccionada)

    st.write(f"El valor numérico correspondiente para '{forma_mandibula_seleccionada}' es: {valor_numerico_forma_mandibula}")
    
    
    # TAMAÑO INCISIVOS
    mapeo_tamano_incisivos = {
    'Muy pequeño': 1,
    'Pequeño': 2,
    'Mediano grande': 3,
    'Grande': 4,
    'Megadoncia': 5
    }

 
    st.title("Tamaño de incisivos")

    opciones_tamano_incisivos = list(mapeo_tamano_incisivos.keys())

    tamano_incisivos_seleccionado = st.selectbox("Seleccione el tamaño de incisivos:", opciones_tamano_incisivos)

    valor_numerico_tamano_incisivos = mapeo_tamano_incisivos.get(tamano_incisivos_seleccionado)
   
    st.write(f"El valor numérico correspondiente para '{tamano_incisivos_seleccionado}' es: {valor_numerico_tamano_incisivos}")



    # TAMAÑO DE LOS CANINOS
    
    canine_s_mapping = {
    'Grande': 0,
    'Pequeño': 1
    }

    st.title("Tamaño de los Caninos")

    opciones_caninos = list(canine_s_mapping.keys())
 
    seleccion_tamaño_caninos = st.selectbox("Selecciona el tamaño de los caninos:", opciones_caninos)

    valor_numerico_caninos = canine_s_mapping.get(seleccion_tamaño_caninos)

    st.write(f"El valor numérico correspondiente para '{seleccion_tamaño_caninos}' es: {valor_numerico_caninos}")

    # FORMA DE LOS CANINOS

    mapeo_forma_caninos = {
    'Cónicos': 0,       # más antigua
    'Incisiformes': 1   # más reciente
    }

    st.title("Selección de Forma de los Caninos")
 
    opciones_forma_caninos = list(mapeo_forma_caninos.keys())

    forma_caninos_seleccionada = st.selectbox("Seleccione la forma de los caninos:", opciones_forma_caninos)

    valor_numerico_forma_caninos = mapeo_forma_caninos.get(forma_caninos_seleccionada)

    st.write(f"El valor numérico correspondiente para '{forma_caninos_seleccionada}' es: {valor_numerico_forma_caninos}")

    # GROSOR DEL ESMALTE DENTAL
  
    tooth_enamel_mapping = {
        'Muy grueso': 0,
        'Grueso': 0,
        'Medio-grueso': 1,
        'Medio-fino': 1,
        'Fino': 2,
        'Muy fino': 2 
    }

    st.title("Datos sobre el esmalte dental")

    opciones_esmalte = list(tooth_enamel_mapping.keys())

  
    seleccion_esmalte_dental = st.selectbox("Selecciona el grosor del esmalte dental:", opciones_esmalte)

    valor_numerico_esmalte = tooth_enamel_mapping.get(seleccion_esmalte_dental)

    
    st.write(f"El valor numérico correspondiente para '{seleccion_esmalte_dental}' es: {valor_numerico_esmalte}")


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
    
    imagenes_prediccion = {
    'Hominino Sahelanthropus tchadensis': '../img/Hominino_Sahelanthropus_tchadensis.png',
    'Hominino Orrorin tugenencin': '../img/Hominino_Orrorin_tugenencin.png',
    'Hominino Ardipithecus ramidus / kabadda':'../img/Hominino_Ardipithecus_ramidus_kabadda.png',
    'Ardipithecus Ramidus / Kadabba':'../img/Ardipithecus_Ramidus_Kadabba.png',
    'Australopithecus Anamensis':'../img/Australopithecus_Anamensis.png',
    'Australopithecus Afarensis':'../img/Australophitecus_afarensis.png',
    'Australopithecus Bahrelghazali':'../img/Australopithecus_Bahrelghazali.png',
    'Australopithecus Africanus':'../img/Australopithecus_Africanus.png',
    'Australopithecus Garhi':'../img/Australopithecus_Garhi.png',
    'Australopithecus Sediba':'../img/Australopithecus_Sediba.png',
    'Paranthropus Aethiopicus':'../img/Australopithecus_Aethiopicus.png',
    'Paranthropus Robustus':'../img/Paranthropus_Robustus.png',
    'Paranthropus Boisei':'../img/Paranthropus_Boisei.png',
    'Homo Habilis':'../img/Homo_Habilis.png',
    'Homo Rudolfensis':'../img/Homo_Rudolfensis.png',
    'Homo Georgicus':'../img/Homo_Georgicus.png',
    'Homo Ergaster':'../img/Homo_Ergaster.png',
    'Homo Erectus':'../img/Homo_Erectus.png',
    'Homo Naledi':'../img/Homo_Naledi.png',
    'Homo Floresiensis':'../img/Homo_Florensis.png',
    'Homo Antecesor':'../img/Homo_Antecesor.png',
    'Homo Heidelbergensis':'../img/Homo_Heidelbergensis.png',
    'Homo Rodhesiensis':'../img/Homo_Rodhesiensis.png',
    'Homo Neanderthalensis':'../img/Homo_Neanderthalensis.png',
    'Homo Sapiens':'../img/Homo_Sapiens.png'
    }
    
    st.title('Predicciones del Modelo:')
    predicciones = modelo.predict(df_respuestas)
    #predicciones_proba=modelo.predic_proba(df_respuestas)
    etiquetas_prediccion = [especies[numero] for numero in predicciones]
    df_predicciones = pd.DataFrame({'Predicción clase': etiquetas_prediccion})
    
    df_predicciones.rename(columns={0: 'Predicción clase'}, inplace=True)
    st.write(df_predicciones)

    for prediccion in etiquetas_prediccion:
        imagen_p = imagenes_prediccion.get(prediccion, 'imagen_predeterminada.jpg')
        st.image(imagen_p, caption=f'Imagen para la clase: {prediccion}')

if seleccion == 'Home':
    st.title("Evolución humana:")
    st.title(" Modelo Clasificación de Homínidos fósiles.\n")

    imagen_path = "../img/img1.png"  
    def cargar_imagen(imagen_path):
        st.image(imagen_path, caption='Clasificación de homínidos.Fuente: https://www.museoevolucionhumana.com/media/files/Evolucion.pdf', use_column_width=True)

        
    cargar_imagen(imagen_path)


elif seleccion == 'Predicciones del Modelo':
    main()
    pass  
elif seleccion == 'Desempeño del Modelo':
    imagen_local = '../img/output.png'
    imagen_local2 = '../img/output18.png'
    imagen_local3='../img/output2.png'
    st.title("Matriz de confusión del modelo")
    st.image(imagen_local, caption='Vemos el desempeño del modelo y su precisión actual clasificando etiquetas', use_column_width=True)
    st.image(imagen_local2, caption='Porcentaje de varianza acumulada explicada', use_column_width=True)
    st.title('Importancia de las variables para el modelo')
    st.image(imagen_local3, caption='Porcentaje de varianza acumulada explicada', use_column_width=True)
    st.title('Importancia de los componentes por la varianza acumulada explicada')
    
    
    pass  
