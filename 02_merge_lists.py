import heapq

def merge_k_lists(arr:list[list[int]]):
    heap = []
    max_len=0
    for li in arr:
        max_len = max(max_len, len(li))
    for i in range(max_len):
        for li in arr:
            if i<len(li):
                heapq.heappush(heap, li[i])
    print("Сформована купа:", heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)

def heap_merge(arr:list[list[int]]):
    return list(heapq.merge(*arr))

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = heap_merge(lists)
print("Відсортований список через злиття:", merged_list)
