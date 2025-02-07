import os

def create_file(path, content=""):
    """Creates a file with the given content."""
    with open(path, "w") as f:
        f.write(content)

def create_project_structure(base_dir):
    directories = {
        "data/raw": ["creditcard.csv", "README.txt"],
        "data/processed": ["train.csv", "test.csv", "validation.csv", "README.txt"],
        "notebooks": ["01_eda.ipynb", "02_feature_engineering.ipynb", "03_model_training.ipynb", "04_model_evaluation.ipynb", "README.txt"],
        "src": ["data_preprocessing.py", "model_pipeline.py", "smote_augmentation.py", "train.py", "evaluate.py", "inference.py", "utils.py", "README.txt"],
        "models/saved_models": ["README.txt"],
        "models/model_logs": ["README.txt"],
        "configs": ["config.yaml", "model_params.json", "README.txt"],
        "reports": ["eda_report.html", "model_comparison.csv", "feature_importance.png", "README.txt"],
        "deployment/mlflow": ["README.txt"],
        "deployment/docker": ["README.txt"],
        "deployment/aws": ["README.txt"],
        "deployment/inference_api": ["README.txt"],
        "tests": ["test_data_preprocessing.py", "test_model_pipeline.py", "test_inference.py", "README.txt"],
        "logs": ["training_logs.log", "error_logs.log", "README.txt"],
        "environment": ["requirements.txt", "Dockerfile", "README.txt"],
    }
    

    for dir_path, files in directories.items():
        os.makedirs(os.path.join(base_dir, dir_path), exist_ok=True)
        for file in files:
            create_file(os.path.join(base_dir, dir_path, file))
    
    
    create_file(os.path.join(base_dir, "README.md"), "# Credit Card Fraud Detection\n\nProject description...")
    create_file(os.path.join(base_dir, ".gitignore"), "__pycache__/\n*.csv\n*.pkl\nlogs/")
    create_file(os.path.join(base_dir, "setup.py"), "from setuptools import setup\n\nsetup(name='credit_card_fraud_detection')")

if __name__ == "__main__":
    project_root = "credit_card_fraud_detection"
    create_project_structure(project_root)
    print(f"Project structure created under: {project_root}")