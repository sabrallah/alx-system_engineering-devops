#!/usr/bin/env ruby

# Accept the argument passed to the script
input = ARGV[0]

# Use the regular expression to match "School"
regex = /School/

# Check if the input matches the regular expression
if input.match?(regex)
  puts input
end
