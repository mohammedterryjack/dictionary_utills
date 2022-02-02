Dict(dict):
  """
  convert a dictionary into an object
  """
  __getattr__ = dict.get
  __setattr__ = dict.__setitem__
  __delattr__ = dict.__delitem__

def objectify(data:dict) -> Dict:
  """
  recursively convert a nested dictionary
  into an object
  """
  for key,value in data.items():
    if isinstance(value,dict):
      data[key] = objectify(value)
  return Dict(data)

#example = objectify(dict(a=None, b=dict(c=1)))
#example.b.c
