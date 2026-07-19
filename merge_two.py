import json
def merge_two(dictionary):
   new={}
   while True:
      key= input("Enter Key: ")
      if key =="exit":
            break
      v=input("Enter value: ")
      try:
            value = int(v)
      except ValueError:
          break
      new[key]=value
      d=dictionary.copy()
      d.update(new)
   return json.dumps(d)


