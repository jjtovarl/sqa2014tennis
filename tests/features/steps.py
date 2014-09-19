# -*- coding: utf-8 -*-
from lettuce import *
import app.match as m


@step(u'Given: "([^"]*)" and "([^"]*)" start a match to "([^"]*)" sets')
def given_group1_and_group2_start_a_match_to_group3_sets(step, group1, group2, group3):
    world.match = m.Match(group1,group2,group3)


@step(u'When: "([^"]*)" and "([^"]*)" start a match to "([^"]*)" sets')
def when_group1_and_group2_start_a_match_to_group3_sets(step, group1, group2, group3):
    assert world.match.anotar(p1, int(group2[0]), group3, group4)


@step(u'Then: I see score: "([^"]*)"')
def then_i_see_score_group1(step, group1):
    assert world.match.score() == group1, 'Error got: '+ world.match.score()


@step(u'When: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def when_group1_won_the_group2_set_group3_group4(step, group1, group2, group3, group4):
	world.match.anotar(group1, int(group2[0]), group3, group4)


@step(u'And: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def and_group1_won_the_group2_set_group3_group4(step, group1, group2, group3, group4):
    world.match.anotar(group1, int(group2[0]), group3, group4)


@step(u'Then: The match score is: "([^"]*)"')
def then_the_match_score_is_group1(step, group1):
    assert world.match.score() == group1, "Got: " % world.match.score()

