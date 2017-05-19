import pandas as pd

def isfaulty(err):
	if len(err['Location']) == 0:
		return False
	else:
		return True

def write_errors(pid,data,err):
	temp1 = []
	temp2 = []
	k = 0
	c = 0
	mask = err.apply(isfaulty)
	indices = [i for i,x in enumerate(mask) if x == True]
	err = err[mask]
	for i in indices:
		for j in range(len(err[i]['Location'])):
			temp1.append([pid[i]])
			temp1[k] += err[i]['Rule'],
			temp1[k] += err[i]['Location'],
			temp1[k] += err[i]['Message'],
			temp1[k] += err[i]['Replacements'],
			k += 1
		temp2.append([pid[i]])
		temp2[c] += data[i],
		c += 1
	col1 = ['ProductId','Rule','Location','Message','Replacements']
	col2 = ['ProductId','Description']
	results1 = pd.DataFrame(temp1,columns=col1)
	results2 = pd.DataFrame(temp2,columns=col2)
	results1.to_csv('pid_err.csv',encoding='utf8',index=False)
	results2.to_csv('pid_desc.csv',encoding='utf8',index=False)