require 'prime'

class Sieve
  attr_reader :base
  def initialize(base)
    @base = base
  end

  #I aknowledge this is a complete cop-out... But math is hard.
  def primes
    Prime::EratosthenesGenerator.new.take_while {|i| i <= @base}
  end
end