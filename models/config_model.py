
import yaml

# Mejores parámetros obtenidos
best_params = {
    'scaler': None,
    'pca__n_components': 8,
    'classifier__n_estimators': 500,
    'classifier__max_depth': 6,
    'classifier__max_leaf_nodes': 18
}

file_path = 'best_params.yaml'

# Guardar los mejores parámetros en un archivo YAML
with open(file_path, 'w') as file:
    yaml.dump(best_params, file)