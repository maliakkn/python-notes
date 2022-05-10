#Variable Types in Python
#integer
x = 8
#float
y = 3.2
#complex
z = 8j + 18
#string
a = "hello world!"
#boolean
b = True
c = 23 < 22
#list
l = [1, 2, 3, 4]
#dictionary
d = {"name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
#tuple
t = ("Machine Learning", "Data Science")
#set
s = {"Python", "Machine Learning", "Data Science"}

#learning type of a variable with type()
type(s)

#capitalizing, replacing and splitting with strings
text = "The goal is to turn data into information, and information into insight."
a = text.upper()
b = a.replace(",", " ")
c = b.replace(".", " ")
d = c.split()
print(d)

#deleting and replacing variables of lists using indexes
lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
len(lst)
var = lst[0], lst[10]
lstdata = lst[0:4]
print(lstdata)
lst.pop(8)
lst.insert(8, "N")
lst.pop(8)
lst

#creating dicts and learning and updating keys and values of dicts
dict = dict(Christian=["America", 18], Daisy=["England", 12], Antonio=["Spain", 22], Dante=["Italy", 25])
dict.keys()
dict.values()
dict.update({"Daisy": ["England", 13]})
dict.update({"Ahmet": ["Turkey", 24]})

#learning methods applicable to dictionaries using dir() function
dir(dict)
dict.pop("Antonio")
dict

# how to create functions
def func(x):
    """

    :param x:
    :return:
    """
    print(x + 5)


func(4)

l = [2, 13, 18, 93, 22]
even_list = []
odd_list = []



#adding docstring to a function
def func(num):
    """
    this function tries to seperate odd and even numbers and add them to different lists
    Parameters
    num : list or numbers
    """
    if num % 2 == 0:
        odd_list.append(num)
        print(odd_list)
    else:
        even_list.append(num)
        print(even_list)


for i in l:
    func(i)

print(even_list, odd_list)


#example of list comprehensions method for creating lists

df = sns.load_dataset("car_crashes")
var = df.columns



no_flag = [(i + "_FLAG").upper() if "no" not in i else i.upper() for i in df.columns]
no_flag


new_cols = [col for col in df.columns if col not in og_list]

new_df = df[new_cols]

new_df.head()
