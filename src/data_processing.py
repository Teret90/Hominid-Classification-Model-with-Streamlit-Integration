
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

# FORAMEN MAGNUM POSITION

foramen_mapping = {
    'posterior': 0,
    'semi-anterior': 1,
    'anterior': 2,
    'modern': 3
}

df2['Foramen_encoded'] = df2['Foramen_Mágnum_Position'].map(foramen_mapping)

# CANINE SIZE
canine_s_mapping = {
    'big': 0,
    'small': 1,

}

df2['Canine_Size_encoded'] = df2['Canine Size'].map(canine_s_mapping)

# CANINES SHAPE

canines_shape_mapping = {
    'conicalls': 0,  # más antigua
    'incisiform': 1  # más reciente
}

df2['Canines_Shape_encoded'] = df2['Canines_Shape'].map(canines_shape_mapping)

# TOOTH EMMEL

tooth_enamel_mapping = {
    'thick': 0,
    'thick-medium': 1,
    'medium-thick': 1,
    'thin': 2,
    'very thick': 0,
    'medium-thin': 1,
    'very thin': 2
}


df2['Tooth_Enamel_encoded'] = df2['Tooth_Enamel'].map(tooth_enamel_mapping)

# TECNO

tecno_mapping ={
    'no':0,
    'yes':2,
    'likely':1}
df2['Tecno_encoded'] = df2['Tecno'].map(tecno_mapping)

# TECNO TYPE

tecno_type_mapping = {
    'no': 0,
    'primitive': 1,
    'mode 1': 2,
    'mode 2': 3,
    'mode 3': 4,
    'mode 4': 5,
    
}

df2['tecno_type_mapping_encoded'] = df2['Tecno_type'].map(tecno_type_mapping)

# BIPED

biped_mapping = {
    'modern': 3,
    'high probability': 1,
    'yes': 2,
    'low probability': 0
}

df2['Biped_encoded'] = df2['biped'].map(biped_mapping)

# ARMS

arms_mapping = {
    'climbing': 0,
    'manipulate': 1,
    'manipulate with precision':2
}

df2['arms_encoded'] = df2['Arms'].map(arms_mapping)

# FOOTS

foots_mapping = {
    'climbing':0,
    'walk':1
}

df2['foots_encoded'] = df2['Foots'].map(foots_mapping)

# DIET

diet_mapping = {
    'carnivorous': 0,
    'omnivore': 1,
    'soft fruits': 2,
    'hard fruits': 3,
    'dry fruits': 4
}

df2['Diet_encoded'] = df2['Diet'].map(diet_mapping)

# SEXUAL DIMORPHISM

sexual_dimorphism_mapping = {
    'high': 0,
    'medium-high': 1,
    'reduced': 2
}

df2['Sexual_Dimorphism_encoded'] = df2['Sexual_Dimorphism'].map(sexual_dimorphism_mapping)


# HIP

hip_mapping = {
    'very modern': 3,
    'modern': 2,
    'wide': 1,
    'slim': 0
}

df2['Hip_encoded'] = df2['Hip'].map(hip_mapping)
### no creo que esta característica sea muy crucial y no se si esta bien etiquetada

# VERTICAL FRONT

vertical_front_mapping = {
    'modern': 2,
    'yes': 1,
    'no': 0
}

df2['Vertical_Front_encoded'] = df2['Vertical_Front'].map(vertical_front_mapping)

# ANATOMY

anatomy_mapping = {
    'old': 0,
    'mixed': 1,
    'modern': 2,
    'very modern': 3
}

df2['Anatomy_encoded'] = df2['Anatomy'].map(anatomy_mapping)

# MIGRATED

df2['Migrated_encoded'] = label_encoder.fit_transform(df2['Migrated'])

# SKELETON

skeleton_mapping = {
    'light':2, 
    'refined':1, 
    'robust':0
}

df2['Skeleton_encoded'] = df2['Skeleton'].map(skeleton_mapping)

# TARGET2, ESPECIES

especies = {
    'hominino Orrorin tugenencin':0,
    'hominino Sahelanthropus tchadensis': 1,
    'hominino Ardipithecus ramidus / kabadda':2,
    'Ardipithecus Ramidus / Kadabba':3,
    'Australopithecus Anamensis': 4,
    'Australopithecus Afarensis': 5,
    'Australopithecus Bahrelghazali':6,
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

df2['genero_especie_num'] = df2['Genus_&_Specie'].map(especies)

### df 

df_genus_encoded= df2[['Genus_&_Specie','genero_etiqueta','Time',
       'Location_encoded',
       'Zone_encoded', 'Habitat_encoded', 'Incisor_Size_encoded',
       'Jaw_Shape_encoded', 'Torus_Supraorbital_encoded',
       'Prognathism_encoded', 'Foramen_encoded', 'Canine_Size_encoded',
       'Canines_Shape_encoded', 'Tooth_Enamel_encoded', 'Tecno_encoded',
       'tecno_type_mapping_encoded', 'Biped_encoded', 'foots_encoded',
       'Diet_encoded', 'Sexual_Dimorphism_encoded', 'Hip_encoded',
       'Vertical_Front_encoded', 'Anatomy_encoded', 'Migrated_encoded','genero_especie_num']]




df_genus_encoded.to_csv('../data/processed/df_genus_encoded.csv',index=False)

### df para el modelo generalista

df= df2[['genero_etiqueta','Time',
       'Location_encoded',
       'Zone_encoded', 'Habitat_encoded', 'Incisor_Size_encoded',
       'Jaw_Shape_encoded', 'Torus_Supraorbital_encoded',
       'Prognathism_encoded', 'Foramen_encoded', 'Canine_Size_encoded',
       'Canines_Shape_encoded', 'Tooth_Enamel_encoded', 'Tecno_encoded',
       'tecno_type_mapping_encoded', 'Biped_encoded', 'foots_encoded',
       'Diet_encoded', 'Sexual_Dimorphism_encoded', 'Hip_encoded',
       'Vertical_Front_encoded', 'Anatomy_encoded', 'Migrated_encoded','genero_etiqueta_num','genero_especie_num']]

df.to_csv('../data/processed/df_encoded.csv',index=False)