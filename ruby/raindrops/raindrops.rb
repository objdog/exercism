module BookKeeping
    VERSION = 2
end

class Raindrops
    DICTIONARY = {
        3 => 'Pling',
        5 => 'Plang',
        7 => 'Plong',
    }
    
    private_constant :DICTIONARY
    
    def self.convert(number)
        result = ''
        DICTIONARY.each do |(num, drop)|
            result << drop if number % num == 0
        end
        
        result.empty? ? number.to_s : result
    end
end