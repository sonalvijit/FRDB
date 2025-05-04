# API Endpoints

## Overview

This document outlines all available API endpoints for the project. Each endpoint includes the HTTP method, URL, description, parameters, example requests, and responses.

## Authentication

All API endpoints require an **Authorization** header with a valid Bearer token. To obtain a token, use the `/login` endpoint.

------

## Endpoints

### 1. **GET /register**
- **Description**: Register user
- **Method**: `POST`
- **Authentication**: Not required
- **Parameters**:
     - `username`
     - `email`
     - `password`
          ```json
          {
               "username":"<username>",
               "email":"<email>",
               "password":"<password>"
          }
          ```
- **Response**:
     - `201 OK`
          ```json
          {
               "message":"User registered successfully"
          }
          ```
     - `400 Error`
          ```json
          {
               "error":"Username or email already exists"
          }
          ```

### 2. **GET /login**
- **Description**: Login into application
- **Method**: `POST`
- **Authentication**: Not required (Will be authenticated later)
- **Parameters**:
     - `username`
     - `password`
          ```json
          {
               "username":"<username>",
               "password":"<password>"
          }
          ```
- **Response**:
     - `200 OK`
          ```json
          {
               "message":"User logged in successfully!"
          }
          ```
     - `400 Error`
          ```json
          {
               "error":"Something went wrong!"
          }
          ```

### 3. **GET /profile/(username)**
- **Description**: Get User info via username
- **Method**: `GET`
- **Authentication**: Not required
- **Parameters**: Not required
- **Response**:
     - `200 OK`
          ```json
          {
               "username":"<user.username>",
               "email":"<user.email>"
          }
          ```
     - `400 Error`
          ```json
          {
               "error":"Unable to find username"
          }
          ```

### 4. **GET /create_tweet**
- **Description**: Get User info via username
- **Method**: `GET`
- **Authentication**: Required (Session token will be allocated)
- **Parameters**:
     - `tweet`
          ```json
          {
               "tweet":"<tweet_content>"
          }
          ```
- **Response**:
     - `201 OK`
          ```json
          {
               "message":"tweet posted successfully!"
          }
          ```
     - `400 Error`
          ```json
          {
               "error":"Unable to tweet!"
          }
          ```