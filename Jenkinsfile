pipeline {
    agent any
    stages {
        stage('Set ut testing environment') {
            steps {
                sh '''
                    echo Install requirements
                    python3 -m venv venv
                    . venv/bin/activate
                    pip3 install -r requirements.txt
                    pip3 install --editable .

                    fuhub --help
                '''
            }
        }

        stage('Upload Python package') {
            environment {
                PYPI_ACCESS_TOKEN = credentials('naesheim-private-pypi')
                RELEASE = sh(script: 'test -n "$(git log -1 --pretty=oneline| awk \'/deploy/ {print $1}\')" && echo true || echo false',returnStdout: true)
            }
            when { expression { environment name: 'RELEASE', value: true } } 
            steps {
                sh '''
                    echo "only build when commit message include [deploy]
                    rm -rf dist
                    . venv/bin/activate
                    pip3 install twine wheel
                    python3 setup.py sdist bdist_wheel
                    python3 -m twine upload -u __token__ -p $PYPI_ACCESS_TOKEN dist/*
                '''
            }
        }
    }
}
