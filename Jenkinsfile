pipeline {
    agent { label 'linux-agent-170' }

    environment {
        APP_NAME     = "django-ecommerce"
        GIT_REPO     = "https://github.com/hnagpal-qasource/ecommerce-py.git"
        GIT_BRANCH   = "helm"
        KIND_CLUSTER = "develop-cluster"
    }

    stages {

        stage('Checkout Source') {
            steps {
                sh '''
                  rm -rf src
                  git clone -b ${GIT_BRANCH} ${GIT_REPO} src
                '''
            }
        }

        stage('Set Image Version') {
            steps {
                script {
                    def commitId = sh(
                        script: "cd src && git rev-parse --short HEAD",
                        returnStdout: true
                    ).trim()

                    env.IMAGE_TAG = "${GIT_BRANCH}-${BUILD_NUMBER}-${commitId}"
                    env.IMAGE_TAR = "${APP_NAME}-${IMAGE_TAG}.tar"
                    env.IMAGE_NAME = "${APP_NAME}:${IMAGE_TAG}"
                }
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
                    --tar-path=/workspace/${IMAGE_TAR} \
                    --destination=${IMAGE_NAME} \
                    --no-push
                '''
            }
        }

        stage('Load Image into KIND Cluster') {
            steps {
                sh '''
                  cd src
                  kind load image-archive ${IMAGE_TAR} --name ${KIND_CLUSTER}
                '''
            }
        }

        // stage('Archive Image Artifact') {
        //     steps {
        //         sh 'mv src/${IMAGE_TAR} .'
        //         archiveArtifacts artifacts: '*.tar', fingerprint: true
        //     }
        // }
    }
}
