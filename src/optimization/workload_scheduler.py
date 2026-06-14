# src/optimization/workload_scheduler.py

"""
Workload Scheduler

Consumes hourly renewable energy scores and recommends the best
consecutive time window to run energy-intensive workloads.

Pipeline integration:
    Renewable Score → Optimization Engine → Scheduling Decision
"""


class WorkloadScheduler:
    """Scheduler that finds the optimal run window based on renewable scores."""

    @staticmethod
    def find_best_window(scores, duration_hours):
        """Find the consecutive time window with the highest average renewable score.

        Args:
            scores (list): 24 integer scores (0–100), one per hour.
            duration_hours (int): Desired run length in hours.

        Returns:
            dict: Scheduling recommendation containing:
                - "best_start_hour" (int): Start hour (0–23).
                - "best_start_time" (str): Formatted as "HH:00".
                - "average_score" (float): Average score, rounded to 2 decimals.
                - "window_scores" (list): The actual scores in that window.

        Raises:
            TypeError:  If inputs are of the wrong type.
            ValueError: If scores doesn't have exactly 24 values or
                        duration_hours is outside 1–24.
        """
        # Input guards
        if scores is None:
            raise TypeError("scores cannot be None")
        if not isinstance(scores, (list, tuple)):
            raise TypeError(
                f"scores must be a list or tuple, got {type(scores).__name__}"
            )
        if not isinstance(duration_hours, int):
            raise TypeError(
                f"duration_hours must be an integer, got {type(duration_hours).__name__}"
            )

        if len(scores) != 24:
            raise ValueError(
                f"scores must contain exactly 24 values, got {len(scores)}"
            )
        if duration_hours < 1 or duration_hours > 24:
            raise ValueError(
                f"duration_hours must be between 1 and 24, got {duration_hours}"
            )

        # Sliding window scan
        best_start = 0
        best_avg = -1.0
        num_windows = 24 - duration_hours + 1

        for start in range(num_windows):
            window = scores[start:start + duration_hours]
            avg = sum(window) / duration_hours

            # Use strict > so ties favor the earliest window
            if avg > best_avg:
                best_avg = avg
                best_start = start

        best_window = scores[best_start:best_start + duration_hours]

        return {
            "best_start_hour": best_start,
            "best_start_time": f"{best_start:02d}:00",
            "average_score": round(best_avg, 2),
            "window_scores": best_window,
        }

    @classmethod
    def schedule(cls, hourly_scores, job_duration_hours):
        """High-level API: recommend a schedule from a daily score profile.

        Args:
            hourly_scores (list): 24 integer renewable scores.
            job_duration_hours (int): How long the job runs.

        Returns:
            dict: Scheduling recommendation (same shape as find_best_window).
        """
        return cls.find_best_window(hourly_scores, job_duration_hours)
