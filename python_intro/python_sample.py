def hello_world():
    print('hello world')
 
hello_world()
 
def add_one(x):
    return x + 1
    
my_basket = []
juice = [1, 2, 3]
carrots = [8, 9]
my_basket += (carrots + juice)
my_basket
my_basket[2]
print(len(my_basket))


prices = {}
prices['truck'] = 25000
prices['sedan'] = 20000
prices['coupe'] = 30000
print prices
prices['truck']
#You can overwrite dictionary values:
prices['coupe'] = 50000
print dir(prices)

my_set = set([9, 11, 15, 17])
for my_num in my_set:
    print my_num