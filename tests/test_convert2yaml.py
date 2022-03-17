import yaml

from src import convert2yaml

def test_verify_num_args_passed_empty():
    # given
    args = []

    # when
    result = convert2yaml.verify_num_args_passed(args)

    # then
    assert result is False


def test_verify_num_args_passed_correct():
    # given
    args = ["a", "b", "c"]

    # when
    result = convert2yaml.verify_num_args_passed(args)

    # then
    assert result is True


def test_verify_num_args_passed_invalid():
    # given
    args = ["a", "b"]

    # when
    result = convert2yaml.verify_num_args_passed(args)

    # then
    assert result is False


def test_verify_num_args_passed_none():
    # given
    args = None

    # when
    result = convert2yaml.verify_num_args_passed(args)

    # then
    assert result is False


def test_create_list_of_dicts():
    # given
    test_csv = 'csv-input.csv'

    # when
    s = convert2yaml.process_csv()

    # verify string by reading it as YAML
    result = yaml.load(s)


def test_junk():
    assert(convert2yaml.junk(), 1)

