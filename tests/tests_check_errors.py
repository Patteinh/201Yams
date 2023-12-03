from src.check_errors import check_args
import pytest

def test_check_args_valid():
    # Valid arguments
    ac = 7
    av = ["./201yams", "1", "2", "3", "4", "5", "pair_3"]
    check_args(ac, av)

def test_check_args_invalid_num_args():
    # Invalid number of arguments
    ac = 6
    av = ["./201yams", "1", "2", "3", "4", "5"]
    with pytest.raises(Exception, match="ERROR: The number of arguments must be 7."):
        check_args(ac, av)

def test_check_args_invalid_dice_num():
    # Invalid dice number
    ac = 7
    av = ["./201yams", "0", "7", "3", "4", "5", "pair_3"]
    with pytest.raises(Exception, match="ERROR: The numbers passed are not correct."):
        check_args(ac, av)

def test_check_args_invalid_combination():
    # Invalid combination
    ac = 7
    av = ["./201yams", "1", "2", "3", "4", "5", "invalid_combination"]
    with pytest.raises(Exception, match="ERROR: Invalid combination"):
        check_args(ac, av)

def test_check_args_invalid_full_combination():
    # Invalid full combination
    ac = 7
    av = ["./201yams", "1", "2", "3", "4", "5", "full_33"]
    with pytest.raises(Exception, match="ERROR: Invalid full combination"):
        check_args(ac, av)

def test_check_args_valid_full_combination_full():
    # Invalid full combination
    ac = 7
    av = ["./201yams", "1", "2", "3", "4", "5", "full_2_3"]
    check_args(ac, av)

def test_check_args_valid_combination_straight():
    # Invalid full combination
    ac = 7
    av = ["./201yams", "1", "2", "3", "4", "5", "straight_5"]
    check_args(ac, av)

def test_check_args_invalid_combination_straight():
    # Invalid full combination
    ac = 7
    av = ["./201yams", "1", "2", "3", "4", "5", "straight_7"]
    with pytest.raises(Exception, match="ERROR: Invalid combination"):
        check_args(ac, av)

def test_check_args_help_option():
    # Help option
    ac = 2
    av = ["./201yams", "-h"]
    with pytest.raises(SystemExit):
        check_args(ac, av)
