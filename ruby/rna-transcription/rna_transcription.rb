module BookKeeping
 VERSION = 4
end

class Complement
 def self.of_dna(dna)
  if (dna.count "^GTAC") == 0
   result = dna.gsub(/[GCTA]/, 'G' => 'C', 'C' => 'G', 'T' => 'A', 'A' => 'U')
   return result
  else
   return ''
  end
 end
end