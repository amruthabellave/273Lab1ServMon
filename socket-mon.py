import psutil

tmp = "\"%s\",\"%s\",\"%s\",\"%s\""
conn_tuples = psutil.net_connections(kind='tcp')
conn_sorted = sorted(conn_tuples, key=lambda conn: conn[6])


final = []
for t in conn_sorted:
    if(t.laddr and t.raddr and t.pid):
       newladdr = "%s@%s" % (t.laddr)
       newraddr = "%s@%s" % (t.raddr)
       final.append((t.pid, newladdr, newraddr, t.status))
       

pidset = set(e[0] for e in final)
cnt_list = []
for p in pidset:
    cnt = 0
    for f in final:
        if p==f[0]:
            cnt = cnt+1
    
    cnt_list.append((p,cnt))

cnt_list_sorted = sorted(cnt_list, key=lambda c: c[1], reverse = True)
print (tmp % ("pid", "laddr" ,"raddr", "status"))
for c in cnt_list_sorted:
    pidval = c[0]
    for a in final:
        if(a[0]==pidval):
            print (tmp % ( a[0], a[1], a[2], a[3]))
