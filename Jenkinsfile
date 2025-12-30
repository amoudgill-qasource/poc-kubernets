pipeline {
    agent { label 'linux-agent-170' }

    environment {
        APP_NAME     = "django-ecommerce"
        KIND_CLUSTER = "develop-cluster"
    }

    stages {

        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        stage('Build Image with Kaniko') {
            steps {
                script {
                    int buildNum = BUILD_NUMBER.toInteger()
                    int major = buildNum / 10
                    int minor = buildNum % 10

                    env.IMAGE_TAG  = "${major}.${minor}"
                    env.IMAGE_NAME = "${APP_NAME}:${env.IMAGE_TAG}"

                    sh '''
                      docker run --rm \
                        -v $(pwd):/workspace \
                        -v /var/run/docker.sock:/var/run/docker.sock \
                        gcr.io/kaniko-project/executor:debug \
                        --context=/workspace \
                        --dockerfile=/workspace/Dockerfile \
                        --destination=${IMAGE_NAME} \
                        --no-push
                    '''
                }
            }
        }

        stage('Load Image into KIND') {
            steps {
                sh '''
                  kind load docker-image ${IMAGE_NAME} --name ${KIND_CLUSTER}
                '''
            }
        }
    }
}
