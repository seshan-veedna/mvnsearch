# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from app import mvn
import json

# Press the green button in the gutter to run the script.

#for log4j 2.x version
output = mvn.get_purl("org.apache.logging.log4j","log4j-core")
print(json.dumps(output))

#for log4j 1-x version
output=mvn.get_purl("log4j","log4j")
print(json.dumps(output))

#https://search.maven.org/classic/remotecontent?filepath=org/apache/logging/log4j/log4j/2.17.0/log4j-2.17.0.pom