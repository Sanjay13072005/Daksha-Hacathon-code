import cProfile
import pstats
import io

def profile_code(func, *args, **kwargs):
    """Profiles the given function and returns a performance report."""
    profiler = cProfile.Profile()
    profiler.enable()
    result = func(*args, **kwargs)  # Execute the function
    profiler.disable()

    s = io.StringIO()
    stats = pstats.Stats(profiler, stream=s)
    stats.strip_dirs().sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    return s.getvalue(), result

if __name__ == "_main_":
    # Example usage
    def sample_function():
        total = 0
        for i in range(1000000):
            total += i
        return total

    report, _ = profile_code(sample_function)
    print("Performance Profile Report:\n", report)