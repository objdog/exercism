module BookKeeping
  VERSION = 1
end

class Phrase

  attr_reader :entry

  def initialize(entry)
    @entry = entry
  end

  def make_array
    entry.downcase.scan(/\b[\w']+\b/) do |word|
      yield word
    end
  end

  def word_count
    response = Hash.new(0)
    make_array do |word|
      response[word] += 1
    end
    response
  end
end