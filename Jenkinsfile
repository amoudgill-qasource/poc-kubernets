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
                    def commitId = sh(
                        script: 'git rev-parse --short HEAD',
                        returnStdout: true
                    ).trim()

                    env.IMAGE_TAG  = "${BRANCH_NAME}-${BUILD_NUMBER}-${commitId}"
                    env.IMAGE_TAR  = "${APP_NAME}-${IMAGE_TAG}.tar"
                    env.IMAGE_NAME = "${APP_NAME}:${IMAGE_TAG}"

                    sh '''
                      docker run --rm \
                        -v $(pwd):/workspace \
                        gcr.io/kaniko-project/executor:debug \
                        --context=/workspace \
                        --dockerfile=/workspace/Dockerfile \
                        --tar-path=/workspace/${IMAGE_TAR} \
                        --destination=${IMAGE_NAME} \
                        --no-push
                    '''
                }
            }
        }

        stage('Load Image into KIND') {
            steps {
                sh '''
                  kind load image-archive ${IMAGE_TAR} --name ${KIND_CLUSTER}
                '''
            }
        }
    }
}
