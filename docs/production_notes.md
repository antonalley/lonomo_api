# TODO for production
Must only be accessible over https if using token authentication


to run on docker:
docker run -d -it -p 8000:8000 lonomo-api-app

to build on docker: 
docker build -t lonomo-api-app .

to see what's running:
docker ps -a