pipeline {
    agent any
    stages {
        stage('checkout') {
            steps{
                git branch: 'dev', url: 'https://github.com/hkm7/calculator-application/'
                sh "ls -al"
            }
        }
        stage('build'){
            steps{
                sh "pip install -r requirements.txt --break-system-packages"
            }
            
        }
        stage('Test'){
            steps{
                sh "python3 test.py"
            }
            
        }
        stage('deploy'){
            steps{
                sh "python3 app.py" 
            }
        }
    }
    post {
            success{
                    echo "Build completed successully"
            }
            always {
                echo "marker for EOF"
            }
            failure{
                echo "Build failed"
            }
        } 
}
