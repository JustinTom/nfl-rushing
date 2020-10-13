#!/bin/bash
cd backend
docker build -t nfl-rushing-backend .

cd ../dashboard
docker build -t nfl-rushing-frontend .