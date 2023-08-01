#!/usr/bin/env ruby

# Extracts the sender, receiver, and message from a log entry
def extract_textme_info(log_entry)
  sender = log_entry.scan(/\[from:(.*?)\]/).flatten.first
  receiver = log_entry.scan(/\[to:(.*?)\]/).flatten.first
  message = log_entry.scan(/\[msg:\d+:(.*?)\]/).flatten.first
  [sender, receiver, message]
end

# Example usage
log_entry = "Feb  1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:+14169955502] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]"

sender, receiver, message = extract_textme_info(log_entry)

puts "Sender: #{sender}"
puts "Receiver: #{receiver}"
puts "Message: #{message}"
