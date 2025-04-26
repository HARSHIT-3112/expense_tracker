#!/bin/bash

# Add all changes
git add .

# Commit with a message
echo "Enter your commit message: "
read commit_message
git commit -m "$commit_message"

# Push to the current branch
git push origin $(git branch --show-current)

echo "✅ Code pushed successfully!"
