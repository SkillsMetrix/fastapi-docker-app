pipeline {
    agent any

    environment {
        IMAGE_NAME = "fastapi-demo"
        CONTAINER_NAME = "fastapi-container"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/SkillsMetrix/fastapi-docker-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run -d -p 8000:8000 --name $CONTAINER_NAME $IMAGE_NAME
                '''
            }
        }

    }

    post {
        success {
            echo "FastAPI deployed successfully!"
        }
    }
}