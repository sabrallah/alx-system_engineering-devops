#!/usr/bin/env ruby

log_file = ARGV[0]

File.open(log_file, 'r') do |file|
  file.each_line do |line|
    match_data = line.match(/\[from:(\+\d+)\] \[to:(\+\d+)\] \[msg:\d+:(.*?)\]/)
    if match_data
      sender = match_data[1]
      recipient = match_data[2]
      message = match_data[3]
      puts "Sender: #{sender}"
      puts "Recipient: #{recipient}"
      puts "Message: #{message}"
      puts "------------------------"
    end
  end
end
