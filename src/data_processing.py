
#### IMPORTAMOS LAS LIBRERÍAS NECESARIAS

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

#### LEEMOS NUESTRO DATASET Y LO DECLARAMOS EN UNA VARIABLE:

df2=pd.read_csv('../data/raw/Evolution_DataSets.csv')


#### FEATURE ENGINEERING


# CLASIFICACIÓN GENÉRICA DE HOMINIDOS
grupo_homínidos = {
    'Australopithecus Afarensis': 'Australopithecus',
    'Australopithecus Africanus': 'Australopithecus',
    'Australopithecus Anamensis': 'Australopithecus',
    'Australopithecus Bahrelghazali': 'Australopithecus',
    'Australopithecus Garhi': 'Australopithecus',
    'Australopithecus Sediba': 'Australopithecus',
    'Paranthropus Aethiopicus': 'Paranthropus',
    'Paranthropus Boisei': 'Paranthropus',
    'Paranthropus Robustus': 'Paranthropus',
    'Homo Habilis': 'Homo temprano',
    'Homo Georgicus': 'Homo temprano',
    'Homo Ergaster': 'Homo temprano',
    'Homo Erectus': 'Homo temprano',
    'Homo Rudolfensis': 'Homo temprano',
    'Homo Antecesor': 'Homo temprano',
    'Homo Heidelbergensis': 'Homo temprano',
    'Homo Neanderthalensis\n': 'Homo tardío',
    'Homo Rodhesiensis': 'Homo tardío',
    'Homo Sapiens': 'Homo tardío',
    'Homo Floresiensis': 'Otros',
    'Homo Naledi': 'Otros',
    'Ardipithecus Ramidus / Kadabba': 'Hominios',
    'hominino Sahelanthropus tchadensis': 'Homininos',
    'hominino Orrorin tugenencin': 'Homininos',
    'hominino Ardipithecus ramidus / kabadda': 'Homininos',
}

df2['genero_etiqueta'] = df2['Genus_&_Specie'].map(grupo_homínidos)


grupo_homínidos_num = {
    'Homininos':0,
    'Australopithecus':1,
    'Paranthropus':2,
    'Homo temprano':3,
    'Homo tardío':4,
    'Otros':5,
}

df2['genero_etiqueta_num'] = df2['genero_etiqueta'].map(grupo_homínidos_num)


#LOCATION

label_encoder = LabelEncoder()
df2['Location_encoded'] = label_encoder.fit_transform(df2['Location'])


# ZONE

df2['Zone_encoded'] = label_encoder.fit_transform(df2['Zone'])

#HABITAT

habitat_frequencies = df2['Habitat'].value_counts(normalize=True)

habitat_encoded = df2['Habitat'].map(habitat_frequencies)
df2['Habitat_encoded'] = habitat_encoded

# INCISOR SIZE

incisor_size_mapping = {
    'very small': 1,
    'small': 2,
    'medium large': 3,
    'big': 4,
    'megadony': 5
}

df2['Incisor_Size_encoded'] = df2['Incisor_Size'].map(incisor_size_mapping)

# JAW SHAPE

jaw_shape_mapping = {
    'conical': 4,
    'U shape': 3,
    'modern': 2,
    'V shape': 1
}

df2['Jaw_Shape_encoded'] = df2['Jaw_Shape'].map(jaw_shape_mapping)

# TORUS SUPRAORBITAL

torus_supraorbital_mapping = {
    'ultra protruding': 0,
    'very protruding': 1,
    'less protruding': 2,
    'little protruding': 3,
    'flat': 4
}

df2['Torus_Supraorbital_encoded'] = df2['Torus_Supraorbital'].map(torus_supraorbital_mapping)

# PROGNATHISM

prognathism_mapping = {
    'absent': 5,
    'reduced': 4,
    'medium': 3,
    'medium-high': 2,
    'high': 1,
    'very high': 0
}

df2['Prognathism_encoded'] = df2['Prognathism'].map(prognathism_mapping)