module BookKeeping
	VERSION = 3
end

class Squares

	attr_reader :base
	def initialize(base)
		@base = base
	end

	def sum_of_squares
		sum = 0
		(1..@base).each do |i|
			sum += i**2
		end
		sum
	end

	def square_of_sum
		sum = 0
		(1..@base).each do |i|
			sum += i
		end
		sum**2
	end

	def difference
		square_of_sum - sum_of_squares
	end

end