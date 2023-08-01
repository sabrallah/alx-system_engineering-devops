#!/usr/bin/env ruby
# texting me 
puts ARGV[0]
       .scan(/(?<=from:|to:|flags:).*?(?=\])/)
       .join(',')
