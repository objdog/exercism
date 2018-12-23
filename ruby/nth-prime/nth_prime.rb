module BookKeeping
  VERSION = 1
end

class Prime

  #create a function to determine primeness of a number
  def self.is_prime(num)
    #because, come on... 1 isn't prime... even though it is.
    return false if num <= 1
    #determine primeness
    Math.sqrt(num).floor.downto(2).each { |i| return false if num % i == 0 }
    true
  end

  #main function
  def self.nth(number)
    #This seems like a cop-out, but it works well.
    if number <= 0
      fail ArgumentError.new
    end

    #set up the iterative solution
    counter = 0
    initial = 1
    #iterate through numbers up to the nth number
    while counter < number
      initial += 1
      counter += 1 if self.is_prime(initial)
    end
    return initial
  end
end