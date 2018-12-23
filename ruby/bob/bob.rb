module BookKeeping
  VERSION = 1
end

class Bob

  def hey(str)
    return "Fine. Be that way!" if silent?(str) 
    return "Whoa, chill out!" if shouting?(str) 
    return "Sure." if asking?(str) 
    "Whatever."
  end

  def silent?(sentence)
    sentence.strip.empty?
  end

  def shouting?(sentence)
    sentence =~ /[A-Z]/ && sentence !~ /[a-z]/
  end

  def asking?(sentence)
    sentence.end_with?("?")
  end

end