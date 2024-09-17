# Streaming CSV

docker build -t stream-csv-app .

docker-compose up redis -d

docker-compose up zookeeper -d

docker-compose up kafka

docker-compose up kafdrop -d

docker-compose up app

http://localhost:8000/
