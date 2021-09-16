# IntegrationTesting
Code to do integration testing of the website : Sockshop project https://github.com/microservices-demo/microservices-demo

### stpes to run this project
- ``` git clone https://github.com/microservices-demo/microservices-demo ```
- ``` cd microservices-demo/deploy/docker-compose ```
- replace docker-compose.yml file and paste the locustfile.py in the same path .
- run the command : ``` docker-compose -f docker-compose.yml up -d ```
- log files will be generated in the path :  microservices-demo/deploy/docker-compose/integration_test_result.html
