pipeline {
  agent { docker { image "python:3.8-alpine" }}
  stages {
    stage('Build') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh 'pip install -r requirements.txt --user'
          sh 'python coronaService.py & sleep 3'
        }
      }
    }
    stage('Test') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh 'python test.py ${country}'
        }  
      }
    }
  }
}
