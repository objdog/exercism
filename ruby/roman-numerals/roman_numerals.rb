module BookKeeping
	VERSION = 2
end

class Integer

	def to_roman

		number = self

		#set up the 'dictionary'
		roman_map = {
			1000 => "M",
			900 => "CM",
			500 => "D",
			400 => "CD",
			100 => "C",
			90 => "XC",
			50 => "L",
			40 => "XL",
			10 => "X",
			9 => "IX",
			5 => "V",
			4 => "IV",
			1 => "I"
		}

		#initializing the response
		answer = ""
	
		return_value = roman_map.inject(answer) do |result, (arab, roman)|
			whole_part, number = number.divmod(arab)
			result << roman * whole_part
		end

		return return_value

	end
end