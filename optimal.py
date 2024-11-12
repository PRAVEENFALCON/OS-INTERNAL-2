def optimal_page_replacement(pages, frame_size):
    page_frame = []
    page_faults = 0
    hits = 0

    for i in range(len(pages)):
        page = pages[i]
        
        if page in page_frame:
            hits += 1
        else:
            page_faults += 1
            
            if len(page_frame) < frame_size:
                page_frame.append(page)
            else:
                future_uses = []
                
                for frame_page in page_frame:
                    if frame_page in pages[i+1:]:
                        future_uses.append(pages[i+1:].index(frame_page))
                    else:
                        future_uses.append(float('inf'))
                
                frame_to_replace = future_uses.index(max(future_uses))
                page_frame[frame_to_replace] = page

    total_references = len(pages)
    miss_ratio = page_faults / total_references
    hit_ratio = hits / total_references

    return page_faults, hits, miss_ratio, hit_ratio

pages_input = input("Enter the page references string (comma-separated): ")
pages = list(map(int, pages_input.split(',')))
frame_size = int(input("Enter the frame size: "))

page_faults, hits, miss_ratio, hit_ratio = optimal_page_replacement(pages, frame_size)

print("Optimal Page Faults:", page_faults)
print("Hits:", hits)
print("Miss Ratio:", miss_ratio)
print("Hit Ratio:", hit_ratio)

