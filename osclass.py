import random

def generate_reference_string(length):
    return [random.randint(0, 9) for _ in range(length)]

def fifo_page_replacement(ref_string, frames):
    frame = []
    page_faults = 0

    for page in ref_string:
        if page not in frame:
            page_faults += 1
            if len(frame) < frames:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)

    return page_faults


def lru_page_replacement(ref_string, frames):
    frame = []
    page_faults = 0
    recently_used = {}

    for i, page in enumerate(ref_string):
        if page not in frame:
            page_faults += 1
            if len(frame) < frames:
                frame.append(page)
            else:
                lru_page = min(frame, key=lambda x: recently_used.get(x, -1))
                frame.remove(lru_page)
                frame.append(page)
        recently_used[page] = i

    return page_faults

def optimal_page_replacement(ref_string, frames):
    frame = []
    page_faults = 0

    for i, page in enumerate(ref_string):
        if page not in frame:
            page_faults += 1
            if len(frame) < frames:
                frame.append(page)
            else:
                future_uses = {p: ref_string[i+1:].index(p) if p in ref_string[i+1:] else float('inf') for p in frame}
                opt_page = max(future_uses, key=future_uses.get)
                frame.remove(opt_page)
                frame.append(page)

    return page_faults

def main():
    print("Page Replacement Algorithms: FIFO, LRU, Optimal (OPT)")
    num_frames = int(input("Enter the number of page frames: "))
    ref_string_length = int(input("Enter the length of the page-reference string: "))
    
    ref_string = generate_reference_string(ref_string_length)
    print(f"\nGenerated Page-Reference String: {ref_string}\n")
    
    fifo_faults = fifo_page_replacement(ref_string, num_frames)
    lru_faults = lru_page_replacement(ref_string, num_frames)
    opt_faults = optimal_page_replacement(ref_string, num_frames)

    print(f"Number of Page Faults:")
    print(f"FIFO: {fifo_faults}")
    print(f"LRU: {lru_faults}")
    print(f"Optimal (OPT): {opt_faults}")

if __name__ == "__main__":
    main()
