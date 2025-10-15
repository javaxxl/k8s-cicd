pipeline {
    agent any

    stages {
        stage('Build & Load Image') {
            steps {
                script {
                    def imageName = "hello-app"
                    def imageTag = "v${env.BUILD_NUMBER}"
                    
                    echo "Building image: ${imageName}:${imageTag}"
                    sh "docker build -t ${imageName}:${imageTag} ./src"
                    
                    echo "Loading image into cluster nodes..."
                    sh "docker save ${imageName}:${imageTag} | sudo ctr -n=k8s.io image import -"
                    sh "docker save ${imageName}:${imageTag} | multipass exec kafka-1 --  ctr -n=k8s.io image import -"
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'k8s-config', variable: 'KUBECONFIG')]) {
                    script {
                        def imageName = "hello-app"
                        def imageTag = "v${env.BUILD_NUMBER}"
                        
                        echo "Deploying image: ${imageName}:${imageTag}"
                        sh "kubectl set image deployment/hello-deployment hello-app=${imageName}:${imageTag}"
                        
                        echo "Verifying deployment rollout..."
                        sh "kubectl rollout status deployment/hello-deployment"
                    }
                }
            }
        }
    }
}