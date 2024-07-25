import heapq

cables = [1,2,3,5,8,13,21,34]
wastes = []
heapq.heapify(cables)
connected = 0
while len(cables):
    if connected:
        connected = heapq.heappushpop(cables,connected)
    else:
        connected = heapq.heappop(cables)
    connected += heapq.heappop(cables)
    wastes.append(connected)
sum = 0
for waste in wastes:
    sum += waste

print("Витрати на з'єднання", wastes)
print("Загальні витрати", sum)
