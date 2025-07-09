# Basics from 0 to 150:
for b in range(0 , 151):
    print(b);
    
# Multiples Of 5 from 5 to 1000:
for m in range(5 , 1000+5):
    if m % 5 == 0:
        print(m);
    
# Counting The Dojo Way:
for c in range(1 , 101):
    if c % 10 == 0:
        print("Coding Dojo");
    elif c % 5 == 0:
        print("Coding");
    else:
        print(c);

# Whoa. That Sucker's Huge (Add Odd Integers from 0 to 500000) and print thier sum:
sum = 0;
for i in range(0,500000+1):
    if i % 2 == 1:
        sum = sum + i;
print("The Sum is: " , sum);


# Flexible Counter:
mult = 3;
for i in range(9 , 0 , -1):
    if i % mult == 0:
        print(i);