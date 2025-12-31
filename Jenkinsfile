pipeline {
    agent { label 'linux-agent-170' }

    environment {
        APP_NAME     = "sample-app"
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
                    env.IMAGE_TAR  = "${APP_NAME}-${env.IMAGE_TAG}.tar"
                    env.IMAGE_NAME = "${APP_NAME}:${env.IMAGE_TAG}"

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

        stage('Update Helm values.yaml Image Tag') {
            steps {
                sh '''
             
                git clone -b helm ssh://git@github.com/copperdevops/py-ecommerce-k8s.git
                sed -i "s/^\\s*tag:.*/  tag: ${IMAGE_TAG}/" \
                    py-ecommerce-k8s/helm/values.yaml

                echo "✅ Updated image tag in values.yaml:"
                grep -A2 "image:" py-ecommerce-k8s/helm/values.yaml

                '''
            }
        }

        stage('Commit & Push Helm Values Update') {
            steps {
                sh '''
                cd py-ecommerce-k8s

                # Ensure we are on helm branch
                git branch

                git add .

                # Commit only if there is a change
                if ! git diff --cached --quiet; then
                    git commit -m "chore: update image tag to ${IMAGE_TAG}"
                    git push origin helm
                else
                    echo "No changes to commit"
                fi
                '''
            }
        }
    }
}
