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
- **Response**:
     - `201 OK`
          ```json
          {"message":"User registered successfully"}
          ```
     - `400 Error`
          ```json
          {"error":"Username or email already exists"}
          ```