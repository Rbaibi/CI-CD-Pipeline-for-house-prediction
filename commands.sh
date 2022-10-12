python3 -m venv ~/.myvenv

source ~/.myvenv/bin/activate

make install

pip install scikit-learn

pip install pandas

az webapp up --name flaskserverlesswebapp --resource-group Azuredevops --runtime "PYTHON:3.7"

./make_predict_azure_app.sh 
