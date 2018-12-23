module BookKeeping
  VERSION = 3
end

class Hamming
 def self.compute(string_1, string_2)
  str1 = string_1.downcase.split('')
  str2 = string_2.downcase.split('')
  hamming_distance = 0
  
  if string_1.size != string_2.size 
   raise ArgumentError
  else
  
   str1.each_index do |i|
    hamming_distance += 1 if str1.values_at(i) != str2.values_at(i)
   end
  hamming_distance
  end
  
 end
end