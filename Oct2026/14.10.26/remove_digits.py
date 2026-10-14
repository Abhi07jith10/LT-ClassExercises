string="ABcd1234"
new_string=""
for i in string:
    if i.isdigit()==False:
        new_string+=i
print(new_string)