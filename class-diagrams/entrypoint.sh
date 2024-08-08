#!/bin/bash

current_time=$(date -u +%Y-%m-%dT%H:%M:%SZ)

ls -l >> $LOG_FILE

if [ -z "$1" ]; then
    echo "$current_time - No input file provided." >> error.log
    exit 1
fi

INPUT_FILE=$1

if [ ! -f "$INPUT_FILE" ]; then
    echo "$current_time - File of name $INPUT_FILE not found." >> error.log
    exit 1
fi

execute_status=$(java -jar /usr/src/diagrams/plantuml.jar "$INPUT_FILE" 2>&1)

if [ $? -ne 0 ]; then
    echo "$current_time - Failed to generate diagram from $INPUT_FILE. See error details: $execute_status" >> error.log
    exit 1
fi