pipeline {
    agent any

    environment {
        IMAGE_NAME = "fastapi-demo"
        CONTAINER_NAME = "fastapi-container"
        PORT = "8000"
    }

    stages {

        stage('Verify Docker') {
            steps {
                bat 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image..."
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }

        stage('Stop Existing Container') {
            steps {
                echo "Stopping old container if running..."
                bat 'docker stop %CONTAINER_NAME% || exit 0'
                bat 'docker rm %CONTAINER_NAME% || exit 0'
            }
        }

        stage('Run Container') {
            steps {
                echo "Starting FastAPI container..."
                bat 'docker run -d -p %PORT%:8000 --name %CONTAINER_NAME% %IMAGE_NAME%'
            }
        }

        stage('Verify Container') {
            steps {
                bat 'docker ps'
            }
        }
    }

    post {

        success {
            echo "FastAPI deployed successfully!"
            echo "Access application: http://localhost:8000"
            echo "Swagger docs: http://localhost:8000/docs"
        }

        failure {
            echo "Pipeline failed. Check console logs."
        }
    }
}
