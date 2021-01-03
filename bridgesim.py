def take_initial_input():
	flag=input().strip()
	flag=int(flag)
	n=input().strip()#number of bridges
	n=int(n)
	lan_table={}#dictionary of lans and bridges(of type Bridge) connected to them
	bridges=[]# list of bridges (of type Bridge)
	for i in range(n):
		inp = input()
		inp = (inp.strip()).split(':')#Bridge name 
		lan = inp[1].split(' ')[1:]
		bridges.append(Bridge(inp[0], lan))
		for j in lan:
			if j not in lan_table.keys():
				lan_table[j]=[bridges[i]]
			elif  j in lan_table.keys():
				lan_table[j].append(bridges[i])
	return bridges,lan_table,n,flag

def trc_print(flag):
	global bridges,lan_table,n
	trc=[]#h
	for time in range(n):
		config_msg={}
		for i in lan_table.keys():
			msg=[]
			for b in lan_table[i]:
				msg.append(((b.root_bridge,b.dist,b.id),i))
				trc.append(str(time)+" s B"+ str(b.iid+1)+" (" + b.root_bridge + "," + str(b.dist)+","+b.id+")" )
			config_msg[i]=msg

		for i in range(n):
			b=bridges[i]
			b_msg=[]
			for j in b.lan_list:
				b_msg=b_msg+config_msg[j]
				for k in config_msg[j]:
					trc.append(str(time+1)+" r B"+str(b.iid + 1)+" ("+k[0][0]+","+str(k[0][1])+","+k[0][2]+")")
			b.update_config(b_msg)
	if (flag==1):
		for i in sorted(trc):
			print(i)  

def final_updates():
	global bridges,lan_table,n
	dps=[]
	for i in range(n):
		dps.append([])
	for i in lan_table.keys():
		di=n+1
		Id="B"+str(n+1)
		for b in lan_table[i]:
			if b.dist<di:
				di=b.dist
				Id=b.id
			elif b.dist==di and b.id<Id:
				Id=b.id
		if (Id!="B"+str(n+1)):
			dps[int(Id[1:])-1].append(i)

	for i in range(n):
		b=bridges[i]
		rp=b.root_port
		port={}
		for j in b.lan_list:
			if j==rp:
				port[j]="RP"
			elif j in dps[i]:
				port[j]="DP"
			else:
				port[j]="NP"
		b.port_configs=port

def input_hosts():
	global N, lan2host, host2lan
	while(True):
		s = input().strip()
		if s.isnumeric() == False:
			sp = s.split(':')
			lan2host[sp[0]] = sp[1].split(' ')[1:]	
		else:
			N = int(s)
			break
	for lan in lan2host:
		for host in lan2host[lan]:
			host2lan[host] = lan

def create_fwd_table():
	global bridges,lan_table,lan2host,host2lan,fwd_list,fwd_trace
	for i in range(N):
		s = (input().strip()).split(" ")
		sender = s[0]
		receiver = s[1]
		visited = [False for x in range(n)]
		queue = []
		queue.append(host2lan[sender])
		time=1
		while(len(queue) > 0):
			host_lan = queue[0]
			for b in lan_table[host_lan]:
				if (not visited[b.iid]):
					lans, fwd_list = b.send_msg(sender, receiver, host_lan, fwd_list)
					queue = queue + lans
					if (len(lans)>0):
						visited[b.iid] = True
					for l in range(len(lans)):
						trace = str(time) + " s " + b.id + " " + host_lan + " --> " + lans[l]
						fwd_trace.append(trace)
			time = time + 1
			queue = queue[1:]
		for i in range(n):
			bridges[i].print_ft()
		print('')
		if (flag == 1):
			for trace in fwd_trace:
				print(trace)
		fwd_trace=[]


class Bridge:
	id = ''
	iid = -1
	root_bridge = ''
	dist = 0
	root_port = ''
	parent_bridge = ""
	lan_list = []
	port_configs = {}
	fwd_table = []
	def __init__(self, id, lans):
		self.id = id
		self.iid = int(self.id[1:])-1
		self.root_bridge = self.id
		self.dist = 0
		self.lan_list = lans
		for lan in self.lan_list:
			self.port_configs[lan] = 'DP'
	def update_config(self, messages):
		for msg, port in messages:
			if (self.root_bridge > msg[0]):
				self.root_bridge = msg[0]
				self.dist = msg[1]+1
				self.parent_bridge = msg[2]
				self.root_port = port 
			elif (self.root_bridge == msg[0] and self.dist > msg[1] + 1):
				self.dist = msg[1]+1
				self.parent_bridge = msg[2]
				self.root_port = port
			elif (self.root_bridge == msg[0] and self.dist == msg[1] + 1 and self.parent_bridge > msg[2]):
				self.parent_bridge = msg[2]
				self.root_port=port
	def send_msg(self, sender, receiver, port, fwd_list):
		# global fwd_list
		lans = []
		if (self.port_configs[port] != 'NP'):
			fwd_list[self.iid][sender] = port
			if receiver in fwd_list[self.iid]:
				lans.append(fwd_list[self.iid][receiver])
			else:
				for lan in self.lan_list:
					if (self.port_configs[lan] != 'NP' and lan != port):
						lans.append(lan)
		return lans, fwd_list

	def print_ft(self):
		s = self.id + ':'
		print(s)
		print("HOST ID | FORWARDING PORT")
		fwd_tab = fwd_list[self.iid]
		for f in sorted(fwd_tab):
			print(f + ' | ' + fwd_tab[f])
	def print_configs(self):
		s1 = ''
		for l in sorted(self.lan_list):
			s1 = s1 + " " + l + "-" + self.port_configs[l]
		s = self.id + ':' + s1
		print(s)


bridges,lan_table,n,flag=take_initial_input()
trc_print(flag)			
final_updates()

for i in range(n):
	b=bridges[i]
	b.print_configs()
lan2host = {}
host2lan = {}
N = 0
fwd_list=[]
fwd_trace=[]
time=0
input_hosts()
for i in range(n):
	fwd_list.append({})
create_fwd_table()