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

## Live preview
https://images-django.herokuapp.com

## Ready to use Postman Requests
https://www.postman.com/satellite-specialist-27423978/workspace/images/collection/18473958-6fc7ad6d-597d-4806-83d9-56e8a65e535e?ctx=documentation

## Using
- To access data you need to provide access token, which can be generated from `https://images-django.herokuapp.com/api/token/`
- User credentials:
  - Basic
    - username: ```basic_user```
    - password: ```Basic123```
  - Premium
    - username: ```premium_user```
    - password: ```Premium123```
  - Enterprise
   - username: ```enterprise_user```
    - password: ```Enterprise123**```
- API endpoints:
  - GET `/api/images`
    - List all images send by user
  - POST `/api/images`
    - Upload new image
  - GET `/api/images/<int:pk>`
    - Get information about image
  - GET `/api/images/<int:pk>/<int:seconds>`
    - Create temporary link to download image (if possible)
  - GET `/api/temprul/<int:pk>`
    - Download image from temporary url if possible