from helpers import *


@with_driver
def test_calc_mite():
	return series(
		go_to_calc_mite_url(),
		assert_calc_mite_page_header(),
		choose_two_people(),
		choose_mite(),
		choose_krasnodar(),
		calculate(),
		assert_calc_results()
	)
