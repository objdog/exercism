module BookKeeping
 VERSION = 3
end

class Gigasecond
 def self.from(completeDate)
  completeDate + 1000000000
 end
end