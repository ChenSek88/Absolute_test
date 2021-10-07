# -*- coding: utf-8 -*-
import os
from .actions import *
from .locators import CalcPageLocators as cpl
import re


target_url = 'https://www.absolutins.ru/kupit-strahovoj-polis/strahovanie-zhizni-i-zdorovya/ukus-kleshcha/'


def go_to_calc_mite_url():
	return go_to(target_url)


def assert_calc_mite_page_header():
	return assert_text(cpl.header, u'Купить полис страхования от укуса клеща')


def choose_two_people():
	return wait_and_click(cpl.two_people)


def count_of_people(count):
	locator = list(cpl.count)
	new_locator = locator[1] + '[for="fr%s"]' %count
	return wait_and_click(tuple(['css selector']) + tuple([new_locator]))



def choose_mite():
	return series(
		wait_and_click(cpl.mite), wait_vis(cpl.mite_is_active)
	)


def choose_krasnodar():
	return series(
		wait_and_click(cpl.region_list), assert_text(cpl.krasnodar, u'Краснодар'), 
		wait_and_click(cpl.krasnodar), wait_vis(cpl.krasnodar_is_active)
	)


def calculate():
	return series(
		wait_and_click(cpl.calc), wait_vis(cpl.calc_fields_disabled),
		wait_invis(cpl.calc_fields_disabled)
	)


def assert_calc_results():
	return series(
		assert_text(cpl.price, "600"),
		assert_text(cpl.number, re.findall(r'\d*', str(get_text_from_element(cpl.number)))[0])
	)
