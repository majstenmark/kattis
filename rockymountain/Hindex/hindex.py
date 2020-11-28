N = input()
papers = [input() for n in range(N)]
papers.sort()
H = 0
for i, citations in enumerate(papers):
    H = max(H, min(citations, N - i))
print H
