# Test task.
###### The site - https://yandex.ru
Includes test cases for the site's function where user can change his geo position. And that data would change on current location.

The application use next stack of technologies:
- python 3.8.2
- selenium 3.141.0
- pytest 5.4.3
- pytest-rerunfailures 9.0
- requests 2.24.0

### Usages

With selenium I would recommend to use 'reruns' that avoid drops caused of selenium works. Add flag `--reruns` and number after it to set count of try if test would drop.

    pytest -s --reruns 3 test_main_page.py
    
You can use the pytest command without pointing python file, because in this case all tests are only into test_main_page.py.

    pytest -s --reruns 3
    
Test cases were split by markers, and you can use markers in the pytest command. Use option `-m` and name of a marker after that.

    pytest -s -m choose_location --reruns 3
    
Markers:
- `is_present` - tests where are checking that user can see elements on the main and geo position pages.
- `wrong_input` - test cases where are checking that user input incorrect data.
- `choose_location` - test cases where are checking that user change his geo position in the site.


###### author Dmitry Shelukhin