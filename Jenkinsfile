pipeline {
    agent any
    stages { 
        stage('Create_ENV') {
            steps {
                sh 'virtualenv venv'
                sh 'source venv/bin/activate'
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
