pipeline {
    agent any
    
    stages {
        stage('Setup') {
            steps {
                // Create a virtual environment
                sh 'python3 -m venv myenv'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Activate virtual environment and install dependencies
                sh '''
                    source myenv/bin/activate
                    pip install -r requirement.txt
                '''
            }
        }
        
        /*stage('Run Python Script') {
            steps {
                // Activate virtual environment and run Python script
                sh '''
                    source myenv/bin/activate
                    python app.py
                '''
            }
        }*/
        
        stage('Run Tests') {
            steps {
                // Activate virtual environment and run tests
                sh '''
                    source myenv/bin/activate
                    python -m test_app.py
                '''
            }
        }
    }
    
    post {
        always {
            // Clean up: deactivate virtual environment
            sh 'deactivate || true'
        }
    }
}
