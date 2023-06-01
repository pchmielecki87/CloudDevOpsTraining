#!/bin/bash

# Create directories
mkdir -p src/main/java/com/example
mkdir -p src/main/resources
mkdir -p src/test/java/com/example

# Create files
touch src/main/java/com/example/MyApp.java
touch src/test/java/com/example/MyAppTest.java
touch pom.xml

# Print directory structure
echo "Directory structure created:"
tree src
