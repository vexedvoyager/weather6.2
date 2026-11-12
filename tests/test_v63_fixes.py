from src.probability import probability_of_exceeding, probability_within_range

FLAT_LOW = {"p10": 88, "p25": 88, "p50": 88, "p75": 89, "p90": 89}
FLAT_HIGH = {"p10": 50, "p25": 51, "p50": 52, "p75": 52, "p90": 52}


def test_flat_lower_tail_no_crash():
    p = probability_of_exceeding(FLAT_LOW, 80.5, clamp=False)
    assert 0.99 < p <= 1.0


def test_flat_upper_tail_no_crash():
    p = probability_of_exceeding(FLAT_HIGH, 60.5, clamp=False)
    assert 0.0 <= p < 0.01


def test_flat_bracket_no_crash():
    p = probability_within_range(FLAT_LOW, 84.5, 86.5)
    assert 0.0 < p < 0.5
