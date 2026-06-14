# src/forecasting/energy_forecast.py

"""
Energy Forecasting Module

Converts raw solar irradiance predictions (GHI) into normalized
renewable energy scores that downstream optimizers can consume.

Pipeline integration:
    Weather Data → Solar Model → Predicted GHI → Renewable Score
"""


class EnergyForecaster:
    """Forecaster that converts Global Horizontal Irradiance (GHI)
    into a 0–100 renewable energy score.
    """

    MAX_GHI = 1000.0

    @staticmethod
    def ghi_to_renewable_score(ghi_value):
        """Normalize a single GHI value to an integer score between 0 and 100.

        Args:
            ghi_value (float or int): Global Horizontal Irradiance in W/m².

        Returns:
            int: Renewable score (0 = no solar, 100 = peak solar).

        Raises:
            ValueError: If ghi_value is None or cannot be cast to float.
        """
        if ghi_value is None:
            raise ValueError("GHI value cannot be None")

        ghi = float(ghi_value)

        if ghi < 0:
            raise ValueError(f"GHI value cannot be negative, got {ghi}")

        # Scale against theoretical maximum and clamp
        score = (ghi / EnergyForecaster.MAX_GHI) * 100
        score = max(0, min(100, score))

        return round(score)

    @classmethod
    def score_forecast(cls, hourly_ghi_list):
        """Convert a list of 24 hourly GHI values into renewable scores.

        Args:
            hourly_ghi_list (list): 24 GHI values, one per hour.

        Returns:
            list: 24 integer renewable scores.

        Raises:
            ValueError: If the input does not contain exactly 24 values.
            TypeError:  If hourly_ghi_list is not iterable.
        """
        if hourly_ghi_list is None:
            raise TypeError("hourly_ghi_list cannot be None")

        if not isinstance(hourly_ghi_list, (list, tuple)):
            raise TypeError(
                f"hourly_ghi_list must be a list or tuple, got {type(hourly_ghi_list).__name__}"
            )

        if len(hourly_ghi_list) != 24:
            raise ValueError(
                f"Expected 24 hourly values, got {len(hourly_ghi_list)}"
            )

        return [
            cls.ghi_to_renewable_score(ghi)
            for ghi in hourly_ghi_list
        ]
