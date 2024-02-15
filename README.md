# Backend Developer Challenge

## Request statistics exercise

This exercise represents a fully functioning Flask application packaged into
a Docker Compose environment.

The Flask app counts every request by URL path and stores this metric in Redis.
This will form the basis of a component that has a wide range of uses like
request limiting, capacity planning, cost accounting, etc.

It handles the following sets of endpoints:
* `GET /api/*` - Simulated API endpoints
* `GET /stats/` - Returns JSON report of URL request statistics
* `POST /test/{number of requests}/` - Starts a test run to generate fake requests

## Spec

1. Record number of requests for every URL handled by the Flask application.  Data is stored in Redis.
1. The `/api/*` endpoint handles URL paths starting with `/api/` and followed by an arbitrary number of path segments. Example valid URLs: `/api/one/` or `/api/product/1/`. This is used to emulate what would be real API endpoints. For this exercise only `GET` requests are considered but assume there would be millions of unique URLs with different allowed methods. Query strings are ignored.
1. The `/stats/` endpoint returns a JSON response that provides the URL request counts ordered from most requested to least requested.
1. `/test/{number of requests}/` is a testing endpoint that simulates real requests:
   1. A `POST` request simulates a test of `{number of requests}` `GET` requests to the local web application
   1. Each simulated request uses a random URL composed of:
      1. `/api/` followed by 1 to 6 path segments
      1. Each path segment is a random string pulled from a pool of 3 random strings used by a single test run
      1. Example of URLs in a single test run:
         * `/api/xyz/` (Valid: 1 path segment, 1 random string used so far)
         * `/api/xyz/abc/def/` (Valid: 3 path segments, 3 random strings used so far)
         * `/api/xyz/abc/ghi/` (Invalid: 4 different random strings were used for path segments in this test run)
         * `/api/xyz/xyz/xyz/xyz/xyz/xyz/xyz/` (Invalid: 7 path segments)
1. The application is packaged into a fully functioning `docker-compose` project. To test we can run `docker-compose up` and point our local browser to `http://localhost:5000/stats/` to get the initial JSON report.