import gc
import tracemalloc

# ── 1. Global list leak ────────────────────────────────────
cache = []

def add_data(x):
    cache.append(x)   # never cleared — LEAK!

add_data("a")
add_data("b")
add_data("c")
print(f"cache size: {len(cache)}")  # keeps growing

# ── 2. Cycle leak ──────────────────────────────────────────
def create_cycle():
    x = []
    y = []
    x.append(y)
    y.append(x)
    # function ends — but objects stuck in memory!

create_cycle()
print(f"before gc: {gc.get_count()}")
gc.collect()
print(f"after gc:  {gc.get_count()}")

# ── 3. tracemalloc — memory usage track karo ──────────────
tracemalloc.start()

big_list = [i for i in range(10000)]

snapshot = tracemalloc.take_snapshot()
stats = snapshot.statistics("lineno")
print(stats[0])   # konti line jast memory vaparte

tracemalloc.stop()