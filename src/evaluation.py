# IMPORTAMOS LAS LIBRERIAS NECESARIAS

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import os

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score



# IMPORTAMOS NUESTRO MODELO CON PICKLE

filename = '../models/rf2_final.pkl'

with open(filename, 'rb') as archivo_entrada:
    rf1 = pickle.load(archivo_entrada)


# LEEMOS NUESTRO DATASET DE TEST PARA SACAR LAS PREDICCIONES Y LAS MÉTRICAS

df_test= pd.read_csv('../data/test/test2.csv')

# DECLARAMOS LA 'X' E 'Y' DEL TEST

X1=df_test[['Time','Biped_encoded','Foramen_encoded','Torus_Supraorbital_encoded','Tecno_encoded','Diet_encoded','Anatomy_encoded','Location_encoded','Tooth_Enamel_encoded','Canine_Size_encoded']]
y1= df_test['genero_especie_num']

# HACEMOS UNA LISTA QUE SERVIRÁ PARA PONER LAS ETIQUETAS DE LA CONFUSION MATRIX

nombres_hominidos = {
    'hominino Orrorin tugenencin': 0,
    'hominino Sahelanthropus tchadensis': 1,
    'hominino Ardipithecus ramidus / kabadda': 2,
    'Ardipithecus Ramidus / Kadabba': 3,
    'Australopithecus Anamensis': 4,
    'Australopithecus Afarensis': 5,
    'Australopithecus Bahrelghazali': 6,
    'Australopithecus Africanus': 7,
    'Australopithecus Garhi': 8,
    'Australopithecus Sediba': 9,
    'Paranthropus Aethiopicus': 10,
    'Paranthropus Robustus': 11,
    'Paranthropus Boisei': 12,
    'Homo Habilis': 13,
    'Homo Rudolfensis': 14,
    'Homo Georgicus': 15,
    'Homo Ergaster': 16,
    'Homo Erectus': 17,
    'Homo Naledi': 18,
    'Homo Floresiensis': 19,
    'Homo Antecesor': 20,
    'Homo Heidelbergensis': 21,
    'Homo Rodhesiensis': 22,
    'Homo Neanderthalensis\n': 23,
    'Homo Sapiens': 24   
}

lista_nombres_hominidos = list(nombres_hominidos.keys())

# HACEMOS NUESTRAS PREDICCIONES Y_PRED ,Y_PRED_PROBA

y_pred_rf_pca_test1_2=rf1.predict(X1)
y_pred_rf_pca_test1_pproba_2 = rf1.predict_proba(X1)


# SACAMOS LAS MÉTRICAS PARA EVALUAR NUESTRO MODELO SOBRE TEST

precision2 = precision_score(y1, y_pred_rf_pca_test1_2,average='weighted')
recall2 = recall_score(y1, y_pred_rf_pca_test1_2,average='weighted')
f12 = f1_score(y1, y_pred_rf_pca_test1_2,average='weighted')
accuracy2=accuracy_score(y1,y_pred_rf_pca_test1_2)

roc_auc2= roc_auc_score(y1,y_pred_rf_pca_test1_pproba_2,average='weighted',multi_class='ovo')
print("Precision:", precision2)
print("Recall:", recall2)
print("F1-score:", f12)
print('ROC AUC score:', roc_auc2)
print('Accuracy',accuracy2)



plt.figure(figsize=(15,15))
c_matrix1 = confusion_matrix(y1,y_pred_rf_pca_test1_2)
print(c_matrix1)
sns.heatmap(c_matrix1, annot=True,fmt= 'd')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.xticks(rotation=90)
plt.xticks(range(len(lista_nombres_hominidos)), lista_nombres_hominidos)
plt.yticks(rotation=360)
plt.yticks(range(len(lista_nombres_hominidos)), lista_nombres_hominidos)
plt.title('Confusion Matrix: rendimiento del Modelo')


carpeta_imagenes = "../img/"
if not os.path.exists(carpeta_imagenes):
    os.makedirs(carpeta_imagenes)

# Nombre del archivo de la figura
nombre_figura = "confusion_matrix.png"

# Guardar la figura en la carpeta de imágenes
ruta_figura = os.path.join(carpeta_imagenes, nombre_figura)
plt.savefig(ruta_figura)