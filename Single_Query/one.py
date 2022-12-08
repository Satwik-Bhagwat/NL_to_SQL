import json

with open("./data/dev.json","r+") as f:
  d = json.load(f)
  d = d[0]
  col_set = d['col_set']
  col_set_size = len(col_set)
  q_g = d['question_arg_type']
  q_arg = d['question_arg']
  col_pred = []
  ind = 0
  for l in q_g:
    if l[0] in "col":
      print("yes")
      col_name = q_arg[ind][0]
      try:
        col_ind = col_set.index(col_name)
        col_pred.append(col_ind)
      except Exception:
        print("exception")
        pass
    ind+=1
  for i in range(col_set_size):
    if i not in col_pred:
      col_pred.append(i)
  d['col_pred'] = col_pred
  print(col_pred)
  f.seek(0)
  f.truncate(0)
  m=[d]
  json.dump(m,f,indent=4)
