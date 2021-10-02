=begin 
Ruby program to reverse a given string.
=end

puts "Enter the String:"
str1=gets.chomp

newstr= ' '

for  i in  1..str1.length
    newstr+=str1[str1.length - i]
end

puts "The reverse of #{str1} is #{newstr}"
