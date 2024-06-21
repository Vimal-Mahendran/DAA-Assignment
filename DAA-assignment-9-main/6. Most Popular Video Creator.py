from collections import defaultdict


def most_popular_video_creator(creators, ids, views):
    creator_views = defaultdict(int)
    creator_videos = defaultdict(list)

    for i in range(len(creators)):
        creator_views[creators[i]] += views[i]
        creator_videos[creators[i]].append((ids[i], views[i]))

    max_views = max(creator_views.values())

    answer = []
    for creator, total_views in creator_views.items():
        if total_views == max_views:
            max_videos = sorted(creator_videos[creator], key=lambda x: x[0])[::-1]
            max_video_id = max_videos[0][0]
            answer.append([creator, max_video_id])

    return answer


creators = ["alice", "bob", "alice", "chris"]
ids = ["one", "two", "three", "four"]
views = [5, 10, 5, 4]

print(most_popular_video_creator(creators, ids, views))
