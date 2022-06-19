# Recruitment tasks for Backen Django Developer

## Project overview
The project was created for the recruitment process for Hexocean. Task was to build REST API which allows user to upload images.
There are accounts tiers:
- basic
  - link to image thumbnail that's 200px in height
- premium
  - link to image thumbnail that's 200px in height
  - link to image thumbnail that's 400px in height
  - link to original image
- enterprise
  - everything above
  - ability to fetch a link to the binary image that expires after a numbers of seconds specified by user

## Installation

- Build docker containers `docker-compose build`
- Migrate `docker-compose run web python3 manage.py migrate`
- Load data `docker-compose run web python3 manage.py loaddata data.json`
- Run the container `docker-compose up`

## Using
- To access data you need to provide access token, which can be generated from ``