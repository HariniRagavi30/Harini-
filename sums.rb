
# Main Zoo Class
class Zoo
  @@animal_count = 0
  @@bird_count = 0
  @@fish_count = 0

  def self.animal_count
    @@animal_count
  end

  def self.bird_count
    @@bird_count
  end

  def self.fish_count
    @@fish_count
  end
end

# Animal Class
class Animal < Zoo
  def initialize(name)
    @name = name
    @@animal_count += 1
  end
end

# Bird Class
class Bird < Zoo
  def initialize(name)
    @name = name
    @@bird_count += 1
  end
end

# Fish Class
class Fish < Zoo
  def initialize(name)
    @name = name
    @@fish_count += 1
  end
end

# Creating Objects
lion = Animal.new("Lion")
tiger = Animal.new("Tiger")
eagle = Bird.new("Eagle")
sparrow = Bird.new("Sparrow")
goldfish = Fish.new("Goldfish")
shark = Fish.new("Shark")

# Display Count
puts "Animal Count: #{Zoo.animal_count}"
puts "Bird Count: #{Zoo.bird_count}"
puts "Fish Count: #{Zoo.fish_count}"







