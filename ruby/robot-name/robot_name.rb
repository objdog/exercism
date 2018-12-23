module BookKeeping
  VERSION = 2
end

class Robot

  attr_reader :name
 @@used_names = []
  def initialize
    while true
      name = (letter_choose(2) + number_choose(3)).join
      unless @@used_names.include?(name)
        @name = name
        @@used_names << @name
        break
      end
    end
  end

  def reset
    initialize
  end

  def letter_choose(num)
    num.times.map { [*'A'..'Z'].sample }
  end

  def number_choose(num)
    num.times.map { (0..9).to_a.sample.to_s }
  end

end