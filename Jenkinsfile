pipeline {
    agent any

    environment {
        APP_NAME        = "django-app"
        KIND_CLUSTER    = "dev-cluster"
        OCTOPUS_SERVER  = "http://host.docker.internal:8083"
        OCTOPUS_SPACE   = "Default"
        OCTOPUS_PROJECT = "Projects-1"
        OCTOPUS_ENV     = "Development"
        OCTOPUS_API_KEY = credentials('octopus-api-key')
    }

    stages {

        stage('Clean Workspace') {
            steps { cleanWs() }
        }

        stage('Checkout Source') {
            steps { checkout scm }
        }

        stage('Build Image') {
            steps {
                script {
                    env.IMAGE_TAG = "v2"   // 🔥 FIXED (match Helm)

                    sh '''
                      docker build -t ${APP_NAME}:${IMAGE_TAG} .
                    '''
                }
            }
        }

        stage('Load Image into KIND') {
            steps {
                sh '''
                  kind load docker-image ${APP_NAME}:${IMAGE_TAG} --name ${KIND_CLUSTER}
                '''
            }
        }

        stage('Update Helm values.yaml') {
            steps {
                withCredentials([string(credentialsId: 'amoudgill-qasource', variable: 'GIT_TOKEN')]) {
                    sh '''
                      rm -rf poc-kubernets

                      git clone -b helm https://${GIT_TOKEN}@github.com/amoudgill-qasource/poc-kubernets.git
                      cd poc-kubernets

                      sed -i 's/^\\s*tag:.*/  tag: "'${IMAGE_TAG}'"/' helm/values.yaml

                      git config user.email "jenkins@local"
                      git config user.name "Jenkins"

                      git add helm/values.yaml
                      git commit -m "Update image tag to ${IMAGE_TAG}" || echo "No changes"
                      git push origin helm
                    '''
                }
            }
        }

        stage('Octopus Login') {
            steps {
                sh '''
                  octopus login \
                    --server ${OCTOPUS_SERVER} \
                    --api-key ${OCTOPUS_API_KEY}
                '''
            }
        }

        stage('Create Release') {
            steps {
                sh '''
                  octopus release create \
                    --project ${OCTOPUS_PROJECT} \
                    --version ${IMAGE_TAG} \
                    --space ${OCTOPUS_SPACE} \
                    --no-prompt
                '''
            }
        }

        stage('Deploy to Dev') {
            steps {
                sh '''
                  octopus release deploy \
                    --project ${OCTOPUS_PROJECT} \
                    --version ${IMAGE_TAG} \
                    --environment ${OCTOPUS_ENV} \
                    --space ${OCTOPUS_SPACE} \
                    --no-prompt
                '''
            }
        }
    }
}
