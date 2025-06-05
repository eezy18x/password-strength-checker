#!/bin/bash

echo "🔐 Starting Password Strength Checker..."


for i in {1..3}; do
  echo -n "Running"
  for j in {1..3}; do
    echo -n "."
    sleep 0.3
  done
  echo
done

python3 password_checker.py
