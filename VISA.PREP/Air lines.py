x,N = map(int,input().split())
min_planes_required = (N+99) // 100
new_planes_to_buy = max(0,min_planes_required-x)
print(new_planes_to_buy)
