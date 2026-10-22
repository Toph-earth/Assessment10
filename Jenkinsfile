pipeline{
  agent any{
    environment{
      DOCKER_IMAGE='bramag/disaster-relief'
      APP_DIR='set5'
      DEPLOYMENT_NAME='disaster-relief'
    }
    parameters{
      choice(
        name: 'ENVIRONMENT',
        choices:  ["dev", "stage", "prod"],
        description: "Select the deployment environment"
        )
    }
    stages{
      stage('Clone Code'){
        steps{
          git branch: 'main',
            url: ''
        }
      }
      stage('Build Docker image'){
        steps{
          sh 'docker build -t $DOCKER_IMAGE:$BUILD_NUMBER -t $DOCKER_IMAGE:latest $APP_DIR'
        }
      }
      stage('Push Image'){
        steps{
          withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')])
          sh 'docker login -u $DOCKER_USER -p $DOCKER_PASS'
          sh 'docker push $DOCKER_IMAGE:$BUILD_NUMBER'
          sh 'docker push $DOCKER_IMAGE:latest'
        }
      }
      stage('Deploy with Kubernetes'){
        steps{
          withCredentials([file(credentialsId:'kuberconfig', variable: 'KUBECONFIG')]){
          sh 'kubectl apply -f $APP_DIR/deployment.yaml --validate=false'
          sh 'kubectl run deployment/$DEPLOYMENT_NAME $DEPLOYMENT_NAME=$DOCKER_USER:$BUILD_NUMBER'
          sh 'kubectl rollout status deployment/$DEPLOYMENT_NAME --timeout=120s'
          }
        }
      }
      stage('Archive Artifacts'){
        steps{
          sh 'python3 report.py'
          archiveArtifacts artifact: 'report.txt', fingerprint: true
        }
    }
    post {
      failure {
        echo "Build failed. Rolling back $DEPLOYMENT_NAME"
        withCredentials([file(credentialsId:'kuberconfig', variable: 'KUBECONFIG')]){
          sh 'kubectl undo rollout deployment/$DEPLOYMENT_NAME || echo "Nothing to roll back"'
          sh 'kubectl rollout status deployment/$DEPLOYMENT_NAME --timeout=120s || true'
          }
      }
    }
  }
        
      
          
        
