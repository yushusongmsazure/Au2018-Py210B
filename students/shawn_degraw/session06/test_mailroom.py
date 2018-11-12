#!/usr/bin/env python

import mailroompart4

def test_sortDB():
    assert mailroompart4.sortdb() == [('John Wick', [1000.0]), ('John Smith', [500.0, 150.0, 20.0]), ('Jane Doe', [340.0, 30.0, 200.0]), ('Jason Bourne', [240.0, 140.0]), ('GI Jane', [150.0, 60.0])]


def test_report():
    report = mailroompart4.createreport()
    assert report[0] == ('\nDonor Name                | Total Given | Num Gifts | Average Gift ')
    assert report[1] == ('-------------------------------------------------------------------')
    assert report[2] == ('John Wick                  $    1000.00           1  $     1000.00\nJohn Smith                 $     670.00           3  $      223.33\nJane Doe                   $     570.00           3  $      190.00\nJason Bourne               $     380.00           2  $      190.00\nGI Jane                    $     210.00           2  $      105.00\n')


def test_posadddonation():
    assert mailroompart4.adddonation("John Wick", 20) == True


def test_negaddonation():
    assert mailroompart4.adddonation("John Wick", "test") == False


def test_successfuladddonation():
    mailroompart4.adddonation("John Smith", 100)
    assert mailroompart4.donor_db["John Smith"] == [500.0, 150.0, 20.0, 100.0]


def test_newdonoradd():
    mailroompart4.addnewdonordonation("Test User")
    assert "Test User" in mailroompart4.donor_db.keys()
