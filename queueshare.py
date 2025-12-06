import multiprocessing
def matrix1(pipe):
	mmatrix1=[
		[1,2,3],
		[4,5,6]
	]
	mmatrix2=[
		[9,8,7],
		[6,5,4]
	]
	data=[]
	for i in range(len(mmatrix1)):
		matrixsum=[]
		for j in range(len(mmatrix1[i])):
			
			matrixsum.append(mmatrix1[i][j]+mmatrix2[i][j])
		data.append(matrixsum)
	pipe.send(data)
	pipe.close()
def matrixSOLVE(pipe):
	data=pipe.recv()
	for row in data:
		print("Data recieved",row)
if __name__=='__main__':
	parent_conn,child_conn=multiprocessing.Pipe()
	p1=multiprocessing.Process(target=matrix1,args=(child_conn,))
	p2=multiprocessing.Process(target=matrixSOLVE,args=(parent_conn,))
	p1.start()
	p2.start()
	p1.join()
	p2.join()

	

