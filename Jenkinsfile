pipeline {
    agent { label 'linux-agent-170' }

    environment {
        IMAGE_TAR  = "django-ecommerce.tar"
        GIT_REPO   = "https://github.com/hnagpal-qasource/ecommerce-py.git"
        GIT_BRANCH = "test"
    }

    stages {
        stage('Checkout Source (on Agent)') {
            steps {
                sh '''
                  rm -rf src
                  git clone -b ${GIT_BRANCH} ${GIT_REPO} src
                '''
            }
        }
stage('Build Docker Image with Kaniko') {
    steps {
        sh '''
          cd src

docker run --rm \
  -v $(pwd):/workspace \
  gcr.io/kaniko-project/executor:debug \
  --context=/workspace \
  --dockerfile=/workspace/Dockerfile \
  --tar-path=/workspace/django-ecommerce.tar \
  --no-push

        '''
    }
}

        stage('Archive Image') {
            steps {
                sh 'mv src/${IMAGE_TAR} .'
                archiveArtifacts artifacts: '*.tar', fingerprint: true
            }
        }	
    }
}
