#!/usr/bin/env ruby

input_string = ARGV[0]

if input_string.nil?
  puts "Please provide the input string as a command-line argument."
  exit
end

matches = input_string.scan(/(?<=from:|to:|flags:)(\+?\w+)/)

if matches.empty?
  puts "No matches found."
else
  puts matches.join(",")
end
