#!/bin/bash

# variables
pre_commit=".git/hooks/pre-commit"
pre_push=".git/hooks/pre-push"

# pre-commit
if [ ! -f $pre_commit ]
then
    echo "make all" > $pre_commit && chmod +x $pre_commit
fi

# pre-push
if [ ! -f $pre_push ]
then
    echo "make all" > $pre_push && chmod +x $pre_push
fi