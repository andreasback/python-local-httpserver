# Description:
python-local-httpserver allows you to package a built web application in a minimal way so that it can be tested on macOS by clicking on the run-local-server.command in finder without any external dependencies.

# Usage
Copy the files from your frontend project after running "npm build" or equivalent in the dist / build folder into the www folder.

The local server can then be started using run-local-server.command which will listen for connections at http://localhost:3000

The whole thing can then be packed into a zip file

# Details
src/python-localhost-server.py contains a minimal extension of http.server.SimpleHTTPRequestHandler that returns the content of /index.html (if available) instead of returning a HTTP 404 if the requested resource doesn't exist. This is typically whats needed for a SPA frontend to work if the user tries to go to a resource that's served by a router withing the application.
