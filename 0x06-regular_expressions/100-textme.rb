#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(.\W*)\]\s\[to:(\W*\d*)\]\s\[flags:(.*?)\]/).join(',')
