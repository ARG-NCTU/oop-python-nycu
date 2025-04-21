def validPath(n,edges,source,destination):
    
    
    if n==1:
        return True
    
    def gen(src,visited):
        src_list=[]

        # find src_list
        for i in edges:
            if src in i:
                src_list.append(i)
        
        for k in src_list:
            if k[0]==src:
                next=k[1]
            else:
                next=k[0]

            if  next==destination:
                return True
            
            elif not visited[next]:
                
                visited[src]=True #visited src
                if gen(next,visited):
                    return True
                visited[src]=False
        return False
    
    v =[0 for j in range(n)]
    return gen(source,v )

n = 10
edges =[[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
source = 7
destination = 5
print(validPath(n,edges,source,destination))