## IMPORTAMOS LAS LIBRERÍAS NECESARIAS

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import RandomizedSearchCV


# LEEMOS NUESTRO CSV DE NUESTRO DATAFRAME YA PROCESADO (FEATURE ENGIENEERING) PARA PODER ENTRENAR 

df= pd.read_csv('../data/processed/df_genus_encoded.csv')

# DIVIDIMOS EN TRAIN Y TEST PARA PODER COMPROBAR LAS MÉTRICAS DE NUESTRO MODELO CON TRAIN

train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# GUARDAMOS EN DOS CSV DIFERENTES

train_df.to_csv('../data/train/train2.csv', index=False)
test_df.to_csv('../data/test/test2.csv', index=False)

# LEEMOS EL ARCHIVOS DE TRAIN

df_train= pd.read_csv('../data/train/train2.csv')

# DECLARAMOS NUESTRA 'X' E 'Y' PARA ENTRENAR

X=df_train[['Time', 'Location_encoded',
       'Zone_encoded', 'Habitat_encoded','Cranial_Capacity','Height', 'Incisor_Size_encoded',
       'Jaw_Shape_encoded', 'Torus_Supraorbital_encoded',
       'Prognathism_encoded', 'Foramen_encoded', 'Canine_Size_encoded',
       'Canines_Shape_encoded', 'Tooth_Enamel_encoded', 'Tecno_encoded',
       'tecno_type_mapping_encoded', 'Biped_encoded', 'foots_encoded','arms_encoded',
       'Diet_encoded', 'Sexual_Dimorphism_encoded', 'Hip_encoded',
       'Vertical_Front_encoded', 'Anatomy_encoded', 'Migrated_encoded']]
y= df_train['genero_especie_num']

# PIPELINE DEL MEJOR MODELO Y ENTRENAMIENTO

steps = [
    ('scaler', StandardScaler()),
    ('pca', PCA()),
    ('classifier', RandomForestClassifier(random_state=42))
]

pipeline = Pipeline(steps)

param_dist = {
    'scaler': [StandardScaler()],
    'pca__n_components': [25],
    'classifier__n_estimators': [ 500],
    'classifier__max_depth': [5],
    'classifier__max_leaf_nodes': [18]
}


random_search = RandomizedSearchCV(pipeline, param_distributions=param_dist, cv=5, n_iter=10,n_jobs=-1, random_state=42,verbose= 2)


rs=random_search.fit(X, y)


best_score = random_search.best_score_
best_params = random_search.best_params_

print("Best Score:", best_score)
print("Best Parameters:", best_params)

be1=rs.best_estimator_.fit(X,y)


### GUARDAMOS EL MODELO CON PICKLE



filename = '../models/rf2_final.pkl'

with open(filename, 'wb') as archivo_salida:
    pickle.dump(be1, archivo_salida)