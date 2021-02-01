sum_squared_dist = []
K = range(1,50)
for k in K:
    km = KMeans(n_clusters=k, random_state=0)
    km = km.fit(normalized_modeling_data)
    sum_squared_dist.append(km.inertia_)

print(sum_squared_dist)