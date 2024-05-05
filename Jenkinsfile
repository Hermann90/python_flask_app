pipeline {
    agent any
    stages { 
        stage('Create_ENV') {
            steps {
                sh 'ls'
                sh 'pwd'
            }
        }

        stage('config requirement') {
            steps {
                sh 'pip3 install -r requirement.txt'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 app.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m test_app.py'
            }
        }
    }
}
