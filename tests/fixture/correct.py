from gendiff import generate_diff

diff_json = generate_diff(r'tests/fixture/file1.json',
                          r'tests/fixture/file2.json')

diff_yml = generate_diff(r'tests/fixture/file1.yml',
                          r'tests/fixture/file2.yml')


diff_stylish_yml = generate_diff(r'tests/fixture/file1.yml',
                                  r'tests/fixture/file2.yml', 'stylish')

diff_plain = generate_diff(r'tests/fixture/file1.json',
                           r'tests/fixture/file2.json', 'plain')

diff_plain_yml = generate_diff(r'tests/fixture/file1.yml',
                                r'tests/fixture/file2.yml', 'plain')

diffjson_json = generate_diff(r'tests/fixture/file1.json',
                              r'tests/fixture/file2.json', 'json')

diffyml_json = generate_diff(r'tests/fixture/file1.yml',
                              r'tests/fixture/file2.yml', 'json')