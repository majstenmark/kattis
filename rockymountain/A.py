N, M = map(int, raw_input().split())
K, R = map(int, raw_input().split())
def switch(s1, lane1, lane2):
    if lane1 == lane2:
        return lens[s1] + curves[s1][0] + curves[s1][1] * (lane1 + 1)
    if abs(lane1 - lane2) * K > lens[s1]:
        return -1
    return lens[s1] + R * abs(lane1 - lane2) + curves[s1][0] + curves[s1][1] * (lane2+1)

lens = []
curves= []
for n in range(N):
      l = int(raw_input())
      lens.append(l)
for n in range(N-1):
      s, c = map(int, raw_input().split())
      curves.append((s, c))
curves.append((0, 0))
INF = 10**12
ways = [[INF] * M for _ in range(N+1)]
ways[0][0] = 0
for n in range(N):
    for lane in range(M):
        if ways[n][lane] != INF:
            for otherLane in range(M):
                switchDist = switch(n, lane, otherLane)
                if switchDist > -1:
                    alt = ways[n][lane] + switchDist
                    ways[n+1][otherLane] = min(ways[n+1][otherLane], alt)
#print ways
print ways[-1][0]
