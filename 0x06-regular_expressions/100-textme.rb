#!/usr/bin/env ruby

input = ARGV[0]

sender = input.scan(/(?<=from:)(\+?\w+)/).join
receiver = input.scan(/(?<=to:)(\+?\w+)/).join
flags = input.scan(/(?<=flags:)(\w+)/).join

puts "Sender: #{sender}"
puts "Receiver: #{receiver}"
puts "Flags: #{flags}"
