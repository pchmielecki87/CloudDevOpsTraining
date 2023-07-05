#initial
gcloud auth list
gcloud config set project <project-name>

#1
gcloud config set compute/region us-east1
gcloud config set compute/zone us-east1-b
gcloud compute instances create <instance-name> --machine-type f1-micro --zone us-east1-b

#2
gcloud container clusters create --machine-type=f1-micro <cluster-name> --zone us-east1-b
gcloud container clusters get-credentials <cluster-name> 
kubectl create deployment hello-app --image=gcr.io/google-samples/hello-app:2.0
kubectl expose deployment hello-app --type=LoadBalancer --port 8080 
kubectl get service