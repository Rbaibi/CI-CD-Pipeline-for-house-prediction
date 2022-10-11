git clone https://github.com/Rbaibi/CI-CD-Pipeline-for-house-prediction.git

cd CI-CD-Pipeline-for-house-prediction

python3 -m venv ~/.myvenv

source ~/.myvenv/bin/activate

make install

az webapp up --name flaskserverlesswebapp --resource-group Azuredevops --runtime "PYTHON:3.7"

./make_predict_azure_app.sh 
