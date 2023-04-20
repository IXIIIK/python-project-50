from gendiff import generate_diff


def test_generate_stylish():
    diff_json_stylish = generate_diff(
        "tests/fixture/file1.json", "tests/fixture/file2.json"
    )
    diff_yaml_stylish = generate_diff(
        "tests/fixture/file1.yaml", "tests/fixture/file2.yaml"
    )
    diff_yml_stylish = generate_diff(
        "tests/fixture/file1.yml", "tests/fixture/file2.yml"
    )
    result_true_stylish = open("tests/fixture/correct_json_stylish").read()

    assert diff_json_stylish == result_true_stylish
    assert diff_yaml_stylish == result_true_stylish
    assert diff_yml_stylish == result_true_stylish

def test_generate_plain():
    diff_json_plain = generate_diff(
        "tests/fixture/file1.json", "tests/fixture/file2.json", "plain"
    )
    diff_yaml_plain = generate_diff(
        "tests/fixture/file1.yaml", "tests/fixture/file2.yaml", "plain"
    )
    diff_yml_plain = generate_diff(
        "tests/fixture/file1.yml", "tests/fixture/file2.yml", "plain"
    )
    result_true_plain = open("tests/fixture/result_true_plain").read()

    assert diff_json_plain == result_true_plain
    assert diff_yaml_plain == result_true_plain
    assert diff_yml_plain == result_true_plain



