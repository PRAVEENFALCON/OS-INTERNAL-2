def lru_page_replacement(pages, frame_size):
    page_frame = []
    page_faults = 0
    hits = 0

    for page in pages:
        if page in page_frame:
            hits += 1
            page_frame.remove(page)
            page_frame.append(page)
        else:
            page_faults += 1
            if len(page_frame) >= frame_size:
                page_frame.pop(0)
            page_frame.append(page)

    total_references = len(pages)
    miss_ratio = page_faults / total_references
    hit_ratio = hits / total_references

    return page_faults, hits, miss_ratio, hit_ratio

pages_input = input("Enter the page references string (comma-separated): ")
pages = list(map(int, pages_input.split(',')))
frame_size = int(input("Enter the frame size: "))

page_faults, hits, miss_ratio, hit_ratio = lru_page_replacement(pages, frame_size)

print("LRU Page Faults:", page_faults)
print("Hits:", hits)
print("Miss Ratio:", miss_ratio)
print("Hit Ratio:", hit_ratio)

