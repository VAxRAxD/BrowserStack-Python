pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/VAxRAxD/BrowserStack-Python.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Test Script') {
            steps {
                browserstack(credentialsId: "7b09dd74-8599-46a2-9007-852fb6e12b8c") {
                    sh '''
                        cd automate/
                        python3 single.py
                    '''
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}