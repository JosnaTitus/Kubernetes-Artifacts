                                      Kubernetes Artifacts in Action

Problem Statement: 

      We can perform all the operation on kubernetes cluster using the artifacts. Artifacts are nothing but simple YAML POJO where we fill in the details and apply on kubernetes cluster. 
      You have to implement simple Web Application in any language you prefer and deploy that code on Kubernetes cluster using Artifacts. 
      
Expected Output: 

       When I will hit the URL  "http://<Minikube_IP>:<NODEPORT>/pucsd" in any browser I should get below things : 
       1. Current Time in IST
       2. IP Address 
       3. Hostname
       4.City
       5. Region
       6. Country
Steps to solve this Assignment: -
1. Pull the latest code i.e; Open terminal & type following command: -

          git clone https://github.com/JosnaTitus/DockerFile-MySQL.git
          
2. Go to the cloned folder: -
  
          cd  Kubernetes-Artifacts
          
3. Build Docker-Image using command: -

          docker build . -t test

4. To build development file in kubectl use command: -
      
          kubectl apply -f .
          
5. To check if our files are running use command: -

          kubectl get svc
          
6. To run our Python program: -

          python3 webapp.py
          
7. Run the API in the postman by hitting: -

          Open browser and write https://127.0.0.1:5080/pucsd
          
 


