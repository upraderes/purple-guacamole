# prometheus sample

# Install prometheus on kube

Create monitoring namespace :
kubectl apply -f  ./monitoring-ns.yaml
kubectl apply -f  ./volume.yaml
kubectl apply -f ./cluster-role.yaml
kubectl apply -f ./service-account.yaml
kubectl apply -f ./cluster-role-binding.yaml
kubectl apply -f ./config/prom-configmap.yaml
kubectl apply -f ./prom-deployment.yaml


1. From source :

2. From dockerhub :

# Documentation :

https://prometheus.io/docs/prometheus/latest/getting_started/