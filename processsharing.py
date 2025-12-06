import multiprocessing
def holdingvalues(pipe):
	a=10
	b=20
	data=a+b
	pipe.send(data)
def receving(pipe):
	data=pipe.recv()
	print("received data",data)
if __name__=='__main__':
	parent_conn,child_conn=multiprocessing.Pipe()
	p1=multiprocessing.Process(target=holdingvalues,args=(parent_conn,))
	p2=multiprocessing.Process(target=receving,args=(child_conn,))
	p1.start()
	p2.start()
	p1.join()
	p2.join()